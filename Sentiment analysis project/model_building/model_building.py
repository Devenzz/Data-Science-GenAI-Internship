# ================================
# Flipkart Review Sentiment Model
# ================================

import os
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score


# -------------------------------
# Base Directory (Project Root)
# -------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_DIR, "data", "flipkart_reviews.csv")
PKL_DIR = os.path.join(BASE_DIR, "pkl")

os.makedirs(PKL_DIR, exist_ok=True)


# -------------------------------
# Load Dataset
# -------------------------------
df = pd.read_csv(DATA_PATH)

print("Initial shape:", df.shape)

df.dropna(inplace=True)
print("After dropping NA:", df.shape)

X = df["clean_review_text"]
y = df["Sentiment"]


# -------------------------------
# Train-Test Split
# -------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# -------------------------------
# TF-IDF Vectorizer
# -------------------------------
tfidf = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2)
)

X_train_tfidf = tfidf.fit_transform(X_train)
X_test_tfidf = tfidf.transform(X_test)


# -------------------------------
# Model Comparison
# -------------------------------
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Naive Bayes": MultinomialNB(),
    "Linear SVM": LinearSVC(),
    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

results = []

for name, model in models.items():
    model.fit(X_train_tfidf, y_train)
    y_pred = model.predict(X_test_tfidf)
    f1 = f1_score(y_test, y_pred)

    results.append({"Model": name, "F1 Score": f1})


results_df = pd.DataFrame(results).sort_values(
    by="F1 Score", ascending=False
)

print("\nModel Comparison:")
print(results_df)


# -------------------------------
# Final Model
# -------------------------------
final_model = LinearSVC()
final_model.fit(X_train_tfidf, y_train)

print("\nFinal Model Trained: Linear SVM")


# -------------------------------
# Save Model & Vectorizer
# -------------------------------
with open(os.path.join(PKL_DIR, "tfidf_vectorizer.pkl"), "wb") as f:
    pickle.dump(tfidf, f)

with open(os.path.join(PKL_DIR, "sentiment_model.pkl"), "wb") as f:
    pickle.dump(final_model, f)

print("\n✅ Model and Vectorizer saved in /pkl folder")
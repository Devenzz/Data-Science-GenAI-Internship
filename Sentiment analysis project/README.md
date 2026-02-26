# 🛒 Flipkart Review Sentiment Analysis Dashboard

_Analyzing customer sentiment from Flipkart product reviews using NLP, Machine Learning, and Streamlit._

---

## 📌 Table of Contents
- <a href="#overview">Overview</a>
- <a href="#business-objective">Business Objective</a>
- <a href="#dataset">Dataset</a>
- <a href="#tools--technologies">Tools & Technologies</a>
- <a href="#project-structure">Project Structure</a>
- <a href="#data-preparation">Data Preparation</a>
- <a href="#model--approach">Model & Approach</a>
- <a href="#web-app--ui">Web App & UI</a>
- <a href="#key-insights">Key Insights</a>
- <a href="#recommendations">Recommendations</a>
- <a href="#business-impact">Business Impact</a>
- <a href="#conclusion--learnings">Conclusion & Learnings</a>
- <a href="#how-to-run-project">How to Run Project</a>
- <a href="#author--contact">Author & Contact</a>
- <a href="#acknowledgment">Acknowledgment</a>

---

<h2><a class="anchor" id="overview"></a>Overview</h2>

The **Flipkart Review Sentiment Analysis Project** focuses on understanding customer opinions by analyzing product reviews using **Natural Language Processing (NLP)** and **Machine Learning**.

This project classifies reviews into **Positive** or **Negative** sentiments and provides real-time predictions through an interactive **Streamlit web application**, helping businesses quickly assess customer feedback at scale.

---

<h2><a class="anchor" id="business-objective"></a>Business Objective</h2>

The primary objectives of this project are to:
- Analyze customer sentiment from Flipkart product reviews  
- Automatically classify reviews as **Positive** or **Negative**  
- Reduce manual effort in feedback analysis  
- Support data-driven decision-making for product and service improvement  

---

<h2><a class="anchor" id="dataset"></a>Dataset</h2>

- **Dataset Name:** Flipkart Product Reviews Dataset  
- **Records:** 8508 reviews  
- **Columns:** Review Text, Sentiment Label, Product Metadata  
- **Source:** Public e-commerce review dataset  
- **Target Variable:** Sentiment (Positive / Negative)

---

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

- **Python** – Core programming language  
- **Pandas & NumPy** – Data handling and processing  
- **NLTK** – Text preprocessing (tokenization, stopwords, lemmatization)  
- **Scikit-learn** – TF-IDF, ML models, evaluation  
- **Streamlit** – Interactive web application  
- **Pickle** – Model and vectorizer persistence  

---

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

```

Sentiment analysis project/
│
├── app/
│   └── app.py                  # Streamlit web app
│
├── data/
│   └── flipkart_reviews.csv    # Dataset
│
├── model_building/
│   └── model_building.py       # Model training & evaluation
│
├── pkl/
│   ├── sentiment_model.pkl
│   └── tfidf_vectorizer.pkl
│
├── requirements.txt
├── README.md
└── .gitignore

````

---

<h2><a class="anchor" id="data-preparation"></a>Data Preparation</h2>

The following preprocessing steps were applied:

- Removal of missing and duplicate reviews  
- Conversion of text to lowercase  
- Removal of special characters and punctuation  
- Tokenization of text  
- Stopword removal  
- Lemmatization to normalize words  

---

<h2><a class="anchor" id="model--approach"></a>Model & Approach</h2>

- **Feature Extraction:**  
  - TF-IDF Vectorization (Unigrams + Bigrams)

- **Models Trained & Compared:**  
  - Logistic Regression  
  - Naive Bayes  
  - Linear Support Vector Machine (SVM)  
  - Random Forest  

- **Evaluation Metric:**  
  - F1 Score  

- **Final Model Selected:**  
  - **Linear SVM** (best performance)

---

<h2><a class="anchor" id="web-app--ui"></a>Web App & UI</h2>

The Streamlit web application includes:

- Text area for entering product reviews  
- Center-aligned prediction button  
- Emoji-based sentiment output  
  - 😄😊🎉 Positive Review  
  - 😢😞💔 Negative Review  
- Clean, responsive, and user-friendly interface  

---

<h2><a class="anchor" id="key-insights"></a>Key Insights</h2>

1. Linear SVM performed best among all tested models  
2. TF-IDF with bigrams improved sentiment detection accuracy  
3. Short and clear reviews are classified more confidently  
4. NLP preprocessing significantly boosts model performance  

---

<h2><a class="anchor" id="recommendations"></a>Recommendations</h2>

- Extend model to support **Neutral sentiment**  
- Add **confidence score** for predictions  
- Use **deep learning models** for further improvement  
- Integrate sentiment insights into business dashboards  

---

<h2><a class="anchor" id="business-impact"></a>Business Impact</h2>

This project enables organizations to:
- Automatically analyze large volumes of customer feedback  
- Improve product quality using sentiment trends  
- Enhance customer experience and satisfaction  
- Save time and cost compared to manual review analysis  

---

<h2><a class="anchor" id="conclusion--learnings"></a>Conclusion & Learnings</h2>

### 📊 Conclusion
- NLP and ML can effectively classify customer sentiment  
- TF-IDF + Linear SVM provides strong baseline performance  
- Real-time sentiment analysis is achievable with Streamlit  

### 🧠 Learnings
- Built an end-to-end NLP pipeline  
- Gained hands-on experience with text preprocessing  
- Learned model comparison and evaluation techniques  
- Designed a deployable ML web application  

---

<h2><a class="anchor" id="how-to-run-project"></a>How to Run Project</h2>

1. **Clone the repository**
```bash
git clone https://github.com/your-username/flipkart-review-sentiment-analysis.git
````

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Train the model**

```bash
python model_building/model_building.py
```

4. **Run the Streamlit app**

```bash
streamlit run app/app.py
```

---

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

**Devendra Gangurde**
Aspiring Data Scientist | ML | NLP | GenAI

🔗 GitHub: (github.com/Devenzz)
🔗 LinkedIn: (https://www.linkedin.com/in/devendra-gangurde-43620a262/)

---

<h2><a class="anchor" id="acknowledgment"></a>Acknowledgment</h2>

Special thanks to **Innomatics Research Labs** for providing hands-on industry-oriented training.
Heartfelt gratitude to my mentors for their guidance and continuous support throughout this project.

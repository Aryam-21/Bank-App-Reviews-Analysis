# Bank-App-Reviews-Analysis
Project Overview
This project analyzes customer reviews of major Ethiopian bank mobile applications. The goal is to extract insights,identify sentiment trends, detect recurring themes, and recommend actionable improvement to enhance user satisfaction.
The analysis covers:

    - Data Collection and Preprocessing(Task‑1)

    - Sentiment and Thematic Analysis(Task‑2)

    - Store Cleaned Data in PostgreSQL(Task‑3)

    - Insights and Recommendations(Task‑4)
Project Structure
Bank-App-Reviews-Analysis/
│
├── data/
│ ├── raw/
│ │ └── reviews_raw.csv
│ └── processed/
│ ├── reviews_final.csv
│ ├── reviews_processed.csv
│ └── reviews_with_sentiment.csv
│
├── Scripts/
│ ├── config.py
│ ├── processing.py
│ ├── scraper.py
│ ├── task1.ipynb
│ ├── task2.ipynb
│ ├── task3.ipynb
│ └── task4.ipynb
│
├── Src/
├── test/
├── .venv/
├── README.md
├── requirements.txt
└── schema.sql
---


## 🧩 **Task‑1: Data Collection and Preprocessing**
### ✔ Description
Collected customer reviews from Google Play Store and (optionally) Apple App Store using a scraping script.


### ✔ Key Activities
- Scraped reviews for **CBE, BOA, Dashen** apps.
- Extracted: `review_text`, `rating`, `date`, `app_name`, `reviewer_id`.
- Exported dataset to **CSV**.


### ✔ raw Output
- `raw_reviews.csv`
- Initial descriptive statistics


### ✔ Cleaning Steps
- Removed **Amharic and non‑English characters**.
- Lower‑casing, punctuation removal, whitespace normalization.
- Stopword removal.
- Tokenization and optional lemmatization.
- Filtered empty or extremely short reviews.


### ✔ processed Output Files
- `cleaned_reviews.csv`
- Frequency tables & wordlists


---
## 🧩 **Task‑2: Sentiment and Thematic Analysis**
### ✔ Methods Used
- **VADER** and/or Logistic Regression for sentiment.
- Classified reviews into **Positive, Negative, Neutral**.
- TF‑IDF extracted top keywords.
- Optional topic modeling with **LDA**.


### ✔ Outputs
- Sentiment scores
- Keyword lists per bank
- Topic clusters

---
## 🧩 **Task 3: Store Cleaned Data in PostgreSQL**
### ✔ Create PostgreSQL Database 
- Create a database named bank_reviews.
- Define schema:
    -Banks Table: Stores information about the banks.
    -Reviews Table: Stores the scraped and processed review data.
- Insert cleaned review data using Python (psycopg2 or          SQLAlchemy recommended)
- Write SQL queries to verify data integrity (e.g., count reviews per bank, average rating)

### ✔ Outputs
-bank_reviews data base
- bank table
-reviews table
---


## 🧩 **Task‑4: Insights, Visualizations & Recommendations**
### ✔ Insights Identified
- Key **drivers of satisfaction** (fast login, simple UI, stable performance).
- Major **pain points** (crashes, slow loading, poor network handling, failed transactions).
- Cross‑bank comparison highlighting weak and strong performers.


### ✔ Visualizations
- Sentiment distribution per bank
- Keyword frequency bar charts
- Word clouds for each sentiment/theme
- Bank benchmarking dashboard


### ✔ Recommendations
For each bank, at least **2+ improvements** such as:
- Improve system stability
- Redesign UI navigation
- Add budgeting/analytics features
- Enhance security UX


---


## 📊 **Installation & Setup**
### Clone the Repository
git clone cd Bank-App-Reviews-Analysis
### Create and Activate a Virtual Environment
python -m venv .venv source .venv/bin/activate # Linux/macOS .venv\Scripts\activate # Windows
### Install Dependencies
pip install -r requirements.txt


---


## 🚀 **How to Run the Notebooks**
1. Open VS Code.
2. Install the Python and Jupyter extensions.
3. Open each notebook under `/Scripts/`.
4. Select the `.venv` interpreter.
5. Run the cells sequentially.


---


## 📦 **Technologies Used**
- Python (Pandas, NumPy, Regex)
- NLTK / SpaCy
- Scikit‑Learn
- Matplotlib / Seaborn
- WordCloud
- Jupyter Notebook
- psycopg2
- google_play_scraper
- python-dotenv 
- tqdm 
- transformers
- textblob 
- collections 
- re


---


## 📈 **Final Deliverables**
- Cleaned dataset
- Sentiment-labeled dataset
- Visual reports (PNG files)
- Executive summary PDF
- Final recommendations


---


## 📝 **Author**
**Aryam Tesfay**
Data Science Intern — Ethiopian Bank Review Analytics Project


---
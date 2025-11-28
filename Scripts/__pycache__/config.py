import os
from dotenv import load_dotenv

App_IDS = {
    'CBE': os.getenv('CBE_APP_ID', 'com.combanketh.mobilebanking'),
    'Dashen Bank':os.getenv("DASHENBANK_APP_ID","com.dashen.dashensuperapp"),
    "Abyssinia Bank":os.getenv("BOA_APP_ID","com.boa.boaMobileBanking")
}
BANK_NAMES = {
    "CBE": "Commercial Bank of Ethiopia",
    "Dashen Bank": "Dashen Bank",
    "Abyssinia Bank": "Bank of Abyssinia"
}
SCRAPING_CONFIG = {
    'reviews_per_bank': int(os.getenv('REVIEWS_PER_BANK', 400)),
    'max_retries': int(os.getenv('MAX_RETRIES', 3)),
    'lang': 'en',
    'country': 'et'  # Ethiopia
}

DATA_PATHS = {
    'raw': 'data/raw',
    'processed': 'data/processed',
    'raw_reviews': 'data/raw/reviews_raw.csv',
    'processed_reviews': 'data/processed/reviews_processed.csv',
    'sentiment_results': 'data/processed/reviews_with_sentiment.csv',
    'final_results': 'data/processed/reviews_final.csv'
}


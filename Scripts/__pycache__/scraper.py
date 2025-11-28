"""
Google Play Store Review Scraper
Task 1: Data Collection

This script scrapes user reviews from Google Play Store for three Ethiopian banks.
Target: 400+ reviews per bank (1200 total minimum)
"""
import sys
import os
from google_play_scraper import app, Sort, reviews_all, reviews 
import pandas as pd
from datetime import datetime
import time 
from tqdm import tqdm
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import App_IDS, BANK_NAMES, SCRAPING_CONFIG, DATA_PATHS 

class PlayStoreScraper:
    """Scraper class for Google Play Store reviews"""

    def __init__(self):
        self.app_ids = App_IDS
        self.bank_names = BANK_NAMES
        self.reviews_per_bank = SCRAPING_CONFIG['reviews_per_bank']
        self.lang = SCRAPING_CONFIG['lang']
        self.country = SCRAPING_CONFIG['country']
        self.max_retries = SCRAPING_CONFIG['max_retries']
    def get_app_info(self, app_id):
        """
        Get basic information about the app (rating, total reviews, etc.)
        """
        try:
            result = app(app_id=app_id, lang=self.lang, country=self.country)
            return {
                'app_id': app_id,
                'title': result.get('title', 'N/A'),
                'score': result.get('score', 0),
                'ratings': result.get('ratings', 0),
                'reviews': result.get('reviews', 0),
                'installs': result.get('installs', 'N/A')
            }
        except Exception as e:
            print(f"Error getting app info for {app_id}: {str(e)}")
            return None
    def scrape_reviews(self, app_id, count=400):
        """
        Scrape reviews for a specific app.
        Attempts to fetch 'count' number of reviews, sorted by newest first.
        Includes a retry mechanism for stability.
        """
        print(f"\nScraping reviews for {app_id}...")
        for attempt in range(self.max_retries):
            try:
                result, _ = reviews(
                    app_id=app_id,
                    lang = self.lang,
                    country=self.country,
                    sort = Sort.NEWEST,
                    count = count,
                    filter_score_with=None
                )
                print(f"Successfully scraped {len(result)} reviews")
                return result
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {str(e)}")
                # Wait before retrying if it's not the last attempt
                if attempt < self.max_retries - 1:
                    print(f"Retrying in 5 seconds...")
                    time.sleep(5)
                else:
                    print(f"Failed to scrape reviews after {self.max_retries} attempts")
                    return []

        return []
    def process_reviews(self, reviews_data, bank_code):
        """
        Process raw review data from the scraper into a clean dictionary format.
        Extracts only the relevant fields we need for analysis.
        """
        processed = []
        for review in reviews_data:
            processed.append({
                'review_id': review.get('reviewId', ''),
                'review_text': review.get('content', ''),
                'rating': review.get('score', 0),
                'review_date': review.get('at', datetime.now()),
                'user_name': review.get('userName', 'Anonymous'),
                'thumbs_up': review.get('thumbsUpCount', 0),
                'reply_content': review.get('replyContent', None),
                'bank_code': bank_code,
                'bank_name': self.bank_names[bank_code],
                'app_id': review.get('reviewCreatedVersion', 'N/A'),
                'source': 'Google Play'
            })
        return processed
    
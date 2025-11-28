"""
Data Preprocessing Script
Task 1: Data Preprocessing

This script cleans and preprocesses the scraped reviews data.
- Handles missing values
- Normalizes dates
- Cleans text data
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pandas as pd
from datetime import datetime 
from config import DATA_PATHS
import re
import numpy as np
class ReviewPreprocessor:
    """Preprocessor class for review data"""

    def __init__(self, input_path=None, output_path=None):
        """
        Initialize preprocessor

        Args:
            input_path (str): Path to raw reviews CSV
            output_path (str): Path to save processed reviews
        """ 
        self.input_path = input_path or DATA_PATHS['raw_reviews'] 
        self.output_path = output_path or DATA_PATHS['processed_reviews']
        self.data = None
        self.stats = {}
    def load_data(self):
        """Load raw reviews data"""
        try:
            self.data = pd.read_csv(self.input_path)
            print(f"Loaded {len(self.data)} reviews")
            self.stats['original_count'] = len(self.data)
            return True
        except FileNotFoundError:
            print(f"ERROR: File not found: {self.input_path}")
            return False
        except Exception as e:
            print(f"ERROR: Failed to load data: {str(e)}")
            return False
    def clean_columns(self):
        """Ensure all required columns exist even if scraper missed some."""

        required_cols = [
            "review_text",
            "rating",
            "review_date",
            "bank_name",
        ]

        for col in required_cols:
            if col not in self.data.columns:
                print(f"⚠ Missing column '{col}' -> creating placeholder")
                self.data[col] = None

        return self.data
    def remove_amharic(self, text):
        """Remove Amharic and non-English characters."""
        if not isinstance(text, str):
            return ""
        # Regex covers Ethiopian/Amharic unicode range
        text = re.sub(r"[\u1200-\u137F]+", "", text)
        # Remove weird symbols
        text = re.sub(r"[^A-Za-z0-9.,!?()/'\" \-]", " ", text)
        # Normalize spaces
        text = re.sub(r"\s+", " ", text)
        return text.strip()
    def clean_data(self):
        """Clean and preprocess raw review data."""
        # Ensure column structure
        self.data = self.clean_columns()
        
        # Remove duplicates
        self.data.drop_duplicates(subset=["review_text"], keep="first", inplace=True)
        
        # Clean review text
        self.data.dropna(subset=['review_text'], inplace=True)
        self.data["review_text"] = self.data["review_text"].astype(str).apply(self.remove_amharic)
        
        # Clean numeric rating
        self.data["rating"] = self.data["rating"].fillna(0).astype(int)
        
        # Clean bank info
        self.data["bank_name"] = self.data["bank_name"].fillna("Unknown Bank")
        
        # Normalize dates
        print("✔ Normalizing review_date to YYYY-MM-DD...")
        self.data["review_date"] = pd.to_datetime(self.data["review_date"], errors="coerce")
        self.data["review_date"] = self.data["review_date"].dt.strftime("%Y-%m-%d")
        self.data = self.data.dropna(subset=["review_date"])

        print(f"✔ Final cleaned rows: {len(self.data)}")
        return self.data

    def save_processed(self):
        """Save the processed clean CSV."""
        self.data.to_csv(self.output_path, index=False, encoding="utf-8")
        print(f"\n💾 Clean dataset saved at: {self.output_path}")

    def run(self):
        """Execute the full preprocessing pipeline."""
        print("🚀 Starting preprocessing pipeline...")

        self.load_data()
        if not self.load_data():
            print("❌ Pipeline stopped due to load error.")
            return
        self.clean_data()
        self.save_processed()

        print("✅ Preprocessing completed successfully!")

if __name__ == "__main__":
    processor = ReviewPreprocessor()
    processor.run()
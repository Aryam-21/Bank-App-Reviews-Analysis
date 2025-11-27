from google_play_scraper import Sort, reviews
import pandas as pd
from datetime import datetime

app = {
    "CBE Bank": "com.combanketh.mobilebanking",
    "Dashen Bank": "com.dashen.dashensuperapp",
    "Abyssinia Bank":"com.boa.boaMobileBanking"
}
TARGET_REVIEWS = 400
def scrape_reviews(app_name, app_id, count):
    """Scrape reviews for a single banking app."""
    all_reviews = []
    batch_size = 200
    for start in range(0, count, batch_size):
        result, _ = reviews(
            app_id=app_id,
            lang='en',
            country='et',
            sort=Sort.NEWEST,
            count=batch_size,
            filter_score_with=None,
        )
        for r in result:
            all_reviews.append({
                "review":r["content"],
                "rating":r["score"],
                "date":r["at"].strftime("%Y-%m-%d"),
                "bank":app_name,
                "source":"Google Play Store"
            })
    print(f"{app_name}: Collected {len(all_reviews)} reviews.")
    return all_reviews
final_data = []
for app_name, app_id in app.items():
    data = scrape_reviews(app_name, app_id, TARGET_REVIEWS)
    final_data.extend(data)
df = pd.DataFrame(final_data)
df.to_csv('data/raw/reviews_raw.csv', index=False)
print("\nSaved file: reviews_raw.csv")
print(f"Total reviews collected: {len(data)}")
DATA_PATHS = {
    'raw': 'data/raw',
    'processed': 'data/processed',
    'raw_reviews': 'data/raw/reviews_raw.csv',
    'processed_reviews': 'data/processed/reviews_processed.csv',
    'sentiment_results': 'data/processed/reviews_with_sentiment.csv',
    'final_results': 'data/processed/reviews_final.csv'
}
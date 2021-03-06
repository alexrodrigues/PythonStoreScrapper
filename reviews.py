from app_store_scraper import AppStore
from google_play_scraper import app
from pprint import pprint
import json


def fetch_app_store():
    app_store = AppStore(country="br", app_name="xpinvestimentos")
    app_store.review(how_many=20)
    app_store_xp = app_store.reviews
    for review in app_store_xp:
        date = review['date'].strftime("%Y-%m-%d %H:%M:%S")
        review['date'] = date
    return app_store_xp


app_store = fetch_app_store()

pprint(app_store)

with open('appstore.json', 'w', encoding='utf-8') as f:
    json.dump(app_store, f, ensure_ascii=False, indent=4)

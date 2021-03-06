from app_store_scraper import AppStore
from pprint import pprint
import json

app_store = AppStore(country="br", app_name="xpinvestimentos")
app_store.review(how_many=20)
app_store_xp = app_store.reviews

for review in app_store_xp:
    date = review['date'].strftime("%Y-%m-%d %H:%M:%S")
    review['date'] = date

pprint(app_store_xp)

with open('appstore.json', 'w', encoding='utf-8') as f:
    json.dump(app_store_xp, f,  ensure_ascii=False, indent=4)
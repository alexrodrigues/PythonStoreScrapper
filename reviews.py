from app_store_scraper import AppStore
from google_play_scraper import app
from pprint import pprint
import json
from google_play_scraper import Sort, reviews


def fetch_app_store():
    app_store = AppStore(country="br", app_name="xpinvestimentos")
    app_store.review(how_many=20)
    app_store_xp = app_store.reviews
    for review in app_store_xp:
        date = review['date'].strftime("%Y-%m-%d %H:%M:%S")
        review['date'] = date
    return app_store_xp

#'br.com.xp.carteira',
def fetch_google_play():
    result, continuation_token = reviews(
        'br.com.xp.carteira',
        lang='pt', # defaults to 'en'
        country='BR', # defaults to 'us'
        sort=Sort.MOST_RELEVANT, # defaults to Sort.MOST_RELEVANT
        count=20 # defaults to 100
        # ,filter_score_with=5 # defaults to None(means all score)
    )
    result, _ = reviews(
        'br.com.xp.carteira',
        continuation_token=continuation_token # defaults to None(load from the beginning)
    )
    for review in result:
        date = review['at'].strftime("%Y-%m-%d %H:%M:%S")
        review['at'] = date
        if review['repliedAt']:
            review['repliedAt'] = review['repliedAt'].strftime("%Y-%m-%d %H:%M:%S")

    return result



app_store = fetch_app_store()
# pprint(app_store)

google_play = fetch_google_play()
# pprint(google_play)

with open('appstore.json', 'w', encoding='utf-8') as f:
    json.dump(app_store, f, ensure_ascii=False, indent=4)

with open('playstore.json', 'w', encoding='utf-8') as f:
    json.dump(google_play, f, ensure_ascii=False, indent=4)

from app_store_scraper import AppStore
from pprint import pprint

appStoreXp = AppStore(country="br", app_name="xpinvestimentos")
appStoreXp.review(how_many=20)

pprint(appStoreXp.reviews)
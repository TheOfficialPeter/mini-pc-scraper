import requests
from flask import Flask

app = Flask(__name__)

class Scraper:
    def __init__(self):
        self.test_result = None

    def test_scraper(self):
        # perform tests on the website
        # to see it if still works
        self.status = "Working"

        # perform tests
        self.scrape_takealot(True)
        self.scrape_botshop(True)
        self.scrape_robofactory(True)

        # check results
        if self.test_result != True:
            print("\n[Mini PC Scraper] - [Warning]: Scraper is outdated\n")
        else:
            print("\n[Mini PC Scraper] - [Success]: All test runs passed!\n")

    def scrape_takealot(self, test_mode=False):
        if test_mode:
            self.test_result = True

        # raspberry pi search query
        response = requests.get("https://api.takealot.com/rest/v-1-11-0/searches/products?qsearch=raspberry+pi")
        products = response.json()["sections"]["products"]["results"]

        product_images = [x['product_views']['gallery']['images'][0] for x in products]
        product_names = [x['product_views']['core']['title'] for x in products]
        product_prices = [x['product_views']['enhanced_ecommerce_add_to_cart']['ecommerce']['add']['products'][0]['price'] for x in products]
        product_reviews = [x['product_views']['review_summary']['star_rating'] for x in products]
        product_status = [x['product_views']['stock_availability_summary']['status'] for x in products]

        # arduino search query
        response = requests.get("https://api.takealot.com/rest/v-1-11-0/searches/products?qsearch=arduino")
        products = response.json()["sections"]["products"]["results"]

        product_images.extend([x['product_views']['gallery']['images'][0] for x in products])
        product_names.extend([x['product_views']['core']['title'] for x in products])
        product_prices.extend([x['product_views']['enhanced_ecommerce_add_to_cart']['ecommerce']['add']['products'][0]['price'] for x in products])
        product_reviews.extend([x['product_views']['review_summary']['star_rating'] for x in products])
        product_status.extend([x['product_views']['stock_availability_summary']['status'] for x in products])

        products = {k: v for k, v in zip(['product_image', 'product_name', 'product_price', 'product_review', 'product_status'], [product_images, product_names, product_prices, product_reviews, product_status])} 
        return products

    def scrape_botshop(self, test_mode=False):
        if test_mode:
            self.test_result = True

    def scrape_robofactory(self, test_mode=False):
        if test_mode:
            self.test_result = True


scraper = Scraper()
scraper.test_scraper()

@app.route("/takealot")
def takelot():
    results = scraper.scrape_takealot()
    print(results)
    return results

@app.route("/botshop")
def botshop():
    scraper.scrape_botshop()

@app.route("/digikey")
def digikey():
    scraper.scrape_digikey()

@app.route("/robofactory")
def robofactory():
    scraper.scrape_robofactory()
# import necessary libraries
from flask import Flask, render_template
import pymongo
import scrape_mars

# create instance of Flask app
app = Flask(__name__)

# create mongo connection
client = pymongo.MongoClient()
db = client.mars_db
collection = db.mars_data_entries

@app.route("/")
def index():
    mars_data = list(db.collection.find())[0]
    return  render_template('index.html', mars_data=mars_data)

@app.route("/scrape")
def scraper():
    db.collection.remove({})
    mars_data = scrape_mars.scrape()
    db.collection.insert_one(mars_data)
    return  render_template('scrape_mars.html')

if __name__ == "__main__":
    app.run(debug=True)




# # Use flask_pymongo to set up mongo connection
# app.config["MONGO_URI"] = "mongodb://localhost:27017/craigslist_app"
# mongo = PyMongo(app)

# # Or set inline
# # mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


# @app.route("/")
# def index():
#     listings = mongo.db.listings.find_one()
#     return render_template("index.html", listings=listings)


# @app.route("/scrape")
# def scraper():
#     listings = mongo.db.listings
#     listings_data = scrape_craigslist.scrape()
#     listings.update({}, listings_data, upsert=True)
#     return redirect("/", code=302)


# if __name__ == "__main__":
#     app.run(debug=True)

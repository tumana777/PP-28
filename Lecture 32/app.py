from flask import Flask, Response, render_template
from models import products

app = Flask(__name__)

# @app.route("/")
# def index():
#     return Response("<h1>This is main page</h1>")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/products/")
def products_list():

    available_products = [product for product in products if product['is_available']]

    return render_template('products.html', products=available_products)

@app.route("/about/")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask

from backend.src.DataBase import Product

app = Flask(__name__)


@app.route("/produkt")
def dodaj_produkt(nowy_produkt):
    nowy_produkt = Product()


@app.route("/produkt")
def wyszukaj_produkt(our_product_name):
    return Product.wyszukajProdukt(our_product_name)


app.run()

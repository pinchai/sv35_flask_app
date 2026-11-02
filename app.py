from flask import Flask, render_template
from product_list import product as pro_list

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/about")
def about():
    return ("<center><h1>About Page</h1></center>")


@app.get("/api/products")
def products():
    return pro_list

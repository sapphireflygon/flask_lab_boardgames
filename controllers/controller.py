from flask import render_template
from app import app
from models.boardgames_list import orders

@app.route('/')
def index():
    return render_template("index.html", title="Cool Board Games!", boardgame_orders=orders)

@app.route('/orders/<index>')
def one_order(index):
    return render_template("order.html", order="Your Order!", one_order=orders[int(index)])


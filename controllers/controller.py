from flask import render_template
from flask import send_file

from app import app
from models.orders import order_list as orders

@app.route('/orders')
def index():
    return render_template('index.html', title='Orders', order_list=orders)

@app.route('/orders/<order_number>')
def order_number(order_number):
    return render_template('order.html', title="Your Order", order=orders[int(order_number)])





@app.route('/images/<filename>')
def get_image(filename):
    return send_file(f"images/{filename}")


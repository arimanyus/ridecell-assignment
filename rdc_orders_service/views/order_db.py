"""order_db: Module for creation and initialization of the Orders SQL table"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///orders.db'
db = SQLAlchemy(app=app)

class Orders(db.Model):
    """
    This function initializes our table for orders.

    Args:
        Model: db.Model

    Returns:
        Order ID for reference
    """
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    amount = db.Column(db.Integer)
    type = db.Column(db.String(200))
    date_created = db.Column(db.DateTime, default=datetime.now())

    def __repr__(self):
        return '<Order %r>' % self.id

if __name__ == "__main__":
    app.run()
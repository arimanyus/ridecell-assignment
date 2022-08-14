"""order_post_get_api: Contains POST and GET APIs to enable interaction with Order database/table"""
import json
from flask import Flask, request
from order_db import Orders, db

app = Flask(__name__)

class Order_Operations:
    """Order_Operations"""

    @app.route('add_order', methods=['POST'])
    def update_order(self):
        """
        This API updates the order table with a new record.
        It retrieves the book_id from the form.

        Returns:
            Success or failure response
        """
        book_id = request.form['book_id']
        new_order = Orders(book_id=book_id)

        try:
            db.session.add(new_order)
            db.session.commit()
            return json.dumps({"Message": "Order added successfully"})
        except Exception as e:
            return json.dumps({"Error": f"{e}"})

    @app.route('get_order', methods=['GET'])
    def get_order(self):
        """
        This API retrieves  the order details for a requested record.

        Returns:
            API response
        """
        try:
            order = Orders.query.order_by(Orders.date_created)
            return json.dumps({"Order Details": order})
        except Exception as e:
            return json.dumps({"Error": f"{e}"})


if __name__ == "__main__":
    app.run()
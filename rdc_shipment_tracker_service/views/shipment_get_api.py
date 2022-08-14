import requests, os
from flask import Flask, request, render_template

APP_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_PATH = os.path.join(APP_PATH, "rdc_frontend_service/templates")

app = Flask(__name__, template_folder=TEMPLATE_PATH)

class ShipmentGetAPI:
    """ShipmentGetAPI"""

    @app.route('/get_status', methods=['GET'])
    def get_status_from_third_party(self):
        """
        This function makes request to shipping company's API to fetch shipment details.

        Args:
            shipment_id: fetches shipment_id from request

        Returns:
            API response rendered with tracking page.
        """
        shipment_id = request.args.get("shipment_id")
        # Make (simulated) external call to shipment company's API
        response = requests.get(f'http://127.0.0.1:5001/get_shipment_status?shipment_id={shipment_id}')
        return render_template("tracking_page", value=response)


if __name__ == '__main__':
    app.run()
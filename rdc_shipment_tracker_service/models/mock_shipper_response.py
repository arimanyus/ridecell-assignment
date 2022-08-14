"""mock_shipper_response: This module emulates the response that the third-party shipping company's API will send"""
import json
from flask import Flask, request

app = Flask(__name__)

class MockShipResponse:
    """MockShipResponse"""
    def __init__(self):
        """init for MockShipResponse: sets a few sample records"""
        self.shipment_ids_with_status = {
                                    "1001": "DELIVERED",
                                    "1002": "IN TRANSIT",
                                    "1003": "IN TRANSIT",
                                    "1004": "PICK UP PENDING"
                                    }

    @app.route('/get_shipment_status', methods=['GET'])
    def get_shipment_status(self, shipment_id):
        """
        This function is a simulation of what third-party shipping company's
        API will return.

        Args:
            shipment_id:

        Returns:
            Record in JSON format.
        """
        try:
            return json.dumps({"Shipment status": self.shipment_ids_with_status[shipment_id]})
        except:
            return json.dumps({"Error": "Invalid Shipment ID"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
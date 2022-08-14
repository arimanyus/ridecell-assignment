"""Init for Orders microservice"""
from rdc_orders_service.views.order_post_get_api import Order_Operations

app = Order_Operations(__name__)
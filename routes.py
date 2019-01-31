from order.views import OrderView
from ws.handler import ws_handler


routes = [
    ('GET', '/ws', ws_handler, 'ws_handler'),
    ('*', '/orders/', OrderView, 'order_retrieve'),
]

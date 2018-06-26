from channels.routing import route

from XJBM.consumer import ws_message

channel_routing = [
    route("websocket.receive", ws_message),
]
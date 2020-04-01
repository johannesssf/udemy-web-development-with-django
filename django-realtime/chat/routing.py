from django.urls import re_path

from .consumers import ChatConsumer


websocket_patterns = [
    re_path(r'ws/chat/(?P<nome_sala>\w+)/$', ChatConsumer)
]

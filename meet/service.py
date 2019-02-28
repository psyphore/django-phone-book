import py2neo

from django.conf import settings

from common.neo4j_connector import GraphConnector
from .models import Category, Room, RoomDetail, Event


class MeetService(object):
    def __init__(self):
        default_set = settings.NEO4J_DATABASES.default
        uri = f'{default_set.host}:{default_set.port}'
        username = default_set.neo4j_user
        password = default_set.neo4j_password
        self.dbi = GraphConnector.start_instance(
            self, uri=uri, username=username, password=password)

    def get_all_categories(self, *args, **kwargs):
        pass

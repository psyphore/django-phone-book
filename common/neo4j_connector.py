from py2neo import Graph


class GraphConnector(object):

    def __init__(self, uri, user, password):
        self._driver = Graph(uri, auth=(user, password))

    @staticmethod
    def start_instance(self, uri, username, password):
        self.__init__(uri, username, password)
        return self._driver

    @staticmethod
    def close(self):
        self._driver.close()

    @staticmethod
    def get_instance(self):
        return self._driver

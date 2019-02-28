from neo4j.v1 import GraphDatabase, basic_auth

class HelloWorldExample(object):

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def print_greeting(self, message):
        with self._driver.session() as session:
            greeting = session.write_transaction(self._create_and_return_greeting, message)
            print(greeting)

    @staticmethod
    def _create_and_return_greeting(tx, message):
        result = tx.run("CREATE (a:Greeting) "
                        "SET a.message = $message "
                        "RETURN a.message + ', from node ' + id(a)", message=message)
        return result.single()[0]

    def get_instance(self):
        return self._driver.session()

    def validate_variables(self):
        pass

    @staticmethod
    def process_session(s, query, params, label, many=True):
        result = s.run(str(query), params)
        if many != True:
            return result.single()[0]
        else:
            items = []
            for item in result.get(label):
                items.append(item)
            return items

    @staticmethod
    def process_transaction(tx, query, params, label, many=True):
        result = tx.run(str(query), params)
        if many != True:
            return result.single()[0]
        else:
            items = []
            for item in result.get(label):
                items.append(item)
            return items

    @staticmethod
    def process_multi_label_session(tx, query, params, labels):
        pass
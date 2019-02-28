# from django.db import models
# from py2neo.data import Node, Relationship
from py2neo.ogm import GraphObject, Property, Label

class Asset(GraphObject):
    asset=Label("Asset")

    __primarykey__ = "serial_number"

    name = Property()
    serial_number = Property()
    tag = Property()
    date_captured = Property()
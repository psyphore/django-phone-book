from py2neo.ogm import GraphObject, Property, Label


class Person(GraphObject):
    person = Label("Person")

    __primarykey__ = "serial_number"

    title = Property()
    firstname = Property()
    lastname = Property()
    mobile_number = Property('mobileNumber')
    email_address = Property('emailAddress')
    date_updated = Property('updatedOn')

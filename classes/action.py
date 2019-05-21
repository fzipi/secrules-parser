class Action(object):
    """
    """
    def __init__(self, parent, name, value):
        self.parent = parent
        self.name = name
        self.value = value

    def __repr__(self):
        value = ""
        if self.value is not None:
            value = self.value
        repr = "{indent}{name}{value}".format(name=self.name, value=value, indent="")

        return repr


class ActionType(object):
    """
        Tag | id=ID | INT | "'"? STRING "'"? | msg=MessageValue |
    CollectionType | StringWithMacros | transformations*=Transformation[','];
    """
    def __init__(self, parent, collection, value, msg, transformations):
        self.parent = parent
        self.collection = collection
        self.value = value
        self.msg = msg
        self.transformations = transformations

    def __repr__(self):
        value = ""
        msg = ""
        if self.value is not None:
            value = self.value
        if self.msg is not None:
            msg = self.msg

        repr = ':{value}{msg}'.format(value=value,msg=msg)

        return repr
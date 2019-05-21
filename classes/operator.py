class OperatorType(object):
    def __init__(self, parent, path, uri, ipmatch, pm, host):
        self.parent = parent
        self.path = path
        self.uri = uri
        self.ipmatch = ipmatch
        self.pm = pm
        self.host = host

    def __repr__(self):
        path = ""
        uri = ""
        ipmatch = ""
        pm = ""
        host = ""
        repr = ""
        if self.path is not None:
            path = self.path
        if self.uri is not None:
            uri = self.uri
        if self.ipmatch:
            ipmatch = self.ipmatch
        if self.pm is not None:
            pm = self.pm
        if self.host is not None:
            host = self.host
        repr = "{path}{uri}{ipmatch}{pm}{host}".format(path=path,uri=uri,ipmatch=ipmatch,pm=pm,host=host)
        return repr

class Operator(object):
    def __init__(self, parent, name, value):
        self.parent = parent
        self.name = name
        self.value = value

    def __repr__(self):
        name = ""
        value = ""
        if self.name:
            name = "{name}".format(name=self.name)
        if self.value:
            value = self.value

        repr = "@{name} {value}".format(name=name,value=value)
        return repr
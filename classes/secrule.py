class RuleFormatException(Exception):
    def __init__(self, message):
        self.message = message

class SecRule(object):
    """
    'SecRule' variables+=Variable['|']'"' negated='!'? '@'? operator=Operator '"' '"'? actions+=Action[',']? '"'?;
    """
    def __init__(self, parent, variables, negated, operator, actions):
        self.parent = parent
        self.negated = negated
        self.variables = variables
        self.operator = operator
        self.actions = actions
        self.id = None
        self.chained = False
        self.capture = False
        self.chain = []

        for action in self.actions:
            if action.name == 'chain':
                self.chained = True
            if action.name == 'id':
                self.id = action.value
            if action.name == 'capture':
                self.capture = True

        if self.__class__.__name__ == "SecRule":
            if self.id is None:
                for rev in reversed(self.parent.rules):
                    if rev.__class__.__name__ == "SecRule" and rev.chained == True:
                        self.chain.append(rev)
                        if rev.id:
                            self.chained = rev.id
                            break
        elif self.__class__.__name__ == "SecAction":
            if seld.id is None:
                raise RuleFormatException("SecAction without id")

    def __repr__(self):
        if self.chained and self.id is None:
            repr = "{indent}This SecRule is the {number} chained from {id}".format(indent=self.indent(),number=self.indentation_level(), id=self.get_parent_id())
        else:
            repr = "This is SecRule {id}".format(id=self.get_id())

        return repr

    def indentation_level(self):
        return len(self.chain)

    def indent(self):
        return '    ' * self.indentation_level()

    def actions_indent(self):
        return self.indent() + '    '

    def get_id(self):
        """
        Id makes sense only on SecRule and maybe chained rules
        :return: Id
        :raise: Unsupported ID for this type of Rules
        """
        if self.__class__.__name__ == "SecRule" or self.__class__.__name__ == "SecAction":
            if self.id is not None:
                return self.id
            else:
                # This should be a chained tule
                self.get_parent_id()
        else:
            raise("Unsupported ID for this type of Rules")

    def get_parent_id(self):
        for i, t in enumerate(self.chain):
            print(i)
            print(t.id)
        return self.chain[len(self.chain)-1].id

    def print_ordered(self):
        """
        From: https://github.com/SpiderLabs/owasp-modsecurity-crs/blob/v3.2/dev/CONTRIBUTING.md, order is:
            id
            phase
            disruptive-action
            status
            capture
            t:xxx
            log
            nolog
            auditlog
            noauditlog
            msg
            logdata
            tag
            sanitiseArg
            sanitiseRequestHeader
            sanitiseMatched
            sanitiseMatchedBytes
            ctl
            setenv
            ver
            severity
            setvar
            expirevar
            chain
            skip
            skipAfter

        :return:
        """
        if self.__class__.__name__ == "SecRule" :
            negated = ""
            if self.negated:
                negated = "!"
            variables = '|'.join(map(repr,self.variables))
            actions = ',\\\n'.join(map(repr, self.actions))
            output = '{indent}SecRule "{variables}" "{negated}{operator}" \\\n{actions_indent}"{actions}"{newline}'.format(
                    variables=variables,
                    negated=negated,
                    operator=self.operator,
                    actions=actions,
                    indent=self.indent(),
                    actions_indent=self.actions_indent(),
                    newline="" if self.chained else "\n",
            )
            print(output)
        else:
            print("No SecRule")
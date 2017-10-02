#!/usr/bin/env python

import os
import glob
import pprint
from textx.metamodel import metamodel_from_file
from textx.exceptions import TextXSyntaxError

def print_rule(rule):
    if rule.__class__.__name__ == "SecRule":
        for action in rule.actions.action:
            if action.id:
                print "Rule id = {}".format(action.id)
            if action.chain:
                print "Rule id = {} is a chained rule.".format(action.id)

modsec_mm = metamodel_from_file('modsec.tx')

for rules in glob.glob('owasp-modsecurity-crs/rules/*.conf'):
    print 'Processing file %s:' % rules
    try:
        model = modsec_mm.model_from_file(rules)
        for rule in model.rules:
            print_rule(rule)
    except TextXSyntaxError as e:
        print e

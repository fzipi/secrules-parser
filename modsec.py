#!/usr/bin/env python

""""
ModSecurity CRS Parser
-----------------------------------------------

Copyright (C) 2017 Felipe Zipitria <felipe.zipitria@owasp.org>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License, either
version 3, or (at your option), any later version.

"""

import os
import glob
import pprint
import argparse
from textx.metamodel import metamodel_from_file
from textx.exceptions import TextXSyntaxError
import yaml
import jsonpickle
import json

# Parse Arguments
cmdline = argparse.ArgumentParser(description='ModSecurity CRS parser script.')
cmdline.add_argument('-v', '--verbose', help='Print verbose messages', action="store_true")
cmdline.add_argument('-d', '--debug', help='You don\'t want to do this!', action="store_true")
cmdline.add_argument('-f', '--files', type=str, help='Parse these files')
cmdline.add_argument('-r', '--reorder', help='Reorder rules using CRS standard', action="store_true")

args = cmdline.parse_args()


class Rule(object):
    """ Rules are:
    - a list of variables,
    - negated (bool)
    - Operator
    - a list of actions """
    def __init__(self, variables, negated, count, operator, actions):
        print "rule init called"
        if count:
            self.count = True
        for var in variables:
            print var
        for action in actions:
            print action
            #if action.id:
            #  self.id = action.id
        self.operator = operator
        self.variables = variables

# Main
def order_using_crs_standard(rule):
    """ Order rule output using CRS standard """
    #if rule.__class__.__name__ == "SecRule":
    #    for action in rule.actions:
    #        if action.id:
    #            return action.id

def debug_rule(rule):
    """ Don't use this unless you want to wait and read too much """
    serialized = jsonpickle.encode(rule)
    print yaml.dump(yaml.load(serialized), indent=2)

def get_rule_id(rule):
    """ Gets rule ID. Only for SecAction or SecRule """
    if rule.__class__.__name__ == "SecRule" or rule.__class__.__name__ == "SecAction":
        for action in rule.actions:
            if action.id:
                return action.id
    return 0

def print_comment(comment):
    """ Comments are discarded, so this method is irrelevant now """
    print "Comment: ".format(comment)

def print_rule(rule):
    """ This is just for printing something until we see the real capabilities of this parser """
    if rule.__class__.__name__ == "SecRule":
        for variable in rule.variables:
            if variable.collection == "TX" and variable.collectionArg == "PARANOIA_LEVEL":
                print "[One-liner Paranoia level Rule, id {}]".format(get_rule_id(rule))

        for action in rule.actions:
            if action.id:
                print "* Rule id = {}".format(action.id)
            if action.chain:
                print "* > This is a chained rule from the above.".format(action.id)
        if args.reorder:
            self.order_using_crs_standard(rule)

# rules_processors
def secrule_id_processor(rule):
    """ Processor for each rule, if neeeded """
    # print "secrule_id_processor_called"
    # print(rule)

def variable_processor(var):
    print(var)

def operator_processor(op):
    print(op)

def action_processor(action):
    print(action)
def disruptive_action(da):
    print "DisruptiveAction: {}".format(da)

# Load Meta-Model
# auto_init_attributes=False
modsec_mm = metamodel_from_file('modsec.tx', classes=[Rule])
# Register test processor
rules_processors = {
    'SecRule': secrule_id_processor,
    'Variable': variable_processor,
    'Operator': operator_processor,
    'Action': action_processor,
    'DisruptiveAction': disruptive_action
}
modsec_mm.register_obj_processors(rules_processors)

# files is a glob pattern
files = args.files if args.files else 'owasp-modsecurity-crs/rules/*.conf'

for rules in glob.glob(files):
    if args.verbose:
        print 'Processing file %s:' % rules
    try:
        model = modsec_mm.model_from_file(rules)
        if args.verbose:
            for rule in model.rules:
                print_rule(rule)
            for comment in model.comments:
                print_comment(comment)
        if args.reorder:
            for rule in model.rules:
                order_using_crs_standard(rule)
        if args.debug:
            for rule in model.rules:
                debug_rule(rule)
        if model.rules:
            print "Syntax OK: {}".format(rules)
    except TextXSyntaxError as e:
        print "Syntax error in line {}, col {}: {}".format(e.line, e.col, e.message)

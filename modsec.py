#!/usr/bin/env python

""""
ModSecurity CRS Parser 
-----------------------------------------------

Copyright (C) 2017 Felipe Zipitria <felipe.zipitria@owasp.org>

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License, either
version 3, or (at your option), any later version.

"""

from __future__ import print_function
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

args = cmdline.parse_args()

def secrule_id_processor(rule):
    """ Processor for each rule, if neeeded """
    # print "secrule_id_processor_called"
    # print(rule)

def debug_rule(rule):
    """ Don't use this unless you want to wait and read too much """
    serialized = jsonpickle.encode(rule)
    print(yaml.dump(yaml.load(serialized), indent=2))

def get_rule_id(rule):
    """ Gets rule ID. Only for SecAction or SecRule """
    if rule.__class__.__name__ == "SecRule" or rule.__class__.__name__ == "SecAction":
        for action in rule.actions:
            if action.id:
                return action.id
    return 0

def print_rule(rule):
    """ This is just for printing something until we see the real capabilities of this parser """
    if rule.__class__.__name__ == "SecRule":
        for variable in rule.variables:
            if variable.collection == "TX" and variable.collectionArg == "PARANOIA_LEVEL":
                print("[One-liner Paranoia level Rule, id {}]".format(get_rule_id(rule)))

        for action in rule.actions:
            if action.id:
                print("* Rule id = {}".format(action.id))
            if action.chain:
                print("* > This is a chained rule from the above.".format(action.id))

# Load Meta-Model
modsec_mm = metamodel_from_file('modsec.tx', memoization=True)
# Register test processor
modsec_mm.register_obj_processors({'SecRule': secrule_id_processor})

# files is a glob pattern
files = args.files if args.files else 'owasp-modsecurity-crs/rules/*.conf'

for rules in glob.glob(files):
    if args.verbose:
        print('Processing file %s:' % rules)
    try:
        model = modsec_mm.model_from_file(rules)
        if args.verbose:
            for rule in model.rules:
                print_rule(rule)
        if args.debug:
            for rule in model.rules:
                debug_rule(rule)
        if model.rules:
            print("Syntax OK: {}".format(rules))
    except TextXSyntaxError as e:
        print("Syntax error in line {}, col {}: {}".format(e.line, e.col, e.message))



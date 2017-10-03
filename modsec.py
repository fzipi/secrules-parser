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

# Parse Arguments
cmdline = argparse.ArgumentParser(description='ModSecurity CRS parser script.')
cmdline.add_argument('-v', '--verbose', help='Print verbose messages', action="store_true")
cmdline.add_argument('-f', '--files', type=str, help='Parse these files')

args = cmdline.parse_args()

def print_rule(rule):
    if rule.__class__.__name__ == "SecRule":
        for action in rule.actions.action:
            if action.id:
                print "Rule id = {}".format(action.id)
            if action.chain:
                print "> Rule is a chained rule.".format(action.id)

modsec_mm = metamodel_from_file('modsec.tx', memoization=True)

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
        if model.rules:
            print "Syntax OK: {}".format(rules)
    except TextXSyntaxError as e:
        print "Syntax error in line {}, col {}: {}".format(e.line, e.col, e.message)
    except TextXSemanticError as e:
        print e



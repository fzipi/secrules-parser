#!/usr/bin/env python

import os
import glob
import pprint
from textx.metamodel import metamodel_from_file
from textx.exceptions import TextXSyntaxError

modsec_mm = metamodel_from_file('modsec.tx')

for rules in glob.glob('owasp-modsecurity-crs/rules/*.conf'):
    print 'Processing file %s:' % rules
    try:
        modsec_model = modsec_mm.model_from_file(rules)
        pp = pprint.PrettyPrinter(indent=4,depth=6)
        pp.pprint(modsec_model)
    except TextXSyntaxError as e:
        print e

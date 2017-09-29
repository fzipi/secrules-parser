#!/usr/bin/env python

import os
import glob
import pprint
from textx.metamodel import metamodel_from_file

modsec_mm = metamodel_from_file('modsec.tx')

for rules in glob.glob('test/*.conf'):
    print 'Processing %s' % rules
    modsec_model = modsec_mm.model_from_file(rules)
    pp = pprint.PrettyPrinter(indent=4,depth=6)
    pp.pprint(modsec_model)

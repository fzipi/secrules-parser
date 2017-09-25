#!/usr/bin/env python

from textx.metamodel import metamodel_from_file
modsec_mm = metamodel_from_file('modsec.tx')

modsec_model = modsec_mm.model_from_file('test/rules.conf')

# OWASP CRS Rules parser

Incomplete parser for mod_security rules. 

To use it:
 . Init submodules (get the CRS ruleset):
```
git submodule init
git submodule update
```
 . Install dependencies
```
pip install -r requirements.txt
```
 . Call `modsec.py` and it will scan the `*.conf` files in 'owasp-modsecurity-crs/rules'

For visualizing the syntax tree, use:
```
textx visualize modsec.tx
dot -Tpng -O modsec.tx.dot
```
Then view the generated PNG `modsec.tx.dot.png`!

# OWASP CRS Syntactic checker

Incomplete parser for mod_security rules.

This repo has submodules, please the commands below to get the CRS ruleset:
```
git submodule init
git submodule update
```

For visualizing, use:

```
textx visualize modsec.tx
dot -Tpng -O modsec.tx.dot
```

Then view `modsec.tx.dot.png`

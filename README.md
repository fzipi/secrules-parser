# OWASP CRS Rules parser

Incomplete parser model and sample application for parsing [mod_security CRS rules](https://github.com/SpiderLabs/owasp-modsecurity-crs/). It uses the python library [textX](http://www.igordejanovic.net/textX/) for parsing.

How to use it:
1. Init submodules (get the CRS ruleset):
    ```
    git submodule init
    git submodule update
    cd owasp-modsecurity-crs; git checkout v3.1/dev; cd ..
    ```
1. Install dependencies
    Dependencies can be installed system-wide, or just for your user (using `--user`).
    System-wide:
    ```
    sudo pip install -r requirements.txt
    ```
    User:
    ```
    pip install --user -r requirements.txt
    ```
1. Execute `./modsec.py` and it will scan the `*.conf` files in 'owasp-modsecurity-crs/rules'

    For visualizing the syntax tree, use:
    ```
    textx visualize modsec.tx
    dot -Tpng -O modsec.tx.dot
    ```
    Then watch the generated PNG `modsec.tx.dot.png`!

Execution stops because some of the rules aren't fully cleaned and/or there are differences in files.

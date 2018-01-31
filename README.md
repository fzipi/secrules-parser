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
1. Execute `./modsec.py` and it will scan the `*.conf` files in 'owasp-modsecurity-crs/rules':
   ```
    $ ./modsec.py
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-901-INITIALIZATION.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-903.9001-DRUPAL-EXCLUSION-RULES.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-903.9002-WORDPRESS-EXCLUSION-RULES.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-905-COMMON-EXCEPTIONS.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-910-IP-REPUTATION.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-911-METHOD-ENFORCEMENT.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-912-DOS-PROTECTION.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-913-SCANNER-DETECTION.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-920-PROTOCOL-ENFORCEMENT.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-921-PROTOCOL-ATTACK.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-930-APPLICATION-ATTACK-LFI.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-931-APPLICATION-ATTACK-RFI.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-932-APPLICATION-ATTACK-RCE.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-933-APPLICATION-ATTACK-PHP.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-941-APPLICATION-ATTACK-XSS.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-942-APPLICATION-ATTACK-SQLI.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-943-APPLICATION-ATTACK-SESSION-FIXATION.conf
    Syntax OK: owasp-modsecurity-crs/rules/REQUEST-949-BLOCKING-EVALUATION.conf
    Syntax OK: owasp-modsecurity-crs/rules/RESPONSE-950-DATA-LEAKAGES.conf
    Syntax OK: owasp-modsecurity-crs/rules/RESPONSE-951-DATA-LEAKAGES-SQL.conf
    Syntax OK: owasp-modsecurity-crs/rules/RESPONSE-952-DATA-LEAKAGES-JAVA.conf
    Syntax OK: owasp-modsecurity-crs/rules/RESPONSE-953-DATA-LEAKAGES-PHP.conf
    Syntax OK: owasp-modsecurity-crs/rules/RESPONSE-954-DATA-LEAKAGES-IIS.conf
    Syntax OK: owasp-modsecurity-crs/rules/RESPONSE-959-BLOCKING-EVALUATION.conf
    Syntax OK: owasp-modsecurity-crs/rules/RESPONSE-980-CORRELATION.conf
    ```

To visualize the syntax tree, use:
```
textx visualize modsec.tx
dot -Tpng -O modsec.tx.dot
```
Then review the generated PNG `modsec.tx.dot.png`!

Please file an [issue](https://github.com/fzipi/secrules-parser/issues) if you find a bug or you want some feature added.

#!/bin/bash

epydoc -v doc/EClass/*.py -o ../design/ --debug

sed -i "s/http:\/\/THIS_WILL_BE_REMOVED_TO_CREATE_A_RELATIVE_LINK//" ../design/EClass-module.html

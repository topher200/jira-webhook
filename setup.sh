#!/bin/sh

# install these in the root directory so we can zip them up

# we include setup.cfg in the root dir because amazon tells us to:
# http://docs.aws.amazon.com/lambda/latest/dg/lambda-python-how-to-create-deployment-package.html
# (end of step #3 as of this writing)

pip install requests -t .

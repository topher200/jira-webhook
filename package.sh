#!/bin/bash

zip -q -r aws_package.zip .

aws lambda update-function-code --function-name iot-button-to-kasa --zip-file fileb://aws_package.zip

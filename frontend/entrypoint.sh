#!/bin/bash

set -e

if ! test -d ./node_modules; then
    echo "{0}: install react dependencies"
    npm install
fi

if [$NODE_ENV -eq "production"]; then
    npm run build
    npm run start:prod
else
    npm start
fi

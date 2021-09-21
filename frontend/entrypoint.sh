#!/bin/bash

set -e

if ! test -d ./build; then
    echo "{0}: build and optimize react app."
    npm run build
fi

npm run start:prod

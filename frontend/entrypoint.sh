#!/bin/bash

set -e

echo "{0}: build and optimize react app."
npm run build

npm run start:prod

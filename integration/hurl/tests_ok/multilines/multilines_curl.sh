#!/bin/bash
set -Eeuo pipefail

hurl --verbose --no-output --curl build/multilines.curl tests_ok/multilines/multilines.hurl

cat build/multilines.curl

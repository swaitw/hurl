#!/bin/bash
set -Eeuo pipefail

hurl --output - tests_ok/encoding/encoding.hurl

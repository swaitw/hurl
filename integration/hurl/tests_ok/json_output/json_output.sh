#!/bin/bash
set -Eeuo pipefail

hurl --json tests_ok/json_output/json_output.hurl

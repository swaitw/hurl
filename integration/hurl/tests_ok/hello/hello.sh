#!/bin/bash
set -Eeuo pipefail

hurl --verbose tests_ok/hello/hello.hurl

#!/bin/bash
set -Eeuo pipefail

hurl --variable age=30 --variable strict=true --variable string_variable=\\ --variable key=dynamic_key tests_ok/post/post_json.hurl

#!/usr/bin/env sh

# sort command:
# -t determines the field separator
# -d sorts using only blanks and alphanumeric characters
# -k sorts the Nth column (indexed from 1)
# uniq command:
# -s skips the first N characters during comparison
# -D prints all duplicate lines
sort -t, -d -k2 "$1" | uniq -s 20 -D

#!/usr/bin/env sh

# sort command:
# -t determines the field separator
# -d sorts using only blanks and alphanumeric characters
# -k sorts the Nth column (indexed from 1)
# uniq command:
# -s skips the first N characters during comparison
# -D prints all duplicate lines
sort -t, -d -k2 "$1" | uniq -s 20 -D

#./remove-duplicates.sh res/puzzle.csv
#6440 0FY9 TEVX VZ2B,b5ed3762-9c52-4a3c-a3b2-ca5aeed9056e
#6449 CV4F AB7B 2VEK,b5ed3762-9c52-4a3c-a3b2-ca5aeed9056e

#./remove-duplicates.sh res/puzzle_bonus.csv
#64G3 QCZF HBAM NEWQ,27a7edab-1c35-4ddc-b28e-e8cc2c552480
#64G7 XH56 3HPM M8CN,27a7edab-1c35-4ddc-b28e-e8cc2c552480

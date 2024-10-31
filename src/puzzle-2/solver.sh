#!/usr/bin/env sh

# Solution:
# z a p y n
# l d e w p
# l c y m j
# o z t y r

. "$HOME/git-proj/learn-by-doing/src/puzzle-2/functions.sh"

#echo_read_prompt() {
#  echo "Enter a pattern matcher for row $1 column $2"
#}
#
#read_regex() {
#  read -r regex
#  echo "$regex"
#}
#
#all_letters=()
#
#for row in {1..4}; do
#  for column in {1..5}; do
#    echo_read_prompt "$row" "$column"
#    pattern1=$(read_regex "$row" "$column")
#
#    echo_read_prompt "$row" "$column"
#    pattern2=$(read_regex "$row" "$column")
#
#    letter=$(get_letter_from_patterns "$pattern1" "$pattern2")
#    all_letters+=("$letter")
#  done
#done

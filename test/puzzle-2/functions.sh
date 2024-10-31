#~/git-proj/bash_unit/bash_unit ~/git-proj/learn-by-doing/test/puzzle-2/functions.sh

PROJECT_PATH="$HOME/git-proj/learn-by-doing/"
SRC_DIR="$PROJECT_PATH/src/puzzle-2/"
TEST_DIR="$PROJECT_PATH/test/puzzle-2/"

R1='[zsh]a(py|th)[on]'
R2='[gil](i|de)[web]{1,2}[path]?'
R3='[lua][curl][^sed][mock][js]'
R4='[^tlm][zip][^read][ruby]+'

C1='z[^ig][toml]{2}'
C2='a?d?a?c?[xz]'
C3='(pe|rl)[yes][dart]'
C4='([yaml])[wasm]{2}\1'
C5='[net][ph]p?[^ts]?[rails]'

letters_array=('z' 'a' 'p' 'y' 'o' 'z' 'a' 'p' 'y' 'o')

setup() {
  . "$SRC_DIR/functions.sh"
}

test_get_letter_does_not_match() {
  expected=""
  actual=$(get_letter_from_patterns '_')
  assert_equals "$expected" "$actual"
}

test_get_letter_matches_two_groups() {
  expected="z"
  actual=$(get_letter_from_patterns '[zsh]' 'z')
  assert_equals "$expected" "$actual"
}

test_get_two_letters_matches() {
  expected="py"
  actual=$(get_two_letters_from_patterns '(py|th)')
  assert_equals "$expected" "$actual"
}

test_get_three_letters_matches() {
  expected="adc"
  actual=$(get_three_letters_from_patterns 'a?d?a?c?')
  assert_equals "$expected" "$actual"
}

test_get_four_letters_matches() {
  expected="dewp"
  actual=$(get_four_letters_from_patterns '(i|de)[web]{1,2}[path]?')
  assert_equals "$expected" "$actual"
}

test_print_rows() {
  expected="$(echo -e "\n| z | a | p | y | o |\n| z | a | p | y | o |")"
  actual=$(print_rows "${letters_array[@]}")
  assert_equals "$expected" "$actual"
}

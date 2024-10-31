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

setup() {
  . "$SRC_DIR/functions.sh"
}

test_two_matching_groups_checked() {
  expected="z"
  actual=$(get_letter_from_patterns '[zsh]' 'z')
  assert_equals "$expected" "$actual"
}

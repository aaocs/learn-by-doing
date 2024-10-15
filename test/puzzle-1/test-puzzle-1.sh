#~/git-proj/bash_unit/bash_unit ~/git-proj/learn-by-doing/test/puzzle-1/test-puzzle-1.sh

PROJECT_PATH="$HOME/git-proj/learn-by-doing/"
SRC_DIR="$PROJECT_PATH/src/puzzle-1/"
TEST_DIR="$PROJECT_PATH/test/puzzle-1/"

test_should_print_two_duplicates() {
  expected="(0000 0000 0000 0003, 0000 0000 0000 0001)"
  actual=$("$SRC_DIR"/remove-duplicates.sh "$TEST_DIR"/res/one-duplicate.csv)
  assert_equals "$expected" "$actual"
}

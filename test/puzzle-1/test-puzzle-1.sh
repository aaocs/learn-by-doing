#~/git-proj/bash_unit/bash_unit ~/git-proj/learn-by-doing/test/puzzle-1/test-puzzle-1.sh

PROJECT_PATH="$HOME/git-proj/learn-by-doing/"
SRC_DIR="$PROJECT_PATH/src/puzzle-1/"
TEST_DIR="$PROJECT_PATH/test/puzzle-1/"

test_should_print_zero_duplicates() {
  expected=""
  actual=$("$SRC_DIR"/remove-duplicates.sh "$TEST_DIR"/res/zero-duplicates.csv)
  assert_equals "$expected" "$actual"
}

test_should_print_two_lines_same_id() {
  expected="0000 0000 0000 0001,00000000-0000-0000-0000-000000000000
0000 0000 0000 0003,00000000-0000-0000-0000-000000000000"
  actual=$("$SRC_DIR"/remove-duplicates.sh "$TEST_DIR"/res/one-duplicate.csv)
  assert_equals "$expected" "$actual"
}

test_should_print_three_lines_same_id() {
  expected="0000 0000 0000 0001,00000000-0000-0000-0000-000000000000
0000 0000 0000 0003,00000000-0000-0000-0000-000000000000
0000 0000 0000 0004,00000000-0000-0000-0000-000000000000"
  actual=$("$SRC_DIR"/remove-duplicates.sh "$TEST_DIR"/res/two-duplicates.csv)
  assert_equals "$expected" "$actual"
}

test_should_print_four_lines_two_ids() {
  expected="0000 0000 0000 0001,00000000-0000-0000-0000-000000000000
0000 0000 0000 0004,00000000-0000-0000-0000-000000000000
0000 0000 0000 0008,00000000-0000-0000-0000-000000000007
0000 0000 0000 0009,00000000-0000-0000-0000-000000000007"
  actual=$("$SRC_DIR"/remove-duplicates.sh "$TEST_DIR"/res/two-one-duplicates.csv)
  assert_equals "$expected" "$actual"
}

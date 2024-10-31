__check_regex_matches() {
  chars="$1"
  shift

  for arg in "$@"; do
    if [[ ! $chars =~ $arg ]]; then
      return 1;
    fi
  done

  return 0;
}

get_letter_from_patterns() {
  for letter in {a..z}; do
    if (__check_regex_matches "$letter" "$@"); then
      echo "$letter"
      return 0 # Terminates on the first match.
    fi
  done
}

get_two_letters_from_patterns() {
  for letters in {a..z}{a..z}; do
    if (__check_regex_matches "$letters" "$@"); then
      echo "$letters"
      return 0 # Terminates on the first match.
    fi
  done
}

get_three_letters_from_patterns() {
  for letters in {a..z}{a..z}{a..z}; do
    if (__check_regex_matches "$letters" "$@"); then
      echo "$letters"
      return 0 # Terminates on the first match.
    fi
  done
}

get_four_letters_from_patterns() {
  for letters in {a..z}{a..z}{a..z}{a..z}; do
    if (__check_regex_matches "$letters" "$@"); then
      echo "$letters"
      return 0 # Terminates on the first match.
    fi
  done
}

# A Bash array should be the last argument and only one array can be passed.
print_rows() {
  out=""

  arr=("$@") # Rebuild the array with suffixed arguments.
  counter=0
  for str in "${arr[@]}"; do
    if ! ((counter % 5)); then
      out+="\n|"
    fi

    out+=" $str |"
    ((counter++))
  done

  echo -e "$out"
}

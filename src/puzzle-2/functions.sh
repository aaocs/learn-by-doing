get_letter_from_patterns() {
  for letter in {a..z}; do
    letter_matches_patterns=true

    for arg in "$@"; do
        if [[ ! $letter =~ $arg ]]; then
          letter_matches_patterns=false
          break
        fi
    done

    if [[ $letter_matches_patterns = true ]]; then
      echo "$letter"
      return 0 # Terminate as soon as a letter matches.
    fi
  done
}

#A Bash array should be the last argument and only one array can be passed.
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

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

all_digits_dict = {
  '0': 6,
  '1': 2,
  '2': 5,
  '3': 5,
  '4': 4,
  '5': 5,
  '6': 5,
  '7': 3,
  '8': 7,
  '9': 5,
  ### Smallest numbers without leading 0s:
  '10': 8,
  '18': 9,
  '22': 10,
  '20': 11,
  '28': 12,
  '80': 13,
  '200': 17,
  # Since the most matchsticks for a single digit is 7,
  # if a range of 7 matchsticks with the same number of digits is correct
  # without having to add a better digit combination then all ranges of 7
  # (and hence all integers) are correct.
  # All matchstick values up to and including the range 22 to 28 are correct,
  # hence no more manual checking is required.
}

'''
# Analysing digits depending on whether the target is large or small:

# Use as few matchsticks as possible for each digit.
largest_number_digits_dict = {
  #0: 6 # 111 > 0
  1: 2 # This is the best repeater digit.
  #2: 5 # Larger digit with same number of matchsticks.
  #3: 5 # Larger digit with same number of matchsticks.
  #4: 4 # 11 > 4
  #5: 5 # Larger digit with same number of matchsticks.
  #6: 5 # Larger digit with same number of matchsticks.
  7: 3 # This is required once for odd numbers of matchsticks.
  #8: 7 # 711 > 8
  #9: 5 # 71 > 9
}

# Use as many matchsticks as possible for each digit.
smallest_number_digits_dict = {
  0: 6
  1: 2
  2: 5
  #3: 5 # Smaller digit with same number of matchsticks.
  4: 4
  #5: 5 # Smaller digit with same number of matchsticks.
  #6: 5 # Smaller digit with same number of matchsticks.
  7: 3
  8: 7 # This is the best repeater digit.
  #9: 5 # Smaller digit with same number of matchsticks.
}
'''

def add_final_digit(answer, digit):
  answer['matchsticks'] += all_digits_dict[digit]
  answer['digits'] = answer['digits'] + digit

def get_smallest_number(num_matchsticks):
  answer = {'matchsticks': 0, 'digits': ''}
  while answer['matchsticks'] <= num_matchsticks - all_digits_dict['0']:
    answer['matchsticks'] += all_digits_dict['0']
    answer['digits'] += '0'
  match num_matchsticks - answer['matchsticks']:
    case 5:
      add_final_digit(answer, '2')
    case 4:
      add_final_digit(answer, '4')
    case 3:
      add_final_digit(answer, '7')
    case 2:
      add_final_digit(answer, '1')
    case 1:
      answer['matchsticks'] -= all_digits_dict['0']
      answer['digits'] = answer['digits'][1:]
      add_final_digit(answer, '8')
  return answer

def remove_last_digit(answer):
  answer['matchsticks'] -= all_digits_dict['8']
  answer['digits'] = answer['digits'][:-1]

def add_final_digits(answer, digits):
  answer['matchsticks'] += all_digits_dict[digits]
  answer['digits'] = digits + answer['digits']

def get_smallest_number_no_leading_zeros(num_matchsticks):
  answer = {'matchsticks': 0, 'digits': ''}
  while answer['matchsticks'] <= num_matchsticks - all_digits_dict['8']:
    answer['matchsticks'] += all_digits_dict['8']
    answer['digits'] += '8'
  match num_matchsticks - answer['matchsticks']:
    case 6:
      remove_last_digit(answer)
      add_final_digits(answer, '80')
    case 5:
      remove_last_digit(answer)
      add_final_digits(answer, '28')
    case 4:
      remove_last_digit(answer)
      add_final_digits(answer, '20')
    case 3:
      remove_last_digit(answer)
      if num_matchsticks < 17:
        add_final_digits(answer, '22')
      else:
        remove_last_digit(answer)
        add_final_digits(answer, '200')
    case 2:
      remove_last_digit(answer)
      add_final_digits(answer, '18')
    case 1:
      remove_last_digit(answer)
      add_final_digits(answer, '10')
  return answer

def get_largest_number(num_matchsticks):
  answer = {'matchsticks': 0, 'digits': ''}
  while answer['matchsticks'] <= num_matchsticks - all_digits_dict['1']:
    answer['matchsticks'] += all_digits_dict['1']
    answer['digits'] += '1'
  if answer['matchsticks'] != num_matchsticks:
    # The number of matchsticks must be num_matchsticks - 1
    answer['matchsticks'] -= all_digits_dict['1']
    answer['digits'] = answer['digits'][1:]
    answer['matchsticks'] += all_digits_dict['7']
    answer['digits'] = '7' + answer['digits'] # Prepend the extra digit since 7 > 1
  return answer

# Tested for all matchsticks numbers greater than 7.
for matchsticks in [10, 25, 100, 1000, 10000]:
  largest = get_largest_number(matchsticks)
  smallest = get_smallest_number(matchsticks)
  smallest_modified = get_smallest_number_no_leading_zeros(matchsticks)

  print(f'{largest} - # chars: {len(largest['digits'])} - get_largest_number')
  print(f'{smallest} - # chars: {len(smallest['digits'])} - get_smallest_number')
  print(f'{smallest_modified} - # chars: {len(smallest_modified['digits'])} - get_smallest_number_no_leading_zeros')

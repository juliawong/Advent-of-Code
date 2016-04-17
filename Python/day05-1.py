''' How many strings in Santa's text file are nice? '''
import re

def count_nice_strings(santa_strings):
    nice_count = 0
    bad = ["ab", "cd", "pq", "xy"]
    vowels = ["a", "e", "i", "o", "u"]

    for string in santa_strings.split():
        # check for bad strings
        if any(i in string for i in bad):
            continue
        # count vowels
        if sum(map(string.count, vowels)) < 3:
            continue
        # check for letter twice in a row
        if re.search(r"(\w)\1+", string):
            # \w letters
            # \1 back reference to group (\w)
            nice_count += 1

    return nice_count

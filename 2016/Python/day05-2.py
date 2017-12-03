''' How many strings in Santa's text file are nice? '''
import re

def count_nice_strings(santa_strings):
    nice_count = 0

    for string in santa_strings.split():
        # check for pair of two letters appearing twice
        if not re.search(r"(\w{2}).*?(\1)", string):
            # *? Between zero and unlimited times, lazy match
            continue
        # check for letter repeating with another letter between
        if re.search(r"(\w)[^\1]{1}\1", string):
            nice_count += 1

    return nice_count

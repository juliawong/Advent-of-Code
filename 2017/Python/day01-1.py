def captcha(digits):
    total = 0
    curr_digit = digits[0]

    for i in range(1, len(digits)):
        if curr_digit == digits[i]:
            total += int(curr_digit)
        curr_digit = digits[i]

    if digits[0] == digits[-1]:
        total += int(digits[0])

    return total


def captcha(digits):
    total = 0
    step = len(digits)/2

    for i in range(len(digits)):
        if digits[i] == digits[(i + step) % len(digits)]:
            total += int(digits[i])

    return total


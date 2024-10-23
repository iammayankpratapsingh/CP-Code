def my_atoi(s):
    s = s.strip()
    if not s:
        return 0
    sign = -1 if s[0] == '-' else 1
    if s[0] in ['-', '+']:
        s = s[1:]
    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    result *= sign
    return max(-2**31, min(result, 2**31 - 1))

if __name__ == "__main__":
    s = "42"
    print("String to Integer:", my_atoi(s))

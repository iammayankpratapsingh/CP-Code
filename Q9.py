def str_str(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

if __name__ == "__main__":
    haystack = "hello"
    needle = "ll"
    print(str_str(haystack, needle))

def length_of_longest_substring(s):
    char_map = {}
    max_len = start = 0
    for i, char in enumerate(s):
        if char in char_map and char_map[char] >= start:
            start = char_map[char] + 1
        char_map[char] = i
        max_len = max(max_len, i - start + 1)
    return max_len

if __name__ == "__main__":
    s = "abcabcbb"
    print("Length of Longest Substring:", length_of_longest_substring(s))

def first_uniq_char(s):
    count = {}
    for c in s:
        count[c] = count.get(c, 0) + 1
    for i in range(len(s)):
        if count[s[i]] == 1:
            return i
    return -1

if __name__ == "__main__":
    s = "loveleetcode"
    print("First non-repeating character index:", first_uniq_char(s))

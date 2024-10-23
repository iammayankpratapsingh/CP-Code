def is_unique(s):
    return len(set(s)) == len(s)

if __name__ == "__main__":
    s = "abcde"
    print("Has all unique characters:", is_unique(s))

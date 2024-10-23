from collections import defaultdict

def group_anagrams(strs):
    anagrams = defaultdict(list)
    for word in strs:
        key = tuple(sorted(word))
        anagrams[key].append(word)
    return list(anagrams.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(group_anagrams(strs))

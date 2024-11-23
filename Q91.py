from collections import deque

def wordLadder(beginWord, endWord, wordList):
    wordList = set(wordList)
    if endWord not in wordList:
        return 0
    queue = deque([(beginWord, 1)])
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        for i in range(len(word)):
            for char in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + char + word[i+1:]
                if new_word in wordList:
                    wordList.remove(new_word)
                    queue.append((new_word, length + 1))
    return 0

print(wordLadder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))

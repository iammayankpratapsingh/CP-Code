from itertools import permutations

def cryptarithmeticPuzzle():
    letters = 'SENDMORY'
    for perm in permutations('0123456789', len(letters)):
        letter_map = dict(zip(letters, perm))
        send = int(''.join([letter_map[c] for c in 'SEND']))
        more = int(''.join([letter_map[c] for c in 'MORE']))
        money = int(''.join([letter_map[c] for c in 'MONEY']))
        if send + more == money:
            return {'SEND': send, 'MORE': more, 'MONEY': money}
    return {}

print(cryptarithmeticPuzzle())

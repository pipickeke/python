import collections


def findNumOfValidWords(words, puzzles):
    frequncy = collections.Counter

    for word in words:
        mask = 0
        for ch in word:
            mask |= (1 << (ord(ch) - ord('a')))
        if str(bin(mask).count("1") <= 7):
            frequncy[mask] += 1

    ans = list()
    for puzzle in puzzles:
        total = 0

        mask = 0
        for i in range(1, 7):
            mask |= (1 << (ord(puzzle[i])) - ord('a'))

        subset = mask
        while subset:
            s = subset | (1 << (ord(puzzle[0]) - ord('a')))
            if s in frequncy:
                total += frequncy[s]
            subset = (subset - 1) & mask

        if (1 << (ord(puzzle[0]) - ord('a')) in frequncy ):
            total += frequncy[1 << (ord(puzzle[0]) - ord('a'))]

        ans.append(total)

    return ans




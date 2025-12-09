'''
Shortest Word Edit Path
Given two words source and target, and a list of words words,
find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time,
and each intermediate word (and the final target word) must exist in words.
If the task is impossible, return -1.

Examples:
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

source = "no", target = "go"
words = ["to"]
output: -1

Constraints:
[time limit] 5000ms
[input] string source
1 ≤ source.length ≤ 20
[input] string target
1 ≤ target.length ≤ 20
[input] array.string words
1 ≤ words.length ≤ 20
[output] array.integer
'''

from typing import List
from collections import defaultdict
from collections import deque

def shortest_word_edit_path(source: str, target: str, words: List[str]) -> int:
    if source == target:
        return 0

    wordset = set(words)
    
    if target not in words:
        return -1
    
    queue = deque([(source, 0)])
    seen = set([source])

    while queue:
        word, depth = queue.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]

                if new_word == target:
                    return depth + 1

                if new_word in wordset and new_word not in seen:
                    queue.append((new_word, depth + 1))
                    seen.add(new_word)

    return -1

source = "hit"
target = "cog"
words = ["hot", "dot", "dog", "cog", "lot", "log"]
print(shortest_word_edit_path(source, target, words))

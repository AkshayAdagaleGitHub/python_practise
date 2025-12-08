# Smallest Substring of All Characters

from typing import List

def get_shortest_unique_substring(arr: List[str], s: str) -> str:
     count_map = {char: 0 for char in s}

     head_index = 0
     unique_count = 0
     result = ""

     for tail_index in range(len(s)):
         tail_char = s[tail_index]
         if tail_char in count_map:
             if count_map[tail_char] == 0:
                 unique_count += 1
             count_map[tail_char] += 1
         while unique_count == len(arr):
             temp_length = tail_index - head_index + 1
             if temp_length == len(arr):
                 return s[head_index:tail_index +1]
             if result == "" or temp_length < len(result):
                 result = s[head_index:tail_index + 1]

             head_char = s[head_index]
             if head_char in count_map:
                 count_map[head_char] -= 1
                 if count_map[head_char] == 0:
                     unique_count -= 1
             head_index += 1

     return result

# def __main__():
arr = ["x", "y", "z"]
s="xyyzyzyx"
print(get_shortest_unique_substring(arr, s))

# if __name__ == '__main__':
#     __main__()
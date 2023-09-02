# https://leetcode.com/problems/merge-strings-alternately/

class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    merged = []
    for w1, w2 in zip(word1, word2):
        merged.append(w1)
        merged.append(w2)
    merged += word1[len(word2):]
    merged += word2[len(word1):]
    return "".join(merged)

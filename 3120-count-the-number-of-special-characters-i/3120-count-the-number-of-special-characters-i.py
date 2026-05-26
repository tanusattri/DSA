class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        char_set= set(word)
        count=0
        for char in char_set:
            if char.islower():
                if char.upper() in char_set:
                    count+=1
        return count 
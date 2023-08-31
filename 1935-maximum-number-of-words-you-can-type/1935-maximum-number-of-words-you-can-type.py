class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        words = text.split()
        for word in words:
            for letter in brokenLetters:
                if letter in word:
                    break;
            else:
                count += 1

        return count
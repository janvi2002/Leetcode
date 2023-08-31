class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        text=text.split(' ')
        for i in text:
            for j in brokenLetters:
                if j in i:
                    c+=1
                    break
        return len(text)-c
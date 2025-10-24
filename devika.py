class Solution:
    def isPalindrome(self, s: str) -> bool:
        self.s = s
        line = ''

        #normalising input
        for i in s:
            if i.isalpha() or i.isnumeric():
                line += i.lower()

        for i in range(len(line)-1):
            if line[i] != line[len(line)-1-i]:
                return False
        return True
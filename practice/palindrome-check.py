class Solution:
    def isPalindrome(self, word: str) -> bool:
        # Write your code here
        if word == word[::-1]:
            return True
        else:
            return False

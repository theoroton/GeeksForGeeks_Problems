class Solution:
    def reverseWords(self, s):
        split_s = s.split(".") # Split the words of the sting based on "."
        array_s = list(filter(None, split_s)) # Delete empty words generated on split
        array_s.reverse() # Reverse the array of words
        return ".".join(array_s) # Join the reversed words with "."
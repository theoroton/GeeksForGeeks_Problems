class Solution:
    def longestCommonPrefix(self, arr):
        arr.sort() # Sort words by alphabetical order
        
        # Get first and last word of the sorted array
        first_word = arr[0]
        last_word = arr[-1]
        
        common_prefix = ""
        # Compare first and last word 
        # (those 2 words being at each end or the sorted array allows us to make the assumption that they have the most different prefix between them)
        for idx in range(0, len(first_word)):
            # If we find same character in order => add it to the prefix
            if first_word[idx] == last_word[idx]:
                common_prefix += first_word[idx]
            # Else => stop iterating
            else:
                break
                
        return common_prefix
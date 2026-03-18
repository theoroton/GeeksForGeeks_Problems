class Solution:
    def segregate0and1(self, arr):
        start_idx = 0 # Index to which send a zero element
        
        # Iterate over each element
        for idx in range(0, len(arr)):
            # If element is a zero
            if arr[idx] == 0:
                # Add it to the start of the array
                temp_e = arr[idx]
                arr[idx] = arr[start_idx]
                arr[start_idx] = temp_e
                start_idx += 1
            
        return arr
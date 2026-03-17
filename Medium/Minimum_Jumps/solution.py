class Solution:
    def minJumps(self, arr):
        jumps = 0 # Number of jumps to reach the end of the array
        idx = 0 # Current index from which we need to jump
        can_reach_end = False # Bool which indicate if we can reach the end of the array
        
        # While the end of the array hasn't been reach yet
        while not can_reach_end:
            # If we can't jump anywhere from current position => we can't reach the end of the array
            if arr[idx] == 0:
                jumps = -1
                break
            # If we can reach the end from the current position => we stop iterating
            elif idx + arr[idx] >= len(arr) - 1:
                can_reach_end = True
                jumps += 1
            # Else, we search for the next index to jump to
            else:
                max_next_jump = 0
                next_jump = idx
                # For all the next indexes we can reach => search the one who maximize the distance [steps to next jump + steps possible on next jump]
                for nidx in range(idx + 1, idx + arr[idx] + 1):
                    if nidx + arr[nidx] > max_next_jump:
                        max_next_jump = nidx + arr[nidx]
                        next_jump = nidx
                        
                # Prepare next jump
                idx = next_jump
                jumps += 1
       
        return jumps
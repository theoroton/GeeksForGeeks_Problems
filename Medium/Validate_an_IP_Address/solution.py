class Solution:
    def isValid(self, s):
        split_s = s.split(".") # Split the string on "."
        
        # If there is not 4 seperate substrings, the IP address is not valid
        if len(split_s) != 4:
            return False
        
        # For each substring
        for ss in split_s:
            # If the length of the substring is not included 1 and 3, the IP address is not valid
            if len(ss) == 0 or len(ss) > 3:
                return False
            
            # If there is a leading zero when the substring is 2 or 3 length long, the IP address is not valid
            if len(ss) > 1 and ss[0] == "0":
                return False
                
            # If the integer value of the substring is not included between 0 and 255, the IP address is not valid
            int_ss = int(ss)
            if int_ss < 0 or 255 < int_ss:
                return False
        
        return True
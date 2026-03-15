class Solution:
    def getAngle(self, s: str) -> float:
        H, M = (int(t) for t in s.split(":")) # Get Hours and Minutes
        H = H%12 # To fit 24 hours format on 12 hours format
        M_angle = M*6 # Minutes * 6° (360°/60 minutes => 6° equals a minute)
        H_angle = H*30 + M*0.5 # Hours * 30° (360°/12 hours => 30° equals a hour) + Minutes * 0.5° (30°/60 minutes => 0.5° equals 1 minute during the hour)
        angle = abs(M_angle - H_angle)
        return min(angle, 360-angle) # Return smallest angle
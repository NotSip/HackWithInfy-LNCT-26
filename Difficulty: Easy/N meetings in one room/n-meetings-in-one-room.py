class Solution:
    
    def maximumMeetings(self,start,end):
        n = len(start)
        meetings = []
        for k in range(n):
            meetings.append((start[k],end[k]))
            
        meetings.sort(key=lambda x: x[1])
        count = 0
        last_end = -1
        for m in meetings:
            current_start = m[0]
            current_end = m[1]
            
            if current_start > last_end:
                count +=1
                last_end = current_end
                
        return count
            
        
                
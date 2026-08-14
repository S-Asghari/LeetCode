class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        times = []
        for s, e in intervals:
            times.append((s, 's'))
            times.append((e, 'e'))
        times = sorted(times, key=lambda x: (x[0], x[1]))
        print(times)
        rooms = 0
        
        curRooms = 0
        for t, k in times:
            if k == 's':
                curRooms += 1
                rooms = max(rooms, curRooms)
            else: # k == 'e'
                curRooms -= 1
        
        return rooms
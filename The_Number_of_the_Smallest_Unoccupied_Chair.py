import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        newArr = []

        for i in range(len(times)):
            newArr.append((times[i][0], 1, i))
            newArr.append((times[i][1], -1, i))
        
        newArr.sort(key=lambda x: (x[0], x[1]))

        availableSeats = list(range(len(times)))
        
        friendSeat = [-1] * len(times)

        for time in newArr:
            if time[1] == -1:
                heapq.heappush(availableSeats, friendSeat[time[2]])
            else:
                seat = heapq.heappop(availableSeats)
                friendSeat[time[2]] = seat

                if time[2] == targetFriend:
                    return seat

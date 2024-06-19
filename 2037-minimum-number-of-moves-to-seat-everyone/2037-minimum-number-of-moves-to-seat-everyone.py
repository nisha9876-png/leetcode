class Solution(object):
    def minMovesToSeat(self, seats, students):
        """
        :type seats: List[int]
        :type students: List[int]
        :rtype: int
        """
        seats.sort()
        students.sort()
        n = len(seats)
        min_moves = 0
        for i in range(n):
            min_moves += abs(seats[i] - students[i])
        
        return min_moves
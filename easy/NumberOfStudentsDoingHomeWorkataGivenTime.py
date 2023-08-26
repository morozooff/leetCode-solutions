class Solution:
    def busyStudent(self, startTime, endTime, queryTime):
        counter = 0
        for i in range(len(startTime)):

            if queryTime in range(startTime[i], endTime[i] + 1):
                counter += 1

            else:
                pass

        return counter
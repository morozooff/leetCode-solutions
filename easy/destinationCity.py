class Solution:
    def destCity(self, paths):
        departure_point = []
        destination_point = []
        for path in paths:
            departure_point.append(path[0])
            destination_point.append(path[1])
        result_point = list(set(destination_point) - set(departure_point))
        return result_point[0]
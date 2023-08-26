class Solution:
    def largestAltitude(self, gain) -> int:
        current_altitude = 0
        altitudes = [current_altitude]

        for diff in gain:
            altitude = current_altitude + diff
            altitudes.append(altitude)
            current_altitude = altitude

        return max(altitudes)
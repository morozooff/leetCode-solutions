class Solution:
    def maximumUnits(self, boxTypes: list, truckSize: int) -> int:
        maximum_units = 0

        boxTypes.sort(reverse=True, key=lambda x: x[1])

        for box in boxTypes:

            if truckSize <= 0:
                break

            diff = box[0] - truckSize
            if diff <= 0:
                box_num = box[0]
            else:
                box_num = box[0] - diff

            truckSize -= box_num
            box_power = box_num * box[1]
            maximum_units += box_power

        return maximum_units
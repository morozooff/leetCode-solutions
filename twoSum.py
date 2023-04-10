def twoSum(nums, target):
        result = []
        isSoluted = False
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] + nums[j] == target:
                    result.append(i)
                    result.append(j)
                    isSoluted = True
                else:
                    continue
            if isSoluted:
                break
        return result

list = [3, 2, 4]
print(twoSum(list, 6))
def findDifference(nums1, nums2):
    distinct_nums1 = set(nums1)
    distinct_nums2 = set(nums2)
    mutual = distinct_nums1 & distinct_nums2
    answer = [list(distinct_nums1 - mutual), list(distinct_nums2 - mutual)]
    return answer
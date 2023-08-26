class Solution:
    def maximumWealth(self, accounts) -> int:
        return(max([sum(sub_list) for sub_list in accounts]))
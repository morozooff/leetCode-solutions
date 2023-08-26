class Solution:
    def countMatches(self, items: list, ruleKey: str, ruleValue: str) -> int:

        keys = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        match_counter = 0

        for item in items:
            key_num = keys[ruleKey]
            if item[key_num] == ruleValue:
                match_counter += 1

        return match_counter


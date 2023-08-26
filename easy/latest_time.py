class Solution:
    def maximumTime(self, time: str) -> str:

        def IsKnown(symb):
            return not symb == '?'

        def IsNotKnown(symb):
            return symb == '?'

        new_time = ''
        time_parts = time.split(':')
        after_20 = ['0', '1', '2', '3']
        not_20 = ['0', '1']

        if IsNotKnown(time_parts[0][0]) and IsNotKnown(time_parts[0][1]):
            new_time += '23:'
        elif IsNotKnown(time_parts[0][0]) and IsKnown(time_parts[0][1]):
            if time_parts[0][1] in after_20:
                new_time += f'2{time_parts[0][1]}:'
            else:
                new_time += f'1{time_parts[0][1]}:'
        elif IsKnown(time_parts[0][0]) and IsNotKnown(time_parts[0][1]):
            if time_parts[0][0] in not_20:
                new_time += f'{time_parts[0][0]}9:'
            else:
                new_time += f'{time_parts[0][0]}3:'
        else:
            new_time += time_parts[0] +':'



        if IsNotKnown(time_parts[1][0]) and IsNotKnown(time_parts[1][1]):
            new_time += '59'
        elif IsKnown(time_parts[1][0]) and IsKnown(time_parts[1][1]):
            new_time += time_parts[1]
        elif IsNotKnown(time_parts[1][0]) and time_parts[1][1] == "0":
            new_time += '50'
        elif IsNotKnown(time_parts[1][1]):
            new_time += f'{time_parts[1][0]}9'
        else:
            new_time += f'5{time_parts[1][1]}'

        return new_time
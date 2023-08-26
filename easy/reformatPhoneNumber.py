import re


class Solution:
    def reformatNumber(self, number: str) -> str:

        def deleteExtraSymbols(number: str) -> str:
            number_strings = re.findall(r'\d+', number)
            solid_string = ''
            for string in number_strings:
                solid_string += string

            return solid_string

        def isStringDivideOnThree(number: str) -> bool:
            if len(number) % 3 == 0:
                return True
            else:
                return False

        def divideIntoSections(number: str) -> str:
            dividing_string = ''

            while number != '':
                if isStringDivideOnThree(number):
                    sectors = re.findall(r'.{3}', number)
                    part_of_string = ' '.join(sectors)
                    dividing_string = part_of_string + ' ' + dividing_string
                    number = ''
                else:
                    dividing_string = number[len(number) - 2:len(number)] + ' ' + dividing_string
                    number = number[:len(number) - 2]
                    continue

            return dividing_string.strip()

        number = deleteExtraSymbols(number)
        print(number)
        sections_string = divideIntoSections(number)
        print(sections_string)
        return sections_string.replace(' ', '-')
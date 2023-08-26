class Solution:
    def countStudents(self, students, sandwiches) -> int:
        def get_out_from_queue():
            sandwiches.pop(0)
            students.pop(0)

        def is_possible_to_eat_sandwich():

            if sandwiches == []:
                return False

            if sandwiches[0] not in students:
                return False

            return True

        while is_possible_to_eat_sandwich():
            current_sandwich = sandwiches[0]
            current_student_preference = students[0]

            if current_sandwich == current_student_preference:
                get_out_from_queue()
            else:
                student_for_transition = students.pop(0)
                students.append(student_for_transition)

        return len(students)
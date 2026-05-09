class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        student_choice = {0: 0, 1: 0}
        for s in students:
            student_choice[s] += 1
        
        while students and sandwiches:
            student = students[0]
            sandwich = sandwiches[0]
            if student == sandwich:
                student_choice[student] -= 1
                students.pop(0)
                sandwiches.pop(0)
            else:
                if student_choice[sandwich] == 0:
                    return len(students)
                else:
                    students = students[1:] + [student]
        
        return 0
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)
 
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'       

    def average_student (self):
        numbers = []

        for number in self.grades.values():
            numbers.extend(number)
        if len(numbers) > 0:    
            Result = sum(numbers) / len(numbers) 
        else:
            Result = 0
        return Result

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)

        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: '
            f'{self.average_student():.1f}\n'
            f'Курсы в процессе изучения: {courses_in_progress}\n'
            f'Завершенные курсы: {finished_courses}\n'
        )
    def __eq__(self, other):
        return self.average_student() == other.average_student()

    def __gt__(self, other):
        return self.average_student() > other.average_student()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
  
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'  

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_lecturer (self):
        numbers = []

        for number in self.grades.values():
            numbers.extend(number)
        if len(numbers) > 0:    
            Result = sum(numbers) / len(numbers) 
        else:
            Result = 0
        return Result 

    def __str__(self):

        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: '
            f'{self.average_lecturer():.1f}\n'
        )        
    def __eq__(self, other):
        return self.average_lecturer() == other.average_lecturer()

    def __gt__(self, other):
        return self.average_lecturer() > other.average_lecturer()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
   
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'   
 
    def __str__(self):

        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
        )

 
lecturer = Lecturer("Иван", "Иванов")
lecturer_1 = Lecturer("Иван", "Петров")
lecturer_2 = Lecturer("Петр", "Иванов")
reviewer = Reviewer("Петр", "Петров")
reviewer_1 = Reviewer("Михаил", "Петров")  
reviewer_2 = Reviewer("Петр", "Михайлов")        
student = Student('Алёхина', 'Ольга', 'Ж')
student_1 = Student('Алёхин', 'Олег', 'М')
student_2 = Student('Калугин', 'Олег', 'М')
 
student_1.courses_in_progress += ['Python', 'Java']
student_2.courses_in_progress += ['C++', 'Java']
lecturer_1.courses_attached += ['Python', 'C++']
lecturer_2.courses_attached += ['Python', 'Java']
reviewer_1.courses_attached += ['Python', 'Java']
reviewer_2.courses_attached += ['Python', 'C++']
student_1.rate_lecture(lecturer_1, 'Python', 7) 
student_1.rate_lecture(lecturer_2, 'Python', 7) 
student_1.rate_lecture(lecturer_1, 'Java', 10) 
reviewer_1.rate_hw(student_1, 'Python', 10) 
reviewer_1.rate_hw(student_1, 'Java', 10) 
reviewer_2.rate_hw(student_2, 'java', 9)  

def avg_grade_all_students(student_list, course_name):
    all_grades = []
    for student in student_list:
        if isinstance(student, Student) and course_name in student.grades:
            all_grades.extend(student.grades[course_name])
    if not all_grades:
        return f"Нет оценок по курсу '{course_name}'"

    return sum(all_grades) / len(all_grades)        

def avg_grade_all_lecturers(lecturers_list, course_name):
    all_grades = []

    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in lecturer.grades:
            all_grades.extend(lecturer.grades[course_name])

    if not all_grades:
        return f"Нет оценок по курсу '{course_name}'"

    return sum(all_grades) / len(all_grades)

avg_students_python = avg_grade_all_students([student_1, student_2], "Python")
avg_lecturers_python = avg_grade_all_lecturers([lecturer_1, lecturer_2], "Python")

print(f"Средняя оценка всех студентов по курсу 'Python': {avg_students_python:.1f}")
print(f"Средняя оценка всех лекторов по курсу 'Python': {avg_lecturers_python:.1f}")


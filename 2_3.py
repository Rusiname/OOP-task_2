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
reviewer = Reviewer("Петр", "Петров")      
student = Student('Алёхина', 'Ольга', 'Ж')
student_1 = Student('Алёхин', 'Олег', 'М')
 
student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']
 
print(student.rate_lecture(lecturer, 'Python', 7))   # None
print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 

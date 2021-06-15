class Student:
  students_list = []
  def __init__(self, name, surname, gender):
    self.name = name                                  
    self.surname = surname                            
    self.gender = gender                              
    self.finished_courses = []                        
    self.courses_in_progress = []                     
    self.grades = {}
    Student.students_list.append(self)
                          
  def add_courses(self, course_name):
    self.finished_courses.append(course_name)
    print('Данный курс добавлен в список завершённых курсов') 
    
  def evaluation_lecturer(self, course, lecturer, mark):
    if isinstance(self, Student) and course in self.courses_in_progress and course in lecturer.courses_attached:
      lecturer.marks.append(mark)
      print('Спасибо за оценку выставленную лектору')
    else:
      print('Ошибка, проверьте правильность введенных данных')

  def average(self):
    for self.marks in self.grades.values():
      x = sum(self.marks) / len(self.marks)
    return x

  def __str__(self):
    reviewer = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average()}
Курсы в процессе изучения: {self.courses_in_progress}
Заверешенные курсы: {self.finished_courses}'''
    return reviewer

  def __lt__(self, other):
    if not isinstance(other, Student):
      print ('Данный человек не является представителем класса Student')
      return 
    else:
      for self.grade in self.grades.values():
        self.mark = sum(self.grade) / len(self.grade)
      for other.grade in other.grades.values():
        other.mark = sum(other.grade) / len(other.grade)
        if self.mark < other.mark:
          print('Ваши оценки хуже чем у вашего товарища, стоит начать усерднее трудится')
        else:
          print('У вас очень хорошие оценки продолжайте в том же духе')
        return self.mark < other.mark

def average_course(list_students, course):
  marks_list = []
  for people in list_students:
    if course in people.courses_in_progress:
      for marks in people.grades.values():
        marks_list += marks
    else:
      print('Данный студент не обучается на этом курсе')   
  if True:
    marks = sum(marks_list) / len(marks_list)
    print(marks)
  

class Mentor:
  def __init__(self, name, surname):
    self.name = name                                 
    self.surname = surname                            

class Lecturer(Mentor):
  lecturers_list = []
  def __init__(self, name, surname):
    super().__init__(name, surname)
    self.courses_attached = []
    self.marks = []
    Lecturer.lecturers_list.append(self)

  def __str__(self):
    reviewer = f'''
Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {sum(self.marks) / len(self.marks)}'''
    return reviewer  

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Данный человек не является представителем класса Lecturer')
      return
    else:
      self.average = sum(self.marks) / len(self.marks)
      other.average = sum(other.marks) / len(other.marks)
      if self.average < other.average:
        print('Ученики вас не очень любят, стоит пересмотреть свои методы преподавания')
      else:
        print('Вы прекрасный преподаватель, ученики вас очень любят!)))')
      return self.average < other.average

def average_course_lecturer(list_lecturers, course):
  grades_list = []
  for lecturer in list_lecturers:
    if course in lecturer.courses_attached:
      grades_list += lecturer.marks
    else:
      print('Данный лектор не ведет лекции на данном курсе') 
  if True:
    grades = sum(grades_list) / len(grades_list)
    print(grades) 

class Reviewer(Mentor):
  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []

  def rate_hw(self, student, course, grade):            
    if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
      if course in student.grades:
        student.grades[course] += [grade]
        print('Оценка выставлена')
      else:
        student.grades[course] = [grade]
        print('Оценка выставлена')
    else:
      return 'Ошибка'
  
  def __str__(self):
    reviewer = f'''
Имя: {self.name}
Фамилия: {self.surname}'''
    return reviewer  

peter = Student('Питер', 'Паркер', 'мужской')
olga = Student('Ольга', 'Иванова', 'женский')
oleg = Lecturer('Олег', 'Булыгин')
jeny = Lecturer('Евгений', 'Шмаргунов')
sasha = Reviewer('Александр', 'Бардин')
philipp = Reviewer('Филипп', 'Воронов')

peter.add_courses('Введение в программирование')
olga.add_courses('Java - разработчикк  нуля')

peter.courses_in_progress.append('Python')
olga.courses_in_progress.append('Python')

oleg.courses_attached.append('Python')
peter.evaluation_lecturer('Python', oleg,  10)
olga.evaluation_lecturer('Python', oleg, 8)

jeny.courses_attached.append('Python')
peter.evaluation_lecturer( 'Python', jeny, 9)
olga.evaluation_lecturer( 'Python', jeny, 3)

peter.grades['Python'] = [3, 4, 5, 3]
olga.grades['Python'] = [5, 4, 5, 5]
print(peter)
print(olga)

print(peter < olga)
print(olga < peter)

print(oleg)
print(jeny)

print(oleg < jeny)
print(jeny < oleg) 

sasha.courses_attached.append('Python')
philipp.courses_attached.append('Python')
sasha.rate_hw(peter, 'Python', 5)
philipp.rate_hw(olga, ' Python', 4)

print(sasha)
print(philipp)

average_course(Student.students_list, 'Python')
average_course_lecturer(Lecturer.lecturers_list, 'Python')
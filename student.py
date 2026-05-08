class Student:
    def __init__(self, student_id, name, major):
        self.student_id = student_id
        self.name = name
        self.major = major

students = []

def add_student(student_id, name, major):
    for s in students:
        if s.student_id == student_id:
            return False
    new_student = Student(student_id, name, major)
    students.append(new_student)
    return True

def get_all_students():
    return students

def search_student_by_id(student_id):
    for s in students:
        if s.student_id == student_id:
            return s
    return None

def delete_student(student_id):
    global students
    initial_length = len(students)
    students = [s for s in students if s.student_id != student_id]
    return len(students) < initial_length
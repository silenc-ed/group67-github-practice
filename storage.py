import json
from student import Student

def save_data(students, filename="data.json"):
    data = []
    for s in students:
        data.append({"id": s.student_id, "name": s.name, "major": s.major})
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename="data.json"):
    students = []
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
            for item in data:
                students.append(Student(item["id"], item["name"], item["major"]))
    except FileNotFoundError:
        pass
    return students

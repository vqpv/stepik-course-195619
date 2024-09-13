def create_student(name, age, marks=None):
    return {
        'name': name,
        'age': age,
        'marks': marks or []
    }


def add_mark(student, mark):
    student['marks'].append(mark)

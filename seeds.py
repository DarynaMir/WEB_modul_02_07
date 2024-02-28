from random import randint, choice
from datetime import datetime
from faker import Faker
from conf.db import session
from models import Teacher, Student, Group, Subject, Grade

fake = Faker('uk-UA')

def seed_database():
    groups = [Group(name=f'Group {i}') for i in range(1, 4)]
    session.add_all(groups)
    session.commit()

    teachers = [Teacher(name=fake.name()) for _ in range(3)]
    session.add_all(teachers)
    session.commit()

    subjects = [Subject(name=fake.word(), teacher_id=choice(teachers).id) for _ in range(5)]
    session.add_all(subjects)
    session.commit()

    students = [Student(fullname=fake.name(), group_id=choice(groups).id) for _ in range(30)]
    session.add_all(students)
    session.commit()

    current_date = datetime.now()

    for student in students:
        for subject in subjects:
            grades_count = randint(1, 20)
            for _ in range(grades_count):
                grade_value = randint(1, 12)
                grade = Grade(student_id=student.id, subject_id=subject.id, grade=grade_value, grade_date=current_date)
                session.add(grade)
    session.commit()

    print("Database seeded successfully.")

if __name__ == "__main__":
    seed_database()

from sqlalchemy import func, desc, select, and_

from models import Grade, Teacher, Student, Group, Subject
from conf.db import session


def select_01():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS avg_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id, s.fullname
    ORDER BY avg_grade DESC
    LIMIT 5
    """

    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade),2).label('avg_grade')) \
        .select_from(Student).join(Grade).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    return result

if __name__== "__main__":
    print(select_01())

def select_02():
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade),2) AS avg_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE g.subject_id = 8
    GROUP BY s.id, s.fullname
    ORDER BY avg_grade DESC
    LIMIT 1;
    """

    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade),2).label('avg_grade')) \
        .select_from(Student).join(Grade).filter(Grade.subject_id == 1).group_by(Student.id).order_by(desc('avg_grade')).limit(1).all()
    return result

if __name__== "__main__":
    print(select_02())


def select_03():
    """
    SELECT
        s.group_id,
        ROUND(AVG(g.grade),2) AS avg_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE g.subject_id = 3
    GROUP BY s.group_id;
    """

    result = session.query(Student.group_id, func.round(func.avg(Grade.grade),2).label('avg_grade')) \
        .select_from(Student).join(Grade).filter(Grade.subject_id == 3).group_by(Student.group_id).all()
    return result

if __name__== "__main__":
    print(select_03())

def select_04():
    """
    SELECT
        ROUND(AVG(grade), 2) AS avg_grade
    FROM grades;
    """

    result = session.query(func.round(func.avg(Grade.grade),2).label('avg_grade')) \
        .select_from(Grade).all()
    return result

if __name__== "__main__":
    print(select_04())

def select_05():
    """
    SELECT
        name AS course_name
    FROM subjects
    WHERE teacher_id = 4;
    """

    result = session.query(Subject.name.label('course_name')) \
        .select_from(Subject).filter(Subject.teacher_id == 4).all()
    return result

if __name__== "__main__":
    print(select_05())

def select_06():
    """
    SELECT
        fullname AS student_name
    FROM students
    WHERE group_id = 1;
    """

    result = session.query(Student.fullname.label('student_name')) \
        .select_from(Student).filter(Student.group_id == 1).all()
    return result

if __name__== "__main__":
    print(select_06())

def select_07():
    """
    SELECT
        s.fullname AS student_name,
        g.grade,
        g.grade_date
    FROM students s
    JOIN grades g ON s.id = g.student_id
    WHERE s.group_id = 1 AND g.subject_id = 2;
    """

    result = session.query(Student.fullname.label('student_name'), Grade.grade, Grade.grade_date) \
        .select_from(Student).join(Grade).filter(and_(Student.group_id == 1, Grade.subject_id == 2)).all()
    return result

if __name__== "__main__":
    print(select_07())

def select_08():
    """
   SELECT
        t.name AS teacher_name,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM teachers t
    JOIN subjects s ON t.id = s.teacher_id
    JOIN grades g ON s.id = g.subject_id
    GROUP BY t.name;
    """

    result = session.query(Teacher.name.label('teacher_name'),func.round(func.avg(Grade.grade), 2).label('avg_grade')) \
        .select_from(Teacher).join(Subject).join(Grade).group_by(Teacher.name).all()
    return result

if __name__== "__main__":
    print(select_08())

def select_09():
    """
   SELECT
        DISTINCT sub.name AS subject_name
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects sub ON g.subject_id = sub.id
    WHERE s.fullname = 'Дарина Панчук';
    """

    result = session.query(func.distinct(Subject.name.label('subject_name'))) \
        .select_from(Student).join(Grade).join(Subject) \
        .filter(Student.fullname == 'Дарина Панчук').all()
    return result

if __name__== "__main__":
    print(select_09())


def select_10():
    """
   SELECT
    DISTINCT
        sub.name AS subject_name
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects sub ON g.subject_id = sub.id
    JOIN teachers t ON sub.teacher_id = t.id
    WHERE s.fullname = 'Мартин Рябошапка'
    AND t.name = 'Ярина Павлик';
    """

    result = session.query(func.distinct(Subject.name.label('subject_name'))) \
        .select_from(Student).join(Grade).join(Subject).join(Teacher) \
        .filter(and_(Student.fullname == 'Дарина Панчук', Teacher.name == 'Ярослав Ірванець')).all()
    return result

if __name__== "__main__":
    print(select_10())

def select_11():
    """
   SELECT
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    JOIN subjects sub ON g.subject_id = sub.id
    JOIN teachers t ON sub.teacher_id = t.id
    WHERE s.fullname = 'Дарина Панчук'
    AND t.name = 'Ярослав Ірванець';
    """

    result = session.query(func.round(func.avg(Grade.grade),2).label('avg_grade')) \
        .select_from(Student).join(Grade).join(Subject).join(Teacher) \
        .filter(and_(Student.fullname == 'Дарина Панчук', Teacher.name == 'Ярослав Ірванець')).all()
    return result

if __name__== "__main__":
    print(select_11())
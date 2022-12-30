import peewee as pw

from python.config import BaseModel, db


class Student(BaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=20, null=False, unique=True)
    password_ = pw.CharField(max_length=20, null=False)
    phone = pw.CharField(max_length=15, null=False)
    address = pw.CharField(max_length=50, null=False)


class Admin(BaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=20, null=False, unique=True)
    password_ = pw.CharField(max_length=20, null=False)
    phone = pw.CharField(max_length=15, null=False)
    address = pw.CharField(max_length=50, null=False)


class Teacher(BaseModel):
    id = pw.IntegerField(primary_key=True)
    surname = pw.CharField(max_length=20, null=False)
    name = pw.CharField(max_length=20, null=False)
    education = pw.CharField(max_length=50, null=False)
    teaching_exp = pw.SmallIntegerField(null=False)
    vocal_exp = pw.SmallIntegerField(null=False)
    description = pw.CharField(max_length=500)


class Cabinet(BaseModel):
    id = pw.IntegerField(primary_key=True)
    number = pw.SmallIntegerField(null=False)
    building = pw.SmallIntegerField(null=False)


class Module(BaseModel):
    id = pw.IntegerField(primary_key=True)
    name = pw.CharField(max_length=50, null=False)
    pg_description = pw.CharField(max_length=100)
    quantity = pw.SmallIntegerField(null=False)
    price = pw.IntegerField(null=False)


class Timetable(BaseModel):
    id = pw.IntegerField(primary_key=True)
    available = pw.BooleanField(null=False)
    time_ = pw.TimeField(null=False)
    date_ = pw.DateField(null=False)
    teacher = pw.ForeignKeyField(Teacher, on_delete='CASCADE')
    cabinet = pw.ForeignKeyField(Cabinet, on_delete='CASCADE')
    type = pw.CharField(max_length=20, null=False)


class Student_Module(BaseModel):
    id = pw.IntegerField(primary_key=True)
    student = pw.ForeignKeyField(Student, on_delete='CASCADE')
    module = pw.ForeignKeyField(Module, on_delete='CASCADE')
    quantity = pw.SmallIntegerField()


class Timetable_Student_Module(BaseModel):
    id = pw.IntegerField(primary_key=True)
    timetable = pw.ForeignKeyField(Timetable, on_delete='CASCADE')
    student_module = pw.ForeignKeyField(Student_Module, on_delete='CASCADE')


with db:
    db.create_tables([
        Student, Admin, Teacher, Cabinet, Module, Timetable, Student_Module, Timetable_Student_Module
    ])

from django.db import models


class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    address = models.TextField()
    guardian_parent_name = models.CharField(max_length=80)
    guardian_parent_contact = models.CharField(max_length=10)
    guardian_parent_profession = models.CharField(max_length=80)

    def __str__(self):
        return self.email


class Department(models.Model):
    name = models.CharField(max_length=100)
    acronym = models.CharField(max_length=100)

    def __str__(self):
        return self.acronym


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    hall_ticket_number = models.CharField(max_length=100, unique=True)
    gender = models.BooleanField()
    caste = models.CharField(max_length=100)
    career_goal = models.TextField()

    tenth_marks = models.IntegerField()
    inter_marks = models.IntegerField()

    btech_marks = models.IntegerField(default=-1)
    backlogs = models.IntegerField(default=-1)

    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name + " - " + self.hall_ticket_number


class Marks(models.Model):
    subject_code = models.CharField(max_length=15)
    subject_name = models.CharField(max_length=100)
    internal_marks = models.IntegerField()
    external_marks = models.IntegerField()
    total_marks = models.IntegerField()
    result = models.CharField(max_length=10)

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="marks")

    def __str__(self):
        return self.subject_code+" "+str(self.external_marks)+" "+self.result



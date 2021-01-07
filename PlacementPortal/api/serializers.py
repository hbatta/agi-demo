from rest_framework.serializers import ModelSerializer

from PlacementPortal.models import *


class DepartmentSerializer(ModelSerializer):
    class Meta:
        model = Department
        exclude = []


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        exclude = []


class MarksSerializer(ModelSerializer):
    class Meta:
        model = Marks
        exclude = []


class StudentSerializer(ModelSerializer):
    department = DepartmentSerializer()
    contact = ContactSerializer()
    marks = MarksSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        exclude = []
        # include = ['marks']

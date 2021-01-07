from rest_framework.generics import RetrieveAPIView, ListAPIView

from PlacementPortal.models import Student

from .serializers import StudentSerializer


class StudentListView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(RetrieveAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "hall_ticket_number"
    lookup_url_kwarg = "htno"


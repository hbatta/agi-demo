from django.views.generic import ListView

from PlacementPortal.models import Marks, Student


class MarkList(ListView):
    context_object_name = "marks_list"
    template_name = "PlacementPortal/marks_list.html"

    def get_queryset(self):
        queryset = Marks.objects.filter(student__id=self.kwargs['pk'])
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MarkList, self).get_context_data(**kwargs)
        context['student'] = Student.objects.get(pk=self.kwargs['pk'])
        return context



from django.views.generic import DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin


from PlacementPortal.models import Contact, Student


class ContactDetail(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "PlacementPortal/contact_detail.html"
    context_object_name = "contact"

    def get_context_data(self, **kwargs):
        context = super(ContactDetail, self).get_context_data(**kwargs)
        student_detail = Student.objects.get(pk=self.kwargs['pk'])
        student_contact = Contact.objects.get(student__id=self.kwargs['pk'])
        context.update(
            {
                'student_detail': student_detail,
                'student_contact': student_contact
            }
        )
        return context




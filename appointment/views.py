from pytils.translit import slugify
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from appointment.forms import AppointmentForm
from appointment.models import Appointment


class AppointmentListView(ListView):
    model = Appointment





class AppointmentDetailView(DetailView):
    model = Appointment


class AppointmentCreateView(CreateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("appointment:appointment_list")

    def form_valid(self, form):
        if form.is_valid():
            new_appointment = form.save()
            new_appointment.slug = slugify(new_appointment.pet_name)
            new_appointment.save()
        return super().form_valid(form)


class AppointmentUpdateView(UpdateView):
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy("appointment:appointment_list")

    def get_success_url(self):
        from django.urls import reverse

        return reverse("appointment:appointment_detail", args=[self.kwargs.get("pk")])


class AppointmentDeleteView(DeleteView):
    model = Appointment
    template_name = 'appointment/appointment_confirm_delete.html'
    success_url = reverse_lazy('appointment:appointment_list')

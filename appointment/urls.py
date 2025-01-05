from appointment.apps import AppointmentConfig
from appointment.views import AppointmentDetailView, AppointmentListView, AppointmentCreateView, AppointmentUpdateView, \
    AppointmentDeleteView

from django.urls import path


app_name = AppointmentConfig.name

urlpatterns = [
    path('', AppointmentListView.as_view(), name='appointment_list'),
    path('appointment/<int:pk>/', AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointment/create/', AppointmentCreateView.as_view(), name='appointment_create'),
    path('appointment/<int:pk>/create/', AppointmentUpdateView.as_view(), name='appointment_update'),
    path('appointment/<int:pk>/delete/', AppointmentDeleteView.as_view(), name='appointment_delete')
]

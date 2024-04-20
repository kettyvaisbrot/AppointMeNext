from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Appointment, BusinessHours, ReminderOption
from .forms import RegistrationForm
from datetime import datetime, timedelta
from django.utils import timezone



class ModelTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.reminder_option = ReminderOption.objects.create(name='Test Option')
        self.business_hours = BusinessHours.objects.create(
            monday_open_time='08:00', monday_close_time='17:00',
            tuesday_open_time='08:00', tuesday_close_time='17:00',
            wednesday_open_time='08:00', wednesday_close_time='17:00',
            thursday_open_time='08:00', thursday_close_time='17:00',
            friday_open_time='08:00', friday_close_time='17:00',
            saturday_open_time='08:00', saturday_close_time='17:00',
            sunday_open_time='08:00', sunday_close_time='17:00'
        )
        self.appointment = Appointment.objects.create(
            customer=self.user, date_time=timezone.now() + timedelta(days=1),
            time=datetime.now().time(), duration=timedelta(hours=1)
        )
        self.appointment.reminder_options.add(self.reminder_option)

    def test_user_creation(self):
        user_count = get_user_model().objects.count()
        self.assertEqual(user_count, 1)

    def test_appointment_creation(self):
        appointment_count = Appointment.objects.count()
        self.assertEqual(appointment_count, 1)

    def test_form_valid_data(self):
        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'username': 'testuser',
            'user_type': 'owner',
            'day': 'monday',
            'open_time': '08:00',
            'close_time': '17:00',
            'password1': 'testpass123!',
            'password2': 'testpass123!',
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form_data = {
            'full_name': 'Test User',
            'email': 'test@example.com',
            'phone_number': '1234567890',
            'username': 'testuser',
            'user_type': 'owner',
            'day': 'monday',
            'open_time': '08:00',
            'close_time': '17:00',
            'password1': 'testpass123!',
            'password2': 'wrongpassword',
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())

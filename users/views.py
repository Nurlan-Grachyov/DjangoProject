from django.contrib.auth import login
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView

from config.settings import EMAIL_HOST_USER
from users.forms import CustomUserCreationForm


class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('library:book_new_list')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.self_welcome_email(user.email)
        return super().form_valid(form)

    def self_welcome_email(self, user_email):
        subject = 'TEST'
        message = 'TEST'
        recipient_list = [user_email, ]
        send_mail(subject, message, EMAIL_HOST_USER, recipient_list)

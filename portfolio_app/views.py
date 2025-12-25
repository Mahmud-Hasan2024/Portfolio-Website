from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views import View
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from portfolio_app.models import Project, ContactMessage
from portfolio_app.forms import ContactForm

# Create your views here.

class HomeView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'projects'

    def get_queryset(self):
        # latest 6 projects
        return Project.objects.all()[:6]


class ProjectsView(ListView):
    model = Project
    template_name = 'projects.html'
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    # lookup by slug field
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ContactView(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'contact.html', {"form": form})

    def post(self, request):
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message_text = form.cleaned_data["message"]

            # Save in DB
            ContactMessage.objects.create(
                name=name,
                email=email,
                message=message_text
            )

            # Send email to YOU
            subject = f"New message from {name}"
            full_message = (
                f"Sender Name: {name}\n"
                f"Sender Email: {email}\n\n"
                f"Message:\n{message_text}"
            )

            send_mail(
                subject,
                full_message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],  # email where YOU receive messages
                fail_silently=False
            )

            messages.success(request, "Thanks! Your message has been sent successfully.")
            return redirect("contact")

        messages.error(request, "Please correct the errors below.")
        return render(request, "contact.html", {"form": form})

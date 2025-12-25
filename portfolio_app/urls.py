from django.urls import path
from portfolio_app.views import HomeView, ProjectsView, ProjectDetailView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='project_detail'),
    path('contact/', ContactView.as_view(), name='contact'),
]

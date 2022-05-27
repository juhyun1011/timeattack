from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.sign_up_view, name='sign-up'),
]
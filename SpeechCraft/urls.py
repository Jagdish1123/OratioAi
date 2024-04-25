# SpeechCraft/urls.py


from django.urls import path
from . import views

urlpatterns = [
    path('', views.text_to_voice, name='text_to_voice'),
    path('convert/', views.convert, name='convert')
  # Route the root URL to the text_to_voice view
]

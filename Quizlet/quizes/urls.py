from django.urls import path
from . import views
from .views import (
    QuizListView,
    quiz_view
)

app_name = 'quizes'

urlpatterns = [
    path('', QuizListView.as_view(), name='main-view'),
    path('<pk>/', views.quiz_view, name='quiz-view' ),
]

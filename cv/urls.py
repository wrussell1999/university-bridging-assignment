from django.urls import path
from . import views

urlpatterns = [
    path('', views.cv_page),
    path('new/education', views.new_education),
    path('new/experience', views.new_experience),
    path('new/skill', views.new_skill),
    path('new/project', views.new_project),
    path('remove/education/<int:pk>', views.remove_education),
    path('remove/experience/<int:pk>', views.remove_experience),
    path('remove/skill/<int:pk>', views.remove_skill),
    path('remove/project/<int:pk>', views.remove_project),
]

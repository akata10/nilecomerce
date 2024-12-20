from django.urls import path
from . import views 

urlpatterns=[
    path('register/',views.RegistrationView.as_view()),
    path('login/',views.loginview.as_view()),
    path('logout/',views.logoutView.as_view()),
    path('dashboard/',views.dashboardview.as_view()),
    path('update/',views.updateView.as_view()),
    
    ] 
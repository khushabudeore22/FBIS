from django.urls import path
from .views import login,index

urlpatterns = [
    path('', index, name="index"),
    # path('about/', about, name="about"),
    path('login/', login , name="login")
]
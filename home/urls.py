
from django.urls import path


from .views import home, services
app_name = 'home'
urlpatterns = [
    path('', home,  name="homepage"),
    path('services/', services, name="services"),
]
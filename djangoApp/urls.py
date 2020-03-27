
from django.contrib import admin
from django.urls import path
from adoptions import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'',views.home, name='home'),
    path(r'adoptions/<int:id>/', views.pet_details, name='pet_details'),
]

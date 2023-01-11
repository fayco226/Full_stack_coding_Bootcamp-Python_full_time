from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home" ),
    path('delete/<id>', views.home, name= "delete" ),
    path('rent/rental/', views.rentallist, name="rental_list" ),
]
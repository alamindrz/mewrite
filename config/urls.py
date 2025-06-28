from django.contrib import admin
from django.urls import path, include
from notes import views as note_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notes/', include('notes.urls')),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('signup/', note_views.signup_view, name='signup'),
]
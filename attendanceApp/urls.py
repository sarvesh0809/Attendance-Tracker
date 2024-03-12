from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    # dashboards
    path('dashboard/',views.dashboard, name='dashboard'),
    path('view_attendance/',views.view_attendance, name='view_attendance'),
    path('mark_attendance/',views.mark_attendance, name='mark_attendance'),
    path('save-leave/', views.save_leave, name='save_leave'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('holiday_lists/', views.holiday_lists, name='holiday_lists'),
     path('apple/', views.apples, name='apple'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
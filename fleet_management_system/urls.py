"""
URL configuration for drivers project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from fleet_management_system import settings
from lauda.views import (driver_views, auth_views,
                         index_views, export_to_pdf_view,
                         manager_views, export_to_excel_view)

from lauda.views.error_view import errors_view

urlpatterns = [

    path('admin/', admin.site.urls),

    path('register/',
         auth_views.register_user,
         name='django_registration_register'),

    path('',
         auth_views.login,
         name='login'),

    path('email_verification/',
         auth_views.verify_email,
         name='email_verification'),

    path('email_confirmation/',
         auth_views.confirm_email,
         name='email_confirmation'),

    path('forgot_password/',
         auth_views.forgot_password,
         name='forgot_password'),

    path('reset_password/',
         auth_views.reset_password,
         name='reset_password'),

    path('forgot_password_confirmation/',
         auth_views.forgot_password_confirmation,
         name='forgot_password_confirmation'),

    path('driver_dashboard/',
         driver_views.driver_dashboard,
         name='driver_dashboard'),

    path('manager_dashboard/',
         manager_views.manager_view,
         name='manager_dashboard'),

    path('export_to_excel/',
         export_to_excel_view.export_to_excel,
         name='export_to_excel'),

    path('export-to-pdf/',
         export_to_pdf_view.export_to_pdf,
         name='export_to_pdf'),

    # path('', include('django_registration.backends.one_step.urls')),
    # path('__reload__/', include('django_browser_reload.urls')),
    path('404/', errors_view, name="404"),
    path('logout/', auth_views.logout_view, name='logout')
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),  # Dashboard URLs
    path('accounts/', include('accounts.urls')),  # Accounts URLs
    path('banks/', include('banks.urls')),  # Banks URLs
]



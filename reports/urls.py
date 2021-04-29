from django.urls import path
from .views import report1, report2, report3


urlpatterns = [
    path('report1', report1),
    path('report2/', report2),
    path('report3', report3),
]

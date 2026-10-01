from django.contrib import admin
from django.urls import path
from colleges.views import home, sistec, lnct, oist

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('sistec/', sistec, name='sistec'),
    path('lnct/', lnct, name='lnct'),
    path('oist/', oist, name='oist'),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()

from django.contrib import admin
from django.urls import path
from Maqola.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Login),
    path('blog/', Blog),
    path('maqola/', Maqola),
]


from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('survey.urls')),
    path('survey/', include('survey.urls'))
]

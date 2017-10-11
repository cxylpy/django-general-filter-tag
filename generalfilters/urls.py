from django.conf.urls import url
from generalfilters import views
urlpatterns = [
    url('^demo$',views.demo)
]

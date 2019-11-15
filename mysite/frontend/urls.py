from django.conf.urls import url
from frontend import views

urlpatterns = [
    url(r'^$', views.FrontWebPage.as_view()),
    url(r'^google08f29c7b03e739ef/', views.google08f29c7b03e739ef, name='google08f29c7b03e739ef'),
]

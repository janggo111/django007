from django.urls import path
from . import views

app_name = "book"  # 별칭을 app 마다 분리
urlpatterns = [
    path('index/', views.index, name="index"),
    path('create/', views.create, name="create"),
]

from django.urls import path
from . import views

app_name = "trans"  # 별칭을 app 마다 분리
urlpatterns = [
    path('index/', views.index, name="index"),
]
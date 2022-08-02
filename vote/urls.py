from django.urls import path
from . import views

app_name = "vote"  # 별칭을 app 마다 분리
urlpatterns = [
    path('index/', views.index, name="index"),
    path('detail/<tpk>', views.detail, name="detail"),
    path('create/', views.create, name="create"),
    path('vote/<tpk>', views.vote, name="vote"),
    path('cancel/<tpk>', views.cancel, name="cancel"),
    path('delete/<tpk>', views.delete, name="delete"),
]

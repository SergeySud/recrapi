from django.urls import path, re_path

from recrApi import views
from recrApi.views import BasicView, AnchoredView

urlpatterns = [
    path('<name>&<message>', BasicView.as_view()),
    re_path(r'/?', AnchoredView.as_view()),

]

from django.urls import path
from .views import SearchView


urlpatterns = [
    path('autocomplete', SearchView.as_view()),
]

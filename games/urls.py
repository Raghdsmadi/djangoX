from django.urls import path
from .views import gameListView, gameDetailView, gameCreateView, gameUpdateView, gameDeleteView

urlpatterns = [
    path('game/', gameListView.as_view(), name='games_list'),
    path('game/<int:pk>/', gameDetailView.as_view(), name='game_detail'),
    path('game/create/', gameCreateView.as_view(), name='game_create'),
    path('game/<int:pk>/update/', gameUpdateView.as_view(), name='game_update'),
    path('game/<int:pk>/delete/', gameDeleteView.as_view(), name='game_delete'),
]
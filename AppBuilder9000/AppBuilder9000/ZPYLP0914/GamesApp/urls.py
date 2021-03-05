from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='GamesAppHome'),
    path('GameLibrary', views.game_library, name="GameLibrary"),
    path('Details/<int:pk>', views.details, name="GameDetails"),
    path('AddGame', views.add_game, name="AddGame"),
    path('CreateProfile', views.create_profile, name="CreateProfile"),
    path('UserIndex', views.user_index, name="UserIndex"),
    path('EditGame/<int:pk>', views.edit_game, name="EditGame"),
    path('DeleteGame/<int:pk>', views.delete_game, name="DeleteGame"),
    # path('EditUser/<int:pk>', views.edit_user, name="EditUser")
]

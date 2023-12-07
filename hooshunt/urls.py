from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logoutView, name='logout'),
    path('adminView', views.adminView, name='admin'),
    path('userView', views.userView, name='user'),
    path('eWay/', views.bundleView, {'bundle': 'E-Way Bundle'}, name='eWay'),
    path('spotsToVisit/', views.bundleView, {'bundle': 'Spots to Visit'}, name='spotsToVisit'),
    path('dorms/', views.bundleView, {'bundle': 'Dorms'}, name='dorms'),
    path('food/', views.bundleView, {'bundle': 'Food'}, name='food'),
    path('map/', views.map, name='map'),
    # path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('submittingClue/', views.submitClue.as_view(), name='submitClue'),
    path('bundles/', views.listOfBundles, name='listOfBundles'),
    path('display_unapproved_clues/', views.display_unapproved_clues, name='display_unapproved_clues'),
    path('eWay/calculate_score/', views.calculate_score, name='calculate_score'),
    path('map/get_solved_clues/', views.get_solved_clues, name='get_solved_clues'),
]

from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [ 
    path('', views.IndexView.as_view(), name='index'),
    path('author/<int:author_id>', views.StoriesByAuthor.as_view(), name='authorstory'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(), name='newStory'),
    path('<int:pk>/update/', views.EditStoryView.as_view(), name='storyedit' ),
    path('<int:pk>/delete/', views.DeleteStoryView.as_view(), name='deletestory' ),
]

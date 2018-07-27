from django.urls import path

from quiz import views

urlpatterns=[
    path('',views.index,name='index'),
    path('play-quiz',views.playquiz,name='play-quiz'),
    path('play-quiz-next', views.playquiznext,name='play-quiz-next'),
    path('questions',views.QuestionList.as_view(),name='qlist'),
    path('questions/<int:pk>',views.QuestionDetail.as_view(),name='qlist'),
    path('create',views.QuestionCreate.as_view(),name='create'),
    path('edit/<int:pk>',views.QuestionUpdate.as_view(),name='edit'),
    path('delete/<int:pk>',views.QuestionDelete.as_view(),name='delete'),

         ]

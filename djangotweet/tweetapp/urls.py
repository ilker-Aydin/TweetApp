
from django.urls import path
from . import views
app_name='tweetapp' #bunu kullanarak html içinde jinja ve reverse kullanabiliyoruz

urlpatterns = [
    path('',views.listtweet,name='listtweet'),
    path('addtweet/',views.addtweet,name='addtweet'),
    path('addtweetbyform/',views.addtweetbyform,name='addtweetbyform'),
    path('addtweetbymodelform/',views.addtweetbymodelform,name='addtweetbymodelform'),
    path('signup/',views.SignUpView.as_view(),name="signup"),#bu oncekiler gibi fonksiyon degil sınıf bu yuzden sonuna .as_view() diyerek bunu gorunuume cevirebiliyoruz
    path('deletetweet/<int:id>',views.DeleteTweet,name='DeleteTweet'),#id alabilmek içinde gordgn gibi yaptk şimdi listweet de delete kısmına link vercez
]


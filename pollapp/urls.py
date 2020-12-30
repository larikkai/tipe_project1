from django.urls import path
from .views import index, detail, results, vote, signup

app_name = 'pollapp'
urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('login/signup/', signup, name='signup'),
    
]

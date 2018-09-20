from django.conf.urls import url
from testapp.views import testview, LeaderBoard

urlpatterns = [
    url(r'^', LeaderBoard.as_view(), name='testview')
]

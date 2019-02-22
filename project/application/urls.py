from django.conf.urls import url,include
from .import views
app_name='application'

urlpatterns = [
    url(r'^$',views.home,name='home'),
    url(r'^reg$',views.reg,name='reg'),
    url(r'^login$',views.login,name='login'),
    url(r'^event$',views.event,name='event'),
    url(r'^auth/', include('social_django.urls', namespace='social')),


]
from django.urls import re_path, path

from . import views

# lets follow reddit url format
# i.e /user/MrPotato
# .. /user/MrPotato/profile
# .. /user/MrPotato/preferences
app_name = 'account'
urlpatterns = [
    path(r'^$', views.view_profile, name='view_profile')
]

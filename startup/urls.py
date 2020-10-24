from django.urls import path
from . import views


urlpatterns = [
    path('', views.startup, name='startup'),
    path('<int:id>', views.listing, name='listing'),    
    path('delete/<int:startuplist_id>', views.delstartup, name='delstartup'),
    
    path('edit/<int:startuplist_id>', views.editstartup, name='editstartup'),
    path('changeoccur/<int:startuplist_id>', views.changeoccur, name='changeoccur')


]


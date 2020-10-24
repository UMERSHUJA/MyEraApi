from django.urls import path
from . import views


urlpatterns = [
    path('', views.joblist, name='joblist'),
    path('listing/<int:id>', views.listing, name='joblisting'),
    path('edit/<int:joblist_id>', views.editjob, name='editjob'),
    path('delete/<int:joblist_id>', views.deljob, name='deljob'),
    path('changeoccur/<int:joblist_id>', views.changeoccur, name='changeoccur')
]


from django.urls import path

from joblist.api.views import(
    api_detail_job_view,
    api_update_job_view,
    api_delete_job_view,
    api_create_job_view,
    ) 

app_name='joblist'

urlpatterns = [
    path('<slug>/', api_detail_job_view, name='job_detail'),
    path('<slug>/update', api_update_job_view, name='job_update'),
    path('<slug>/delete', api_delete_job_view, name='job_delete'),
    path('create', api_create_job_view, name="job_create"),

    ]
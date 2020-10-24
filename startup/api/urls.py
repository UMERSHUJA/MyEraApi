from django.urls import path

from startup.api.views import(
    api_detail_startup_view,
    api_update_startup_view,
    api_delete_startup_view,
    api_create_startup_view,
    ) 

app_name='startup'

urlpatterns = [
    path('<slug>/', api_detail_startup_view, name='detail'),
    path('<slug>/update', api_update_startup_view, name='update'),
    path('<slug>/delete', api_delete_startup_view, name='delete'),
    path('create', api_create_startup_view, name="create"),

    ]
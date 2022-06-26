from django.urls import path
from . import views
# from rest_framework_swagger.views import get_swagger_view
# schema_view = get_swagger_view(title='Voltlines API')

urlpatterns = [
	path('', views.ApiOverview, name='home'),
	path('create/', views.add_items, name='add-items'),
	path('create_trip/', views.add_trip, name="add-trip"),
	path('all/', views.view_items, name='view_items'),
	path('all_trips/', views.view_trips, name='view_trips'),
	path('update/<int:pk>/', views.update_items, name='update-items'),
	path('update_trip/<int:pk>/', views.update_trips, name="update-trips"),
	path('passenger/<int:pk>/delete/', views.delete_items, name='delete-items'),
]


# urlpatterns = [
#     path("",views.ListVoltlinesAPIView.as_view(),name="voltlines_list"),
#     path("create/", views.CreateVoltlinesAPIView.as_view(),name="voltlines_create"),
#     path("update/<int:pk>/",views.UpdateVoltlinesAPIView.as_view(),name="update_voltlines"),
#     path("delete/<int:pk>/",views.DeleteVoltlinesAPIView.as_view(),name="delete_voltlines")
# ]
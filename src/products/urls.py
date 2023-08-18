from django.urls import path

from .views import (product_detail_view, product_create_view,
                            dynamic_lookup_view, product_delete_view, product_list_view)

app_name = 'products'
urlpatterns = [

    path("<int:id>/", dynamic_lookup_view, name='detail'),  # dynamic
    path("<int:id>/delete/", product_delete_view, name="delee"),
    path("create/", product_create_view, name="create"),
    path("list/", product_list_view, name="list"),

]

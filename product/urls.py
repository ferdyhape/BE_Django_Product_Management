from django.urls import path
from . import views
from django.views.generic import ListView

urlpatterns = [
    path(
        "products/",
        ListView.as_view(
            template_name="product/index.html",
            model=views.Product,
            extra_context={
                "title": "Product Management",
            },
        ),
        name="products",
    ),
    path("products/create/", views.create, name="create_product"),
    path(
        "products/update/<int:product_id>/",
        views.update,
        name="update_product",
    ),
    path(
        "products/delete/<int:product_id>/",
        views.delete,
        name="delete_product",
    ),
    path(
        "product/<str:category_name>/",
        views.product_by_category,
        name="product_by_category",
    ),
]

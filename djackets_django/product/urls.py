from django.urls import path, include

from product import views

urlpatterns =[
    path('latest-products/', views.LatestProductsList.as_view(), name='latest-products'),
    path('products/search/', views.search, name='search'),
    path('products/<slug:category_slug>/<slug:product_slug>/', views.ProductDetails.as_view(), name='products'),
    path('products/<slug:category_slug>/', views.CategoryDetails.as_view(), name='category'),
]

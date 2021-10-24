from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from technodevicesApp import views
from technodevicesApp.views.productsUserView import ProductsUserView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('categoria/', views.CategoriaCreateView.as_view()),
    path('categorias/', views.CategoriasListView.as_view()),
    path('marca/', views.MarcaCreateView.as_view()),
    path('marcas/', views.MarcasListView.as_view()),
    path('producto/<int:pk>/create/', views.ProductCreateView.as_view()),
    path('productos/<int:user>/',  views.ProductsUserView.as_view()),
    path('contacto/<int:pk>/',  views.ContactDetailsView.as_view()),
    path('producto/remove/<int:user>/<int:pk>/', views.ProductDeleteView.as_view()),
    path('producto/update/<int:user>/<int:pk>/', views.ProductUpdateView.as_view()),
    path('producto/<int:pk>/', views.ProductDetailView.as_view()),
    path('productos/', views.AllProductsListView.as_view()),
    path('telefono/update/<int:pk>/', views.TelefonoUpdateView.as_view()),
    path('email/update/<int:pk>/', views.EmailUpdateView.as_view()),
]

'''if settings.DEBUG:'''
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
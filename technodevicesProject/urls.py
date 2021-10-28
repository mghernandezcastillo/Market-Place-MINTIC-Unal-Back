from django.urls import path, include
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)
from technodevicesApp import views
from technodevicesApp.views.productsUserView import ProductsUserView
from django.conf import settings
from django.conf.urls.static import static
from django.dispatch import receiver
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail
from django.urls import reverse
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

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
    path('auth/reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]

'''if settings.DEBUG:'''
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    #send_mail( 'prueba de asunto', 'Este seria el mensaje.', 'mghernandezcastillo@gmail.com', ['imperiumintro@gmail.com'], fail_silently=False,)
    #print(f"\nRecupera la contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde la API http://localhost:8000/api/auth/reset/confirm/.""\n")
    send_mail( 'Recupera la contraseña del correo', f"\Cree una nueva contraseña del correo '{reset_password_token.user.email}' usando el token '{reset_password_token.key}' desde el siguiente https://technodevices-fe.herokuapp.com/#/user/ResetPasswordConfirm/""\n", 'noreply@somehost.local', [reset_password_token.user.email], fail_silently=False,)
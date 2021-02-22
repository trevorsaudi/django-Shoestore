from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
  path('',views.home, name='home'),
  path('home2/',views.home2, name='home2'),
  path('about/',views.home2, name='about'),
  path('home2/',views.home2, name='home2'),
  path('store/', views.store, name='store'), 
  path('cart/', views.cart, name='cart'), 
  path('checkout/', views.checkout, name='checkout'), 
  path('contact/',views.contact, name='contact')

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
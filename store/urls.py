from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.loginPage, name="login"),
	path('home/', views.home, name="home"),
	path('about/', views.about, name="about"),
	path('contact/', views.contact, name="contact"),
	path('blog/', views.blog, name="blog"),
	path('cart/', views.cart, name="cart"),
	path('store/', views.store, name="store"),
	path('checkout/', views.checkout, name="checkout"),
	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('registration/', views.registerPage, name="registration"),
	path('login/', views.loginPage, name="login"),
	path('logout/', views.logoutUser, name="logout"),

]
from django.urls import path,include
from cust import views
urlpatterns = [
    path('',views.Homepage,name='home'),
    path('login/',views.Loginpage,name='login'),
    path('register/',views.Registerpage,name='register'),
    path('otpp/',views.Otppage,name='otpp'),
    path('logout/',views.LogoutPage,name='logout'),
    path('profilec/',views.Profilepage,name='profilec'),
    path('address/',views.Addresspage,name='address'),
    path('address/addressedit/<int:id>/',views.addresseditpage,name='addressedit'),
    path('address/newaddress',views.Newaddrersspage,name='newaddress'),
    path('category/<int:id>/',views.category,name='category'),
    path('category/<int:c_id>/subcategory/<int:s_id>/',views.subcategory,name='subcategory'),
    path('singleproduct/<int:id>/',views.singleproduct,name='singleproduct'),
    path('forgot/',views.forgot,name='forgot'),
    path('forgototp/',views.forgototp,name='forgototp'),
    path('forgotpassword/',views.forgotpassword,name='forgotpassword'),
    path('resendotp/',views.Resendotp,name='resendotp'),
    path('changecolor/<int:id>',views.changecolor,name='changecolor'),
    path('singproduct/<int:id>',views.singproduct,name='singproduct'),
    path('userorders',views.userorders,name='userorders'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('addwishlist/<int:id>/',views.Addwishlist,name='addwishlist'),
    path('deletewishlist/<int:id>/',views.Deletewishlist,name='deletewishlist'),
    path('changecolor/cartaddjs/<int:id>/', views.cartaddjs, name='cartaddjs'),
    path('singproduct/cartaddjs/<int:id>/', views.cartaddjs, name='cartaddjs'),
    path('order_deatails/<int:id>/',views.order_deatails,name='order_deatails'),
    path('userorder_cancel/<int:id>/', views.userorder_cancel, name='userorder_cancel'),
    path('searchproduct/', views.searchproduct, name='searchproduct'),
    path('product_return/<int:id>/', views.product_return, name='product_return'),
    path('tryy',views.tryy,name='tryy'),
    path('invoice',views.invoice,name='invoice'),
    path('gtouser/<str:s_id>/',views.gtouser,name='gtouser'),
    path('profilec/changepassword/',views.changepassword,name='changepassword'),
    path('generate_invoice/<int:id>/', views.generate_invoice, name='generate_invoice'),
    path('deleteaddress/<int:id>/',views.Addressdelete,name='deleteaddress'),
    
]
#mtu asiguze hii pia


from django.urls import path
from . import views 
from rest_framework.urlpatterns import format_suffix_patterns

app_name= 'products'

urlpatterns = [
#we will use the restframework api to mainipulate the products.
  path('drinks/', views.product_list),
  path('drinks/<int:id>', views.drink_detail) , #this is the detail view for drinks
]

urlpatterns = format_suffix_patterns(urlpatterns)

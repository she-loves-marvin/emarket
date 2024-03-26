

#marvo achana na hii file.



from django.contrib import admin
from django.conf import settings
from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [
    path('', include('products.urls', namespace="products")),
    path('', include('users.urls', namespace="users")),
    # path('', include('myapp.urls', namespace="myapp")),
    path('admin/', admin.site.urls),
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
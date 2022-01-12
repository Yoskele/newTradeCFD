
from django.contrib import admin
from django.urls import path, include

# for Static files like images.
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from django.conf.urls.static import static 
from django.conf import settings


urlpatterns = [
    path('', include('website.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    # path('sitemap.xml', sitemap, {'sitemaps':sitemaps}),
]



urlpatterns+=staticfiles_urlpatterns()


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.conf import settings
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf.urls import url
from ckeditor_uploader import views
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    path('sign/', include('sign.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('protect.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^ckeditor/upload/', login_required(views.upload), name='ckeditor_upload'), url(r'^ckeditor/browse/', never_cache(login_required(views.browse)), name='ckeditor_browse')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


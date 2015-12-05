from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from landingpage.views import TeamSignUp

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TeamSignUp.as_view(), name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

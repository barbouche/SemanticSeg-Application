from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from decorator_include import decorator_include
from django.contrib.admin.views.decorators import staff_member_required
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.documentation import include_docs_urls
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.views.generic import RedirectView, TemplateView
import django.views.defaults



schema_view = get_schema_view(
   openapi.Info(
      title="Nvidia Text To Speech API",
      default_version='v1',
      description="Nvidia Text To Speech Converter API (Version 1, 160 character) / Token 8370b4d44d1d005b32961002cf3cb8a0d5b81844 ",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),#IsAdminUser
)
def custom_page_not_found(request):
    return django.views.defaults.page_not_found(request, None)

app_name = 'main'

urlpatterns = [
    #path('', custom_page_not_found),
    path('spotbills/dashboard/api/', admin.site.urls),    
    path('spotbills/nvidia/api/', include('nvidia.urls')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', staff_member_required(schema_view.without_ui(cache_timeout=0)), name='schema-json'),
    path('spotbills/dashboard/api/documentation/', staff_member_required(schema_view.with_ui('swagger', cache_timeout=0)), name='schema-swagger-ui'),
    path('redoc/', staff_member_required(schema_view.with_ui('redoc', cache_timeout=0)), name='schema-redoc'),
    path(r'favicon.ico', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True)),
    path(r'robots.txt', TemplateView.as_view(template_name='users/well-known/robots.txt',content_type='text/plain'), name="robots"),    
    #re_path(r'$', custom_page_not_found),


  ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




#handler404 = 'nvidia.views.handler404'



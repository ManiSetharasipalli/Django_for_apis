from django.contrib import admin
from django.urls import path, include 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# The following external libraries are not compatible with the current version of DRF
# from rest_framework.schemas import get_schema_view  # For API schema   
# from rest_framework.documentation import include_docs_urls  # For documentation

schema_view = get_schema_view(
    openapi.Info(
        title="Blog API",
        default_version='v1',
        description="API documentation for the Blog API",
    ),
    public=True,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('posts.urls')),
    path('schema/', schema_view.with_ui('swagger', cache_timeout=0)),  # Swagger UI for API documentation
    # path('schema/', get_schema_view()),  # Alternative schema view (deprecated)
    # path('docs/', include_docs_urls(title='Blog API')),  # DRF's default API documentation (deprecated)
]

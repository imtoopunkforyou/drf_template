"""Файл конфигурации и настройки swagger"""
from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg.generators import OpenAPISchemaGenerator


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = ["https", "http"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title='SWAGGER API',
        default_version='verison 1',
        description='API',
    ),
    public=True,
    generator_class=BothHttpAndHttpsSchemaGenerator,
    permission_classes=[permissions.AllowAny]
)

docs_urls = [
    path(
        'docs.json',
        schema_view.without_ui(cache_timeout=0),
        name='schema-json',
    ),
    path(
        'docs',
        schema_view.with_ui(renderer='swagger'),
        name='schema-swagger-ui',
    ),
    path(
        'redoc',
        schema_view.with_ui(renderer='redoc'),
        name='schema-redoc',
    )
]
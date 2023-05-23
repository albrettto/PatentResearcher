from django.urls import path
from rest_framework import routers
from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views


#Метаданные Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="Patent API",
        default_version="v1",
        description="Patent - получаем патенты по жаропрочным никелевым сплавам",
        contact=openapi.Contact(email="a.husamov@yandex.ru"),
        license=openapi.License(name="Albrettto License"),
    ),
    public=True,
    permission_classes=(AllowAny, ),
)

router = routers.DefaultRouter()

urlpatterns = [
    path('patents/all', views.GetAllPatents.as_view()),
    path('patent', views.PostPatent.as_view()),
    path('patents/all/updated', views.GetNewPatents.as_view()),
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
]
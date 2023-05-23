from rest_framework.generics import GenericAPIView
from rest_framework.request import Request
from rest_framework.renderers import JSONRenderer
from .serializers import PatentSerializer
from .services.patent_service import PatentService
from rest_framework.response import Response


patent_service = PatentService()


class GetAllPatents(GenericAPIView):
    serializer_class = PatentSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """Получить все патенты"""
        response = patent_service.get_all_patents()
        return Response(data=response.data)


class GetNewPatents(GenericAPIView):
    serializer_class = PatentSerializer
    renderer_classes = [JSONRenderer]

    def get(self, request: Request, *args, **kwargs) -> Response:
        """Получить новые патенты"""
        patent_service.parse_new_patents()
        get_del_all_patents_view = GetAllPatents()
        # Вызываем метод get из GetDelAllPatents
        response = get_del_all_patents_view.get(request)
        return Response(data=response.data)


class PostPatent(GenericAPIView):
    serializer_class = PatentSerializer
    renderer_classes = [JSONRenderer]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """Добавить новый патент"""
        serializer = PatentSerializer(data=request.data)
        if serializer.is_valid():
            patent_service.add_patent(serializer)
            return Response(status=201)
        return Response(serializer.errors, status=400)

from rest_framework.viewsets import ModelViewSet
from core.models import PontosTuristicos
from core.api.serializers import PontosTuristicosSerializer
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class PontosTuristicosViewSet(ModelViewSet):
    queryset = PontosTuristicos.objects.all()
    serializer_class = PontosTuristicosSerializer
    filter_backends = (SearchFilter,)
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    search_fields = ['nome', 'descricao', 'endereco__linha1']

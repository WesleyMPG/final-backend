from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from cadastro_de_bens.api import views
from django.urls import path, include, re_path

api_router = routers.DefaultRouter()


api_router.register(r'marcas', 
                    views.MarcaViewSet,
                    basename='Marcas')

api_router.register(r'situacoes', 
                    views.SituacaoUsoBemViewSet, 
                    basename='Situaçôes')

api_router.register(r'estados', 
                    views.EstadosBemViewSet, 
                    basename='Estados')

api_router.register(r'naturezas', 
                    views.NaturezasDespesaViewSet, 
                    basename='Naturezas')

api_router.register(r'fornecedores', 
                    views.FornecedoresViewSet, 
                    basename='Fornecedores')

api_router.register(r'bens', 
                    views.BensViewSet, 
                    basename='Bens')

api_router.register(r'notas-fiscais', 
                    views.NotasFiscaisViewSet, 
                    basename='Notas fiscais')

api_router.register(r'itens-nota-fiscal', 
                    views.ItensNotaFiscalViewSet,
                    basename='Itens nota fiscal')


urlpatterns = format_suffix_patterns([
    re_path(r'^notas-fiscais/(?P<id_nota_fiscal>[^/.]+)/itens$', 
        views.ItensNotaFiscalViewSet.as_view({'get': 'get_by_nota_id'}), 
        name="Itens da nota fiscal"),
    
    re_path(r'^itens-nota-fiscal/(?P<id_item_nota_fiscal>[^/.]+)/bens$', 
        views.BensViewSet.as_view({'get': 'get_by_item_nota_id'}), 
        name="Bens do item"),
])

urlpatterns.append(path('', include(api_router.urls)))
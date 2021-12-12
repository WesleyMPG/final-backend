from rest_framework.viewsets import  ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from cadastro_de_bens import models


class MarcaViewSet(ModelViewSet):
    serializer_class = serializers.MarcaSerializer
    queryset = models.Marca.objects.all()


class SituacaoUsoBemViewSet(ModelViewSet):
    serializer_class = serializers.SituacaoUsoBemSerializer
    queryset = models.SituacaoUsoBem.objects.all()


class EstadosBemViewSet(ModelViewSet):
    serializer_class = serializers.EstadosBemSerializer
    queryset = models.EstadosBem.objects.all()


class NaturezasDespesaViewSet(ModelViewSet):
    serializer_class = serializers.NaturezasDespesaSerializer
    queryset = models.NaturezasDespesa.objects.all()


class FornecedoresViewSet(ModelViewSet):
    serializer_class = serializers.FornecedoresSerializer
    queryset = models.Fornecedores.objects.all()

    def list(self, request):
        m_notas = models.NotasFiscais.objects
        s_notas = serializers.NotasFiscaisSerializer
        
        fornecedores = models.Fornecedores.objects.all()
        list_fornecedores = []
        for f in fornecedores:
            notas = m_notas.filter(id_fornecedor=f.id_fornecedor,
                                   id_natureza_despesa=1)
            if len(notas) > 0:
                new_f = self.serializer_class(f).data
                new_f['notas_fiscais'] = s_notas(notas, many=True).data
                list_fornecedores.append(new_f)

        return Response(list_fornecedores)


class NotasFiscaisViewSet(ModelViewSet):
    serializer_class = serializers.NotasFiscaisSerializer
    queryset = models.NotasFiscais.objects.all()


class BensViewSet(ModelViewSet):
    serializer_class = serializers.BensSerializer
    queryset = models.Bens.objects.all()

    def get_by_item_nota_id(self, request, *args, **kwargs):
        m_bens = models.Bens.objects

        id_item = self.kwargs['id_item_nota_fiscal']
        bens = m_bens.filter(id_item_nota_fiscal=id_item)
        serializer = self.serializer_class(bens, many=True)
        return Response(serializer.data)


class ItensNotaFiscalViewSet(ModelViewSet):
    serializer_class = serializers.ItensNotaFiscalSerializer
    queryset = models.ItensNotaFiscal.objects.all()

    def get_by_nota_id(self, request, *args, **kwargs):
        m_itens = models.ItensNotaFiscal.objects

        id_nota = self.kwargs['id_nota_fiscal']
        itens = m_itens.filter(id_nota_fiscal=id_nota)
        serializer = self.serializer_class(itens, many=True)
        return Response(serializer.data)


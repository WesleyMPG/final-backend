from rest_framework import serializers
from rest_framework.response import Response
from cadastro_de_bens import models


class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Marca
        fields = '__all__'
    

class SituacaoUsoBemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SituacaoUsoBem
        fields = '__all__'


class EstadosBemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EstadosBem
        fields = '__all__'


class NaturezasDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NaturezasDespesa
        fields = '__all__'


class FornecedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fornecedores
        fields = '__all__'

    
class NotasFiscaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NotasFiscais
        fields = '__all__'


class ItensNotaFiscalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItensNotaFiscal
        fields = '__all__'


class BensSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bens
        fields = '__all__'
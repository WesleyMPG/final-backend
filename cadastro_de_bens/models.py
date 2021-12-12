from django.db import models

# Create your models here.


class Marca(models.Model):
    id_marca = models.AutoField(primary_key=True)
    marca = models.CharField(max_length=80)
    id_user_cad = models.IntegerField(default=1)
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.IntegerField(default=1)
    dt_alt = models.DateField(auto_now=True, null=True, blank=True)
    
    def __str__(self):
        return self.marca


class SituacaoUsoBem(models.Model):
    id_situacao_uso_bem = models.AutoField(primary_key=True)
    situacao_uso_bem = models.CharField(max_length=80)
    descricao = models.CharField(max_length=255)
    ativo = models.CharField(max_length=1)

    def __str__(self):
        return self.situacao_uso_bem


class EstadosBem(models.Model):
    id_estado_bem = models.AutoField(primary_key=True)
    estado_bem = models.CharField(max_length=80)
    descricao = models.CharField(max_length=255)
    ativo = models.CharField(max_length=1)

    def __str__(self):
        return self.estado_bem


class NaturezasDespesa(models.Model):
    id_natureza_despesa = models.AutoField(primary_key=True)
    cod_natureza_despesa = models.CharField(max_length=8)
    desc_natureza_despesa = models.CharField(max_length=60)

    def __str__(self):
        return self.desc_natureza_despesa


class Fornecedores(models.Model):
    id_fornecedor = models.AutoField(primary_key=True)
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20, unique=True)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=20)
    id_user_cad = models.IntegerField(default=1)
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.IntegerField(default=1)
    dt_alt = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.razao_social


class NotasFiscais(models.Model):
    id_nota_fiscal = models.AutoField(primary_key=True)
    id_fornecedor = models.ForeignKey(Fornecedores, on_delete=models.CASCADE)
    id_natureza_despesa = models.ForeignKey(NaturezasDespesa, on_delete=models.CASCADE)
    numero = models.IntegerField()
    ano = models.IntegerField()
    id_user_cad = models.IntegerField(default=1)
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.IntegerField(default=1)
    dt_alt = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return str(self.numero)


class ItensNotaFiscal(models.Model):
    id_item_nota_fiscal = models.AutoField(primary_key=True)
    id_nota_fiscal = models.ForeignKey(NotasFiscais, on_delete=models.CASCADE)
    qtd = models.IntegerField()
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    produto_servico = models.CharField(max_length=100)
    vinculado = models.CharField(max_length=1)
    id_user_cad = models.IntegerField(default=1)
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.IntegerField(default=1)
    dt_alt = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.id_nota_fiscal}/{self.id_item_nota_fiscal}'


class Bens(models.Model):
    id_bem = models.AutoField(primary_key=True)
    id_item_nota_fiscal = models.ForeignKey(ItensNotaFiscal, 
                                            on_delete=models.CASCADE)
    tombamento = models.CharField(max_length=10)
    id_estado_bem = models.ForeignKey(EstadosBem, 
                                      on_delete=models.CASCADE)
    id_situacao_uso_bem = models.ForeignKey(SituacaoUsoBem, 
                                            on_delete=models.CASCADE)
    valor_aquisicao = models.DecimalField(max_digits=7, 
                                          decimal_places=2)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    data_lim_garantia = models.DateField()
    data_fim_garantia = models.DateField()
    data_inicio_uso = models.DateField(auto_now_add=True)
    observacoes = models.TextField(null=True, blank=True)
    id_user_cad = models.IntegerField(default=1)
    dt_cad = models.DateField(auto_now_add=True)
    id_user_alt = models.IntegerField(default=1)
    dt_alt = models.DateField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return f'{self.id_bem}/{self.tombamento}'


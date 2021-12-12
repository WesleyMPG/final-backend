# SumeSoftware

Esse projeto é o backend do desafio final do curso de desenvovedor fullstack júnior do LCCV/UFAL.


#### Conteúdo

Estão implementados os modelos e rotas requeridos no backlog. Também aqui são feitos alguns filtros pedidos, como o de retornar apenas fornecedores que sejam relacionados à natureza de despesa "Equipamentos e material permanente"; se olhado no django admin é possível ver que o banco contem outros fornecedores e outros dos itens que possuem filtros semelhantes, mas não se enquadram.

Importante ressaltar que as tabelas necessárias para o cadastro de um bem (Fornecedor, NotaFiscal, etc) podem ser populadas com o comando:

> python manage.py loaddata cadastro_de_bens/fixture/db_data.json


#### Dificuldades

Essa parte do projeto acabou sendo mais dífícil por falta de familiaridade com a tecnologia em questão. Mesmo django e django-rest adiantando muito o trabalho da criação de rotas, tabelas, etc, sofri um pouco na hora de pegar um id passado na rota (no caso de uma relação), por exemplo.
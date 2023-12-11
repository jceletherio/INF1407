# INF1407
Trabalho da disciplina INF1407 usando Django

No trabalho implementei uma plataforma para ter acesso aos candidatos as eleições, com foto, nome, numero, partido e plano de governo.

O site conta com login e tem uma lista de candidatos escolhidos por cada usuario

Os candidatos são armazenados em banco de dados e inseridos manualmente pelo administrador da plataforma

Já as operações de CRUD acontecem quando um usuario faz login é feita a criação de uma tabela contendo seu username e seus candidatos escolhidos.
As tabelas são lidas nas paginas paginaCandidatos.html e minhaLista.html, aonde são lidos os candidatos e exibidos.
A atualização da tabela ocorre atraves de formulario na pagina upLista.html aonde o usuario pode colocar os novos numeros de candidatos.
E por ultimo o usuario e sua lista de candidatos podem ser deletadas selecionando deletar minha conta.

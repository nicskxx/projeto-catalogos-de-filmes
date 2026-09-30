## 1. Introdução

**Nome do projeto:** Catálogo de filmes 
**Equipe de desenvolvimento:** Nicolas de Campos Barboza

### 1.1 Objetivo

O projeto **Catálogo de Filmes** tem como objetivo desenvolver um sistema simples para que o usuário possa cadastrar e organizar seus filmes de forma visual.

O sistema permitirá armazenar informações como título, ano de lançamento, gênero, nota pessoal e imagem da capa do filme.

### 1.2 Contexto

O cliente atualmente utiliza uma planilha do Excel para registrar os filmes que assiste. Porém, a quantidade de informações tornou a planilha difícil de organizar e não permite uma apresentação visual adequada.

Por isso, foi solicitada a criação de um sistema próprio, com login e uma galeria de filmes com suas respectivas capas.

----------

## 2. Escopo do Projeto

O sistema deverá permitir que o usuário:

-   Fazer login no sistema;
-   Cadastrar novos filmes;
-   Visualizar os filmes cadastrados;
-   Editar informações de um filme;
-   Excluir filmes;
-   Adicionar uma imagem de capa para cada filme;
-   Dar uma nota de 0 a 10 para cada filme.

Funcionalidades como compartilhamento dos filmes com amigos, comentários ou integração com serviços externos **não fazem parte da primeira versão do projeto**.

----------

## 3. Requisitos Funcionais

### RF01 — Login

O sistema deverá permitir que o usuário entre utilizando seu login e senha.

### RF02 — Cadastro de Filme

O sistema deverá permitir cadastrar um novo filme informando:

-   Título;
-   Ano de lançamento;
-   Gênero;
-   Nota de 0 a 10;
-   Imagem da capa.

### RF03 — Visualização dos Filmes

O sistema deverá apresentar os filmes cadastrados em formato de lista ou galeria, mostrando principalmente a capa e o título.

### RF04 — Edição de Filme

O usuário deverá poder alterar as informações de um filme já cadastrado.

### RF05 — Exclusão de Filme

O usuário deverá poder excluir um filme cadastrado.

### RF06 — Upload da Capa

O sistema deverá permitir que o usuário selecione e envie uma imagem para ser utilizada como capa do filme.

### RF07 — Validação da Nota

O sistema deverá aceitar somente notas entre **0 e 10**.

----------

## 4. Requisitos Não Funcionais

### RNF01 — Segurança

O sistema deverá exigir autenticação para que o usuário tenha acesso ao catálogo.

### RNF02 — Usabilidade

A interface deverá ser simples e fácil de utilizar.

### RNF03 — Compatibilidade

O sistema deverá funcionar em navegadores modernos, como Google Chrome, Microsoft Edge e Mozilla Firefox.

### RNF04 — Organização

As informações dos filmes deverão ser armazenadas de forma organizada para facilitar sua consulta e alteração.

----------

## 5. Regras de Negócio

-   Cada filme deverá possuir um título.
-   O ano deverá ser informado como um ano válido.
-   A nota deverá estar entre 0 e 10.
-   O usuário deverá estar logado para cadastrar, editar ou excluir filmes.
-   Cada filme poderá possuir uma imagem de capa.
-   Somente o usuário responsável pelo catálogo poderá alterar seus filmes.

----------

## 6. Principais Telas

O sistema deverá possuir, inicialmente, as seguintes telas:

### 6.1 Tela de Login

Campos:

-   Usuário ou e-mail;
-   Senha;
-   Botão **Entrar**.

### 6.2 Tela Principal / Catálogo

Deverá apresentar os filmes cadastrados em formato de galeria.

Cada filme poderá apresentar:

-   Capa;
-   Título;
-   Ano;
-   Nota;
-   Botão para editar;
-   Botão para excluir.

### 6.3 Tela de Cadastro

Deverá possuir campos para:

-   Título;
-   Ano;
-   Gênero;
-   Nota;
-   Upload da capa;
-   Botão **Cadastrar**.

### 6.4 Tela de Edição

Deverá permitir alterar os dados de um filme já cadastrado.

----------

## 7. Exemplo de Dados de um Filme

Campo

Exemplo

Título

Interestelar

Ano

2014

Gênero

Ficção Científica

Nota

9,5

Capa

imagem do pôster

----------

## 8. Fluxo Básico do Sistema

1.  O usuário acessa o sistema.
2.  O usuário informa seu login e senha.
3.  O sistema verifica os dados.
4.  Após o login, o usuário acessa seu catálogo.
5.  O usuário pode cadastrar um novo filme.
6.  O filme aparece na galeria.
7.  O usuário pode editar ou excluir o filme quando desejar.

----------

## 9. Fora do Escopo

Para manter o projeto simples nesta primeira versão, não serão desenvolvidas as seguintes funcionalidades:

-   Compartilhamento de filmes com amigos;
-   Sistema de comentários;
-   Avaliações de outros usuários;
-   Cadastro de vários usuários;
-   Recomendações automáticas;
-   Integração com APIs de filmes;
-   Aplicativo para celular.

Essas funcionalidades poderão ser consideradas em versões futuras.

----------

## 10. Estimativa Inicial

Por se tratar de um projeto de pequeno porte, a primeira versão poderá ser desenvolvida em aproximadamente **2 a 4 semanas**, dependendo das tecnologias utilizadas e do tempo disponível para desenvolvimento.

O custo deverá ser definido de acordo com as tecnologias escolhidas, tempo de desenvolvimento e necessidade de hospedagem.

----------

## 11. Conclusão

O **Catálogo de Filmes** será um sistema simples para substituir a planilha utilizada pelo cliente, permitindo organizar seus filmes de maneira mais prática e visual.

A primeira versão terá como foco as funções principais de **login, cadastro, visualização, edição e exclusão de filmes**, além do armazenamento das capas dos filmes.


**Abaixo fluxograma sobre a visão geral**
![](Diagrama%20sem%20nome.jpg)
=======
>>>>>>> 81bd2aa29a48b739253395d60726b2924f22826e


**Abaixo foto do modelo logico**
![](modelo%20logico.png)

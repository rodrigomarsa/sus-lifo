# Projeto `SUS-LIFO`

Este repositório contém um mini-projeto desenvolvido para atender às necessidades de gestão de fila de pacientes da UPA, seguindo a lógica SUS-LIFO (Last In, First Out), ou seja, o último a chegar é o primeiro a ser atendido.

## Descrição do Projeto

O desafio consiste em implementar um sistema web com as seguintes características:

- **Frontend**: Desenvolvido em Flutter, contendo duas telas. A tela inicial exibe as informações do último paciente na fila, enquanto a segunda tela permite o registro de um novo paciente, coletando apenas o nome do mesmo.

- **Backend**: Desenvolvido em Python utilizando o framework Flask. O backend será responsável por gerenciar os dados dos pacientes e interagir com o banco de dados MySQL.

- **Banco de Dados**: Utilização do MySQL para persistência dos dados dos pacientes, com uso do ORM SQLAlchemy, para fazer a interação com o banco de dados.

## Estrutura do Projeto

O projeto está dividido em duas partes principais:

1. **Frontend em Flutter**: Localizado no diretório `frontend`. Contém os arquivos e código-fonte para a interface do usuário desenvolvida em Flutter.

2. **Backend em Flask (Python)**: Localizado no diretório `backend`. Contém os arquivos e código-fonte para o servidor Flask responsável pelo gerenciamento dos dados e interação com o banco de dados.

## Instruções de Uso

### Requisitos

Certifique-se de ter os seguintes requisitos instalados em sua máquina:

- Python 3.x
- Flutter SDK

### Configuração e Execução

1. **Backend Flask**:

   - Acesse o diretório `backend`.
   - Crie e ative o ambiente virtual do Python:

   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   ```

   - Instale as dependências usando:

   ```bash
   python3 -m pip install -r dev-requirements.txt
   ```

   - Rode o MySQL via Docker, execute os seguintes comandos na raiz do projeto:

   ```bash
   docker build -t sus-lifo-db .
   docker run -d -p 3306:3306 --name=sus-lifo-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=sus_lifo_database sus-lifo-db
   ```

   Esses comandos irão fazer o build da imagem e subir o container Docker.

   **Nota:** Se a porta 3306 já estiver sendo usada, considere alterá-la no comando acima.

   - Execute o servidor Flask:

   ```bash
   python3 src/app.py
   ```

   - Acesse a rota `/users` para visualizar a lista de pacientes cadastrados no banco de dados.

2. **Frontend Flutter**:

   - Acesse o diretório `frontend`.
   - Abra o arquivo `lib/main.dart` e verifique se o dispositivo de destino está selecionado `web`.

     No canto inferior direito do VS Code, você encontra um botão que mostra o dispositivo de destino atual. Clique nele para mudar.

   - Aperte a tecla `F5` para iniciar o app no modo de depuração ou execute o comando no terminal:

   ```bash
   flutter run
   ```

## Organização do Código

Para garantir a qualidade do código, foi utilizado neste projeto um linter.
O código foi estruturado seguindo as boas práticas de desenvolvimento, buscando uma organização clara e objetiva, bem como a aderência aos princípios SOLID.

##

<p align="center">
<a href="https://rodrigomarsa.github.io" target="_blank"><img alt="Portfólio" src="https://img.shields.io/badge/Portfólio-rodrigomarsa.github.io-blue?style=flat&logo=google-chrome"></a>
<a href="https://www.linkedin.com/in/rodrigomarsa" target="_blank"><img alt="LinkedIn" src="https://img.shields.io/badge/-rodrigomarsa-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rodrigomarsa/"></a>
<a href="https://github.com/rodrigomarsa" target="_blank"><img alt="GitHub" src="https://img.shields.io/github/followers/rodrigomarsa?label=follow&style=social"></a>
<a href="mailto:rodrigomartins.agro@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-rodrigomartins.agro@gmail.com-blue?style=flat&logo=gmail"></a>
</p

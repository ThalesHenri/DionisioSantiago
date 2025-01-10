Dionísio Santiago 🧶✨

Um site de e-commerce minimalista desenvolvido em Django para vendas de peças de crochê, criado com carinho para atender a um familiar. Este projeto combina funcionalidade simples e design elegante, com foco em proporcionar uma experiência direta e prática para os clientes. 💡 Funcionalidades

Catálogo de produtos: Exibição de produtos com imagens, descrições e preços.
Compra inteligente: Permite que o cliente selecione o produto desejado e envie o pedido diretamente para um e-mail comercial, facilitando a comunicação e o atendimento.
Notificação de compra: Cada pedido gera uma notificação automática enviada para o e-mail do administrador com os detalhes do pedido.

🎨 Design

O layout segue um estilo minimalista, com foco em destacar os produtos de crochê. O objetivo é criar um ambiente acolhedor e fácil de navegar, ressaltando a delicadeza do trabalho artesanal. 🛠️ Tecnologias

Backend: Django
Frontend: HTML, CSS (estilo minimalista e sem frameworks externos como Bootstrap)
Banco de dados: SQLite (desenvolvimento) / PostgreSQL (produção)
Outros: Sistema de notificações via e-mail (configurável com SMTP).

🚀 Como rodar o projeto localmente

Clone o repositório:

git clone https://github.com/seuusuario/dionisio-santiago.git cd dionisio-santiago

Crie e ative um ambiente virtual:

python -m venv venv
source venv/bin/activate # No Windows, use: venv\Scripts\activate

Instale as dependências:

pip install -r requirements.txt

Realize as migrações do banco de dados:

python manage.py migrate

Configure as variáveis de ambiente para o envio de e-mails (arquivo .env):

EMAIL_HOST=smtp.seuprovedor.com
EMAIL_PORT=587
EMAIL_HOST_USER=seuemail@dominio.com
EMAIL_HOST_PASSWORD=suasenha
EMAIL_USE_TLS=True

Inicie o servidor de desenvolvimento:

python manage.py runserver

Acesse o projeto no navegador:
http://127.0.0.1:8000

📂 Estrutura do Projeto

main/: Aplicação principal com as funcionalidades do e-commerce.
static/: Arquivos estáticos (CSS, imagens).
templates/: Templates HTML organizados por páginas.
forms.py: Formulários simples para envio de pedidos.
models.py: Modelos representando os dados (produtos, pedidos, etc.).

📝 Licença

Este projeto está sob a licença MIT.

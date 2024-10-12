Gordão Cyber Bullet 1.0 - Bloco de Notas Web

Gordão Cyber Bullet 1.0 é um aplicativo web simples de bloco de notas, desenvolvido com Flask, SQLAlchemy e SQLite, que permite aos usuários adicionar, editar e excluir tarefas. O layout utiliza um tema escuro inspirado no Dracula, proporcionando uma interface moderna e minimalista.
Funcionalidades

    Adicionar Tarefas: Insira tarefas com descrições curtas no campo de entrada.
    Editar Tarefas: Modifique qualquer tarefa existente através da interface de edição.
    Excluir Tarefas: Remova tarefas indesejadas diretamente na página principal.
    Banco de Dados: As tarefas são armazenadas em um banco de dados SQLite local.

Tecnologias Utilizadas

    Flask: Framework web em Python que gerencia as rotas e lógica do aplicativo.
    SQLAlchemy: ORM utilizado para interagir com o banco de dados SQLite.
    HTML5: Estrutura básica das páginas web.
    CSS3: Design responsivo e estilização com tema Dracula.
    Jinja2: Engine de templates usada no Flask para renderizar as páginas dinâmicas.

#########################################################################################
Estrutura do projeto:

.
├── app.py              # Arquivo principal da aplicação Flask
├── database.db         # Banco de dados SQLite gerado automaticamente
├── templates/          # Páginas HTML (base.html, index.html, edit.html)
│   ├── base.html
│   ├── index.html
│   └── edit.html
├── static/
│   └── styles.css      # Arquivo de estilização com o tema Dracula
└── README.md           # Este arquivo

#########################################################################################
Como Executar o Projeto
git clone https://github.com/renatoroberto25/gordao-cyber-bullet.git
cd gordao-cyber-bullet
python3 -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
flask run
http://127.0.0.1:5000


#########################################################################################
Melhorias Futuras

    Implementação de autenticação de usuário.
    Adição de status de conclusão nas tarefas.
    Opção para marcar tarefas como concluídas ou pendentes.

Contribuições

Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias. Toda contribuição é bem-vinda!


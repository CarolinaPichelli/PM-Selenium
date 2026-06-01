# 🎬 IMDb Web Scraper - Validação de Elenco

> Projeto de automação e raspagem de dados desenvolvido para a disciplina de Programação Multiplataforma.

---

### 👥 Autoras & Contexto

* **Estudantes:** Carolina Pichelli Souza & Heloísa Pichelli Souza
* **Curso:** Análise e Desenvolvimento de Sistemas (AMS 2)
* **Matéria:** Programação Multiplataforma

---

### 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python 3
* **Biblioteca Principal:** Selenium WebDriver (Automação de navegador)

---

### 🤖 Resumo do Funcionamento

O script inicializa um robô via Google Chrome (em modo incógnito e maximizado) para realizar o seguinte fluxo automatizado no site do IMDb:

1. **Busca Principal:** Acessa o IMDb, pesquisa pelo ator `John Travolta` e entra no seu perfil oficial.
2. **Navegação por Conteúdo:** Procura pelo filme **"Swordfish"** (Operação Swordfish) na filmografia e clica nele.
3. **Validação de Dados:** Localiza o bloco de elenco correspondente ao ator dentro da página do filme e verifica se o nome do seu personagem (**Gabriel**) é detectado com sucesso.

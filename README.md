# Documentação do Projeto Indústrias Wayne

## 1. Resumo do Projeto

O sistema **Indústrias Wayne** é uma aplicação web de controle de acesso e gerenciamento de recursos internos de segurança (equipamentos, veículos e dispositivos de segurança). O projeto inclui:

- Tela de login com autenticação
- Controle de acesso por tipo de usuário (admin, gerente, funcionário)
- Painel com dashboard visual
- Cadastro, listagem e remoção de recursos apenas pelo admin

## 2. Tecnologias Utilizadas

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python 3.12, Flask
- **Banco de Dados**: SQLite
- **Outras libs**: JWT (PyJWT), Flask-CORS, Chart.js

## 3. Estrutura das Pastas

```
WAYNE/
├── backend/
│   ├── app.py               #API Flask
│   ├── db.py                #Inicialização do banco
│   ├── models.py            #Funções de autenticação e banco
├── database/
│   └── industrias_wayne.db  #Banco de dados SQLite
├── frontend/
│   ├── index.html           #Tela de login para funcionarios
│   ├── dashboard.html       #Painel de controle
│   ├── style.css            #Design
│   └── script.js            #Lógica de interação
```

## 4. Funcionalidades

- **Login** com validação JWT
- **Controle de acesso**:
  - Admin: acesso completo
  - Gerente e Funcionário: apenas acesso de leitura
- **Painel de Controle**:
  - Visualização de recursos
  - Adição e remoção de recursos
  - Gráfico de distribuição de recursos
  - Atividades recentes

## 5. Instruções para Execução

### a) Backend

1. Acesse a pasta do projeto:
2. Ative o ambiente virtual:
3. Instale as dependências:
(pip install -r requirements.txt)
4. Inicie o backend:
python app.py

### b) Frontend

1. Abra o arquivo index.html no navegador.

## 6. Usuários do Sistema

| Usuário | Senha      | Nome Completo     | Cargo       |
| ------- | ---------- | ----------------- | ----------- |
| bruce   | batman     | Bruce Wayne       | admin       |
| alfred  | alfred123  | Alfred Pennyworth | gerente     |
| lucius  | lucius123  | Lucius Fox        | funcionario |
| barbara | barbara123 | Barbara Gordon    | funcionario |

## 7. Endpoints da API

### POST `/login`

- Autentica usuário e retorna token JWT

### GET `/recursos`

- Lista todos os recursos (requer token)

### POST `/recursos`

- Adiciona novo recurso (apenas admin)

### DELETE `/recursos/<id>`

- Remove recurso (apenas admin)

## 8. Observações Finais

- O sistema é responsivo e conta com uma interface adaptada para dispositivos modernos.
- O vídeo de fundo e a identidade visual remetem à marca "Wayne Enterprises", utilizando a logo e uma paleta de cores relacionada a figura.
- JWT é usado para segurança na comunicação entre frontend e backend.
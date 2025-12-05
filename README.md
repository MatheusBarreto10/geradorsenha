<h1 align="center">🔐 Password Generator</h1>
<p align="center">Gerador de senhas seguras desenvolvido em Python — com versão CLI e interface Web em Flask.</p>

<p align="center">
  <strong>Simples • Seguro • Personalizável</strong>
</p>

---

## 📌 Sobre o Projeto

Este repositório contém um **gerador de senhas seguras**, ideal para estudos, portfólio, demonstração de lógica em Python e boas práticas de desenvolvimento.  
O projeto oferece tanto uma **interface de linha de comando (CLI)** quanto uma **versão Web usando Flask**, permitindo explorar diferentes formas de interação com o mesmo backend.

---

## ✨ Funcionalidades

- Definição do tamanho da senha  
- Ativação/desativação de:
  - Letras minúsculas  
  - Letras maiúsculas  
  - Dígitos  
  - Símbolos  
- Remoção de caracteres ambíguos (`l`, `I`, `1`, `O`, `0`)  
- Opção para garantir que cada grupo esteja presente  
- Copiar senha para a área de transferência (quando disponível)  
- Interface Web minimalista com Flask  
- Testes automatizados com Pytest  

---

## 🧩 Estrutura do Projeto

password-generator/
├─ README.md
├─ LICENSE
├─ .gitignore
├─ generator/
│ ├─ init.py
│ ├─ generator.py
│ ├─ cli.py
│ └─ webapp.py
├─ tests/
│ └─ test_generator.py
└─ requirements.txt


---

# 🚀 Como Usar – CLI

### 1️⃣ Instale as dependências
```bash
pip install -r requirements.txt

2️⃣ Execute o gerador

python -m generator.cli

Exemplos de uso

Gerar uma senha de 20 caracteres:

python -m generator.cli --length 20

Gerar senha sem símbolos:

python -m generator.cli --no-symbols

Excluir caracteres ambíguos:

python -m generator.cli --no-ambiguous

Copiar para área de transferência:

python -m generator.cli --copy

🌐 Como Usar – Versão Web (Flask)
Inicie o servidor:

export FLASK_APP=generator.webapp
flask run

Acesse em:

http://127.0.0.1:5000

🧪 Testes

Este projeto utiliza Pytest para garantir corretude da geração de senhas.

Para executar:

pytest

🛠 Tecnologias Utilizadas

    Python 3+

    Flask (versão web)

    Pytest (testes automatizados)

    Secrets (geração criptograficamente segura)

📄 Licença

Este projeto está sob a licença MIT.
Você pode usar, modificar e distribuir livremente.
👨‍💻 Autor

Matheus Barreto
Desenvolvedor • Web • Python • Automação

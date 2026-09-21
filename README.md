# 💡 Calculadora de Consumo de Energia — Projeto da Turma

Este é um projeto feito em **Python (Flask)** para praticar como construir uma aplicação web simples, com várias páginas que se conectam e um cálculo no final.

A ideia: o usuário informa o tamanho da casa, a quantidade de luminárias e a quantidade de aparelhos, e a aplicação calcula uma estimativa de consumo de energia.

Este README foi feito para ajudar você a **rodar o projeto na sua máquina** e **entender onde mexer** para completar a atividade.

---

## ✅ O que você precisa ter instalado

1. **Python 3**
2. **Flask**
3. **Jinja2**

## 🚀 Passo a passo para rodar o projeto

**1. Baixe o projeto**

Se você usa Git:
```bash
git clone https://github.com/aladus14/calculator-bra-main.git
cd calculator-bra-main
```
Se preferir, também dá para baixar o ZIP pelo botão verde **Code > Download ZIP** no GitHub e extrair na sua pasta.

**2. Instale o Flask**

No terminal, dentro da pasta do projeto:
```bash
pip install flask
```
> Se der erro de "comando não encontrado", tente `pip3 install flask` ou `python -m pip install flask`.

**3. Instale o Jinja**

No terminal, dentro da pasta do projeto:
```bash
pip install Jinja2
```

**4. Rode a aplicação a partir do main.py**

**5. Abra no navegador**

Depois de rodar os comandos acima, o terminal vai mostrar algo como:
```
Running on http://127.0.0.1:5000
```
Copie esse endereço e cole no navegador. Pronto, o projeto está no ar! 🎉

> Para parar a aplicação, volte ao terminal e aperte `Ctrl + C`.

---

## 🧭 Como o projeto está organizado

```
calculator-bra-main/
├── main.py          → o "cérebro" do projeto: rotas e cálculo
├── templates/        → as páginas HTML que o usuário vê
├── static/           → CSS, imagens e outros arquivos de estilo
└── .gitignore
```

- **`main.py`**: aqui ficam as rotas (endereços) da aplicação e a função que faz o cálculo.
- **`templates/`**: cada arquivo `.html` aqui dentro é uma página do site.
- **`static/`**: arquivos que dão estilo/visual ao site (CSS, imagens etc).

---

## 🖱️ Como o usuário navega pelo site

1. Página inicial (`/`) → pede o **tamanho da casa**
2. Próxima página → pede a **quantidade de luminárias**
3. Próxima página → pede a **quantidade de aparelhos**
4. Página final → mostra o **resultado do consumo estimado**

Cada resposta do usuário vira parte do endereço (URL), por isso as rotas em `main.py` têm essa cara: `/<size>/<lights>/<device>`.

---

## 🧮 Entendendo o cálculo

A fórmula usada está na função `result_calculate`, dentro de `main.py`:

```python
consumo = tamanho * 100 + luminárias * 0.04 + aparelhos * 5
```

Ou seja:
- Cada metro (ou unidade) de tamanho pesa **100** no cálculo
- Cada luminária pesa **0.04**
- Cada aparelho pesa **5**

---

## 📝 Atividades — o que precisa ser feito
 
O código está cheio de comentários `ATIVIDADE` marcando exatamente onde você precisa completar algo. Ao todo são **4 atividades, espalhadas em 4 arquivos**. Siga a ordem abaixo — ela segue o fluxo que o usuário percorre no site.
 
### Atividade 1 — Link para o formulário na página de resultado
📄 Arquivo: `templates/end.html`
 
Na página de resultado final, tem duas partes marcadas:
- `ATIVIDADE 1` — pede para escrever uma mensagem convidando o usuário a preencher o formulário.
- `ATIVIDADE 1.2` — pede para completar essa tag, que está vazia:
```html
  <a>Preencher o formulário</a>
```
  Você precisa adicionar o `href` apontando para a rota do formulário e uma `class` (para ficar com o mesmo estilo dos outros botões/links do site). Exemplo de padrão a seguir:
```html
  <a href="{{ url_for('form') }}" class="button">Preencher o formulário</a>
```
 
### Atividade 2 — Campo de e-mail no formulário
📄 Arquivo: `templates/form.html`
 
O formulário já tem um campo pronto para o nome do usuário (linhas 27–28):
```html
<label for="name">Seu nome</label>
<input type="text" name="name" id="name" placeholder="Digite seu nome completo" required>
```
Logo abaixo, dentro do `ATIVIDADE 2`, você precisa criar o campo equivalente para o **e-mail**, seguindo o mesmo padrão, mas trocando o `type` para `"email"`:
```html
<label for="email">Seu e-mail</label>
<input type="email" name="email" id="email" placeholder="Digite seu e-mail" required>
```
 
### Atividade 3 — Exibir os dados corretos no resultado do formulário
📄 Arquivo: `templates/form_result.html`
 
Depois que o formulário é enviado, essa página deveria mostrar nome, e-mail, endereço e data — mas hoje todos os campos mostram `{{ name }}` (copiado e colado sem trocar):
```html
<p><strong>Seu nome:</strong> {{ name }}</p>
<p><strong>Seu email:</strong> {{name }}</p>
<p><strong>Seu endereço:</strong> {{ name }}</p>
<p><strong>Sua data:</strong> {{ name }}</p>
```
Você precisa trocar o nome dentro de cada `{{ }}` pela variável certa (`email`, `address`, `date`), assim:
```html
<p><strong>Seu nome:</strong> {{ name }}</p>
<p><strong>Seu email:</strong> {{ email }}</p>
<p><strong>Seu endereço:</strong> {{ address }}</p>
<p><strong>Sua data:</strong> {{ date }}</p>
```
> ⚠️ Essas variáveis só vão aparecer certinho depois que você completar a Atividade 4 no `main.py` (é lá que elas são enviadas para essa página).
 
### Atividade 4 — Coletar os dados do formulário
📄 Arquivo: `main.py`
 
Na rota `/submit`, só o campo `name` está sendo coletado:
```python
name = request.form['name']
```
Você precisa fazer o mesmo para os outros campos que existem no formulário (`email`, `address`, `date`), seguindo esse padrão:
```python
email = request.form['email']
address = request.form['address']
date = request.form['date']
```
E depois, lembre de passar todas essas variáveis para o `render_template`, senão elas não chegam até `form_result.html`:
```python
return render_template('form_result.html',
    name=name,
    email=email,
    address=address,
    date=date,
)
```
 
> 💡 Dica: o `name="..."` usado em cada `<input>` do `form.html` precisa ser **exatamente igual** ao nome usado em `request.form['...']` no `main.py`. Se estiver diferente, vai dar erro `KeyError`.
 
---
 
## 🛠️ Problemas comuns

| Problema | Possível solução |
|---|---|
| `ModuleNotFoundError: No module named 'flask'` | Rode `pip install flask` novamente, verifique se está na pasta certa |
| Página não abre no navegador | Confira se o terminal ainda está rodando e copie o endereço certinho (`http://127.0.0.1:5000`) |
| Alterei o código e nada mudou | Salve o arquivo e recarregue a página no navegador. Como `debug=True` está ativado, o Flask recarrega sozinho |
| `KeyError` ao enviar o formulário | Verifique se o `name="..."` no HTML do formulário é igual ao nome usado em `request.form['...']` no `main.py` |

---

## 📚 Aprendizados desse projeto

- Como criar rotas dinâmicas no Flask (`/<size>/<lights>/<device>`)
- Como passar dados entre páginas usando a URL
- Como usar `render_template` para exibir HTML com dados do Python
- Como capturar dados de um formulário com `request.form`

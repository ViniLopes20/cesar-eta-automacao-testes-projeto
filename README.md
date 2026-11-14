# XYZ Bank — Automação de Testes (Selenium + Python)

Projeto final da disciplina **Automação de Testes Ágeis**, feito em grupo. Automatiza os casos de teste atribuídos ao grupo (9 dos 15 casos `CT01`–`CT15`) da aplicação [XYZ Bank](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login) (AngularJS) com **Selenium WebDriver + Python + pytest**, usando o padrão **Page Object** (em funções, sem classes).

## Índice

- [1. Instalação](#1-instalação)
- [2. Estrutura do projeto](#2-estrutura-do-projeto)
- [3. Como funciona](#3-como-funciona)
- [4. Como criar o seu teste (passo a passo)](#4-como-criar-o-seu-teste-passo-a-passo)
- [5. Regras do grupo](#5-regras-do-grupo)
- [6. Executando os testes](#6-executando-os-testes)

## 1. Instalação

Você precisa ter: **Python 3.9+**, **Google Chrome** e **Git**.
Não precisa instalar o ChromeDriver: o Selenium 4 baixa o driver sozinho na primeira execução (precisa de internet).

### macOS

1. Instale o Python e o Git. Com o [Homebrew](https://brew.sh): `brew install python git`. Ou baixe o Python em [python.org](https://www.python.org/downloads/).
2. Instale o [Google Chrome](https://www.google.com/chrome/).
3. No Terminal:

```bash
git clone <url-do-repo>
cd cesar-eta-automacao-testes-projeto

python3 --version                  # deve mostrar 3.9 ou superior
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

pytest --collect-only              # deve terminar sem erro
```

### Windows

1. Instale o Python em [python.org](https://www.python.org/downloads/) e **marque a opção "Add python.exe to PATH"** no instalador. Instale também o [Git](https://git-scm.com/download/win) e o [Google Chrome](https://www.google.com/chrome/).
2. Abra o **PowerShell** e rode:

```powershell
git clone <url-do-repo>
cd cesar-eta-automacao-testes-projeto

python --version                   # deve mostrar 3.9 ou superior
python -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt

pytest --collect-only              # deve terminar sem erro
```

Se o PowerShell bloquear a ativação ("a execução de scripts foi desabilitada"), rode uma vez `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` e tente de novo. No **Prompt de Comando (cmd)**, a ativação é `.venv\Scripts\activate.bat`.

### Depois de instalado

Sempre que abrir um terminal novo, ative o ambiente virtual de novo (`source .venv/bin/activate` no macOS, `.venv\Scripts\Activate.ps1` no Windows). Com ele ativo, o terminal mostra `(.venv)` no início da linha.

## 2. Estrutura do projeto

```
.
├── src/
│   ├── config/settings.py            # URL, timeout, modo sem janela
│   ├── core/driver_factory.py        # abre o Chrome
│   ├── interface/                    # funções genéricas, usadas por pages e testes
│   │   ├── actions_interface.py      # ações: click, type_text, select_option, get_text...
│   │   ├── locators_interface.py     # locators: by_id, by_css, by_xpath
│   │   ├── expect_interface.py       # verificações: verify_url, verify_text, verify_count...
│   │   └── __init__.py               # exporta as funções para importar de `src.interface`
│   └── pages/                        # um arquivo por tela, com locators e funções
│       ├── home_page.py              # tela inicial / login
│       ├── manager_page.py           # área do gerente
│       ├── customer_page.py          # área do cliente
│       └── transactions_page.py      # extrato
├── tests/
│   ├── conftest.py                   # fixture `driver` (Chrome novo por teste)
│   ├── manager/                      # Gerente     (CT01, CT02, CT03, CT05)
│   ├── customer/                     # Cliente     (CT07, CT08)
│   ├── statement/                    # Extrato     (CT10, CT11)
│   └── navigation/                   # Navegação   (CT13)
├── pytest.ini                        # marcadores e relatório
└── requirements.txt
```

As pastas de `tests/` seguem a coluna **Módulo** dos casos de teste. Só existem as pastas dos módulos que o grupo vai automatizar.

### Divisão dos casos

| Pessoa | Casos | Módulos |
| --- | --- | --- |
| Debora | CT05, CT07, CT08 | Gerente, Cliente |
| Gaby | CT01, CT02, CT03 | Gerente |
| Vini | CT10, CT11, CT13 | Extrato, Navegação |

Os CT04, CT06, CT09, CT12, CT14 e CT15 ainda não foram atribuídos a ninguém; se forem automatizados depois, crie a pasta do módulo e o marcador no `pytest.ini`.

## 3. Como funciona

O projeto não usa classes: tudo são **funções** que recebem o `driver` (o Chrome) como primeiro argumento.

| Camada | O que tem | Regra |
| --- | --- | --- |
| `src/interface/` | **Ações** (`click`, `type_text`, `select_option`, `get_text`, `accept_alert`), **locators** (`by_id`, `by_css`, `by_xpath`) e **verificações** (`verify_url`, `verify_text`, `verify_visible`, `verify_not_visible`, `verify_count`). Todas já esperam a tela atualizar. | Use sempre estas funções; não use `By` nem `driver.find_element` direto. |
| `src/pages/` | Um arquivo por tela, com os **locators** (constantes), as **ações** e as **verificações** da tela | Importa só de `src.interface`. Para verificar, use as funções `verify_*` da interface; função de ação não tem `assert`. |
| `tests/` | O teste: chama as funções das pages e valida com as funções `verify_*` (da interface ou das pages) | Não usa `By`, nem `driver.find_element`. |

- **Um Chrome novo por teste** (fixture `driver`): como os dados ficam no `localStorage`, cada teste começa com os mesmos 5 clientes e contas 1001–1015. Um teste **nunca** depende de outro.
- O teste só declara `def test_x(driver):` e o pytest entrega o navegador.

## 4. Como criar o seu teste (passo a passo)

1. **Pegue seus casos** (veja a [divisão](#divisão-dos-casos)). Crie uma branch: `git checkout -b feat/ct07-depositar-valor`.
2. **Execute o caso à mão** no site, seguindo os passos e conferindo o resultado esperado.
3. **Crie ou complete o arquivo da tela** em `src/pages/`:
   - locators como constantes no topo do arquivo, preferindo `id`, depois `ng-model`/`ng-click`, `placeholder` ou `name`; evite XPath por posição e classes de estilo;
   - uma função por ação ou leitura, sempre com `driver` como primeiro argumento;
   - uma função **faz uma coisa só**: ou executa uma ação (`deposit`), ou verifica (`verify_message`);
   - a verificação usa as funções `verify_*` de `src.interface` (o `assert` e a espera já estão lá); nunca misture ação e verificação na mesma função;
   - antes de criar algo novo, veja se `src.interface` já tem.

   ```python
   from src.interface import by_css, click, verify_text

   DEPOSIT_TAB = by_css("button[ng-click='deposit()']")
   MESSAGE = by_css("span.error")


   def open_deposit(driver):
       click(driver, DEPOSIT_TAB)


   def verify_message(driver, expected):
       verify_text(driver, MESSAGE, expected)
   ```
4. **Crie o teste** em `tests/<módulo>/test_<assunto>.py`:

   ```python
   import pytest

   from src.pages import customer_page, home_page


   @pytest.mark.cliente
   @pytest.mark.positivo
   @pytest.mark.alta
   def test_ct07_depositar_valor_na_conta(driver):
       home_page.open_home_page(driver)
       home_page.login_as_customer(driver, "Harry Potter")

       customer_page.deposit(driver, "500")

       customer_page.verify_message(driver, "Deposit Successful")
   ```

   - nome da função: `test_ct<número>_<descrição_em_português>`, com o código do caso em minúsculo (ex.: `test_ct10_filtrar_extrato_por_periodo`). Assim dá para achar o caso com `pytest -k ct10` ou `git grep -i ct10`, e o nome aparece no relatório;
   - marcadores de **módulo** (`gerente`, `cliente`, `extrato`, `navegacao`), **tipo** (`positivo`, `negativo`) e **prioridade** (`alta`, `media`, `baixa`), iguais aos do caso;
   - cada verificação comprova uma regra do caso; as funções `verify_*` já mostram o valor esperado e o atual quando falham.
5. **Rode seu teste** (com a janela aberta e depois sem janela, com `HEADLESS`) e **duas vezes seguidas**, para detectar instabilidade.
6. **Abra um Pull Request** pequeno para a `main`.

### Cuidados com este site

- **Esperas explícitas** (`WebDriverWait` + `expected_conditions`), nunca `time.sleep()`: o AngularJS atualiza a tela sem recarregar. Depois de depositar, ordenar, filtrar ou excluir, espere o resultado antes de ler.
- **Alertas JavaScript** (*Add Customer* e *Open Account*): use `accept_alert(driver)`; ele espera, devolve o texto e fecha.
- **Não fixe** número de cliente/conta no código: leia do texto do alerta.
- **Não recarregue a página** no meio do teste; use os botões da aplicação (Home, Back, abas).
- As URLs têm `#`: compare a URL completa, usando `settings.url("/manager/addCust")`.
- Os `<select>` são nativos: `select_option` já usa a classe `Select` do Selenium.
- Filtro de data do extrato (`datetime-local`): se `send_keys` não funcionar, preencha por JavaScript e dispare os eventos `input` e `change`.

## 5. Regras do grupo

- Mínimo de **3 testes por pessoa**. Cada um faz os casos da [divisão](#divisão-dos-casos); se quiser trocar, combine com o grupo antes de começar.
- Um teste por caso; uma branch por pessoa/caso; Pull Requests pequenos.
- Mudanças em `src/interface/`, `conftest.py` ou no arquivo de tela de outra pessoa: avise o grupo no PR, porque afetam todos.
- Nomes de funções, variáveis e arquivos em **inglês**; nomes dos testes e textos esperados em **português**.
- Sem comentários nem docstrings no código, sem `time.sleep`, sem `print`, sem imports não usados. Estilo PEP 8.
- Não commite `.venv/`, `reports/` nem `__pycache__/` (já estão no `.gitignore`).
- Serão avaliados: testes funcionando, qualidade dos testes, qualidade do código e boas práticas.

## 6. Executando os testes

```bash
pytest                                  # todos
pytest tests/manager                    # um módulo
pytest tests/customer/test_deposit.py   # um arquivo
pytest -m "alta and positivo"           # por marcador
pytest -k deposito                      # por nome
HEADLESS=true pytest                    # sem abrir a janela (macOS)
$env:HEADLESS="true"; pytest            # sem abrir a janela (Windows PowerShell)
```

Relatório HTML em `reports/report.html`.

# Laboratório de SQL Injection

Este exercício usa SQLite em memória, dados fictícios e nenhum serviço de rede.
As senhas em texto puro são uma simplificação didática; não use este login em produção.

Na raiz do projeto, com Python 3 instalado:

```powershell
python lab/app.py
```

Observe os três resultados. Por que uma senha incorreta é recusada no segundo
caso e aceita no terceiro? Examine a consulta montada e o efeito do comentário `--`.

## Correção e comparação

Este arquivo preserva o exemplo vulnerável; a versão corrigida está em
[`app.py`](../app.py), na raiz. Consulte os placeholders `?` e o segundo argumento de
`execute` na [documentação do SQLite em Python](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).
O objetivo é transmitir os valores separadamente da instrução SQL.

Execute na raiz:

```powershell
python app.py
python -m unittest discover -s tests -v
```

Os testes verificam:

- Login legítimo continua aceito.
- Senha errada é recusada.
- A entrada de laboratório é recusada.
- Um nome contendo apóstrofo é tratado como dado, sem erro de sintaxe.

Esses testes demonstram o comportamento da consulta exercitada; não comprovam
a segurança de uma aplicação completa. Autenticação real também exige hash de
senhas apropriado, controle de tentativas e gestão de sessão.

## Como pedir a revisão ao agente

> Este é meu laboratório local, com dados fictícios e sem rede. Leia lab/app.py
> como mentor de AppSec. Ajude-me a localizar a falha, entender a entrada de
> teste e construir a correção. Diferencie CWE-89 de MITRE ATT&CK e explique
> quando T1190 seria aplicável. Não execute testes em sistemas externos.

SQL Injection é uma categoria de fraqueza [CWE-89](https://cwe.mitre.org/data/definitions/89.html).
[T1190](https://attack.mitre.org/techniques/T1190/) descreve exploração de aplicação
exposta para acesso inicial: é um mapeamento condicional para um cenário real,
não uma classificação automática deste script sem rede.

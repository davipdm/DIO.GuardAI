# Análise AppSec — execução e revisão crítica

Em 21/10/2026, Hermes v0.22.2 recebeu o pedido de revisar `lab/app.py`,
`app.py` e os testes, com contexto de laboratório autorizado, dados fictícios,
banco em memória e sem rede. Foi pedida somente análise estática.

## Trechos reais da resposta inicial

> Falha encontrada: **SQL Injection / bypass de autenticação**

> Causa: `username` e `password` são inseridos diretamente no comando SQL por formatação de string (`f-string`), sem placeholders do driver.

> Menor mudanca: use placeholders do driver, exatamente como `app.py` ja faz:

```python
query = "SELECT username FROM users WHERE username = ? AND password = ?"
return connection.execute(query, (username, password)).fetchone() is not None
```

> Nao executei comandos nem testes; apenas leitura estatica.

## Revisão crítica da resposta

A resposta identificou a falha e reconheceu a correção. Também apresentou
imprecisões que não devem ser reproduzidas como conclusão técnica:

- Associou o bypass a T1078 sem evidência de uso de credenciais válidas.
  Para este script, nenhuma técnica ATT&CK foi demonstrada; T1190 só se
  justifica no cenário hipotético de aplicação exposta para acesso inicial.
- Afirmou que um espaço depois de `--` seria essencial no SQLite; essa
  exigência não se aplica ao comentário SQLite usado aqui.
- Sugeriu exibição de dados por UNION, mas a função retorna apenas booleano.
- Misturou níveis de impacto e escolheu impacto 2 apesar de os recursos serem
  fictícios e descartáveis, contrariando a matriz do projeto.

Esses resultados motivaram orientações mais precisas na skill sobre classificação,
retorno da função e aplicação da matriz. A evidência mostra por que uma resposta
de IA precisa de revisão, mesmo quando reconhece corretamente a correção SQL.

A invocação via `hermes.cmd` retornou o relatório e encerrou com código 1,
com mensagem de comando `CK` não reconhecido. O prompt continha `ATT&CK`;
esse sintoma é compatível com interpretação do caractere `&` pelo launcher.
A execução seguinte evita esse caractere no argumento do comando.

## Conclusão verificada no código e nos testes

SQL concatenado permite comentar a condição de senha. A consulta parametrizada
mantém os valores como dados e os testes recusam a mesma entrada na versão
corrigida. O risco técnico é real, mas o contexto é exclusivamente local.
Pela matriz didática: impacto 1 (dados fictícios), probabilidade 2 (acesso local
específico), produto 2, severidade baixa no laboratório. Uma implantação real
exige nova avaliação de exposição, dados, privilégios e controles.

Referências usadas na revisão: [comentários no SQLite](https://www.sqlite.org/lang_comment.html),
[MITRE T1078](https://attack.mitre.org/techniques/T1078/) e
[MITRE T1190](https://attack.mitre.org/techniques/T1190/).

A [nova execução](hermes-appsec-recheck.txt) registra a resposta após o refinamento
da skill. Foi um teste direcionado às imprecisões observadas, não uma avaliação cega.

A nova resposta corrigiu o mapeamento para T1078 e a matriz (impacto 1,
probabilidade 2, severidade baixa), e reconheceu a mitigação na consulta.
Ainda repetiu a alegação incorreta sobre espaço depois de `--`, citou números
de linha imprecisos e descreveu CVE como identificador de versão. CVE identifica
vulnerabilidades específicas, não versões. Portanto, a transcrição é evidência
do comportamento observado, não uma fonte técnica a ser seguida sem revisão.
A base de conhecimento passou a explicar a sintaxe SQLite explicitamente e os
testes agora cobrem também o payload sem espaço final. Esses ajustes finais
foram validados nos testes locais, sem uma terceira conversa no Hermes.

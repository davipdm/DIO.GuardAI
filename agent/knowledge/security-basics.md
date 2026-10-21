# Fundamentos de segurança

## Vulnerabilidade, ameaça e risco

- **Vulnerabilidade:** fraqueza que pode ser explorada, como concatenar entrada
  externa numa consulta SQL.
- **Ameaça:** ator ou evento capaz de causar dano explorando uma fraqueza.
- **Risco:** possibilidade de dano num contexto, considerando probabilidade,
  impacto e controles. Uma fraqueza confirmada não determina sozinha o risco.

## Tríade CIA

- **Confidencialidade:** informação acessível somente a quem tem autorização.
- **Integridade:** informação e operações protegidas contra alteração indevida.
- **Disponibilidade:** serviço e informação acessíveis quando necessários.

Um bypass de login viola a autenticação. Acesso a dados, alterações e interrupção
dependem do que a conta e a aplicação permitem; não afirme esses efeitos sem evidência.

## Matriz didática de priorização

Impacto: **1 baixo**, dano limitado a dados fictícios/recursos descartáveis;
**2 médio**, dano restrito e recuperável a dados ou serviço;
**3 alto**, dados sensíveis, privilégios relevantes ou interrupção importante.
Considere o maior efeito plausível sustentado pelo contexto na tríade.

Probabilidade: **1 baixa**, acesso restrito e pré-condições difíceis;
**2 média**, acesso ou condições específicas viáveis;
**3 alta**, entrada facilmente alcançável e exploração simples, sem controle eficaz.
Êxito de um teste local comprova a reprodução, não a exposição na internet.

Multiplique impacto × probabilidade: **1–2 baixa**, **3–4 média**, **6 alta**,
**9 crítica**. Sem informação para um dos eixos, registre **pendente**.

| Impacto / Probabilidade | 1 | 2 | 3 |
| --- | --- | --- | --- |
| 1 | Baixa (1) | Baixa (2) | Média (3) |
| 2 | Baixa (2) | Média (4) | Alta (6) |
| 3 | Média (3) | Alta (6) | Crítica (9) |

Esta escala é própria do projeto, não é CVSS e não estima frequência estatística.
Reavalie após a correção e quando mudar o contexto.

## Boas práticas

Use consultas parametrizadas para valores SQL e listas permitidas para nomes
dinâmicos de coluna/tabela. Valide tipos e limites de entrada como defesa adicional.
Restrinja privilégios, mantenha dependências corrigidas e minimize exposição de
serviços. Armazene senhas com algoritmo apropriado, como Argon2id, usando biblioteca
mantida; implemente controle de tentativas e gestão de sessão em aplicações reais.
Proteja segredos fora do Git, evite dados sensíveis em logs, faça backups e teste
a restauração. Registre evidências antes/depois e inclua regressão no desenvolvimento.

## Referências e distinções

No SQLite, `--` inicia um comentário até a quebra de linha ou o fim da entrada;
não exige espaço após os hífens. Em `lab/app.py`, a entrada `aluno' --` também
burla a senha. A função retorna booleano: não exibe as linhas de uma consulta.

- [Python sqlite3: parâmetros](https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders).
- [Sintaxe de comentários SQLite](https://www.sqlite.org/lang_comment.html).
- [CWE-89](https://cwe.mitre.org/data/definitions/89.html): categoria de fraqueza SQL Injection.
- [MITRE ATT&CK T1190](https://attack.mitre.org/techniques/T1190/): exploração de
  aplicação exposta para acesso inicial. Um script local sem rede não demonstra
  essa técnica, embora uma implantação exposta possa tornar o mapeamento pertinente.
- [OWASP Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).

CWE descreve fraquezas; ATT&CK descreve comportamentos de adversários; CVE
identifica vulnerabilidades específicas publicadas. Não são identificadores intercambiáveis.

# Evidências de execução

Data: 21/10/2026 (America/Sao_Paulo).

- [Testes do laboratório](tests.txt): reprodução e regressão da correção.
- [Triagem Ubuntu no Hermes](hermes-ubuntu.md): resposta real à primeira pergunta.
- [Análise AppSec no Hermes](hermes-appsec.md): revisão da falha e da correção.
- [Nova revisão no Hermes](hermes-appsec-recheck.txt): saída integral após ajustes na skill.

Os arquivos de texto são registros de execução, não prints simulados.
Os cenários 1 e 2 de `docs/behavior-checks.md` são exercitados nessas conversas;
o cenário 3 é um roteiro adicional, ainda não executado.

Ambiente: Windows, laboratório SQLite em memória; Hermes Agent v0.22.2,
instalação local existente com Python 3.14.7. Não houve varredura externa.
As conversas do Hermes usam o provedor/modelo previamente configurado localmente.
Credenciais e configuração pessoal não fazem parte deste repositório.

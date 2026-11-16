# Aula 9 — testes de aceitação, de integração e Specification by Example

Duas pastas:

- `exemplo/` — código completo para ler e correr: a regra dos conflitos de
  datas com testes unitários, de aceitação e de integração (SQLite).
- `exercicio/` — o exercício da aula. Comecem por `EXERCICIO.md`.

Para correr os testes, entrem na pasta e usem:

    python3 -m pytest -v

No exemplo, experimentem também:

    python3 -m pytest tests/aceitacao -v        # só os de aceitação
    python3 -m pytest -m "not integracao"       # tudo menos os de integração
    python3 -m pytest -m integracao -v          # só os de integração

Precisam de Python 3.9 ou superior e do pytest (`pip install pytest`).
O SQLite já vem com o Python.

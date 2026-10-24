"""Arruma o kit publicado da Aula 2 em decks/curso-ia-aula2/kit/: move os gabaritos para fora das pastas dos casos,
monta a skill conferir-temas, gera o relatório em Word de cada caso e o README. NUNCA apaga casos/ nem temas/.
Precisa de python-docx (uv pip install --python ~/.venvs/apresentacao/bin/python python-docx)."""
import pathlib, shutil, subprocess, sys, zipfile

AQUI = pathlib.Path(__file__).parent
KIT = AQUI.parent / "kit"
FONTE = AQUI / "kit_fonte"
SKILL = KIT / "gabarito" / "skills" / "conferir-temas"

README = """# Kit da Aula 2: conferir os Temas 6 e 1234 do STF

Seis casos de medicamento, todos fictícios (recriados a partir de situações reais, sem nenhum dado verdadeiro).
O escritório (Dias & Moura) também é fictício.

## O que tem aqui

- `casos/`: os autos de cada caso em PDF (petição inicial, laudo, receita e o que mais importa).
- `temas/`: o texto dos Temas 6 e 1234 em Markdown, com fonte e data da consulta.
- `escritorio/`: o logo do escritório, usado no relatório.
- `gabarito/`: o relatório pronto de cada caso, a resposta (`gabarito.json`) e a skill `conferir-temas`.
  Só abra depois de tentar a sua.

## Como usar na aula

1. Baixe o kit: botão verde **Code** > **Download ZIP**, e extraia a pasta.
2. Abra a pasta no seu app (Claude, ChatGPT Work ou Codex).
3. Escolha um caso e peça ao agente que confira, com os temas, se o autor cumpriu os requisitos do Tema 6 e qual é a
   competência pelo Tema 1234. Use os seis elementos do pedido e a regra "se não souber, diga".
4. Instale a skill `conferir-temas` (copie a pasta `gabarito/skills/conferir-temas` para a pasta de skills da sua
   ferramenta, ou peça ao agente: instale a skill da pasta gabarito/skills/conferir-temas) e rode no caso 6, para ver o
   relatório em Word.
5. Grave o que o agente gerar em `saida/caso-N/`, não dentro de `casos/`.
6. Compare com `gabarito/caso-N/` e confira as páginas decisivas nos PDFs. Em (c) e (d) a leitura é de juízo: o
   gabarito é conservador, e você pode discordar com a fonte na mão.

Para o relatório em Word o agente usa a biblioteca `python-docx`. Se o seu computador recusar a instalação, peça ao
agente que crie um ambiente virtual (`python3 -m venv .venv`) e instale nele.

O relatório organiza a leitura. A conferência da fonte e a decisão sobre a defesa são suas.
"""


def main():
    for p in ("caso", "escritorio/modelo.docx", "escritorio/padrao-do-escritorio.md",
              "gabarito/cronologia.docx", "gabarito/cronologia.md", "gabarito/skills/parecer-no-padrao"):
        alvo = KIT / p
        if alvo.is_dir():
            shutil.rmtree(alvo)
        elif alvo.exists():
            alvo.unlink()
    SKILL.mkdir(parents=True, exist_ok=True)
    shutil.copy(FONTE / "SKILL.md", SKILL / "SKILL.md")
    shutil.copy(FONTE / "relatorio.py", SKILL / "relatorio.py")
    shutil.copy(FONTE / "caso-exemplo.json", SKILL / "exemplo.json")
    shutil.copy(KIT / "escritorio" / "logo-escritorio.png", SKILL / "logo-escritorio.png")
    for pasta in sorted((KIT / "casos").glob("caso-*")):
        destino = KIT / "gabarito" / pasta.name
        destino.mkdir(parents=True, exist_ok=True)
        js = pasta / "gabarito.json"
        if js.exists():
            shutil.move(str(js), destino / "gabarito.json")
        subprocess.run([sys.executable, str(SKILL / "relatorio.py"), str(destino / "gabarito.json"),
                        str(KIT / "escritorio" / "logo-escritorio.png"), str(destino / f"relatorio-{pasta.name}.docx")], check=True)
    with zipfile.ZipFile(KIT / "gabarito" / "conferir-temas.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for f in sorted(SKILL.iterdir()):
            z.write(f, f"conferir-temas/{f.name}")
    (KIT / "README.md").write_text(README, encoding="utf-8")
    print("kit ok")


if __name__ == "__main__":
    main()

"""Gera o escritório fictício da prática da Aula 2: logo, padrão de documentos e o exemplo do resultado em Word.
O emblema (escritorio/emblema.png) foi gerado pelo ./ap imagem (GPT Image) em 23/10/2026 e o nome é composto aqui,
em texto, para não depender da escrita da IA. Uso: python3 escritorio.py (precisa de Chrome e Pillow)."""
import pathlib, subprocess
from PIL import Image

AQUI = pathlib.Path(__file__).parent
ESC = AQUI / "escritorio"
MIDIA = AQUI.parent / "midia"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
VERDE, COBRE = "#064A45", "#B87548"          # amostrados do emblema gerado
NOME = "Dias & Moura"

PADRAO = f"""# Padrão de documentos do escritório {NOME}

- Fonte Georgia, corpo 11, entrelinha 1,3.
- Títulos em verde {VERDE}, com um filete cobre {COBRE} embaixo.
- Cabeçalho: o logo à esquerda (logo-escritorio.png) e, à direita, "Documento de trabalho".
- Título do documento em caixa alta, centralizado, corpo 14, negrito.
- Datas no formato dd/mm/aaaa. Valores em reais com duas casas.
- Tabelas com o cabeçalho verde e o texto branco; linhas alternadas em cinza claro.
- Rodapé: "{NOME} Advocacia · documento fictício" e o número da página.
- O documento termina com a seção "Pontos para conferência humana".
"""

CRONOLOGIA = """# Cronologia do caso

| Data | Fato | Fonte |
|---|---|---|
| 12/03/2019 | Contrato assinado, vigência de 36 meses | contrato.pdf, cláusula terceira |
| 01/04/2021 | Aditivo prorroga por 12 meses, até 12/03/2023 | aditivo.pdf, cláusula primeira |
| 14/02/2023 | Relatório de janeiro entregue, com 9 dias de atraso | notificacao.pdf, segundo parágrafo |
| 20/02/2023 | Multa de 2% notificada, R$ 960,00 | notificacao.pdf, terceiro parágrafo |
| (último pagamento) | Não encontrei nos documentos | sem fonte |
"""


def shot(html: str, destino: pathlib.Path, w: int, h: int):
    tmp = ESC / "_tmp.html"
    tmp.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}",
                    f"--screenshot={destino}", tmp.as_uri()], check=True, capture_output=True)
    tmp.unlink()


def limpar():
    """O fundo gerado é quase branco, não branco; deixa-o branco puro para não aparecer uma caixa no logo."""
    im = Image.open(ESC / "emblema.png").convert("RGB")
    px = im.load()
    for y in range(im.height):
        for x in range(im.width):
            if min(px[x, y]) > 215:
                px[x, y] = (255, 255, 255)
    im.save(ESC / "emblema-limpo.png")


def logo():
    em = (ESC / "emblema-limpo.png").resolve().as_uri()
    html = f"""<meta charset=utf-8><style>body{{margin:0;background:#fff;display:flex;align-items:center;gap:26px;padding:26px 40px;
    font-family:Georgia,serif;color:{VERDE}}} img{{height:150px}} .n{{font-size:62px;letter-spacing:.01em;line-height:1}}
    .s{{font-size:22px;letter-spacing:.32em;color:{COBRE};margin-top:12px}}</style>
    <img src="{em}"><div><div class=n>{NOME}</div><div class=s>ADVOCACIA</div></div>"""
    shot(html, ESC / "logo-escritorio.png", 760, 200)


def exemplo():
    em = (ESC / "emblema-limpo.png").resolve().as_uri()
    linhas = [("12/03/2019", "Contrato assinado, vigência de 36 meses", "contrato.pdf, cláusula terceira"),
              ("01/04/2021", "Aditivo prorroga por 12 meses, até 12/03/2023", "aditivo.pdf, cláusula primeira"),
              ("14/02/2023", "Relatório de janeiro entregue, com 9 dias de atraso", "notificacao.pdf, 2º parágrafo"),
              ("20/02/2023", "Multa de 2% notificada, R$ 960,00", "notificacao.pdf, 3º parágrafo"),
              ("(último pagamento)", "Não encontrei nos documentos", "sem fonte")]
    tr = "".join(f"<tr style='background:{'#f1f1f1' if i % 2 else '#fff'}'><td>{a}</td><td>{b}</td><td>{c}</td></tr>"
                 for i, (a, b, c) in enumerate(linhas))
    html = f"""<meta charset=utf-8><style>
    body{{margin:0;background:#fff;font:11pt/1.3 Georgia,serif;color:#222;width:794px;height:1123px;position:relative}}
    .cab{{display:flex;justify-content:space-between;align-items:center;padding:34px 60px 10px;border-bottom:2px solid {COBRE}}}
    .cab img{{height:56px}} .cab span{{font-size:10pt;color:#666}}
    h1{{text-align:center;text-transform:uppercase;font-size:14pt;color:{VERDE};margin:48px 0 6px}}
    .f{{width:160px;height:3px;background:{COBRE};margin:0 auto 34px}}
    p,h2,table{{margin-left:60px;margin-right:60px}} h2{{font-size:12pt;color:{VERDE};border-bottom:2px solid {COBRE};padding-bottom:4px;margin-top:30px}}
    table{{border-collapse:collapse;width:674px;font-size:10pt}} th{{background:{VERDE};color:#fff;text-align:left;padding:7px 9px}} td{{padding:7px 9px;vertical-align:top}}
    .rod{{position:absolute;bottom:34px;left:60px;right:60px;display:flex;justify-content:space-between;font-size:8.5pt;color:#666;border-top:1px solid #ccc;padding-top:8px}}
    </style>
    <div class=cab><img src="{em}"><span>Documento de trabalho</span></div>
    <h1>Cronologia do contrato nº 07/2019</h1><div class=f></div>
    <h2>Datas e fontes</h2>
    <table><tr><th>Data</th><th>Fato</th><th>Fonte</th></tr>{tr}</table>
    <h2>Pontos para conferência humana</h2>
    <p>Conferir a data do último pagamento, que não consta dos documentos, e os prazos e a multa nos papéis originais.</p>
    <div class=rod><span>{NOME} Advocacia · documento fictício</span><span>1</span></div>"""
    shot(html, MIDIA / "caso-parecer-exemplo.png", 794, 1123)
    Image.open(MIDIA / "caso-parecer-exemplo.png").convert("RGB").save(MIDIA / "caso-parecer-exemplo.webp", "WEBP", quality=88)
    (MIDIA / "caso-parecer-exemplo.png").unlink()


if __name__ == "__main__":
    (ESC / "padrao-do-escritorio.md").write_text(PADRAO, encoding="utf-8")
    (ESC / "cronologia-exemplo.md").write_text(CRONOLOGIA, encoding="utf-8")
    limpar()
    logo()
    exemplo()
    Image.open(ESC / "logo-escritorio.png").convert("RGB").save(MIDIA / "logo-escritorio.webp", "WEBP", quality=90)
    print("ok")

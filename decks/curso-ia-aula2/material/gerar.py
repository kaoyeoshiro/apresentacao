"""Gera o caso fictício da Aula 2 (contrato, aditivo e notificação) em PDF, o PDF único, o .zip e as imagens dos slides.
Tudo é inventado para a aula; nomes, CNPJs e valores não existem. Uso: python3 gerar.py (precisa de Chrome e PyMuPDF)."""
import subprocess, zipfile, pathlib, shutil
import fitz
from PIL import Image

AQUI = pathlib.Path(__file__).parent
SAIDA = AQUI / "caso-ficticio"
MIDIA = AQUI.parent / "midia"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 22mm 20mm 20mm 20mm; }
body { font: 12.5pt/1.55 Georgia, 'Times New Roman', serif; color: #1a1a1a; }
h1 { font-size: 15pt; text-align: center; margin: 0 0 4pt; letter-spacing: .02em; }
h2 { font-size: 11pt; text-align: center; margin: 0 0 18pt; font-weight: normal; }
p { margin: 0 0 9pt; text-align: justify; }
.cl { font-weight: bold; }
.ass { margin-top: 30pt; display: flex; justify-content: space-between; gap: 30pt; }
.ass div { flex: 1; border-top: 1px solid #333; padding-top: 4pt; font-size: 10.5pt; text-align: center; }
.rod { position: fixed; bottom: 0; left: 0; right: 0; text-align: center; font-size: 8.5pt; color: #666; }
mark { background: #f3c85a; color: inherit; padding: 0 2px; }
.cab { text-align: center; font-size: 10.5pt; margin-bottom: 14pt; }
.dest { margin-bottom: 14pt; }
"""

RODAPE = '<div class="rod">Documento fictício, criado para fins didáticos. Nomes, números e valores não existem.</div>'

def html(titulo, subtitulo, corpo, destaque=None):
    if destaque:
        corpo = corpo.replace(destaque, f"<mark>{destaque}</mark>")
    return f"<!doctype html><meta charset='utf-8'><style>{CSS}</style><h1>{titulo}</h1><h2>{subtitulo}</h2>{corpo}{RODAPE}"

PARTES = ("<p><b>CONTRATANTE:</b> MUNICÍPIO DE VILA SERENA, pessoa jurídica de direito público, inscrita no CNPJ sob o nº 12.345.678/0001-90, "
          "neste ato representado pelo Prefeito Municipal.</p>"
          "<p><b>CONTRATADA:</b> HORIZONTE MANUTENÇÃO PREDIAL LTDA., inscrita no CNPJ sob o nº 98.765.432/0001-10, "
          "neste ato representada por seu sócio-administrador.</p>")

CONTRATO = PARTES + """
<p>As partes acima qualificadas firmam o presente contrato, que se rege pelas cláusulas a seguir.</p>
<p><span class="cl">CLÁUSULA PRIMEIRA, do objeto.</span> A CONTRATADA prestará serviços de manutenção predial preventiva e corretiva nos prédios da Secretaria Municipal de Educação, conforme o termo de referência anexo ao processo administrativo.</p>
<p><span class="cl">CLÁUSULA SEGUNDA, do valor.</span> A CONTRATANTE pagará à CONTRATADA o valor mensal de R$ 48.000,00 (quarenta e oito mil reais), mediante medição aprovada pela fiscalização.</p>
<p><span class="cl">CLÁUSULA TERCEIRA, do prazo.</span> As partes firmam este contrato em 12/03/2019, com vigência de 36 (trinta e seis) meses, contados da assinatura.</p>
<p><span class="cl">CLÁUSULA QUARTA, do pagamento.</span> O pagamento será feito até o décimo dia útil do mês seguinte ao da medição, por ordem bancária, após o atesto da nota fiscal.</p>
<p><span class="cl">CLÁUSULA QUINTA, da medição.</span> A medição dos serviços será mensal. A CONTRATADA entregará o relatório mensal de serviços até o dia 5 (cinco) do mês seguinte ao da execução.</p>
<p><span class="cl">CLÁUSULA SEXTA, das obrigações da contratada.</span> Manter equipe habilitada, fornecer os materiais necessários e responder pelos danos que causar aos prédios e a terceiros durante a execução.</p>
<p><span class="cl">CLÁUSULA SÉTIMA, da fiscalização.</span> A fiscalização será exercida por servidor designado pela CONTRATANTE, que atestará as medições e registrará as ocorrências.</p>
<p><span class="cl">CLÁUSULA OITAVA, do reajuste.</span> O valor mensal será reajustado a cada doze meses, pela variação do IPCA, a contar da data da assinatura.</p>
<p><span class="cl">CLÁUSULA NONA, da penalidade.</span> O atraso na entrega do relatório mensal sujeita a CONTRATADA à multa de 2% (dois por cento) sobre o valor mensal, por competência em atraso.</p>
<p><span class="cl">CLÁUSULA DÉCIMA, da rescisão.</span> O contrato poderá ser rescindido por inadimplemento de qualquer das partes, garantido o contraditório e a ampla defesa.</p>
<p><span class="cl">CLÁUSULA DÉCIMA PRIMEIRA, do foro.</span> Fica eleito o foro da Comarca de Vila Serena para dirimir as questões deste contrato.</p>
<p>Vila Serena, 12 de março de 2019.</p>
<div class="ass"><div>MUNICÍPIO DE VILA SERENA</div><div>HORIZONTE MANUTENÇÃO PREDIAL LTDA.</div></div>
"""

ADITIVO = PARTES + """
<p>As partes resolvem aditar o Contrato nº 07/2019, firmado em 12/03/2019, nos termos seguintes.</p>
<p><span class="cl">CLÁUSULA PRIMEIRA.</span> O aditivo altera a cláusula terceira do contrato original e prorroga a vigência por 12 (doze) meses, a contar do término da vigência original (12/03/2022), de modo que o contrato passa a vigorar até 12/03/2023.</p>
<p><span class="cl">CLÁUSULA SEGUNDA.</span> Permanecem inalteradas as demais cláusulas do contrato original, inclusive o valor mensal e a penalidade da cláusula nona.</p>
<p><span class="cl">CLÁUSULA TERCEIRA.</span> A CONTRATANTE publicará o extrato deste aditivo no órgão oficial do Município.</p>
<p>Vila Serena, 01 de abril de 2021.</p>
<div class="ass"><div>MUNICÍPIO DE VILA SERENA</div><div>HORIZONTE MANUTENÇÃO PREDIAL LTDA.</div></div>
"""

NOTIF = """
<p class="dest"><b>À HORIZONTE MANUTENÇÃO PREDIAL LTDA.</b><br>A/C do sócio-administrador</p>
<p><b>Assunto:</b> aplicação de multa contratual, Contrato nº 07/2019.</p>
<p>O MUNICÍPIO DE VILA SERENA, por sua Secretaria Municipal de Educação, comunica que o relatório mensal de serviços referente a janeiro de 2023 foi entregue em 14/02/2023, quando o prazo da cláusula quinta do contrato terminava em 05/02/2023.</p>
<p>Fica a contratada notificada da multa de 2% prevista na cláusula nona, incidente sobre o valor mensal de R$ 48.000,00, no total de R$ 960,00 (novecentos e sessenta reais).</p>
<p>A contratada dispõe de 5 (cinco) dias úteis, a contar do recebimento desta notificação, para apresentar defesa.</p>
<p>Vila Serena, 20 de fevereiro de 2023.</p>
<div class="ass"><div>Secretário Municipal de Educação</div><div>Recebido em ___/___/______</div></div>
"""

DOCS = {
    "contrato": ("CONTRATO DE PRESTAÇÃO DE SERVIÇOS Nº 07/2019", "Manutenção predial", CONTRATO, "As partes firmam este contrato em 12/03/2019, com vigência de 36 (trinta e seis) meses, contados da assinatura."),
    "aditivo": ("PRIMEIRO TERMO ADITIVO AO CONTRATO Nº 07/2019", "Prorrogação de prazo", ADITIVO, "prorroga a vigência por 12 (doze) meses, a contar do término da vigência original (12/03/2022)"),
    "notificacao": ("NOTIFICAÇÃO Nº 031/2023", "Secretaria Municipal de Educação", NOTIF, "multa de 2% prevista na cláusula nona"),
}

def pdf(nome, corpo_html, destino):
    tmp = AQUI / "fonte" / f"{nome}.html"
    tmp.write_text(corpo_html, encoding="utf-8")
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={destino}", tmp.as_uri()],
                   check=True, capture_output=True)

def png(pdf_path, destino, pagina=0, recorte=None, largura=900):
    d = fitz.open(pdf_path)
    pg = d[pagina]
    pix = pg.get_pixmap(matrix=fitz.Matrix(2.2, 2.2), clip=recorte)
    pix.save(str(destino))
    im = Image.open(destino).convert("RGB")
    if im.width > largura:
        im = im.resize((largura, round(im.height * largura / im.width)))
    im.save(destino.with_suffix(".webp"), "WEBP", quality=88)
    destino.unlink()

if __name__ == "__main__":
    SAIDA.mkdir(exist_ok=True)
    for nome, (t, s, corpo, dest) in DOCS.items():
        pdf(nome, html(t, s, corpo), SAIDA / f"{nome}.pdf")
        pdf(nome + "-destaque", html(t, s, corpo, dest), AQUI / "fonte" / f"{nome}-destaque.pdf")
    # PDF único com os três, na ordem do caso
    unico = fitz.open()
    for nome in DOCS:
        unico.insert_pdf(fitz.open(SAIDA / f"{nome}.pdf"))
    unico.save(AQUI / "caso-ficticio-completo.pdf")
    with zipfile.ZipFile(AQUI / "caso-ficticio.zip", "w", zipfile.ZIP_DEFLATED) as z:
        for nome in DOCS:
            z.write(SAIDA / f"{nome}.pdf", f"caso-ficticio/{nome}.pdf")
        esc = AQUI / "escritorio"          # criado por escritorio.py; vai junto para a segunda prática
        for nome in ("padrao-do-escritorio.md", "logo-escritorio.png", "cronologia-exemplo.md"):
            if (esc / nome).exists():
                z.write(esc / nome, f"caso-ficticio/{'reserva/' if nome.startswith('cronologia') else ''}{nome}")
    # imagens dos slides: primeira página inteira de cada papel e a página do contrato com o trecho marcado
    for nome in DOCS:
        png(SAIDA / f"{nome}.pdf", MIDIA / f"caso-{nome}.png", 0)
    png(AQUI / "fonte" / "contrato-destaque.pdf", MIDIA / "caso-contrato-trecho.png", 0)
    print("ok", [p.name for p in SAIDA.iterdir()])

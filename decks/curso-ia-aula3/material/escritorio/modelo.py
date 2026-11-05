"""Gera o modelo timbrado (modelo-timbrado.docx) do escritório fictício Dias & Moura, o mesmo da Aula 2, para a demo da
skill de Word: o parecer é pedido "dentro deste modelo". Segue padrao-do-escritorio.md; o logo vem da Aula 2.
Os estilos (Normal, Title, Heading 1) carregam o padrão, para que quem preencher o modelo o herde sem formatar à mão.
Uso: ~/.venvs/apresentacao/bin/python modelo.py   (precisa de python-docx)"""
import pathlib
from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor

AQUI = pathlib.Path(__file__).parent
VERDE, COBRE, CINZA = "064A45", "B87548", "666666"
NOME = "Dias & Moura"


def fonte(estilo_ou_run, tam=None, negrito=None, cor=None):
    f = estilo_ou_run.font
    f.name = "Georgia"
    rpr = estilo_ou_run.element.get_or_add_rPr()
    fontes = rpr.get_or_add_rFonts(); fontes.set(qn("w:eastAsia"), "Georgia")
    for tema in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):   # a fonte do tema venceria a Georgia
        fontes.attrib.pop(qn(f"w:{tema}"), None)
    if tam: f.size = Pt(tam)
    if negrito is not None: f.bold = negrito
    if cor: f.color.rgb = RGBColor.from_string(cor)


def filete(ppr, cor, tam):
    b = OxmlElement("w:pBdr"); e = OxmlElement("w:bottom")
    for k, v in (("val", "single"), ("sz", str(tam)), ("space", "4"), ("color", cor)):
        e.set(qn(f"w:{k}"), v)
    b.append(e); ppr.append(b)


def pagina(par):
    for tipo, instr in (("begin", None), (None, "PAGE"), ("end", None)):
        r = par.add_run(); fonte(r, 8.5, cor=CINZA)
        if tipo:
            f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), tipo); r._r.append(f)
        else:
            i = OxmlElement("w:instrText"); i.set(qn("xml:space"), "preserve"); i.text = instr; r._r.append(i)


def main():
    d = Document(); sec = d.sections[0]
    sec.page_width, sec.page_height = Cm(21), Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.5); sec.top_margin, sec.bottom_margin = Cm(3.0), Cm(2.2)
    largura = sec.page_width - sec.left_margin - sec.right_margin

    normal = d.styles["Normal"]; fonte(normal, 11)
    normal.paragraph_format.line_spacing = 1.3; normal.paragraph_format.space_after = Pt(6)
    titulo = d.styles["Title"]; fonte(titulo, 14, True, VERDE)
    titulo.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER; titulo.paragraph_format.space_after = Pt(18)
    for velho in titulo.element.pPr.findall(qn("w:pBdr")):
        titulo.element.pPr.remove(velho)
    titulo.font.all_caps = True
    secao = d.styles["Heading 1"]; fonte(secao, 12, True, VERDE)
    secao.paragraph_format.space_before = Pt(18); secao.paragraph_format.space_after = Pt(6)
    filete(secao.element.get_or_add_pPr(), COBRE, 12)

    h = sec.header.paragraphs[0]; h.paragraph_format.tab_stops.add_tab_stop(largura, WD_TAB_ALIGNMENT.RIGHT)
    h.add_run().add_picture(str(AQUI / "logo-escritorio.png"), height=Cm(1.3))
    r = h.add_run("\t\tDocumento de trabalho"); fonte(r, 9, cor=CINZA)
    filete(h._p.get_or_add_pPr(), COBRE, 6)
    f = sec.footer.paragraphs[0]; f.paragraph_format.tab_stops.add_tab_stop(largura, WD_TAB_ALIGNMENT.RIGHT)
    r = f.add_run(f"{NOME} Advocacia · documento fictício\t\tPágina "); fonte(r, 8.5, cor=CINZA); pagina(f)

    d.add_paragraph("Título do documento", style="Title")
    d.add_paragraph("Relatório", style="Heading 1")
    d.add_paragraph("Texto do documento em Georgia, corpo 11, entrelinha 1,3. Datas no formato dd/mm/aaaa e valores em "
                    "reais com duas casas, por exemplo R$ 1.250,00.")
    d.add_paragraph("Fundamentação", style="Heading 1")
    d.add_paragraph("Substitua este texto pelo conteúdo do documento.")
    d.add_paragraph("Pontos para conferência humana", style="Heading 1")
    d.add_paragraph("Liste aqui o que precisa ser conferido na fonte antes de o documento sair do escritório.")
    d.save(AQUI / "modelo-timbrado.docx")
    print("modelo-timbrado.docx ok")


if __name__ == "__main__":
    main()

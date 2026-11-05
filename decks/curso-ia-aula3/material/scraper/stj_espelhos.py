"""Boletim de jurisprudência do STJ: baixa os "Espelhos de acórdãos" de uma turma no Portal de Dados Abertos do STJ
(licença Creative Commons Atribuição), filtra a ementa por tema e grava um CSV que abre no Excel.

Uso:
  python3 stj_espelhos.py --tema medicamento
  python3 stj_espelhos.py --tema "execução fiscal" --turma primeira-turma --saida boletim.csv
  python3 stj_espelhos.py --tema saude --offline amostra/20260930.json      (sem internet)

Pesquisa por tema, nunca por pessoa (Res. CNJ 121/2010, art. 5º). Duas requisições, uma de cada vez, com pausa.
Só biblioteca padrão do Python: não precisa instalar nada."""
import argparse, csv, json, re, sys, time, unicodedata, urllib.request

API = "https://dadosabertos.web.stj.jus.br/api/3/action/package_show?id=espelhos-de-acordaos-{turma}"
AGENTE = {"User-Agent": "curso co.juris, demonstracao em sala"}
# Nomes reais dos campos, conferidos no arquivo 20260930.json e no dicionario-espelhodoacordao.csv do STJ.
CAMPOS = ["siglaClasse", "numeroProcesso", "ministroRelator", "nomeOrgaoJulgador", "dataDecisao", "ementa"]


def baixar(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=AGENTE), timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def mais_recente(recursos):
    """O recurso JSON mensal (nome AAAAMMDD.json) de data maior."""
    mensais = [r for r in recursos if re.fullmatch(r"\d{8}\.json", r.get("name", ""))]
    return max(mensais, key=lambda r: r["name"])


def sem_acento(texto):
    return "".join(c for c in unicodedata.normalize("NFD", texto or "") if unicodedata.category(c) != "Mn").lower()


def filtrar(registros, termo, campos):
    alvo = sem_acento(termo)
    return [r for r in registros if any(alvo in sem_acento(r.get(c)) for c in campos)]


def main(argv=None):
    p = argparse.ArgumentParser(description="Boletim de acórdãos do STJ por tema, em CSV.")
    p.add_argument("--tema", required=True, help="palavra ou expressão procurada na ementa")
    p.add_argument("--turma", default="primeira-turma", help="conjunto no portal (padrão: primeira-turma)")
    p.add_argument("--offline", metavar="ARQUIVO", help="lê um JSON já baixado, sem internet")
    p.add_argument("--saida", default="boletim.csv", help="arquivo CSV de saída (padrão: boletim.csv)")
    a = p.parse_args(argv)

    if a.offline:
        with open(a.offline, encoding="utf-8") as f:
            registros = json.load(f)
    else:
        recurso = mais_recente(baixar(API.format(turma=a.turma))["result"]["resources"])
        print("Arquivo mais recente:", recurso["name"])
        time.sleep(2)
        registros = baixar(recurso["url"])

    achados = filtrar(registros, a.tema, ["ementa"])
    with open(a.saida, "w", newline="", encoding="utf-8-sig") as f:   # utf-8-sig e ";" para o Excel em português
        w = csv.writer(f, delimiter=";")
        w.writerow(CAMPOS)
        for r in achados:
            w.writerow([r.get(c) or "" for c in CAMPOS])
    print(f"{len(achados)} de {len(registros)} acórdãos com '{a.tema}' na ementa -> {a.saida}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

import json, pathlib
from stj_espelhos import mais_recente, filtrar

AMOSTRA = pathlib.Path(__file__).parent / "amostra"

def test_mais_recente_escolhe_o_json_de_data_maior():
    recursos = [{"name": "20260831.json", "format": "JSON", "url": "a"},
                {"name": "dicionario.csv", "format": "CSV", "url": "b"},
                {"name": "20260930.json", "format": "JSON", "url": "c"}]
    assert mais_recente(recursos)["url"] == "c"

def test_filtrar_acha_o_termo_sem_acento_e_sem_caixa():
    regs = [{"ementa": "FORNECIMENTO DE MEDICAMENTO. Saúde."}, {"ementa": "Tributário."}]
    assert len(filtrar(regs, "medicamento", ["ementa"])) == 1
    assert len(filtrar(regs, "saude", ["ementa"])) == 1

def test_amostra_real_tem_os_campos_usados():
    arq = next(AMOSTRA.glob("2026*.json"))
    regs = json.loads(arq.read_text(encoding="utf-8"))
    from stj_espelhos import CAMPOS
    assert all(c in regs[0] for c in CAMPOS)

"""Caminhos do repositório e dos projetos vizinhos de onde vem a matéria-prima."""
from __future__ import annotations

import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MOTOR = RAIZ / "motor"
TEMAS = RAIZ / "temas"
DECKS = RAIZ / "decks"
DEMO = DECKS / "demo"


def video_maker() -> Path:
    """O claude_video_maker: vídeo por código (Remotion, Manim, HTML), vídeo por IA (Omni) e a ponte de imagem
    (image-video-api). Por padrão é a pasta vizinha; CVM_PROJETO troca."""
    p = Path(os.environ.get("CVM_PROJETO") or RAIZ.parent / "claude_video_maker").resolve()
    if not (p / "cvm").is_file():
        raise SystemExit(f"claude_video_maker não encontrado em {p} (defina CVM_PROJETO)")
    return p

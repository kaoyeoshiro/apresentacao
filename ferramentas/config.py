"""Caminhos do repositório e dos projetos vizinhos de onde vem a matéria-prima."""
from __future__ import annotations

import os
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
MOTOR = RAIZ / "motor"
TEMAS = RAIZ / "temas"
DECKS = RAIZ / "decks"
DEMO = DECKS / "demo"            # molde do modo slides (./ap novo --modo slides)
CATALOGO = DECKS / "catalogo"    # molde do plano contínuo, o padrão do ./ap novo (docs/cenas.md)


def video_maker() -> Path:
    """O claude_video_maker: vídeo por código (Remotion, Manim, HTML), vídeo por IA (Omni) e a ponte de imagem
    (image-video-api). Por padrão é a pasta vizinha, procurada também acima do repositório (num worktree em
    .claude/worktrees/, a vizinha fica três níveis acima); CVM_PROJETO troca."""
    vizinha = next((q / "claude_video_maker" for q in RAIZ.parents if (q / "claude_video_maker" / "cvm").is_file()),
                   RAIZ.parent / "claude_video_maker")
    p = Path(os.environ.get("CVM_PROJETO") or vizinha).resolve()
    if not (p / "cvm").is_file():
        raise SystemExit(f"claude_video_maker não encontrado em {p} (defina CVM_PROJETO)")
    return p

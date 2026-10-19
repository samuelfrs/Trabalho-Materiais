"""
Gerador dos 5 Slides em PDF (16:9 Widescreen - Alta Resolução)
Disciplina: TI0060 - Materiais Eletrônicos e Optoeletrônicos (UFC 2026.2)
Tema 2: Efeito Fotoelétrico por meio de Simulação Computacional
Equipe: Logan e Samuel Farias
"""

import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.backends.backend_pdf import PdfPages

# Paleta Institucional UFC
UFC_NAVY = "#0f2c59"
UFC_BLUE = "#0284c7"
UFC_LIGHT = "#f8fafc"
CARD_BG = "#f1f5f9"
BORDER_GRAY = "#cbd5e1"
ALERT_BG = "#fef2f2"
ALERT_BORDER = "#dc2626"
OK_BG = "#f0fdf4"
OK_BORDER = "#16a34a"
GOLD_BG = "#fffbeb"
GOLD_BORDER = "#d97706"
TEXT_DARK = "#0f172a"
TEXT_MUTED = "#475569"


def criar_slide_base(titulo_slide: str, num_slide: int, total_slides: int = 5):
    """Cria uma figura 16:9 (16 x 9 polegadas) com cabeçalho e rodapé estilo Beamer UFC."""
    fig = plt.figure(figsize=(16, 9), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 9)
    ax.axis("off")

    # Fundo branco suave
    ax.add_patch(patches.Rectangle((0, 0), 16, 9, facecolor="#ffffff", zorder=0))

    # Cabeçalho Principal (Top Bar)
    ax.add_patch(patches.Rectangle((0, 8.05), 16, 0.95, facecolor=UFC_NAVY, zorder=1))
    ax.add_patch(patches.Rectangle((0, 7.97), 16, 0.08, facecolor=UFC_BLUE, zorder=2))

    ax.text(
        0.45,
        8.52,
        titulo_slide,
        color="white",
        fontsize=20,
        fontweight="bold",
        va="center",
        ha="left",
        zorder=3,
    )
    ax.text(
        15.55,
        8.52,
        "UFC • TI0060",
        color="#bae6fd",
        fontsize=12.5,
        fontweight="bold",
        va="center",
        ha="right",
        zorder=3,
    )

    # Rodapé (Bottom Bar)
    ax.add_patch(patches.Rectangle((0, 0), 16, 0.42, facecolor=UFC_NAVY, zorder=1))
    ax.text(
        0.45,
        0.21,
        "Equipe (Tema 2): Logan e Samuel Farias  |  Prof. Dr. Joacir Andrade",
        color="#e2e8f0",
        fontsize=10.5,
        va="center",
        ha="left",
        zorder=3,
    )
    ax.text(
        8.0,
        0.21,
        "Efeito Fotoelétrico por meio de Simulação Computacional",
        color="#93c5fd",
        fontsize=10.5,
        fontweight="bold",
        va="center",
        ha="center",
        zorder=3,
    )
    ax.text(
        15.55,
        0.21,
        f"Slide {num_slide} / {total_slides}",
        color="white",
        fontsize=11,
        fontweight="bold",
        va="center",
        ha="right",
        zorder=3,
    )

    return fig, ax


def desenhar_card(ax, x, y, w, h, titulo, bg_color=CARD_BG, border_color=BORDER_GRAY, header_bg=None):
    """Desenha um card com borda arredondada e opcionalmente uma barra de título."""
    box = patches.FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.02,rounding_size=0.12",
        facecolor=bg_color,
        edgecolor=border_color,
        linewidth=1.6,
        zorder=2,
    )
    ax.add_patch(box)
    if titulo:
        cor_titulo = header_bg if header_bg else border_color
        ax.text(
            x + 0.25,
            y + h - 0.35,
            titulo,
            color=cor_titulo,
            fontsize=14,
            fontweight="bold",
            va="center",
            ha="left",
            zorder=4,
        )
        ax.plot([x + 0.2, x + w - 0.2], [y + h - 0.58, y + h - 0.58], color=border_color, lw=1.0, alpha=0.6, zorder=3)


def slide1_questao_central_e_contexto():
    fig, ax = criar_slide_base("1. Efeito Fotoelétrico: Questão Central e Ruptura Quântica", 1)

    # Banner de Identificação e Questão Central
    desenhar_card(
        ax, 0.45, 5.85, 15.1, 1.85,
        "TEMA 2 — EQUIPE: LOGAN E SAMUEL FARIAS  (1ª Avaliação — TI0060 Materiais Eletrônicos e Optoeletrônicos)",
        bg_color="#eff6ff", border_color=UFC_BLUE, header_bg=UFC_NAVY
    )
    ax.text(
        0.72, 6.75,
        "• Questão Central: Como a frequência (f) e a intensidade (I) da luz incidente influenciam a emissão de elétrons\n"
        "  de uma superfície metálica, e como a simulação permite verificar as previsões da teoria quântica da luz?",
        color=TEXT_DARK, fontsize=13.5, fontweight="bold", va="center", ha="left", zorder=4, linespacing=1.45
    )
    ax.text(
        0.72, 6.08,
        "• Método: Simulação computacional parametrizada (Python + Simulador Interativo HTML5) variando f, I e o metal (φ).",
        color="#1e40af", fontsize=12.5, va="center", ha="left", zorder=4
    )

    # Coluna Esquerda: Falha da Teoria Clássica
    desenhar_card(
        ax, 0.45, 0.75, 7.35, 4.85,
        "▸ 1. Por que a Física Clássica Ondulatória Falhou?",
        bg_color=ALERT_BG, border_color=ALERT_BORDER, header_bg="#991b1b"
    )
    texto_classico = (
        "Na teoria eletromagnética clássica (Maxwell), a energia de\n"
        "uma onda luminosa seria contínua e proporcional apenas à\n"
        "sua amplitude ao quadrado (Intensidade $I \\propto E_0^2$):\n\n"
        "1) Ausência de Frequência de Corte:\n"
        "   • Qualquer frequência $f$ deveria arrancar elétrons bastando\n"
        "     aumentar a intensidade $I$ da fonte luminosa.\n\n"
        "2) Energia Cinética Dependente da Intensidade:\n"
        "   • Maior intensidade $I$ (maior campo elétrico $\\vec{E}$) deveria\n"
        "     ejetar elétrons com maior energia cinética $K_{\\max}$.\n\n"
        "3) Atraso Temporal na Emissão:\n"
        "   • Sob luz fraca, o elétron levaria minutos acumulando\n"
        "     energia contínua antes de escapar do metal."
    )
    ax.text(0.72, 4.82, texto_classico, color=TEXT_DARK, fontsize=12.2, va="top", ha="left", zorder=4, linespacing=1.36)

    # Coluna Direita: Hipótese Quântica de Planck-Einstein
    desenhar_card(
        ax, 8.20, 0.75, 7.35, 4.85,
        "▸ 2. A Solução Quântica (Planck 1900 / Einstein 1905)",
        bg_color=OK_BG, border_color=OK_BORDER, header_bg="#166534"
    )
    texto_quantico = (
        "Einstein propôs que a luz é composta por pacotes discretos\n"
        "de energia (quanta de luz ou fótons), cuja energia depende\n"
        "exclusivamente da sua frequência $f$:"
    )
    ax.text(8.47, 4.82, texto_quantico, color=TEXT_DARK, fontsize=12.2, va="top", ha="left", zorder=4, linespacing=1.36)

    # Caixa de destaque da equação E = hf
    ax.add_patch(patches.FancyBboxPatch(
        (9.1, 3.15), 5.55, 0.80,
        boxstyle="round,pad=0.02,rounding_size=0.1",
        facecolor="#dcfce7", edgecolor="#15803d", linewidth=1.5, zorder=3
    ))
    ax.text(
        11.87, 3.55,
        r"$E_{\mathrm{fóton}} = h f = \frac{h c}{\lambda}$",
        color="#14532d", fontsize=19, fontweight="bold", va="center", ha="center", zorder=4
    )

    texto_quantico_2 = (
        "• Constante de Planck:\n"
        "  $h = 6,626\\times 10^{-34}\\text{ J}\\cdot\\text{s} \\approx 4,136\\times 10^{-15}\\text{ eV}\\cdot\\text{s}$\n\n"
        "• Interação Individual (Tudo ou Nada):\n"
        "  Cada colisão ocorre entre 1 único fóton e 1 único elétron.\n"
        "  Se $hf < \\phi$, o elétron não escapa, mesmo com $I$ altíssima!\n"
        "  Se $hf \\geq \\phi$, a emissão é instantânea ($\\sim 10^{-9}$ s)."
    )
    ax.text(8.47, 2.92, texto_quantico_2, color=TEXT_DARK, fontsize=12.0, va="top", ha="left", zorder=4, linespacing=1.38)

    return fig


def slide2_modelagem_e_metais(dir_imgs: str):
    fig, ax = criar_slide_base("2. Função Trabalho (φ), Frequência de Corte e Equação de Einstein", 2)

    # Coluna Esquerda: Equações Governantes
    desenhar_card(
        ax, 0.45, 0.75, 6.75, 6.95,
        "▸ Fundamentação Teórica e Equações Governantes",
        bg_color=CARD_BG, border_color=UFC_BLUE, header_bg=UFC_NAVY
    )

    ax.text(
        0.70, 6.92,
        "1. Função Trabalho ($\\phi$ ou $W_0$):\n"
        "   Energia mínima necessária para arrancar um elétron do\n"
        "   nível de Fermi do metal até o vácuo externo ($v = 0$).",
        color=TEXT_DARK, fontsize=12.0, va="top", ha="left", zorder=4, linespacing=1.35
    )

    ax.text(
        0.70, 5.75,
        "2. Frequência de Corte ($f_0$) e Comprimento Limiar ($\\lambda_0$):\n"
        "   Condição limite de emissão ($hf_0 = \\phi$):",
        color=TEXT_DARK, fontsize=12.0, va="top", ha="left", zorder=4, linespacing=1.35
    )
    ax.add_patch(patches.FancyBboxPatch(
        (1.1, 4.45), 5.4, 0.72,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="#e0f2fe", edgecolor=UFC_BLUE, linewidth=1.3, zorder=3
    ))
    ax.text(
        3.8, 4.81,
        r"$f_0 = \frac{\phi}{h} \qquad \text{e} \qquad \lambda_0 = \frac{c}{f_0} = \frac{h c}{\phi}$",
        color=UFC_NAVY, fontsize=15.5, fontweight="bold", va="center", ha="center", zorder=4
    )

    ax.text(
        0.70, 4.20,
        "3. Equação de Einstein para o Efeito Fotoelétrico:\n"
        "   Conservação de energia para $f \\geq f_0$ ($E_c \\equiv K_{\\max}$):",
        color=TEXT_DARK, fontsize=12.0, va="top", ha="left", zorder=4, linespacing=1.35
    )
    ax.add_patch(patches.FancyBboxPatch(
        (1.1, 2.85), 5.4, 0.78,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="#fef3c7", edgecolor=GOLD_BORDER, linewidth=1.5, zorder=3
    ))
    ax.text(
        3.8, 3.24,
        r"$K_{\max} = h f - \phi = h(f - f_0) = \frac{1}{2} m_e v_{\max}^2$",
        color="#92400e", fontsize=15.5, fontweight="bold", va="center", ha="center", zorder=4
    )

    ax.text(
        0.70, 2.58,
        "4. Potencial de Frenagem / Corte ($V_0$):\n"
        "   Tensão reversa ($V = -V_0$) que zera a fotocorrente ($qV_0 = K_{\\max}$):",
        color=TEXT_DARK, fontsize=12.0, va="top", ha="left", zorder=4, linespacing=1.35
    )
    ax.add_patch(patches.FancyBboxPatch(
        (1.1, 1.05), 5.4, 0.85,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor="#f3e8ff", edgecolor="#7e22ce", linewidth=1.3, zorder=3
    ))
    ax.text(
        3.8, 1.48,
        r"$V_0 = \frac{h}{q} f - \frac{\phi}{q} \quad \Longrightarrow \quad \mathrm{Inclinação} = \frac{h}{q}$",
        color="#581c87", fontsize=14.8, fontweight="bold", va="center", ha="center", zorder=4
    )

    # Coluna Direita: Figura 3 (Comparação dos 9 Metais da Aula 03)
    desenhar_card(
        ax, 7.45, 0.75, 8.10, 6.95,
        "▸ Simulação dos 9 Metais (Aula 03): Barreira φ vs. Energia hf",
        bg_color="#ffffff", border_color=BORDER_GRAY, header_bg=UFC_NAVY
    )

    img3_path = os.path.join(dir_imgs, "fig3_comparacao_metais_barreira.png")
    img3 = mpimg.imread(img3_path)
    ax_img = fig.add_axes([7.60 / 16.0, 2.25 / 9.0, 7.80 / 16.0, 4.70 / 9.0], zorder=5)
    ax_img.imshow(img3)
    ax_img.axis("off")

    ax.add_patch(patches.FancyBboxPatch(
        (7.70, 0.95), 7.60, 1.15,
        boxstyle="round,pad=0.02,rounding_size=0.08",
        facecolor=CARD_BG, edgecolor=BORDER_GRAY, linewidth=1.2, zorder=4
    ))
    ax.text(
        7.90, 1.52,
        "• Análise Crítica da Simulação:\n"
        "  Dentre os 9 metais da Aula 03, apenas o Sódio (Na, $\\phi = 2,28$ eV, $f_0 = 5,51\\times 10^{14}$ Hz)\n"
        "  sofre efeito fotoelétrico com luz visível! Metais como Co, Al, Zn, Fe, Cu, Ag e Pt possuem\n"
        "  $\\phi \\geq 3,90$ eV e exigem radiação Ultravioleta ($f > 9,4\\times 10^{14}$ Hz) para emitir elétrons.",
        color=TEXT_DARK, fontsize=11.0, va="center", ha="left", zorder=5, linespacing=1.35
    )

    return fig


def slide3_simulacao_frequencia(dir_imgs: str):
    fig, ax = criar_slide_base("3. Simulação 1: Efeito da Frequência (f) e do Tipo de Metal", 3)

    # Esquerda: Gráfico Principal fig1_kmax_vs_frequencia.png
    desenhar_card(
        ax, 0.45, 0.75, 9.35, 6.95,
        "▸ Curvas Simuladas: Energia Cinética Máxima ($K_{\\max}$) vs. Frequência ($f$)",
        bg_color="#ffffff", border_color=BORDER_GRAY, header_bg=UFC_NAVY
    )
    img1_path = os.path.join(dir_imgs, "fig1_kmax_vs_frequencia.png")
    img1 = mpimg.imread(img1_path)
    ax_img1 = fig.add_axes([0.58 / 16.0, 0.95 / 9.0, 9.10 / 16.0, 6.05 / 9.0], zorder=5)
    ax_img1.imshow(img1)
    ax_img1.axis("off")

    # Direita: Resolução do Problema do Sódio (Aula 03 - Slide 8)
    desenhar_card(
        ax, 10.00, 0.75, 5.55, 6.95,
        "▸ Caso Prático (Aula 03): Placa de Sódio (Na)",
        bg_color=CARD_BG, border_color=UFC_BLUE, header_bg=UFC_NAVY
    )

    texto_topo = (
        "Parâmetros do Sódio (Na):\n"
        "• Função trabalho: $\\phi = 2,28\\text{ eV}$\n"
        "• Frequência de corte: $f_0 = 5,51\\times 10^{14}\\text{ Hz}$ ($\\lambda_0 = 544\\text{ nm}$)\n"
        "───────────────────────────────────────────"
    )
    ax.text(10.22, 6.95, texto_topo, color=TEXT_DARK, fontsize=11.2, va="top", ha="left", zorder=4, linespacing=1.35)

    # Tabela estilizada dos resultados da simulação no Sódio
    col_headers = ["Cor ($f$ em Hz)", "$E_f$ (eV)", "$K_{\\max}$", "$v_{\\max}$ (m/s)"]
    linhas = [
        ["Vermelha ($4,3\\times 10^{14}$)", "1,78 eV", "0,00 eV", "Não emite"],
        ["Amarela ($5,1\\times 10^{14}$)",  "2,11 eV", "0,00 eV", "Não emite"],
        ["Verde ($5,6\\times 10^{14}$)",    "2,32 eV", "0,04 eV", "$1,12\\times 10^5$"],
        ["Azul ($6,3\\times 10^{14}$)",     "2,61 eV", "0,33 eV", "$3,38\\times 10^5$"],
        ["Violeta ($7,2\\times 10^{14}$)",  "2,98 eV", "0,70 eV", "$4,95\\times 10^5$"],
        ["UV 300nm ($10,0\\times 10^{14}$)","4,13 eV", "1,85 eV", "$8,07\\times 10^5$"],
    ]

    y_tab = 5.45
    ax.add_patch(patches.Rectangle((10.20, y_tab), 5.15, 0.42, facecolor=UFC_NAVY, zorder=3))
    xs = [10.28, 12.18, 13.15, 14.12]
    for cx, h_txt in zip(xs, col_headers):
        ax.text(cx, y_tab + 0.21, h_txt, color="white", fontsize=10.0, fontweight="bold", va="center", ha="left", zorder=4)

    for idx, row in enumerate(linhas):
        yr = y_tab - (idx + 1) * 0.42
        bg_r = "#fee2e2" if "Não" in row[3] else ("#dcfce7" if idx % 2 == 0 else "#f0fdf4")
        ax.add_patch(patches.Rectangle((10.20, yr), 5.15, 0.42, facecolor=bg_r, edgecolor="#cbd5e1", lw=0.6, zorder=3))
        for cx, cell in zip(xs, row):
            cor_c = "#991b1b" if "Não" in cell else TEXT_DARK
            peso = "bold" if ("Violeta" in cell or "Amarela" in cell or "Não" in cell) else "normal"
            ax.text(cx, yr + 0.21, cell, color=cor_c, fontsize=9.8, fontweight=peso, va="center", ha="left", zorder=4)

    respostas_slide8 = (
        "Respostas diretas ao Slide 8 da Aula 03:\n"
        "a) Luz Violeta ($7,2\\times 10^{14}$ Hz): SIM, ejeta elétrons!\n"
        "   $K_{\\max} = 2,98 - 2,28 = \\mathbf{0,70\\text{ eV}} \\approx 1,12\\times 10^{-19}\\text{ J}$.\n\n"
        "b) Luz Amarela ($5,1\\times 10^{14}$ Hz): NÃO ejeta elétrons!\n"
        "   Pois $E_f = 2,11\\text{ eV} < \\phi = 2,28\\text{ eV}$ ($v = 0$).\n\n"
        "c) Luz Ultravioleta ($f > 7,5\\times 10^{14}$ Hz): Ejeção intensa!\n"
        "   $K_{\\max} = hf - 2,28\\text{ eV} > 0,82\\text{ eV}$ (cresce com $f$)."
    )
    ax.text(10.22, 2.72, respostas_slide8, color=TEXT_DARK, fontsize=10.6, va="top", ha="left", zorder=4, linespacing=1.32)

    return fig


def slide4_simulacao_intensidade_vs_frequencia(dir_imgs: str):
    fig, ax = criar_slide_base("4. Simulação 2: Intensidade (I) vs. Frequência (f) na Fotocorrente", 4)

    # Topo: Figura 2 (Painel Duplo I vs V)
    desenhar_card(
        ax, 0.45, 2.75, 15.10, 5.00,
        "▸ Curvas Características Simuladas: Fotocorrente ($I_{\\mathrm{foto}}$) vs. Tensão Aplicada ($V$)",
        bg_color="#ffffff", border_color=BORDER_GRAY, header_bg=UFC_NAVY
    )
    img2_path = os.path.join(dir_imgs, "fig2_corrente_vs_tensao.png")
    img2 = mpimg.imread(img2_path)
    ax_img2 = fig.add_axes([0.65 / 16.0, 2.85 / 9.0, 14.70 / 16.0, 4.30 / 9.0], zorder=5)
    ax_img2.imshow(img2)
    ax_img2.axis("off")

    # Base Esquerda: Conclusão do Painel (a) - Intensidade
    desenhar_card(
        ax, 0.45, 0.65, 7.35, 1.90,
        "▸ Papel da Intensidade Luminosa (I) — [Gráfico (a)]",
        bg_color="#eff6ff", border_color=UFC_BLUE, header_bg=UFC_NAVY
    )
    ax.text(
        0.70, 1.85,
        "• Aumentar $I$ (30% $\\rightarrow$ 60% $\\rightarrow$ 100%) mantendo $f$ fixa aumenta proporcionalmente\n"
        "  a quantidade de fótons por segundo que atingem o metal ($I_{\\mathrm{sat}} \\propto I$).\n"
        "• Porém, todas as curvas convergem para o MESMO Potencial de Corte ($-V_0 = -0,70$ V),\n"
        "  provando que a energia cinética máxima $K_{\\max}$ INDEPENDE da intensidade!",
        color=TEXT_DARK, fontsize=11.0, va="top", ha="left", zorder=4, linespacing=1.34
    )

    # Base Direita: Conclusão do Painel (b) - Frequência
    desenhar_card(
        ax, 8.20, 0.65, 7.35, 1.90,
        "▸ Papel da Frequência da Luz (f) — [Gráfico (b)]",
        bg_color="#fdf2f8", border_color="#db2777", header_bg="#831843"
    )
    ax.text(
        8.45, 1.85,
        "• Aumentar $f$ (Verde $\\rightarrow$ Azul $\\rightarrow$ Violeta $\\rightarrow$ UV) aumenta a energia individual\n"
        "  de cada fóton ($E_f = hf$), elevando a energia cinética máxima $K_{\\max} = hf - \\phi$.\n"
        "• Como resultado, é necessário aplicar uma tensão reversa cada vez mais negativa\n"
        "  ($-V_0 = -K_{\\max}/q$) para frear os fotoelétrons mais velozes!",
        color=TEXT_DARK, fontsize=11.0, va="top", ha="left", zorder=4, linespacing=1.34
    )

    return fig


def slide5_sintese_e_conclusoes():
    fig, ax = criar_slide_base("5. Resposta à Questão Central, Simulador Interativo e Conclusões", 5)

    # Tabela Comparativa Geral: Clássica vs Quântica vs Simulação
    desenhar_card(
        ax, 0.45, 3.65, 15.10, 4.05,
        "▸ Verificação das Previsões da Teoria Quântica da Luz via Simulação Computacional",
        bg_color="#ffffff", border_color=UFC_BLUE, header_bg=UFC_NAVY
    )

    headers = [
        "Parâmetro Variado",
        "Previsão Clássica (Refutada)",
        "Previsão Quântica (Einstein, 1905)",
        "Resultado Observado na Simulação",
    ]
    rows = [
        [
            "Frequência abaixo do\nlimiar ($f < f_0$)",
            "Ocorreria emissão se a\nintensidade $I$ fosse alta",
            "Fóton individual não vence a\nbarreira ($hf < \\phi$): zero emissão",
            "$I_{\\mathrm{foto}} = 0\\text{ }\\mu\\text{A}$ mesmo com $I = 100\\%$\n(Ex: Luz Amarela no Sódio)",
        ],
        [
            "Aumento da Frequência\n($f > f_0$, $I$ constante)",
            "$K_{\\max}$ não dependeria\nda frequência da onda",
            "$K_{\\max} = hf - \\phi$ cresce linearmente\ncom inclinação universal $h$",
            "Reta $K_{\\max} \\times f$ de inclinação $h$ e\ndeslocamento de $-V_0$ para a esquerda",
        ],
        [
            "Aumento da Intensidade\n($I \\uparrow$, $f > f_0$ fixa)",
            "Aumentaria a energia\ncinética máxima $K_{\\max}$",
            "Mais fótons/s $\\Rightarrow$ mais elétrons/s,\nmas cada fóton mantém $E = hf$",
            "Corrente $I_{\\mathrm{sat}}$ cresce linearmente com $I$,\nmantendo $-V_0$ e $K_{\\max}$ fixos",
        ],
        [
            "Troca do Metal\n($\\phi$ maior: Na $\\rightarrow$ Pt)",
            "Sem frequência de corte\nabrupta entre metais",
            "Eleva a barreira $\\phi$, exigindo\nfótons de maior frequência $f_0$",
            "Retas paralelas deslocadas: Na emite\nno visível; Co, Al, Zn, Cu, Pt só no UV",
        ],
    ]

    y_top = 6.55
    col_x = [0.65, 3.85, 7.35, 11.35]
    ax.add_patch(patches.Rectangle((0.60, y_top), 14.80, 0.45, facecolor=UFC_NAVY, zorder=3))
    for cx, h_text in zip(col_x, headers):
        ax.text(cx, y_top + 0.22, h_text, color="white", fontsize=11.2, fontweight="bold", va="center", ha="left", zorder=4)

    for i, r in enumerate(rows):
        yr = y_top - (i + 1) * 0.68
        bg = "#f8fafc" if i % 2 == 0 else "#eff6ff"
        ax.add_patch(patches.Rectangle((0.60, yr), 14.80, 0.68, facecolor=bg, edgecolor="#cbd5e1", lw=0.8, zorder=3))
        for j, (cx, cell_txt) in enumerate(zip(col_x, r)):
            cor_txt = "#991b1b" if j == 1 else ("#166534" if j == 2 else (UFC_NAVY if j == 0 else TEXT_DARK))
            peso = "bold" if j in (0, 3) else "normal"
            ax.text(cx, yr + 0.34, cell_txt, color=cor_txt, fontsize=10.3, fontweight=peso, va="center", ha="left", zorder=4, linespacing=1.25)

    # Card Inferior Esquerdo: Resposta Direta à Questão Central
    desenhar_card(
        ax, 0.45, 0.70, 8.80, 2.70,
        "▸ Conclusão Final: Resposta à Questão Central",
        bg_color=OK_BG, border_color=OK_BORDER, header_bg="#166534"
    )
    ax.text(
        0.70, 2.65,
        "1. A FREQUÊNCIA ($f$) define a energia individual de cada fóton ($E = hf$):\n"
        "   Determina SE haverá emissão ($f \\geq f_0 = \\phi/h$) e governa exclusivamente\n"
        "   a energia cinética máxima ($K_{\\max} = hf - \\phi$) e a velocidade dos elétrons.\n\n"
        "2. A INTENSIDADE ($I$) define o fluxo de fótons por segundo:\n"
        "   Acima de $f_0$, governa a quantidade de elétrons extraídos por segundo\n"
        "   (a fotocorrente $I_{\\mathrm{foto}}$), sem alterar a energia máxima individual $K_{\\max}$.",
        color=TEXT_DARK, fontsize=11.3, va="top", ha="left", zorder=4, linespacing=1.32
    )

    # Card Inferior Direito: Aplicações em Engenharia e Simulador ao Vivo
    desenhar_card(
        ax, 9.50, 0.70, 6.05, 2.70,
        "▸ Aplicações em Optoeletrônica e Telecom",
        bg_color=GOLD_BG, border_color=GOLD_BORDER, header_bg="#92400e"
    )
    ax.text(
        9.75, 2.65,
        "• Fotodetectores e Fotomultiplicadoras:\n"
        "  Escolha do metal/semicondutor depende da faixa espectral\n"
        "  de operação ($\\lambda < hc/\\phi$).\n\n"
        "• Determinação Experimental de $h$:\n"
        "  Pela inclinação $m = h/q$ do gráfico $V_0 \\times f$ (Aula 03).\n\n"
        "• Demonstração Interativa ao Vivo:\n"
        "  Execução do Simulador Computacional (simulador_interativo.html).",
        color=TEXT_DARK, fontsize=10.8, va="top", ha="left", zorder=4, linespacing=1.30
    )

    return fig


def gerar_pdf_completo():
    dir_atual = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(dir_atual, "Apresentacao_Tema02_Efeito_Fotoeletrico.pdf")

    slides_funcs = [
        lambda: slide1_questao_central_e_contexto(),
        lambda: slide2_modelagem_e_metais(dir_atual),
        lambda: slide3_simulacao_frequencia(dir_atual),
        lambda: slide4_simulacao_intensidade_vs_frequencia(dir_atual),
        lambda: slide5_sintese_e_conclusoes(),
    ]

    slides_figs = []
    for idx, fn in enumerate(slides_funcs, start=1):
        fig = fn()
        slide_png = os.path.join(dir_atual, f"slide_{idx:02d}.png")
        fig.savefig(slide_png, dpi=180)
        slides_figs.append(fig)
        print(f"[OK] Slide {idx}/5 renderizado com sucesso.")

    try:
        with PdfPages(pdf_path) as pdf:
            for fig in slides_figs:
                pdf.savefig(fig, dpi=200)
        print(f"\n[SUCESSO] Apresentação em PDF (5 slides) salva em:\n  -> {pdf_path}")
    except PermissionError:
        print(f"\n[AVISO] O PDF já está aberto em outro programa; PNGs atualizados com sucesso.")
    finally:
        for fig in slides_figs:
            plt.close(fig)


if __name__ == "__main__":
    gerar_pdf_completo()

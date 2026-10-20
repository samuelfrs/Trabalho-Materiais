"""
Simulação Computacional do Efeito Fotoelétrico
Disciplina: TI0060 - Materiais Eletrônicos e Optoeletrônicos (UFC 2026.2)
Professor: Dr. Joacir Andrade
Tema 2 - Equipe: Logan e Samuel Farias

Descrição:
    Simula o efeito fotoelétrico verificando as previsões da teoria quântica
    da luz de Planck-Einstein (K_max = h*f - phi) utilizando os metais e
    frequências das Aulas 02 e 03 da disciplina.
    Gera 3 figuras científicas (300 DPI) para a apresentação e imprime o
    relatório analítico completo no terminal.
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. CONSTANTES FÍSICAS FUNDAMENTAIS (CODATA / SI e eV)
# =============================================================================
H_J_S = 6.62607015e-34        # Constante de Planck (J.s)
Q_E = 1.602176634e-19         # Carga elementar do elétron (C)
H_EV_S = H_J_S / Q_E          # Constante de Planck (eV.s) ~ 4.1356677e-15 eV.s
C_LIGHT = 299792458.0         # Velocidade da luz no vácuo (m/s)
M_E = 9.1093837015e-31        # Massa de repouso do elétron (kg)

# =============================================================================
# 2. DADOS DOS SLIDES DA AULA 03 (Prof. Joacir Andrade - Slide 8)
# =============================================================================
METAIS_AULA03 = {
    "Na": {"nome": "Sódio (Na)", "phi": 2.28, "cor_plot": "#1f77b4"},
    "Co": {"nome": "Cobalto (Co)", "phi": 3.90, "cor_plot": "#ff7f0e"},
    "Al": {"nome": "Alumínio (Al)", "phi": 4.08, "cor_plot": "#2ca02c"},
    "Pb": {"nome": "Chumbo (Pb)", "phi": 4.14, "cor_plot": "#9467bd"},
    "Zn": {"nome": "Zinco (Zn)", "phi": 4.31, "cor_plot": "#8c564b"},
    "Fe": {"nome": "Ferro (Fe)", "phi": 4.50, "cor_plot": "#e377c2"},
    "Cu": {"nome": "Cobre (Cu)", "phi": 4.70, "cor_plot": "#d62728"},
    "Ag": {"nome": "Prata (Ag)", "phi": 4.73, "cor_plot": "#7f7f7f"},
    "Pt": {"nome": "Platina (Pt)", "phi": 6.35, "cor_plot": "#17becf"},
}

CORES_LUZ_AULA03 = [
    ("Vermelha", 4.3e14, "#e63946"),
    ("Amarela",  5.1e14, "#f4a261"),
    ("Verde",    5.6e14, "#2a9d8f"),
    ("Azul",     6.3e14, "#0077b6"),
    ("Violeta",  7.2e14, "#7209b7"),
]


# =============================================================================
# 3. FUNÇÕES DO MODELO FÍSICO VETORIZADO
# =============================================================================
def calcular_energia_foton_ev(f_hz: np.ndarray | float) -> np.ndarray | float:
    """Retorna a energia do fóton E = h*f em elétron-volts (eV)."""
    return H_EV_S * np.asarray(f_hz)


def calcular_kmax_ev(f_hz: np.ndarray | float, phi_ev: float) -> np.ndarray:
    """
    Equação de Einstein para o Efeito Fotoelétrico:
    K_max = max(0, h*f - phi) em eV.
    """
    energia_foton = calcular_energia_foton_ev(f_hz)
    return np.maximum(0.0, energia_foton - phi_ev)


def calcular_velocidade_max_m_s(kmax_ev: np.ndarray | float) -> np.ndarray:
    """
    Calcula a velocidade máxima clássica dos fotoelétrons em m/s:
    v_max = sqrt(2 * K_max_Joules / m_e)
    """
    kmax_joules = np.asarray(kmax_ev) * Q_E
    return np.sqrt(np.maximum(0.0, 2.0 * kmax_joules / M_E))


def simular_curva_iv(
    v_aplicada: np.ndarray,
    f_hz: float,
    phi_ev: float,
    intensidade_rel: float,
    i_sat_ref_ua: float = 12.0,
) -> np.ndarray:
    """
    Modela a curva característica Fotocorrente I_foto (uA) vs. Tensão V (Volts).
    - Se h*f <= phi: não há emissão (I = 0 para qualquer V e qualquer intensidade).
    - Se h*f > phi: o potencial de corte é V_corte = -V_0 = -(h*f - phi)/q.
      Para V < -V_0, até os elétrons mais rápidos são freados (I = 0).
      Para V > -V_0, a coleta cresce suavemente até a saturação proporcional
      à taxa de fótons incidentes (intensidade_rel).
    """
    kmax = float(calcular_kmax_ev(f_hz, phi_ev))
    if kmax <= 0.0 or intensidade_rel <= 0.0:
        return np.zeros_like(v_aplicada, dtype=float)

    v0 = kmax  # Numericamento V_0 em Volts é igual a K_max em eV
    i_sat = i_sat_ref_ua * intensidade_rel

    # Transição física suave de coleta entre V = -V_0 e regime de saturação (V > 0)
    # Devido à distribuição de energia dos elétrons (de 0 até K_max) e geometria dos eletrodos
    delta_v = v_aplicada - (-v0)
    corrente = np.where(
        delta_v <= 0.0,
        0.0,
        i_sat * (1.0 - np.exp(-delta_v / 0.35))
    )
    return corrente


# =============================================================================
# 4. GERAÇÃO DOS GRÁFICOS CIENTÍFICOS (300 DPI)
# =============================================================================
def gerar_fig1_kmax_vs_frequencia(output_dir: str) -> str:
    """
    Figura 1: Energia Cinética Máxima (K_max) vs. Frequência (f) para vários metais.
    """
    f_14 = np.linspace(3.5, 18.0, 1000)  # Frequência em unidades de 10^14 Hz
    f_hz = f_14 * 1e14

    fig, ax = plt.subplots(figsize=(9.5, 5.6), dpi=300)

    # Faixas espectrais de fundo
    ax.axvspan(3.5, 4.0, color="#ffcccc", alpha=0.20, label="Infravermelho (IV)")
    ax.axvspan(4.0, 7.5, color="#fff3b0", alpha=0.28, label="Luz Visível (4,0 a 7,5×10¹⁴ Hz)")
    ax.axvspan(7.5, 18.0, color="#e0c3fc", alpha=0.20, label="Ultravioleta (UV)")

    metais_selecionados = ["Na", "Co", "Zn", "Cu", "Pt"]
    for sigla in metais_selecionados:
        dados = METAIS_AULA03[sigla]
        phi = dados["phi"]
        f0_14 = (phi / H_EV_S) / 1e14
        kmax = calcular_kmax_ev(f_hz, phi)

        # Plota apenas onde há emissão (f >= f0) e marca f0 no eixo
        mask = f_14 >= f0_14
        ax.plot(
            f_14[mask],
            kmax[mask],
            linewidth=2.5,
            color=dados["cor_plot"],
            label=f"{dados['nome']}: $\\phi = {phi:.2f}$ eV ($f_0 = {f0_14:.2f}\\times 10^{{14}}$ Hz)",
        )
        ax.scatter([f0_14], [0.0], color=dados["cor_plot"], s=55, zorder=5)

    # Destaca o estudo de caso do Sódio (Na) da Aula 03 - Slide 8
    phi_na = METAIS_AULA03["Na"]["phi"]
    # Ponto Amarelo (5.1e14 Hz -> sem emissão)
    ax.scatter([5.1], [0.0], color="#d97706", marker="x", s=90, linewidths=2.5, zorder=6)
    ax.annotate(
        "Na + Luz Amarela\n($5,1\\times 10^{14}$ Hz)\nSem emissão ($f < f_0$)",
        xy=(5.1, 0.05),
        xytext=(3.7, 1.35),
        fontsize=8.5,
        fontweight="bold",
        color="#92400e",
        bbox=dict(boxstyle="round,pad=0.3", fc="#fef3c7", ec="#d97706", alpha=0.95),
        arrowprops=dict(arrowstyle="->", color="#d97706", lw=1.5),
    )

    # Ponto Violeta no Sódio (7.2e14 Hz -> K_max = 0.70 eV)
    k_na_violeta = float(calcular_kmax_ev(7.2e14, phi_na))
    ax.scatter([7.2], [k_na_violeta], color="#7209b7", s=70, zorder=6)
    ax.annotate(
        f"Na + Luz Violeta\n($7,2\\times 10^{{14}}$ Hz)\n$K_{{\\max}} = {k_na_violeta:.2f}$ eV",
        xy=(7.2, k_na_violeta),
        xytext=(5.85, 1.65),
        fontsize=8.5,
        fontweight="bold",
        color="#4a044e",
        bbox=dict(boxstyle="round,pad=0.3", fc="#f3e8ff", ec="#7209b7", alpha=0.95),
        arrowprops=dict(arrowstyle="->", color="#7209b7", lw=1.5),
    )

    # Nota explicativa sobre a inclinação universal = h
    ax.text(
        12.2,
        0.55,
        "Retas paralelas!\nInclinação universal:\n$\\frac{\\Delta K_{\\max}}{\\Delta f} = h \\approx 4,14\\times 10^{-15}\\text{ eV}\\cdot\\text{s}$",
        fontsize=9.5,
        bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="#334155", lw=1.2, alpha=0.95),
    )

    ax.axhline(0, color="black", linewidth=1.0)
    ax.set_title(
        "Equação de Einstein ($K_{\\max} = hf - \\phi$): Efeito da Frequência e do Metal",
        fontsize=13,
        fontweight="bold",
        pad=10,
    )
    ax.set_xlabel("Frequência da Luz Incidente $f$ ($\\times 10^{14}$ Hz)", fontsize=11)
    ax.set_ylabel("Energia Cinética Máxima $K_{\\max}$ (eV)", fontsize=11)
    ax.set_xlim(3.5, 18.0)
    ax.set_ylim(-0.2, 4.5)
    ax.grid(True, linestyle="--", alpha=0.45)
    ax.legend(fontsize=8.8, loc="upper left", framealpha=0.95)

    plt.tight_layout()
    caminho = os.path.join(output_dir, "fig1_kmax_vs_frequencia.png")
    plt.savefig(caminho, dpi=300)
    plt.close(fig)
    return caminho


def gerar_fig2_corrente_vs_tensao(output_dir: str) -> str:
    """
    Figura 2: Painel duplo de Fotocorrente (I) vs. Tensão (V) para o Sódio (Na).
    (a) Frequência fixa (Violeta) e Intensidade variável.
    (b) Intensidade fixa e Frequência variável.
    """
    v = np.linspace(-2.0, 2.5, 800)
    phi_na = METAIS_AULA03["Na"]["phi"]  # 2.28 eV

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11.5, 4.8), dpi=300)

    # --- Painel (a): Variando a Intensidade (f fixa = 7.2e14 Hz - Violeta) ---
    f_violeta = 7.2e14
    v0_violeta = float(calcular_kmax_ev(f_violeta, phi_na))  # ~ 0.70 V
    intensidades = [
        (1.00, "Intensidade 100% (Alta)", "#1d4ed8", "-"),
        (0.60, "Intensidade 60% (Média)", "#2563eb", "--"),
        (0.30, "Intensidade 30% (Baixa)", "#60a5fa", "-."),
    ]
    for int_rel, rotulo, cor, estilo in intensidades:
        corrente = simular_curva_iv(v, f_violeta, phi_na, int_rel, i_sat_ref_ua=12.0)
        ax1.plot(v, corrente, label=rotulo, color=cor, linestyle=estilo, linewidth=2.4)

    ax1.axvline(-v0_violeta, color="#dc2626", linestyle=":", linewidth=1.8)
    ax1.scatter([-v0_violeta], [0.0], color="#dc2626", s=65, zorder=5)
    ax1.annotate(
        f"Mesmo Potencial de Corte!\n$-V_0 = -{v0_violeta:.2f}$ V\n($K_{{\\max}}$ não depende de $I$)",
        xy=(-v0_violeta, 0.2),
        xytext=(-1.92, 6.5),
        fontsize=8.5,
        fontweight="bold",
        color="#991b1b",
        bbox=dict(boxstyle="round,pad=0.3", fc="#fef2f2", ec="#dc2626", alpha=0.95),
        arrowprops=dict(arrowstyle="->", color="#dc2626", lw=1.5),
    )

    ax1.axvline(0, color="gray", linewidth=0.9, alpha=0.6)
    ax1.set_title(
        "(a) Efeito da Intensidade Luminosa ($I$)\n[Sódio, $f = 7,2\\times 10^{14}$ Hz fixa]",
        fontsize=11,
        fontweight="bold",
    )
    ax1.set_xlabel("Tensão Aplicada $V$ (Volts)", fontsize=10.5)
    ax1.set_ylabel("Fotocorrente $I_{\\text{foto}}$ ($\\mu$A)", fontsize=10.5)
    ax1.set_xlim(-2.0, 2.5)
    ax1.set_ylim(-0.5, 13.5)
    ax1.grid(True, linestyle="--", alpha=0.45)
    ax1.legend(fontsize=8.8, loc="upper left")

    # --- Painel (b): Variando a Frequência (Intensidade fixa = 75%) ---
    int_fixa = 0.75
    testes_freq = [
        ("Amarela ($5,1\\times 10^{14}$ Hz - Sem emissão)", 5.1e14, "#d97706", ":"),
        ("Verde ($5,6\\times 10^{14}$ Hz)", 5.6e14, "#16a34a", "-."),
        ("Azul ($6,3\\times 10^{14}$ Hz)", 6.3e14, "#0284c7", "--"),
        ("Violeta ($7,2\\times 10^{14}$ Hz)", 7.2e14, "#7c3aed", "-"),
        ("UV Próximo ($8,8\\times 10^{14}$ Hz)", 8.8e14, "#db2777", "-"),
    ]
    for rotulo, f_val, cor, estilo in testes_freq:
        corrente = simular_curva_iv(v, f_val, phi_na, int_fixa, i_sat_ref_ua=12.0)
        ax2.plot(v, corrente, label=rotulo, color=cor, linestyle=estilo, linewidth=2.3)
        v0 = float(calcular_kmax_ev(f_val, phi_na))
        if v0 > 0:
            ax2.scatter([-v0], [0.0], color=cor, s=45, zorder=5)

    ax2.annotate(
        "Maior $f \\Rightarrow$ maior $K_{\\max}$\n$\\Rightarrow$ corte $-V_0$ mais negativo!",
        xy=(-1.36, 0.2),
        xytext=(-1.92, 6.2),
        fontsize=8.5,
        fontweight="bold",
        color="#831843",
        bbox=dict(boxstyle="round,pad=0.3", fc="#fdf2f8", ec="#db2777", alpha=0.95),
        arrowprops=dict(arrowstyle="->", color="#db2777", lw=1.5),
    )

    ax2.axvline(0, color="gray", linewidth=0.9, alpha=0.6)
    ax2.set_title(
        "(b) Efeito da Frequência da Luz ($f$)\n[Sódio, Taxa de Fótons Fixa]",
        fontsize=11,
        fontweight="bold",
    )
    ax2.set_xlabel("Tensão Aplicada $V$ (Volts)", fontsize=10.5)
    ax2.set_ylabel("Fotocorrente $I_{\\text{foto}}$ ($\\mu$A)", fontsize=10.5)
    ax2.set_xlim(-2.0, 2.5)
    ax2.set_ylim(-0.5, 13.5)
    ax2.grid(True, linestyle="--", alpha=0.45)
    ax2.legend(fontsize=8.2, loc="upper left")

    plt.tight_layout()
    caminho = os.path.join(output_dir, "fig2_corrente_vs_tensao.png")
    plt.savefig(caminho, dpi=300)
    plt.close(fig)
    return caminho


def gerar_fig3_comparacao_metais(output_dir: str) -> str:
    """
    Figura 3: Comparação dos 9 metais da Aula 03 (Slide 8) quanto à Função Trabalho (phi)
    e a resposta sob Luz Violeta (2.98 eV) vs. Ultravioleta (5.38 eV).
    Otimizada para caber perfeitamente no slide sem encostar nas bordas ou rodapé.
    """
    siglas = list(METAIS_AULA03.keys())
    phis = np.array([METAIS_AULA03[s]["phi"] for s in siglas])
    x = np.arange(len(siglas))

    e_violeta = float(calcular_energia_foton_ev(7.2e14))  # ~ 2.98 eV
    e_uv = float(calcular_energia_foton_ev(1.30e15))      # ~ 5.38 eV (230 nm)

    fig, ax = plt.subplots(figsize=(11.0, 3.4), dpi=300)

    barras = ax.bar(
        x,
        phis,
        width=0.52,
        color=["#2563eb" if p < e_violeta else ("#0d9488" if p < e_uv else "#64748b") for p in phis],
        edgecolor="#0f172a",
        linewidth=1.1,
        alpha=0.92,
        label=r"Função Trabalho $\phi$ (eV)",
        zorder=3,
    )

    ax.axhline(
        e_violeta,
        color="#7209b7",
        linestyle="--",
        linewidth=2.2,
        label=f"Luz Violeta ($f = 7,2\times 10^{{14}}$ Hz $\rightarrow E_f = {e_violeta:.2f}$ eV): Só o Sódio emite!",
        zorder=4,
    )
    ax.axhline(
        e_uv,
        color="#dc2626",
        linestyle="-.",
        linewidth=2.2,
        label=f"Luz UV ($\lambda = 230$ nm $\rightarrow E_f = {e_uv:.2f}$ eV): Emite até a Prata (Ag)",
        zorder=4,
    )

    for barra, phi in zip(barras, phis):
        ax.text(
            barra.get_x() + barra.get_width() / 2.0,
            phi + 0.12,
            f"{phi:.2f} eV",
            ha="center",
            va="bottom",
            fontsize=9.8,
            fontweight="bold",
            color="#0f172a",
            zorder=5,
        )

    ax.set_xticks(x)
    ax.set_xticklabels([METAIS_AULA03[s]["nome"] for s in siglas], rotation=12, ha="right", fontsize=10.5, fontweight="bold")
    ax.set_ylabel("Energia (eV)", fontsize=11.5, fontweight="bold")
    ax.set_title(
        r"Comparação dos 9 Metais (Aula 03): Função Trabalho ($\phi$) vs. Limiares de Energia ($hf$)",
        fontsize=12.0,
        fontweight="bold",
        pad=5,
        color="#0f2c59",
    )
    ax.set_ylim(0, 7.3)
    ax.grid(True, axis="y", linestyle="--", alpha=0.50, zorder=0)
    ax.legend(fontsize=9.5, loc="upper left", framealpha=0.96, facecolor="#ffffff", edgecolor="#cbd5e1")

    plt.tight_layout()
    caminho = os.path.join(output_dir, "fig3_comparacao_metais_barreira.png")
    plt.savefig(caminho, dpi=300)
    plt.close(fig)
    return caminho

# =============================================================================
# 5. RELATÓRIO NO TERMINAL E EXECUÇÃO PRINCIPAL
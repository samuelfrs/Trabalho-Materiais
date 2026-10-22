# ⚡ Efeito Fotoelétrico por meio de Simulação Computacional

> **Universidade Federal do Ceará (UFC) — Centro de Tecnologia**  
> **Curso:** Engenharia de Telecomunicações (Semestre 2026.2)  
> **Disciplina:** TI0060 — Materiais Eletrônicos e Optoeletrônicos  
> **Professor:** Dr. Joacir Andrade  
> **Avaliação:** 1ª Avaliação — **Tema 2 (Grupo 2)**  
> **Equipe:** Logan e Samuel Farias  

---

## 🎯 Sobre o Projeto

Este repositório reúne a **simulação computacional em Python**, o **simulador interativo em HTML5/Canvas**, os **gráficos científicos de alta resolução**, a **apresentação final em LaTeX Beamer (8 slides)** e o **guia de estudos/roteiro de apresentação objetivo** desenvolvidos para o **Tema 2** da 1ª Avaliação de *Materiais Eletrônicos e Optoeletrônicos*.

### Questão Central do Trabalho
> *"Como a frequência e a intensidade da luz incidente influenciam a emissão de elétrons de uma superfície metálica, e como a simulação permite verificar as previsões da teoria quântica da luz?"*

### Estrutura da Apresentação (8 Slides — Atendendo às Recomendações do Professor)
1. **O Problema:** Desafios físicos e variáveis em análise.
2. **Como Resolvemos:** Modelagem matemática das equações quânticas ($E=hf$, $f_0$, $K_{\max}$, $V_0$).
3. **Simulação dos 9 Metais (Página Dedicada):** Gráfico comparativo de $\phi$ vs. luz visível e UV com alta legibilidade.
4. **Resultados 1:** Curvas $K_{\max} \times f$ (inclinação universal $h$) e estudo de caso do Sódio (Aula 03).
5. **Resultados 2:** Curvas características $I_{\text{foto}} \times V$ (efeito de $I$ vs. $f$).
6. **A Simulação Interativa:** Demonstração prática do simulador em tempo real e resposta central.
7. **Diferenciação Teórica:** Tabela comparativa entre **Efeito Fotoelétrico (externo)** e **Efeito Fotovoltaico (interno)**.
8. **Aplicações e Referências:** Aplicações em Telecom e Optoeletrônica e referências bibliográficas formais (Kasap, Eisberg-Resnick, Tipler e Aula 03).

---

## 📂 Estrutura do Repositório

| Arquivo | Descrição |
| :--- | :--- |
| 📝 **[`Apresentacao_Tema02_Beamer.tex`](./Apresentacao_Tema02_Beamer.tex)** | Código-fonte em **LaTeX Beamer** dos 8 slides (pronto para compilar no Overleaf). |
| ⚡ **[`simulador_interativo.html`](./simulador_interativo.html)** | **Simulador computacional interativo (HTML5/Canvas)**. Abre direto no navegador (offline) para demonstração ao vivo durante a apresentação. |
| 📘 **[`GUIA_ESTUDO_E_ROTEIRO_APRESENTACAO.md`](./GUIA_ESTUDO_E_ROTEIRO_APRESENTACAO.md)** | **Roteiro completo e objetivo para a dupla**: divisão de fala minuto a minuto entre **Samuel e Logan** (12–13 min), passo a passo da demonstração ao vivo e arguição com respostas prontas. |
| 🐍 **[`simulacao_efeito_fotoeletrico.py`](./simulacao_efeito_fotoeletrico.py)** | Script Python (NumPy + Matplotlib) que modela a física fotoelétrica, resolve os problemas da Aula 03 e exporta os gráficos em 300 DPI. |
| 📊 **[`fig1_kmax_vs_frequencia.png`](./fig1_kmax_vs_frequencia.png)** | Gráfico simulado: Energia Cinética Máxima ($K_{\max}$) vs. Frequência ($f$) para múltiplos metais. |
| 📊 **[`fig2_corrente_vs_tensao.png`](./fig2_corrente_vs_tensao.png)** | Painel duplo simulado: Fotocorrente ($I_{\text{foto}}$) vs. Tensão ($V$) variando Intensidade vs. Frequência. |
| 📊 **[`fig3_comparacao_metais_barreira.png`](./fig3_comparacao_metais_barreira.png)** | Comparativo das Funções Trabalho ($\phi$) dos 9 metais da Aula 03 frente à luz visível e UV. |

---

## 🚀 Como Usar (Guia Rápido para a Dupla)

### 1. Abrir o Simulador Interativo (Sem instalar nada)
Basta dar **duplo clique** no arquivo **[`simulador_interativo.html`](./simulador_interativo.html)** para abri-lo em qualquer navegador (Chrome, Edge, Firefox, Brave). Ele funciona **100% offline** e permite:
- Escolher qualquer um dos **9 metais da Aula 03** ($\text{Na}, \text{Co}, \text{Al}, \text{Pb}, \text{Zn}, \text{Fe}, \text{Cu}, \text{Ag}, \text{Pt}$);
- Variar a **Frequência ($f$)** / **Comprimento de onda ($\lambda$)** com botões rápidos para as cores da tabela do Prof. Joacir (*Vermelha, Amarela, Verde, Azul, Violeta e UV*);
- Variar a **Intensidade Luminosa ($I$)** de $0\%$ a $100\%$;
- Variar a **Tensão Coletor-Cátodo ($V$)** e clicar no botão **`🛑 Aplicar Potencial de Corte (-V₀)`** para ver os fotoelétrons sendo freados no tubo a vácuo em tempo real.

### 2. Compilar os Slides no Overleaf
1. Crie ou abra o projeto no **Overleaf**;
2. Envie o arquivo **`Apresentacao_Tema02_Beamer.tex`**;
3. Envie as 3 figuras científicas geradas:
   - `fig1_kmax_vs_frequencia.png`
   - `fig2_corrente_vs_tensao.png`
   - `fig3_comparacao_metais_barreira.png`
4. Clique em **Recompile**.

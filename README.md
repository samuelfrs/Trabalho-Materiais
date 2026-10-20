# ⚡ Efeito Fotoelétrico por meio de Simulação Computacional

> **Universidade Federal do Ceará (UFC) — Centro de Tecnologia**  
> **Curso:** Engenharia de Telecomunicações (Semestre 2026.2)  
> **Disciplina:** TI0060 — Materiais Eletrônicos e Optoeletrônicos  
> **Professor:** Dr. Joacir Andrade  
> **Avaliação:** 1ª Avaliação — **Tema 2 (Grupo 2)**  
> **Equipe:** Logan e Samuel Farias  

---

## 🎯 Sobre o Projeto

Este repositório reúne a **simulação computacional em Python**, o **simulador interativo em HTML5/Canvas**, os **gráficos científicos de alta resolução**, a **apresentação final em LaTeX Beamer (5 slides)** e o **guia de estudos/roteiro de apresentação objetivo** desenvolvidos para o **Tema 2** da 1ª Avaliação de *Materiais Eletrônicos e Optoeletrônicos*.

### Questão Central do Trabalho
> *"Como a frequência e a intensidade da luz incidente influenciam a emissão de elétrons de uma superfície metálica, e como a simulação permite verificar as previsões da teoria quântica da luz?"*

### Estrutura da Apresentação (Direta e Técnica)
A apresentação foi estruturada sem rodeios históricos, focando diretamente em:
1. **O Problema:** Fenômenos físicos não intuitivos da emissão fotoelétrica e variáveis envolvidas.
2. **Como Resolvemos o Problema:** Modelagem matemática das equações quânticas e arquitetura computacional nos 9 metais.
3. **Os Resultados:** Curvas $K_{\max} \times f$ (com inclinação universal $h$, caso do Sódio) e curvas $I_{\text{foto}} \times V$ (efeito de $I$ vs. $f$).
4. **A Simulação e Conclusões:** Demonstração prática do simulador interativo em tempo real e resposta objetiva à questão central.

---

## 📂 Estrutura do Repositório

| Arquivo | Descrição |
| :--- | :--- |
| 📝 **[`Apresentacao_Tema02_Beamer.tex`](./Apresentacao_Tema02_Beamer.tex)** | Código-fonte em **LaTeX Beamer** dos 5 slides (pronto para compilar no Overleaf). |
| ⚡ **[`simulador_interativo.html`](./simulador_interativo.html)** | **Simulador computacional interativo (HTML5/Canvas)**. Abre direto no navegador (offline) para demonstração ao vivo durante a apresentação. |
| 📘 **[`GUIA_ESTUDO_E_ROTEIRO_APRESENTACAO.md`](./GUIA_ESTUDO_E_ROTEIRO_APRESENTACAO.md)** | **Roteiro completo e objetivo para a dupla**: divisão de fala minuto a minuto entre **Samuel e Logan** (11–13 min), passo a passo da demonstração ao vivo e arguição com respostas prontas. |
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
1. Crie um projeto no **Overleaf**;
2. Envie o arquivo **`Apresentacao_Tema02_Beamer.tex`**;
3. Envie as 3 figuras científicas geradas:
   - `fig1_kmax_vs_frequencia.png`
   - `fig2_corrente_vs_tensao.png`
   - `fig3_comparacao_metais_barreira.png`
4. Clique em **Recompile**.

---

## 🎤 Divisão Sugerida para a Apresentação (11 a 13 min)

O roteiro detalhado das falas e a demonstração ao vivo estão em **[`GUIA_ESTUDO_E_ROTEIRO_APRESENTACAO.md`](./GUIA_ESTUDO_E_ROTEIRO_APRESENTACAO.md)**:

1. **Slide 1 — O Problema (~2,5 min — Samuel Farias):** Questão central, o desafio físico (frequência de corte estrita, independência de $K_{\max}$ frente a $I$, emissão instantânea) e as variáveis do sistema.
2. **Slide 2 — Como Resolvemos (~2,5 min — Samuel Farias):** Balanço quântico ($E = hf$), frequência de corte ($f_0 = \phi/h$), equação de Einstein ($K_{\max} = hf - \phi$), frenagem eletrostática ($V_0$) e análise dos 9 metais da Aula 03.
3. **Slide 3 — Resultados 1 (~2,5 min — Logan):** Retas paralelas de inclinação universal $h$ em $K_{\max} \times f$ e estudo numérico de caso da placa de Sódio (Luz Amarela vs. Violeta vs. UV).
4. **Slide 4 — Resultados 2 (~2,5 min — Logan):** Curvas de Fotocorrente ($I_{\text{foto}} \times V$), separando matematicamente o efeito da Intensidade (multiplica saturação sem mexer em $-V_0$) e da Frequência (desloca $-V_0$ para valores mais negativos).
5. **Slide 5 + Simulador Interativo ao Vivo (~2,5 min — Samuel + Logan):** Demonstração ao vivo no `simulador_interativo.html` (corte quântico na amarela, frenagem em $-0{,}70\text{ V}$ e troca para Cobre/UV) com fechamento objetivo respondendo à Questão Central.

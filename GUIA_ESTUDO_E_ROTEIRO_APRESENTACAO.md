# 📘 Guia de Apresentação, Roteiro e Manual de Arguição (8 Slides — 10 a 15 min)

**Disciplina:** TI0060 — Materiais Eletrônicos e Optoeletrônicos (UFC 2026.2)  
**Professor:** Dr. Joacir Andrade  
**Avaliação:** 1ª Avaliação — Tema 2 (*Efeito Fotoelétrico por meio de Simulação Computacional*)  
**Equipe:** Logan e Samuel Farias  
**Prazo de envio dos slides:** até **21/10/2026**  
**Tempo regulamentar de exposição:** **10 a 15 minutos** (tempo planejado da dupla: **12 a 13 minutos**)

---

## 1. Visão Geral da Estrutura Atualizada (Com Simulação no Penúltimo Slide)

A sequência de slides foi refinada para colocar a demonstração computacional interativa no **penúltimo slide (Slide 7)**, antecedendo o fechamento com aplicações práticas e referências (Slide 8):

1. **Slide 1:** O Problema (Fenômenos não intuitivos e variáveis do sistema).
2. **Slide 2:** Como Resolvemos (Modelagem teórica e equações governantes).
3. **Slide 3:** Simulação dos 9 Metais (Página dedicada para a barreira $\phi$ vs. luz visível e UV).
4. **Slide 4:** Resultados 1 (Influência de $f$, retas paralelas de inclinação $h$ e caso do Sódio).
5. **Slide 5:** Resultados 2 (Curvas $I_{\text{foto}} \times V$: efeito da Intensidade vs. Frequência).
6. **Slide 6:** Diferenciação Teórica (Efeito Fotoelétrico externo vs. Efeito Fotovoltaico interno).
7. **Slide 7 (PENÚLTIMO):** A Simulação Computacional Interativa (Demonstração prática ao vivo no navegador + Resposta definitiva à Questão Central).
8. **Slide 8 (FINAL):** Aplicações em Engenharia de Telecomunicações e Referências Bibliográficas.

---

## 2. Divisão de Fala da Dupla (8 Slides — Equilíbrio ~6 min cada)

| Slide | Título / Conteúdo | Foco Principal | Apresentador | Duração Sugerida |
| :---: | :--- | :--- | :---: | :---: |
| **1** | **O Problema** | Desafios físicos observados e variáveis em jogo | **Samuel Farias** | ~01:30 min |
| **2** | **Como Resolvemos** | Equações governantes ($E=hf$, $f_0$, $K_{\max}$, $V_0$) | **Samuel Farias** | ~01:30 min |
| **3** | **Simulação dos 9 Metais** | Página inteira: barreira $\phi$ vs. faixas visível e UV | **Samuel Farias** | ~01:45 min |
| **4** | **Resultados 1 (Frequência)** | Curvas $K_{\max} \times f$ com inclinação $h$ e caso do Sódio | **Logan** | ~02:00 min |
| **5** | **Resultados 2 (Fotocorrente)** | Curvas $I_{\text{foto}} \times V$: efeito de Intensidade vs. Frequência | **Logan** | ~02:00 min |
| **6** | **Fotoelétrico vs. Fotovoltaico** | Tabela comparativa: externo vs. interno, $\phi$ vs. $E_g$ | **Logan** | ~01:45 min |
| **7** | **Simulação ao Vivo (Penúltimo)** | Demonstração em tempo real no Canvas + Resposta central | **Logan + Samuel** | ~02:15 min |
| **8** | **Aplicações e Referências** | Aplicações em Telecom e citação bibliográfica formal | **Samuel Farias** | ~01:15 min |
| **Total** | — | — | **Dupla** | **~12:00 min** |

---

## 3. Roteiro de Fala Detalhado (Slide a Slide)

---

### ⏱️ SLIDE 1 — O Problema: Comportamento da Emissão Fotoelétrica (00:00 – 01:30)
* **Quem apresenta:** Samuel Farias
* **Roteiro de Fala:**
  1. *"Boa tarde, professor Joacir e colegas. Eu sou o Samuel Farias e, juntamente com o Logan, somos a equipe do Tema 2: o estudo do Efeito Fotoelétrico por meio de Simulação Computacional."*
  2. *"A nossa Questão Central investiga: **Como a frequência ($f$) e a intensidade ($I$) da radiação governam a emissão de elétrons de uma superfície metálica, e como podemos modelar e verificar esse comportamento computacionalmente?**"*
  3. *"Quando iluminamos uma placa metálica no vácuo, deparamo-nos com três mistérios físicos fundamentais:"*
     - *"Primeiro: a existência de uma **frequência de corte estrita ($f_0$)** — abaixo dela, nenhum elétron escapa, mesmo sob um feixe de luz extremamente potente."*
     - *"Segundo: a **energia dos elétrons independe da intensidade** da fonte luminosa."*
     - *"Terceiro: a **emissão é instantânea** ($\sim 10^{-9}\text{ s}$), sem qualquer atraso de acúmulo contínuo de energia."*
  4. *"Parametrizamos o sistema em três grupos de grandezas: as propriedades da luz incidente ($f, \lambda, I$), a função trabalho do cátodo metálico ($\phi$, avaliando os 9 metais da disciplina) e a resposta elétrica mensurável ($-V_0$ e $I_{\text{foto}}$)."*

---

### ⏱️ SLIDE 2 — Como Resolvemos: Modelagem Teórica e Equações Governantes (01:30 – 03:00)
* **Quem apresenta:** Samuel Farias
* **Roteiro de Fala:**
  1. *"No Slide 2, apresentamos a base matemática utilizada na construção da nossa simulação."*
  2. *"A modelagem baseia-se na quantização da luz proposta por Planck e Einstein:"*
     - *"A radiação é absorvida em pacotes discretos (fótons), onde cada fóton carrega energia $E = hf = hc/\lambda$."*
     - *"Para escapar do metal, o elétron precisa vencer uma barreira mínima de atração atômica chamada **Função Trabalho ($\phi$)**. Isso define o limiar de corte $f_0 = \phi/h$ (ou $\lambda_0 = hc/\phi$)."*
     - *"O saldo de energia converte-se em energia cinética máxima pela **Equação de Einstein**: $K_{\max} = hf - \phi = \frac{1}{2}m_e v_{\max}^2$."*
     - *"No circuito elétrico, medimos essa energia aplicando uma tensão reversa de frenagem $-V_0$. O elétron mais veloz é freado quando o trabalho elétrico anula a energia cinética: $qV_0 = K_{\max} \implies V_0 = \frac{h}{q}f - \frac{\phi}{q}$."*

---

### ⏱️ SLIDE 3 — Simulação dos 9 Metais: Função Trabalho vs. Espectro (03:00 – 04:45)
* **Quem apresenta:** Samuel Farias
* **Roteiro de Fala:**
  1. *"No Slide 3, dedicamos uma página inteira para visualizar o comparativo das funções trabalho dos **9 metais tabelados na Aula 03** pelo professor Joacir."*
  2. *"Observem as duas linhas de referência espectral:"*
     - *"A linha tracejada roxa representa a energia de um fóton de luz violeta ($2{,}98\text{ eV}$), que é o limite máximo da luz visível."*
     - *"O resultado mais importante da simulação é imediato: **apenas o Sódio ($\text{Na}$, $\phi = 2{,}28\text{ eV}$)** possui barreira menor que a luz violeta! Portanto, dentre todos os 9 metais, o Sódio é o único que emite fotoelétrons na faixa da luz visível."*
     - *"Todos os outros 8 metais (Cobalto, Alumínio, Chumbo, Zinco, Ferro, Cobre, Prata e Platina) possuem $\phi \ge 3{,}90\text{ eV}$ até $6{,}35\text{ eV}$ e exigem radiação **Ultravioleta (UV)** para emitir elétrons."*

---

### ⏱️ SLIDE 4 — Resultados 1: Influência da Frequência e Caso do Sódio (04:45 – 06:45)
* **Quem apresenta:** Logan
* **Roteiro de Fala:**
  1. *"Passando para o Slide 4, apresentamos o gráfico da **Energia Cinética Máxima ($K_{\max}$) em função da Frequência ($f$)** obtido com nossa simulação em Python."*
  2. *"O primeiro resultado marcante é que todas as curvas para $f \ge f_0$ são **retas estritamente paralelas**! Isso decorre da equação $K_{\max} = hf - \phi$, onde o coeficiente angular é a **constante universal de Planck ($h$)**."*
  3. *"Na tabela à direita, validamos os itens do estudo de caso do Sódio da Aula 03:"*
     - *"Com **luz amarela ($5{,}1 \times 10^{14}\text{ Hz}$)**: o fóton tem $2{,}11\text{ eV}$. Como $2{,}11 < 2{,}28\text{ eV}$, a simulação acusa **emissão zero** ($v = 0$)."*
     - *"Com **luz violeta ($7{,}2 \times 10^{14}\text{ Hz}$)**: o fóton tem $2{,}98\text{ eV} > 2{,}28\text{ eV}$. Ocorre ejeção com $K_{\max} = \mathbf{0{,}70\text{ eV}}$ e velocidade de $4{,}95 \times 10^5\text{ m/s}$."*
     - *"Com **UV ($10 \times 10^{14}\text{ Hz}$)**: a ejeção é altamente energética com $K_{\max} = 1{,}85\text{ eV}$."*

---

### ⏱️ SLIDE 5 — Resultados 2: Intensidade vs. Frequência na Fotocorrente (06:45 – 08:45)
* **Quem apresenta:** Logan
* **Roteiro de Fala:**
  1. *"No Slide 5, isolamos matematicamente o efeito da Intensidade do efeito da Frequência nas curvas de Fotocorrente ($I_{\text{foto}}$) versus Tensão ($V$)."*
  2. *"No **Gráfico (a)** à esquerda, fixamos a frequência na luz violeta e variamos a intensidade ($30\%, 60\%, 100\%$):"*
     - *"A corrente de saturação triplica porque chegam mais fótons por segundo, mas **todas as curvas cortam exatamente no mesmo Potencial de Corte ($-V_0 = -0{,}70\text{ V}$)**! Isso comprova numericamente que $K_{\max}$ não depende da intensidade."*
  3. *"No **Gráfico (b)** à direita, mantivemos a taxa de fótons fixa e variamos a frequência (Verde, Azul, Violeta, UV):"*
     - *"Todas as curvas atingem o mesmo teto de saturação, mas o potencial de corte $-V_0$ desloca-se para a esquerda (mais negativo), pois fótons de maior frequência geram elétrons mais velozes que exigem maior tensão para frenagem."*

---

### ⏱️ SLIDE 6 — Diferenciação: Efeito Fotoelétrico vs. Efeito Fotovoltaico (08:45 – 10:30)
* **Quem apresenta:** Logan
* **Roteiro de Fala:**
  1. *"No Slide 6, apresentamos a diferenciação física rigorosa entre o **Efeito Fotoelétrico** e o **Efeito Fotovoltaico** antes de irmos para a demonstração prática:"*
  2. *"Existem quatro diferenças fundamentais:"*
     - *"1. **Mecanismo e Localização:** O efeito fotoelétrico é uma **fotoemissão externa** — o elétron absorve o fóton e é ejetado para fora do material (para o vácuo). Já o efeito fotovoltaico é uma **fotoexcitação interna** — o elétron absorve o fóton e é promovido da banda de valência para a banda de condução, gerando um par elétron-buraco dentro do semicondutor."*
     - *"2. **Barreira Energética:** No fotoelétrico, a barreira é a **Função Trabalho ($\phi$)** dos metais (típica de $2{,}2$ a $6{,}5\text{ eV}$), exigindo UV ou violeta. No fotovoltaico, a barreira é a **Energia de Bandgap ($E_g$)** do semicondutor ($\sim 1{,}1\text{ eV}$ no Silício), permitindo absorver praticamente todo o visível e infravermelho próximo."*
     - *"3. **Geração de Tensão:** O efeito fotoelétrico **não gera força eletromotriz espontânea** — ele precisa de uma fonte externa no circuito para drenar a corrente. No efeito fotovoltaico, o campo elétrico interno da **junção p-n** separa os elétrons e buracos, criando uma tensão de circuito aberto útil ($V_{oc}$) capaz de alimentar cargas elétricas diretamente."*
     - *"4. **Dispositivos:** O fotoelétrico dá origem a tubos fotomultiplicadores e fototubos a vácuo; o fotovoltaico é a base das células solares e dos fotodiodos PIN/APD das telecomunicações."*

---

### ⏱️ SLIDE 7 — A Simulação Interativa e Validação ao Vivo (PENÚLTIMO) (10:30 – 12:45)
* **Quem apresenta:** Logan e Samuel Farias
* **Como conduzir:**
  1. *(Samuel introduz o slide em 20 segundos):* *"Agora, no Slide 7, coroamos toda a validação física demonstrando a ferramenta interativa que desenvolvemos: o `simulador_interativo.html`, que funciona offline no navegador com animação física via HTML5 Canvas."*
  2. *(Logan dá `Alt + Tab` para o navegador em tela cheia e faz os 3 testes rápidos em 1 minuto):*
     - **Teste 1 (Corte):** *"Sódio sob Luz Amarela a 100% de intensidade $\implies$ nenhum elétron sai da placa porque $hf < \phi$."*
     - **Teste 2 (Emissão e Frenagem):** *"Luz Violeta $\implies$ fotoelétrons fluem; clicamos no botão vermelho `🛑 Aplicar Potencial de Corte (-V₀)` ($-0{,}70\text{ V}$) e os elétrons freiam no meio do tubo antes de tocar o ânodo, zerando a corrente."*
     - **Teste 3 (Troca de Metal):** *"Mudando para Cobre ($\phi = 4{,}70\text{ eV}$), a luz violeta para de emitir; clicando em UV ($250\text{ nm}$), a emissão é retomada na hora."*
  3. *(Samuel volta ao Slide 7 e resume a resposta central em 30 segundos):*
     - *"Frequência governa a **qualidade da energia** por pacote ($E=hf$), determinando $K_{\max}$ e se haverá emissão."*
     - *"Intensidade governa a **quantidade de pacotes** por segundo, modulando a fotocorrente de saturação."*

---

### ⏱️ SLIDE 8 — Aplicações em Engenharia e Referências Bibliográficas (FINAL) (12:45 – 13:45)
* **Quem apresenta:** Samuel Farias
* **Roteiro de Fala:**
  1. *"Para encerrar nossa apresentação, no Slide 8 destacamos as principais aplicações dessas teorias na Engenharia de Telecomunicações e Optoeletrônica:"*
     - *"**Tubos Fotomultiplicadores (PMT):** Utilizam fotocátodos baseados no efeito fotoelétrico com ganho de até $10^6$ para detecção de fótons únicos em astrofísica, física médica e lidar."*
     - *"**Intensificadores de Imagem:** Base dos dispositivos de visão noturna, onde fótons fracos são convertidos em feixes eletrônicos que excitam telas fosforescentes."*
     - *"**Espectroscopia de Fotoelétrons (XPS/UPS):** Técnica analítica essencial em ciência dos materiais para medir a composição química de superfícies e a estrutura de bandas de sólidos."*
     - *"**Fotodetectores em Comunicações Ópticas:** Operam integrando princípios fotocondutivos e fotovoltaicos em receptores de fibra óptica para taxas de dezenas de gigabits por segundo."*
  2. *"Como referências bibliográficas do trabalho, destacamos o livro-texto da disciplina: o **Principles of Electronic Materials and Devices**, do professor Safa Kasap, o livro clássico de **Física Quântica** de Eisberg e Resnick, além das notas de aula do professor Joacir Andrade. Muito obrigado a todos!"*

---

## 4. Guia Rápido de Arguição (Perguntas Típicas com Respostas Prontas)

1. **Pergunta:** *"Por que no gráfico de $I_{\text{foto}} \times V$ a corrente não cai em degrau em $V=0$, mas tem uma transição suave até $-V_0$?"*
   - **Resposta:** Porque a função trabalho $\phi$ é a energia mínima para extrair elétrons do **Nível de Fermi** (topo da banda). Elétrons em níveis mais profundos ou que sofrem colisões na rede saem com energias menores que $K_{\max}$. Tensões reversas moderadas freiam os elétrons mais lentos, e apenas em $-V_0$ até os mais energéticos ($K_{\max}$) são freados.

2. **Pergunta:** *"Por que uma lâmpada comum não consegue fazer o que um semicondutor faz no efeito fotovoltaico?"*
   - **Resposta:** Porque a barreira dos metais no efeito fotoelétrico ($\phi \ge 2{,}28\text{ eV}$) é alta demais para fótons vermelhos ou infravermelhos ($< 2{,}0\text{ eV}$). Já nos semicondutores fotovoltaicos como o Silício, o bandgap é de apenas $1{,}1\text{ eV}$, de modo que a luz visível inteira e até o infravermelho possuem energia suficiente para excitar portadores.

3. **Pergunta:** *"Como a inclinação do efeito fotoelétrico se conecta com o experimento dos LEDs da Aula 02?"*
   - **Resposta:** São processos inversos: no efeito fotoelétrico, fótons produzem potencial de corte com $\Delta V_0 / \Delta f = h/q$; no LED, uma tensão limiar externa injeta portadores que se recombinam e emitem fótons com $\Delta V_{\text{limiar}} / \Delta f = h/q$. Em ambos os experimentos, a constante fundamental medida é a **constante de Planck ($h$)**.

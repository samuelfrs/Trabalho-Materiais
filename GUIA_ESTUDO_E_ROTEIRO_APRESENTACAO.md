# Guia Completo de Estudo e Roteiro de Apresentação (10 a 15 min)

**Disciplina:** TI0060 — Materiais Eletrônicos e Optoeletrônicos (UFC 2026.2)  
**Professor:** Dr. Joacir Andrade  
**Avaliação:** 1ª Avaliação — Tema 2 (*Efeito Fotoelétrico por meio de Simulação Computacional*)  
**Equipe:** Logan e Samuel Farias  
**Prazo de envio dos 5 slides:** até **21/10/2026**  
**Tempo regulamentar de exposição:** **10 a 15 minutos** (meta recomendada: **12 a 13 minutos**)

---

## 1. Estrutura dos Arquivos na Pasta do Trabalho

Todos os arquivos foram gerados e validados dentro de `07_Materiais_Eletronicos/trabalhos/Tema02_Efeito_Fotoeletrico/`:

1. **`Apresentacao_Tema02_Efeito_Fotoeletrico.pdf`**: Apresentação pronta (exatamente **5 slides** em formato 16:9 Widescreen) para enviar ao Prof. Joacir até 21/10/2026.
2. **`Apresentacao_Tema02_Beamer.tex`**: Código-fonte em LaTeX Beamer dos 5 slides (caso queiram compilar no Overleaf).
3. **`simulador_interativo.html`**: Simulador computacional interativo em tempo real (HTML5/Canvas, funciona offline direto no navegador com duplo clique) para demonstrar ao vivo durante a apresentação.
4. **`simulacao_efeito_fotoeletrico.py`**: Script científico em Python (NumPy/Matplotlib) que modela todas as equações, resolve o estudo de caso do Sódio da Aula 03 e exporta as figuras em 300 DPI:
   - `fig1_kmax_vs_frequencia.png`
   - `fig2_corrente_vs_tensao.png`
   - `fig3_comparacao_metais_barreira.png`

---

## 2. Resumo Conceitual (O que você precisa dominar)

### 2.1 Por que o Efeito Fotoelétrico derrubou a Física Clássica?
No século XIX, as equações de Maxwell provaram que a luz é uma onda eletromagnética. Pela física clássica, a energia transportada por uma onda depende apenas da sua **amplitude ao quadrado** (ou seja, da sua **intensidade luminosa \(I \propto E_0^2\)**), e não da sua frequência \(f\).

Se a visão clássica estivesse correta para a interação em escala atômica, três coisas deveriam acontecer quando iluminamos um metal:
1. **Não existiria frequência de corte (\(f_0\)):** Luz de qualquer cor (mesmo infravermelha ou vermelha), desde que muito intensa (um holofote forte), deveria fornecer energia suficiente para arrancar elétrons. *(Experimento real: abaixo de \(f_0\), nenhum elétron sai, não importa a intensidade!).*
2. **A energia cinética máxima (\(K_{\text{max}}\)) cresceria com a intensidade (\(I\)):** Uma luz mais intensa tem campo elétrico \(\mathbf{E}\) maior, logo deveria empurrar os elétrons com mais força, aumentando \(K_{\text{max}}\). *(Experimento real: aumentar \(I\) aumenta o número de elétrons ejetados por segundo — a fotocorrente —, mas \(K_{\text{max}}\) não muda nada!).*
3. **Havería atraso de tempo sob luz fraca:** Com feixe de baixa intensidade, o elétron levaria minutos ou horas absorvendo energia continuamente até acumular o suficiente para escapar. *(Experimento real: se \(f \ge f_0\), a emissão é instantânea, em \(\sim 10^{-9}\,\text{s}\), mesmo sob luz extremamente fraca!).*

### 2.2 A Explicação Quântica de Einstein (1905)
Baseando-se na quantização de Max Planck (1900), Albert Einstein propôs que a luz não entrega sua energia de forma contínua na superfície do metal, mas em **pacotes discretos e localizados de energia chamados fótons**:
\[
E_{\text{fóton}} = h f = \frac{h c}{\lambda}
\]
onde:
- \(h \approx 6{,}626 \times 10^{-34}\,\text{J}\cdot\text{s} \approx 4{,}136 \times 10^{-15}\,\text{eV}\cdot\text{s}\) é a constante de Planck;
- \(f\) é a frequência da radiação (\(\text{Hz}\)) e \(\lambda\) é o comprimento de onda (\(\text{m}\)).

**A Regra do "1 para 1" (Colisão Individual):**
Cada elétron no metal absorve **um único fóton por vez**. Para escapar da atração eletrostática dos íons da rede cristalina metálica, o elétron precisa vencer uma barreira de energia mínima chamada **Função Trabalho (\(\phi\) ou \(W_0\))**, que é característica de cada metal:
- Se \(h f < \phi\) (ou seja, \(f < f_0\), onde \(f_0 = \phi / h\) é a **frequência de corte**): o fóton individual não tem energia suficiente. O elétron não escapa (**emissão zero**).
- Se \(h f \ge \phi\) (\(f \ge f_0\)): o fóton arranca o elétron instantaneamente, e o excesso de energia converte-se em **energia cinética**. Para os elétrons mais superficiais (no nível de Fermi), a energia cinética é máxima:
\[
K_{\text{max}} = h f - \phi = h(f - f_0) = \frac{1}{2} m_e v_{\text{max}}^2
\]

### 2.3 Como medimos \(K_{\text{max}}\) no experimento e na simulação? (Potencial de Corte \(V_0\))
Aplicamos uma **tensão reversa** (\(V < 0\)) entre o coletor (ânodo) e o emissor (cátodo) para frear os elétrons. A tensão negativa exata \(-V_0\) na qual **até o elétron mais rápido para imediatamente antes de tocar o coletor** (zerando o microamperímetro, \(I_{\text{foto}} = 0\)) satisfaz a conservação de energia eletrostática:
\[
q V_0 = K_{\text{max}} \implies V_0 = \frac{h}{q} f - \frac{\phi}{q}
\]
Por isso, um gráfico de \(V_0\) versus \(f\) é uma **reta cuja inclinação vale exatamente \(m = h/q \approx 4{,}136 \times 10^{-15}\,\text{V/Hz}\)** — permitindo medir experimentalmente a constante de Planck \(h\) (como o Prof. Joacir mostrou nos slides 2 a 5 da Aula 03!).

---

## 3. Roteiro de Fala Minuto a Minuto (12 a 13 Minutos — Dividido para Dupla)

> **Sugestão de divisão equilibrada:**
> - **Parte 1 (Samuel — ~3,5 min):** Slides 1 e 2 (Problema físico, falha clássica vs. solução quântica, equações governantes e barreira dos 9 metais da Aula 03).
> - **Parte 2 (Logan — ~4,5 min):** Slides 3 e 4 (Resultados das simulações gráficas: \(K_{\text{max}} \times f\), resolução do caso do Sódio da Aula 03, e curvas \(I_{\text{foto}} \times V\) variando intensidade vs. frequência).
> - **Parte 3 (Samuel + Logan — ~4,0 min):** Slide 5 + **Demonstração ao Vivo no `simulador_interativo.html`** (2 minutos mostrando os sliders funcionando ao vivo + fechamento respondendo à Questão Central).

---

### ⏱️ SLIDE 1 — Questão Central e Ruptura Quântica (00:00 – 02:00)
* **Quem fala:** Samuel Farias
* **O que falar:**
  1. *"Boa tarde, professor Joacir e colegas. Eu sou o Samuel Farias e, junto com o Logan, somos a equipe responsável pelo Tema 2: o estudo do Efeito Fotoelétrico por meio de Simulação Computacional."*
  2. *"A nossa questão central neste trabalho é investigar como dois parâmetros da luz incidente — a **frequência \(f\)** e a **intensidade luminosa \(I\)** — afetam a ejeção de elétrons de uma superfície metálica, e como a simulação computacional nos permite comprovar as previsões da teoria quântica."*
  3. *"Para contextualizar: no final do século XIX, a teoria ondulatória clássica de Maxwell previa que a energia de uma onda eletromagnética dependia apenas da sua amplitude, isto é, da sua **intensidade**. Isso gerava três previsões clássicas que falharam completamente nos experimentos de Lenard e Millikan: primeiro, que qualquer frequência de luz deveria arrancar elétrons se o feixe fosse intenso o bastante; segundo, que aumentar a intensidade deveria aumentar a energia cinética dos elétrons; e terceiro, que sob luz fraca haveria um atraso de minutos até o elétron acumular energia."*
  4. *"Em 1905, Einstein resolveu esse impasse aplicando a hipótese de Planck: a luz é formada por pacotes discretos de energia — os **fótons** — onde cada fóton carrega individualmente uma energia \(E = hf = hc/\lambda\). A interação no metal não é contínua: é uma colisão individual de **1 fóton com 1 elétron**."*

---

### ⏱️ SLIDE 2 — Modelagem Física e os 9 Metais da Aula 03 (02:00 – 04:00)
* **Quem fala:** Samuel Farias
* **O que falar:**
  1. *"Passando para o Slide 2, temos as equações que governam a nossa simulação. Os elétrons de condução estão presos no metal por uma barreira potencial chamada **Função Trabalho (\(\phi\) ou \(W_0\))**."*
  2. *"Para que um único fóton consiga arrancar um elétron, a energia dele (\(hf\)) precisa ser no mínimo igual a \(\phi\). Isso define uma **frequência de corte \(f_0 = \phi / h\)** (ou um comprimento de onda máximo \(\lambda_0 = hc/\phi\)). Abaixo de \(f_0\), nenhum elétron sai."*
  3. *"Acima de \(f_0\), o fóton paga o 'pedágio' \(\phi\) para tirar o elétron do metal e toda a energia que sobra vira energia cinética máxima, descrita pela **Equação de Einstein: \(K_{\text{max}} = hf - \phi\)**. E no circuito elétrico da simulação, medimos \(K_{\text{max}}\) aplicando uma tensão reversa de frenagem \(-V_0\), onde \(qV_0 = K_{\text{max}}\)."*
  4. *"No gráfico à direita, simulamos exatamente os **9 metais da tabela da Aula 03** do professor Joacir, desde o Sódio (\(\phi = 2{,}28\,\text{eV}\)) até a Platina (\(\phi = 6{,}35\,\text{eV}\)). Reparem na linha tracejada roxa: ela representa a energia de um fóton de luz violeta (\(2{,}98\,\text{eV}\)), que é o limite superior da luz visível. Veja que **apenas o Sódio** tem barra menor que a linha roxa! Todos os outros 8 metais (Cobalto, Alumínio, Chumbo, Zinco, Ferro, Cobre, Prata e Platina) têm função trabalho acima de \(3{,}90\,\text{eV}\) e só sofrem efeito fotoelétrico no **Ultravioleta** (linha vermelha)."*

---

### ⏱️ SLIDE 3 — Simulação 1: Efeito da Frequência e Caso do Sódio (04:00 – 06:30)
* **Quem fala:** Logan
* **O que falar:**
  1. *"Dando continuidade no Slide 3, apresentamos o nosso primeiro conjunto de curvas simuladas em Python: a **Energia Cinética Máxima \(K_{\text{max}}\) em função da frequência \(f\)** para cinco metais da tabela da disciplina."*
  2. *"O primeiro resultado fundamental da simulação é geométrico: todas as curvas para \(f > f_0\) são **retas estritamente paralelas**! Por quê? Porque na equação \(K_{\text{max}} = hf - \phi\), o coeficiente angular de todas as retas é uma constante universal da natureza: a **constante de Planck \(h \approx 4{,}14 \times 10^{-15}\,\text{eV}\cdot\text{s}\)**. Trocar o metal apenas desloca o ponto de partida \(f_0\) para a direita."*
  3. *"À direita, aplicamos a simulação para resolver o estudo de caso proposto pelo professor Joacir no Slide 8 da Aula 03 para uma placa de **Sódio (\(\phi = 2{,}28\,\text{eV}\), \(f_0 = 5{,}51 \times 10^{14}\,\text{Hz}\))**:"*
     - *"Item (a): Sob **luz violeta** (\(7{,}2 \times 10^{14}\,\text{Hz}\)), o fóton tem \(2{,}98\,\text{eV}\). Como supera os \(2{,}28\,\text{eV}\) do Sódio, **há ejeção de elétrons** com \(K_{\text{max}} = 0{,}70\,\text{eV}\), atingindo velocidade máxima de \(4{,}95 \times 10^5\,\text{m/s}\) (ponto roxo no gráfico)."*
     - *"Item (b): Sob **luz amarela** (\(5{,}1 \times 10^{14}\,\text{Hz}\)), o fóton tem apenas \(2{,}11\,\text{eV}\), que é menor que \(2{,}28\,\text{eV}\). Portanto, **não há ejeção** e a velocidade é zero (marcado pelo X laranja na região sem emissão)."*
     - *"Item (c): No **ultravioleta** (por exemplo, \(300\,\text{nm}\), \(10 \times 10^{14}\,\text{Hz}\)), o fóton tem \(4{,}13\,\text{eV}\) e ejeta fotoelétrons altamente energéticos com \(K_{\text{max}} = 1{,}85\,\text{eV}\)."*

---

### ⏱️ SLIDE 4 — Simulação 2: Intensidade vs. Frequência na Fotocorrente (06:30 – 09:00)
* **Quem fala:** Logan
* **O que falar:**
  1. *"No Slide 4 está o teste decisivo que separa o papel da **intensidade** do papel da **frequência** nas curvas de Fotocorrente (\(I_{\text{foto}}\)) versus Tensão Aplicada (\(V\))."*
  2. *"Olhem primeiro para o **Gráfico (a)** à esquerda: aqui nós fixamos a frequência na luz violeta (\(7{,}2 \times 10^{14}\,\text{Hz}\)) sobre o Sódio e variamos apenas a **Intensidade Luminosa** de \(30\%\) para \(60\%\) e \(100\%\). Na visão quântica, aumentar a intensidade mantendo a frequência fixa significa mandar **mais fótons por segundo**, mas cada fóton continua tendo exatamente \(2{,}98\,\text{eV}\). O resultado na simulação é claro: a corrente de saturação dobra e triplica porque mais elétrons saem por segundo, mas **todas as três curvas cortam o eixo horizontal exatamente no mesmo Potencial de Corte \(-V_0 = -0{,}70\,\text{V}\)**! Isso prova que \(K_{\text{max}}\) **não depende da intensidade da luz**."*
  3. *"Agora olhem para o **Gráfico (b)** à direita: aqui nós mantivemos o fluxo de fótons fixo e aumentamos a **Frequência** da luz: Verde, Azul, Violeta e UV. Como a taxa de fótons é a mesma, todas atingem o mesmo patamar de saturação em tensões positivas; porém, à medida que a frequência sobe, a energia individual de cada fóton cresce, os elétrons saem mais rápidos e o **potencial de frenagem \(-V_0\) desloca-se cada vez mais para a esquerda (mais negativo)**!"*

---

### ⏱️ SLIDE 5 + DEMONSTRAÇÃO AO VIVO NO SIMULADOR (09:00 – 12:30)
* **Quem fala:** Samuel e Logan
* **O que fazer e falar:**
  1. **Abram o arquivo `simulador_interativo.html`** no navegador (deixem já aberto em uma aba ao lado do PDF dos slides) e façam 3 cliques rápidos em 1 minuto e meio:
     - **Clique 1:** Com **Sódio (Na)** selecionado, cliquem no botão **`Amarela (5,1)`** e puxem a **Intensidade para 100%**. Mostrem para a turma: *"Vejam que mesmo com a lâmpada em 100% de intensidade disparando dezenas de fótons amarelos, nenhum elétron sai do cátodo porque \(2{,}11\,\text{eV} < 2{,}28\,\text{eV}\)."*
     - **Clique 2:** Cliquem no botão **`Violeta (7,2)`**. Imediatamente os fotoelétrons azuis começam a cruzar o tubo e o amperímetro marca corrente! Agora cliquem no botão **`🛑 Aplicar Potencial de Corte (-V₀)`** (\(-0{,}70\,\text{V}\)): mostrem os elétrons saindo do cátodo, sendo freados pelo campo elétrico reverso e parando bem na frente do ânodo!
     - **Clique 3:** Troquem o metal no menu de **Sódio (Na)** para **Cobre (Cu, \(\phi = 4{,}70\,\text{eV}\))**. A emissão para na hora sob luz violeta! Cliquem então em **`UV 250nm (12,0)`** e a emissão volta a acontecer no Cobre!
  2. **Voltem para o Slide 5** para concluir em 1 minuto:
     - *"Para encerrar, o Slide 5 sintetiza a resposta à nossa Questão Central: na teoria quântica da luz, **Frequência é qualidade de energia por pacote** (\(E = hf\), governa se há emissão e qual a energia cinética máxima \(K_{\text{max}}\)), enquanto **Intensidade é quantidade de pacotes por segundo** (governa a magnitude da fotocorrente acima da frequência de corte). Esse princípio é a base de todos os fotodetectores, tubos fotomultiplicadores e sensores ópticos que utilizamos na Engenharia de Telecomunicações. Muito obrigado! Estamos à disposição para perguntas."*

---

## 4. Possíveis Perguntas do Prof. Joacir na Arguição (Com Respostas Prontas)

1. **Pergunta:** *"Se eu tiver uma frequência abaixo da frequência de corte (\(f < f_0\)) e usar um laser extremamente potente (intensidade altíssima), por que ainda assim na nossa simulação não sai elétron?"*
   - **Resposta:** Porque no regime do efeito fotoelétrico linear, a absorção é de **1 fóton por elétron**. Aumentar a intensidade só aumenta o número de fótons que chegam por segundo, mas cada fóton individual continua tendo energia \(hf < \phi\), insuficiente para vencer a barreira de potencial da função trabalho do metal.

2. **Pergunta:** *"Por que na equação de Einstein nós escrevemos \(K_{\text{max}}\) (energia cinética MÁXIMA) e não simplesmente \(K\)? Todos os elétrons saem com a mesma velocidade?"*
   - **Resposta:** Excelente ponto! Não saem todos com a mesma velocidade. A função trabalho \(\phi\) é a energia mínima para arrancar os elétrons que estão no topo da banda de condução (no **Nível de Fermi**). Elétrons que estão em níveis mais profundos ou que sofrem colisões internas antes de sair perdem parte da energia e saem com \(K < K_{\text{max}}\). É justamente por isso que, no gráfico de \(I_{\text{foto}} \times V\) (Slide 4), a corrente não cai a zero em degrau vertical em \(V = 0\), mas vai caindo gradualmente até zerar totalmente em \(V = -V_0\), quando até os elétrons de energia máxima \(K_{\text{max}}\) são freados!

3. **Pergunta:** *"Como a inclinação do gráfico do efeito fotoelétrico se conecta com aquele experimento dos LEDs que vimos nas Aulas 02 e 03?"*
   - **Resposta:** São fenômenos inversos governados pela mesma constante universal! No efeito fotoelétrico (absorção), um fóton de energia \(hf\) gera um fotoelétron freado por \(qV_0 = hf - \phi\). No LED (emissão espontânea por recombinação elétron-buraco vista na Aula 02), a energia elétrica injetada no limiar \(qV\) converte-se em um fóton emitido \(hf\) (\(qV \approx hf\)). Em ambos os casos, no gráfico de Tensão \(V\) versus Frequência \(f\), o coeficiente angular da reta é \(\Delta V / \Delta f = h / q \approx 4{,}14 \times 10^{-15}\,\text{V/Hz}\), permitindo determinar experimentalmente a constante de Planck \(h\)!

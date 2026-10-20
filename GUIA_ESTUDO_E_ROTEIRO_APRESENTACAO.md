# 📘 Guia de Apresentação, Roteiro e Manual de Arguição (10 a 15 min)

**Disciplina:** TI0060 — Materiais Eletrônicos e Optoeletrônicos (UFC 2026.2)  
**Professor:** Dr. Joacir Andrade  
**Avaliação:** 1ª Avaliação — Tema 2 (*Efeito Fotoelétrico por meio de Simulação Computacional*)  
**Equipe:** Logan e Samuel Farias  
**Prazo de envio dos slides:** até **21/10/2026**  
**Tempo regulamentar de exposição:** **10 a 15 minutos** (tempo planejado da dupla: **11 a 13 minutos**)

---

## 1. Visão Geral da Nova Estrutura (Direta e Sem Reter Histórico)

A apresentação elimina delongas históricas (debates do século XIX, disputas clássicas de Maxwell e biografias) e adota uma estrutura **ágil, técnica e direta em 4 atos**:

1. **O Problema (Slide 1):** O que está sendo investigado, as contradições físicas a explicar e as variáveis do sistema ($f, \lambda, I, \phi, V_0, I_{\text{foto}}$).
2. **Como Resolvemos o Problema (Slide 2):** A modelagem física exata ($E=hf$, $K_{\max}=hf-\phi$, potencial de frenagem $V_0$) e a arquitetura computacional em Python/Canvas mapeando os 9 metais da Aula 03.
3. **Os Resultados (Slides 3 e 4):**
   - **Resultados 1 (Slide 3):** Curvas $K_{\max} \times f$ com inclinação universal $h$ e a validação do estudo de caso do Sódio da Aula 03 (Amarela vs. Violeta vs. UV).
   - **Resultados 2 (Slide 4):** Curvas características de fotocorrente $I_{\text{foto}} \times V$, provando a independência entre $K_{\max}$ e a intensidade, e o papel da frequência no potencial de corte.
4. **A Simulação e Conclusões (Slide 5 + Demonstração Interativa):** Apresentação da ferramenta interativa, teste ao vivo no navegador e síntese final respondendo categoricamente à Questão Central.

---

## 2. Divisão de Fala da Dupla (Equilíbrio ~6 min cada)

| Etapa | Slide | Foco Principal | Apresentador | Duração Sugerida |
| :--- | :---: | :--- | :---: | :---: |
| **Ato 1** | **Slide 1** | **O Problema:** Desafios físicos observados e variáveis em jogo | **Samuel Farias** | 02:30 min |
| **Ato 2** | **Slide 2** | **Como Resolvemos:** Equações governantes e barreira dos 9 metais | **Samuel Farias** | 02:30 min |
| **Ato 3A** | **Slide 3** | **Resultados 1:** Efeito de $f$, retas paralelas e caso prático do Sódio | **Logan** | 02:30 min |
| **Ato 3B** | **Slide 4** | **Resultados 2:** Intensidade vs. Frequência na fotocorrente ($I \times V$) | **Logan** | 02:30 min |
| **Ato 4** | **Slide 5 + Demo** | **A Simulação:** Demonstração ao vivo no navegador e conclusões | **Samuel + Logan** | 02:30 min |
| **Total** | — | — | **Dupla** | **~12:30 min** |

---

## 3. Roteiro de Fala Detalhado (Minuto a Minuto)

---

### ⏱️ SLIDE 1 — O Problema: Comportamento da Emissão Fotoelétrica (00:00 – 02:30)
* **Quem apresenta:** Samuel Farias
* **Objetivo do Slide:** Apresentar a questão central, os fenômenos intrigantes a serem explicados e as variáveis do problema de forma puramente física e técnica.
* **Roteiro de Fala:**
  1. *"Boa tarde, professor Joacir e colegas. Eu sou o Samuel Farias e, juntamente com o Logan, somos a equipe do Tema 2 da 1ª Avaliação: o estudo do Efeito Fotoelétrico por meio de Simulação Computacional."*
  2. *"A nossa Questão Central é direta: **Como a frequência ($f$) e a intensidade ($I$) da radiação governam a emissão de elétrons de uma superfície metálica, e como podemos modelar e verificar esse comportamento computacionalmente?**"*
  3. *"Quando incidimos luz sobre uma placa condutora no vácuo, o fenômeno apresenta quatro desafios físicos não intuitivos que precisam ser compreendidos:"*
     - *"Primeiro: existe uma **frequência de corte estrita ($f_0$)**. Se a radiação estiver abaixo desse limiar, nenhum elétron é liberado do metal, não importando o quão brilhante ou potente seja a fonte."*
     - *"Segundo: a **energia cinética dos elétrons não depende da intensidade**. Colocar uma fonte luminosa dez vezes mais intensa gera mais elétrons, mas não aumenta em nada a velocidade do elétron individual mais rápido."*
     - *"Terceiro: a **resposta é instantânea**. Se a frequência for suficiente, os fotoelétrons emergem em frações de nanossegundos, sem nenhum tempo de espera para acumular energia."*
     - *"Quarto: a **dependência do material**. Cada metal impõe uma barreira própria de extração."*
  4. *"Para resolver e parametrizar esse problema, dividimos o estudo em três blocos de variáveis: os parâmetros da radiação ($f$, $\lambda$ e $I$), as propriedades do cátodo metálico através da sua função trabalho ($\phi$, avaliando os 9 metais da disciplina) e a resposta mensurável no circuito elétrico, que são o potencial de frenagem ($-V_0$) e a fotocorrente ($I_{\text{foto}}$)."*

---

### ⏱️ SLIDE 2 — Como Resolvemos: Modelagem Teórica e Computacional (02:30 – 05:00)
* **Quem apresenta:** Samuel Farias
* **Objetivo do Slide:** Explicar a formulação matemática da solução, a barreira de potencial dos materiais e a estratégia computacional implementada.
* **Roteiro de Fala:**
  1. *"No Slide 2, apresentamos como resolvemos e modelamos esse comportamento fisicamente e computacionalmente."*
  2. *"A modelagem física baseia-se em quatro equações fundamentais:"*
     - *"1. **Energia quantizada do fóton:** A energia da radiação é entregue em pacotes individuais dados por $E = hf = hc/\lambda$, onde $h \approx 4{,}136 \times 10^{-15}\text{ eV}\cdot\text{s}$."*
     - *"2. **Frequência de corte ($f_0$):** O elétron está ligado ao metal por uma barreira de energia chamada Função Trabalho ($\phi$). Para que ocorra ejeção em uma colisão 1 a 1, a energia do fóton precisa superar a função trabalho, definindo o limiar $f_0 = \phi/h$ (ou comprimento de onda máximo $\lambda_0 = hc/\phi$)."*
     - *"3. **Balanço de energia de Einstein:** Todo o excesso de energia do fóton que sobra após vencer a barreira converte-se em energia cinética máxima: $K_{\max} = hf - \phi = h(f - f_0) = \frac{1}{2}m_e v_{\max}^2$."*
     - *"4. **Potencial de frenagem ($V_0$):** No circuito, aplicamos uma tensão reversa $-V_0$ entre cátodo e ânodo. O elétron mais rápido é freado exatamente quando o trabalho elétrico anula $K_{\max}$, resultando em $V_0 = \frac{h}{q}f - \frac{\phi}{q}$."*
  3. *"Computacionalmente, implementamos essas equações em um motor de cálculo vetorizado em Python (`NumPy`), parametrizando com exatidão os **9 metais da tabela da Aula 03** do professor Joacir."*
  4. *"Observem no gráfico à direita a comparação dessas barreiras: a linha tracejada roxa representa a energia máxima da luz visível ($2{,}98\text{ eV}$, violeta). O resultado salta aos olhos: **apenas o Sódio ($\text{Na}$, $\phi = 2{,}28\text{ eV}$)** emite elétrons na faixa da luz visível! Todos os outros 8 metais (Cobalto, Alumínio, Chumbo, Zinco, Ferro, Cobre, Prata e Platina) possuem função trabalho maior ou igual a $3{,}90\text{ eV}$ e exigem radiação Ultravioleta (linha vermelha) para haver emissão."*

---

### ⏱️ SLIDE 3 — Resultados 1: Influência da Frequência e Estudo do Sódio (05:00 – 07:30)
* **Quem apresenta:** Logan
* **Objetivo do Slide:** Analisar o gráfico de $K_{\max} \times f$ e apresentar a resolução numérica do problema do Sódio proposto na Aula 03.
* **Roteiro de Fala:**
  1. *"Passando para o Slide 3, apresentamos o nosso primeiro conjunto de resultados das simulações computacionais: a **Energia Cinética Máxima ($K_{\max}$) em função da Frequência ($f$)**."*
  2. *"O primeiro resultado marcante da simulação é geométrico: todas as curvas simuladas acima do limiar são **retas estritamente paralelas**! Isso acontece porque a derivada $\frac{dK_{\max}}{df}$ é igual à **constante de Planck ($h$)**, que é uma constante universal da física. Mudar o metal não altera a inclinação da reta, apenas desloca a frequência de início ($f_0$) para a direita."*
  3. *"Na tabela à direita, aplicamos a simulação para resolver diretamente o problema da **placa de Sódio ($\phi = 2{,}28\text{ eV}$)** apresentado no Slide 8 da Aula 03:"*
     - *"Com **luz amarela ($5{,}1 \times 10^{14}\text{ Hz}$)**: o fóton tem apenas $2{,}11\text{ eV}$. Como $2{,}11\text{ eV} < 2{,}28\text{ eV}$, a simulação indica **emissão zero** e velocidade zero. Mesmo que aumentemos a potência, nenhum elétron escapa!"*
     - *"Com **luz violeta ($7{,}2 \times 10^{14}\text{ Hz}$)**: o fóton possui $2{,}98\text{ eV}$, superando a barreira do Sódio. Há ejeção com $K_{\max} = 2{,}98 - 2{,}28 = \mathbf{0{,}70\text{ eV}}$, resultando em uma velocidade máxima de fotoelétrons de $4{,}95 \times 10^5\text{ m/s}$."*
     - *"Com **luz ultravioleta ($10 \times 10^{14}\text{ Hz}$)**: a energia do fóton é $4{,}13\text{ eV}$, gerando ejeção altamente energética com $K_{\max} = 1{,}85\text{ eV}$ e velocidade de $8{,}07 \times 10^5\text{ m/s}$."*
  4. *"Esses resultados numéricos validam perfeitamente a previsão linear da teoria para a frequência."*

---

### ⏱️ SLIDE 4 — Resultados 2: Intensidade vs. Frequência na Fotocorrente (07:30 – 10:00)
* **Quem apresenta:** Logan
* **Objetivo do Slide:** Demonstrar as curvas características $I_{\text{foto}} \times V$, isolando matematicamente o efeito da intensidade e da frequência.
* **Roteiro de Fala:**
  1. *"No Slide 4, temos o resultado crucial que esclarece a separação entre o papel da **intensidade** e o papel da **frequência** através das curvas de Fotocorrente ($I_{\text{foto}}$) em função da Tensão Aplicada ($V$)."*
  2. *"Vejam primeiro o **Gráfico (a)** à esquerda: fixamos o metal em Sódio sob luz violeta e variamos a **Intensidade Luminosa** em $30\%$, $60\%$ e $100\%$."*
     - *"O aumento da intensidade multiplica a taxa de fótons incidentes por segundo, fazendo com que a fotocorrente de saturação aumente de forma rigorosamente linear ($I_{\text{sat}} \propto I$)."*
     - *"Porém, reparem no ponto em que as curvas encontram o eixo horizontal: **todas as três curvas cortam exatamente no mesmo Potencial de Corte ($-V_0 = -0{,}70\text{ V}$)**! Isso é a comprovação numérica de que a energia máxima dos fotoelétrons independe da intensidade da luz."*
  3. *"Agora observem o **Gráfico (b)** à direita: aqui mantivemos o fluxo de fótons constante e variamos a **Frequência da luz** (Verde, Azul, Violeta e UV)."*
     - *"Como o número de fótons é o mesmo, todas as curvas atingem o mesmo nível de saturação para tensões positivas."*
     - *"No entanto, à medida que a frequência aumenta, a energia individual de cada fóton sobe, os elétrons emergem com maior energia cinética e o potencial de corte $-V_0$ desloca-se progressivamente para a esquerda (valores mais negativos), pois é necessária uma barreira elétrica maior para frear os elétrons mais velozes."*

---

### ⏱️ SLIDE 5 + DEMONSTRAÇÃO AO VIVO — A Simulação e Conclusões (10:00 – 12:30)
* **Quem apresenta:** Samuel Farias e Logan (em conjunto)
* **Objetivo:** Demonstrar o simulador interativo funcionando no navegador e sintetizar a resposta final à Questão Central.
* **Passo a Passo da Fala e Ações ao Vivo:**
  1. *(Samuel projeta o Slide 5 e faz a introdução — ~45 seg):*
     - *"Para complementar os modelos estáticos do Python, desenvolvemos uma aplicação interativa completa em HTML5 e Canvas: o `simulador_interativo.html`, que funciona direto no navegador sem necessidade de internet."*
     - *"Ele modela em tempo real a trajetória dos fotoelétrons dentro do tubo a vácuo, com medidores virtuais de corrente e tensão."*
  2. *(Logan comuta para o simulador e executa os 3 testes rápidos ao vivo — ~1 min):*
     - *(Ver detalhes operacionais na Seção 5 deste guia).*
  3. *(Samuel volta para o Slide 5 e conclui — ~45 seg):*
     - *"Concluindo a resposta ao nosso problema central:"*
       - *"1. **A FREQUÊNCIA** dita a **qualidade da energia** de cada pacote ($E = hf$). Ela define se haverá emissão e qual é o valor de $K_{\max}$ e do potencial de corte $-V_0$."*
       - *"2. **A INTENSIDADE** dita a **quantidade de pacotes por segundo**. Ela determina o valor da fotocorrente de saturação, sem alterar a energia individual dos elétrons."*
     - *"Esse princípio é a base de funcionamento de todos os fotodetectores em fibra óptica e sensores optoeletrônicos na Engenharia de Telecomunicações. Muito obrigado!"*

---

## 4. Auditoria de Exatidão dos 3 Gráficos Científicos

Todos os gráficos gerados no projeto foram verificados analiticamente e estão **100% corretos**:

### Gráfico 1: `fig1_kmax_vs_frequencia.png` (Slide 3)
* **Equação Base:** $K_{\max} = hf - \phi$.
* **Conferência Física:**
  - O gráfico mostra retas estritamente paralelas para todos os metais.
  - A inclinação de todas as retas é $\frac{\Delta K_{\max}}{\Delta f} = h \approx 4{,}136 \times 10^{-15}\text{ eV}\cdot\text{s}$.
  - Frequência de corte do Sódio: $f_0 = \frac{2{,}28\text{ eV}}{4{,}136\times 10^{-15}\text{ eV}\cdot\text{s}} = 5{,}51 \times 10^{14}\text{ Hz}$.
  - Ponto Amarelo ($5{,}1 \times 10^{14}\text{ Hz}$): marcado com **X** sobre o eixo $K_{\max} = 0$, comprovando ausência de emissão.
  - Ponto Violeta ($7{,}2 \times 10^{14}\text{ Hz}$): marcado em $K_{\max} = 2{,}98 - 2{,}28 = 0{,}70\text{ eV}$.
  - Ponto UV ($10 \times 10^{14}\text{ Hz}$): marcado em $K_{\max} = 4{,}13 - 2{,}28 = 1{,}85\text{ eV}$.

### Gráfico 2: `fig2_corrente_vs_tensao.png` (Slide 4)
* **Painel (a) — Efeito de $I$:**
  - Curvas para $I = 30\%$, $60\%$ e $100\%$ sob luz violeta no Sódio.
  - A fotocorrente de saturação $I_{\text{sat}}$ sobe proporcionalmente à intensidade ($I_{\text{sat}} \propto I$).
  - Todas as três curvas cortam exatamente no mesmo ponto no eixo de tensão: $-V_0 = -0{,}70\text{ V}$.
* **Painel (b) — Efeito de $f$:**
  - Curvas para luz Amarela (corrente zero), Verde, Azul, Violeta e UV sob taxa de fótons fixa.
  - As curvas saturam no mesmo patamar de corrente, mas o potencial de corte $-V_0$ desloca-se para a esquerda (mais negativo) conforme a frequência sobe: $-V_0 = -(hf - \phi)/q$.

### Gráfico 3: `fig3_comparacao_metais_barreira.png` (Slide 2)
* **Dados Tabelados:** Mapeia com exatidão os 9 metais da Aula 03:
  - $\text{Na}$ ($2{,}28\text{ eV}$), $\text{Co}$ ($3{,}90\text{ eV}$), $\text{Al}$ ($4{,}08\text{ eV}$), $\text{Pb}$ ($4{,}14\text{ eV}$), $\text{Zn}$ ($4{,}31\text{ eV}$), $\text{Fe}$ ($4{,}50\text{ eV}$), $\text{Cu}$ ($4{,}70\text{ eV}$), $\text{Ag}$ ($4{,}73\text{ eV}$) e $\text{Pt}$ ($6{,}35\text{ eV}$).
* **Linhas de Energia Incidentes:**
  - Linha roxa (Luz Violeta, $f = 7{,}2 \times 10^{14}\text{ Hz} \implies E_f = 2{,}98\text{ eV}$): mostra que apenas o Sódio está abaixo da linha.
  - Linha vermelha (Luz UV, $\lambda = 230\text{ nm} \implies E_f = 5{,}38\text{ eV}$): mostra que todos até a Prata sofrem emissão, exceto a Platina.

---

## 5. Manual Operacional da Simulação Interativa HTML ao Vivo

### 🎯 Momento Exato de Mostrar
No início do **Slide 5**, por volta do minuto **10:00** da apresentação.

### 💻 Como Mostrar na Prática
1. Antes de iniciar a apresentação, dê duplo clique no arquivo **[`simulador_interativo.html`](./simulador_interativo.html)** para deixá-lo aberto em uma aba do navegador (Chrome ou Edge).
2. Deixe o navegador em tela cheia pressionando **`F11`**.
3. No Slide 5, alterne suavemente do PDF para o navegador usando o atalho **`Alt + Tab`**.
4. Realize os **3 testes rápidos** em sequência (duração total: 1 a 1,5 minuto):

---

#### 🧪 Teste 1: O Corte Quântico (Provar que Intensidade NÃO compensa Frequência)
1. **O que clicar:**
   - Deixe o metal selecionado em **Sódio (Na)**.
   - Clique no botão rápido **`Amarela (5,1)`**.
   - Puxe o slider de **Intensidade Luminosa para 100%**.
2. **O que mostrar na tela:**
   - O tubo a vácuo está sendo bombardeado por feixes amarelos intensos, mas **nenhum elétron sai da placa** e o microamperímetro permanece cravado em $0{,}00\text{ }\mu\text{A}$.
3. **O que falar:**
   > *"Vejam aqui no simulador: mesmo com a lâmpada em 100% de intensidade disparando dezenas de fótons amarelos por segundo, nenhum elétron sai do cátodo. Isso acontece porque a colisão é individual (1 fóton para 1 elétron): cada fóton amarelo carrega apenas 2,11 eV, insuficiente para superar a função trabalho de 2,28 eV do Sódio."*

---

#### 🧪 Teste 2: Emissão e Frenagem Eletrostática (Potencial de Corte $-V_0$)
1. **O que clicar:**
   - Clique no botão rápido **`Violeta (7,2)`**.
   - Os fotoelétrons azuis começarão a se mover pelo tubo e o microamperímetro marcará corrente.
   - Em seguida, clique no botão vermelho **`🛑 Aplicar Potencial de Corte (-V₀)`** (ele ajusta a tensão para $-0{,}70\text{ V}$).
2. **O que mostrar na tela:**
   - Os elétrons saem da placa esquerda, são desacelerados pelo campo elétrico reverso no meio do tubo e **param exatamente antes de tocar o ânodo**, fazendo a corrente cair a zero!
3. **O que falar:**
   > *"Ao mudar para luz violeta (2,98 eV), a energia supera a barreira e os fotoelétrons passam a fluir. Quando clicamos no botão de corte, o circuito aplica a tensão reversa de -0,70 V. Reparem como o campo elétrico freia até os elétrons mais velozes imediatamente antes de tocarem o ânodo, zerando a fotocorrente e comprovando numericamente a conservação de energia qV₀ = K_max."*

---

#### 🧪 Teste 3: Dependência do Material (A Barreira $\phi$)
1. **O que clicar:**
   - No menu seletor de metal, mude de **Sódio (Na)** para **Cobre (Cu)** ($\phi = 4{,}70\text{ eV}$).
   - Observe que a emissão para imediatamente sob luz violeta!
   - Clique então no botão rápido **`UV 250nm (12,0)`**.
2. **O que mostrar na tela:**
   - Sob luz violeta, o Cobre fica inerte. Ao acionar o UV, elétrons voltam a ser ejetados com alta velocidade.
3. **O que falar:**
   > *"Mudando o metal para Cobre, cuja barreira é de 4,70 eV, a luz violeta não consegue mais arrancar elétrons. Precisamos de radiação Ultravioleta para retomar a emissão fotoelétrica."*

5. Dê **`Alt + Tab`** de volta para o Slide 5 para fazer a conclusão final da equipe.

---

## 6. O Que Vocês Devem Saber na Ponta da Língua (Arguição do Professor)

### Pergunta 1: *"Por que na equação escrevemos $K_{\max}$ (energia cinética MÁXIMA) e não simplesmente $K$?"*
* **Resposta Pronta:**
  > *"Excelente ponto, professor. A função trabalho $\phi$ é a energia mínima necessária para extrair os elétrons que estão no topo da banda de condução, no **Nível de Fermi**. Elétrons que se encontram em níveis energéticos mais profundos dentro do metal, ou elétrons que sofrem colisões inelásticas no caminho até a superfície, perdem parte da energia e emergem com energia cinética menor que a máxima ($K < K_{\max}$). É por essa razão que, no nosso gráfico de $I_{\text{foto}} \times V$, a corrente não cai a zero em degrau vertical no zero volt, mas apresenta uma curva suave de transição até zerar completamente no potencial de corte $-V_0$, quando até os elétrons mais energéticos ($K_{\max}$) são freados."*

### Pergunta 2: *"Por que aumentar a intensidade da luz não aumenta a velocidade máxima dos fotoelétrons?"*
* **Resposta Pronta:**
  > *"Porque no regime fotoelétrico linear, a interação ocorre na base de **1 fóton para 1 elétron**. Aumentar a intensidade luminosa mantendo a frequência fixa significa apenas injetar **mais fótons por segundo** no metal, o que gera mais fotoelétrons por segundo e aumenta a fotocorrente de saturação. No entanto, a energia individual entregue a cada elétron é estritamente $E = hf$. Como a barreira $\phi$ do material é constante, o saldo de energia cinética máxima $K_{\max} = hf - \phi$ permanece rigorosamente o mesmo."*

### Pergunta 3: *"Como a inclinação do gráfico do efeito fotoelétrico se conecta com a Aula 02 de LEDs?"*
* **Resposta Pronta:**
  > *"Eles são fenômenos complementares governados pela mesma constante universal da física. No efeito fotoelétrico (absorção), o fóton de radiação gera fotoelétrons freados por $qV_0 = hf - \phi$, onde a razão $\Delta V_0 / \Delta f = h/q$. No experimento com LEDs da Aula 02 (emissão eletroluminescente por recombinação elétron-buraco), a tensão elétrica limiar injetada converte-se na emissão espontânea de um fóton $hf \approx qV_{\text{limiar}}$, onde a razão $\Delta V_{\text{limiar}} / \Delta f$ também é igual a $h/q$. Em ambos os casos, a inclinação linear permite determinar experimentalmente a **constante de Planck ($h$)**."*

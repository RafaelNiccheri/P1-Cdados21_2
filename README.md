# P1-Cdados21_2 (Classificador de tweets do Fantastico)
## Conta do tweeter @RNiccheri

## Problema Apresentado:
### O problema proposto era como descrito a seguir:
Uma empresa queria reunir ‘tweets’ sobre um de seus produtos, no entanto, como o ‘tweeter’ é uma das maiores plataformas digitais, o número de ‘tweets’ era muito grande. Então, era preciso arrumar um modo de separar os tweets que eram relevantes, sendo assim nos teriamos sido contratodos por essa empresa afim de criar um classicador de tweets relevantes e irrelevantes, e teriamos escolhido utilizar o teorema de Naive-Bayes em conjunto com a Suavização de Laplace para criar este classificador. 

## Nossa opinião sobre nosso projeto:
Por mais que nosso classificador esteja com um desempenho de +/- 52.5% de acurácia estamos felizes com o resultado do nosso projeto. Para criar o classificador criamos um módulo para a biblioteca pandas e emoji do zero, tornando a maior parte do código escrito durante o projeto algo que podera ser reutilizado pelos membros do grupo em outros projetos. Além disso, ao procurar maneiras de melhorar a performance, descobrimos tambem novos modos de categorizar textos para programação como a Vetorização de Texto e conseguimos estabelecer conexões entre a relação entre os métodos de vetorização BOW e TF-IDF e a relação entre a Suavização de Laplace e o Teorema de Naive-Bays.

- ## Sobre nosso projeto
     - Por que criamos tantas opções de organização da base de dados?
       - Como nunca é possível prever o que um usuário comum pretende fazer exatamente com a base de dados organizada ou como ele pretende usa-la em sua íntegra pensamo que seria uma ótima adição fazer com que algumas opções retornem dicionários outras retornem listas e outras retornem dataframes.
         - Por que criamos 7 filtros diferentes?
           - Com o intuito de criar um código que além de ser útil para esse projeto pudesse também ser usado para qualquer outro projeto usando pandas pensamo que epenas um ou dois filtros nao seriam o suficiente
             - remove_at - tira palavras com @
             - remove_link - Tira palavras com http
             - remove_ponc - Tira pontuação
             - remove_laugh - Tira palavras que tenham mais do que x k's juntos contanto que eles representem no mínimo y% da palavra
             - remove_word_sts - Tira palavras menores do que x
             - remove_num_str - tira palavras com uma sequência de números maiores que x ou que tenham uma quantidade de números que representem mais de y% de uma palavra
             - remove_options - recebe True/False para cada uma dessas funções e caso a função possa receber ou exija parâmetros ela também os recebe
<p align="center">
  <img src="https://github.com/RafaelNiccheri/gfjh/blob/main/Captura%20de%20tela%202021-09-16%20220519.png">
</p>

- ### Como ele pode ser melhorado:
  - #### Lemmatizing words
  - #### n-grams
  - #### TF-IDF
    - TF-IDF (Term Frequency-Inverse Document Frequency) é um modo de vetorizar textos que podem ser livros, artigos científicos, revistas ou até mesmo ‘tweets’. Vetorizar um texto é o processo de atribuir números para textos. Um exemplo da utilização desse mecanismo no dia a dia é a ferramenta de pesquisa do google e demais navegadores. É possível fazer um paralelo entre a TF-IDF e a Suavização de Laplace, visto que assim como a Suavização de Laplace, este também surgiu para corrigir um problema em outro método, no entanto, nesse caso foi para corrigir um problema na Vetorização de Textos por Bag of Words (BOW). O método BOW vetoriza textos somente conforme a frequência com que cada palavra de uma frase aparece em cada texto analisado. JÁ a TF-IDF também considera a quantidade de vezes em que uma palavra aparece no conjunto do texto. Ao separar o anagrama TF-IDF no “hífen” obtemos TF, o que equivale ao método BOW, e IDF, que considera a frequência total de cada palavra em todos os textos. A seguir está um code snippet com uma ideia incompleta de como codar a TF-IDF e uma imagem do cálculo, com um embedded link para o site usado para entender o que TF-IDF é e como ela pode ser usada e aplicada.
````python
# apos limpar e separar a base de dados em relevante e irrelevante
rel = ['asd356756378fasdf aerg', 'asdfas123df', 'import', 'sys']
irel = ['asdfas123df', 'asd356756378fasdf', 'dsghsdfghs', 'aerg', 'Projetos']
l = rel + irel
l_split = [j for s in l for j in s.split()]
l_join = ' '.join(str(n) for n in l)
frequencia_txt_td = {s: l_join.count(s) for s in l_split}  # cria um dicionario com todas as palavras e suas frquencias no texto inteiro
frequencia_txt_rel = {s: l_join.count(s) for s in l_split}  # cria um dicionario com todas as palavras e suas frquencias no texto rel
frequencia_txt_irel = {s: l_join.count(s) for s in l_split}  # cria um dicionario com todas as palavras e suas frquencias no texto irel
'agr só faltaria matematica - agr só faltaria matematica - agr só faltaria matematica - agr só faltaria matematica'
````
<p align="center">
 <a href="https://towardsdatascience.com/getting-started-with-text-vectorization-2f2efbec6685" >
 <img src="https://raw.githubusercontent.com/RafaelNiccheri/gfjh/main/zdfsg.png?token=AO7T4BXDFZ4FLHVJP4LBPG3BKOHWQ">
  </a>
</p>

### Poderíamos usar esse classificador para gerar mais amostras de treinamento?
Não podemos usar o classificador para gerar novas amostras de treinamento, pois nesse caso, o classificador iria classificar as amostras e ao usa-las para treinar iria obter um acerto de 100% visto que ele está comparando sua classificação com ela mesma ao invés de comparar com uma classificação previa feita de outro modo. Usar o classificador desse modo é igual a fazer uma prova e usar ela mesma como gabarito para checar suas respostas.

# Conclusão
Nosso classificador obteve em média uma acracia de 52%, o que não é muito mais preciso do que rodar um dado, no entanto, ao discorrermos sobre o motivo disso chegamos a algumas hipóteses. Primeiro nós acreditamos que um fator decisivo na perda de acurácia é o tamanho da base de dados utilizada. Como nos utilizamos apensa 300 ‘tweets’ para a base de dados Treinamento, o vocabulário de palavras uteis do nosso classificador estava mt pequeno fazendo com que palavra que frases que potencialmente fossem ser classificadas como relevantes acabassem sendo classificadas erroneamente como irrelevantes ou vice-versa. No entanto, essa hipótese apenas explicava o motivo da acurácia estar tao perto de 50%, mas não explicava o motivo de todas as simulações realizadas terem mais ‘tweets’ totais classificados como relevantes (aproximadamente 56%) do que o total de ‘tweets’ relevantes classificados a mao. Foi então que surgiu nossa segunda hipótese, esta discorre sobre a influência que frases de dupla negação ou sarcasmo tem com relação ao desempenho do nosso classificador, nós acreditamos que como o ‘tweeter’ é uma plataforma informal e livre é comum encontrar frases sarcásticas e de dupla negação, estas são geralmente constituídas por palavras relevantes e que transmitem sentido e opiniões importantes, no entanto, as mesmas, neste caso transmitem apenas criticas e opiniões vazias sem relevância alguma para o contexto do estudo o que infla o número de palavras irrelevantes classificas como relevantes.


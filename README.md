# P1-Cdados21_2 (Classificador de tweets do Fantastico)
## Conta do tweeter @RNiccheri

## Problema Apresentado:
### O problema proposto era como descrito a seguir:
Uma empresa queria reunir ‘tweets’ sobre um de seus produtos, no entanto, como o ‘Twitter’ é uma das maiores plataformas digitais, o número de ‘tweets’ era muito grande. Então, era preciso arrumar um modo de separar os ‘tweets’ que eram relevantes, sendo assim nos teríamos sido contratados por essa empresa de modo a criar um classificador de ‘tweets’ relevantes e irrelevantes, e teríamos escolhido utilizar o teorema de Naive-Bayes em conjunto com a Suavização de Laplace para criar este classificador.

## Nossa opinião sobre nosso projeto:
Por mais que nosso classificador esteja com um desempenho de +/- 52.5% de acurácia estamos felizes com o resultado do nosso projeto. Para criar o classificador criamos um módulo para a biblioteca pandas e ‘emoji’ do zero, tornando a maior parte do código escrito durante o projeto algo que poderá ser reutilizado pelos membros do grupo em outros projetos. Além disso, ao procurar maneiras de melhorar a desempenho, descobrimos também novos modos de categorizar textos para programação como a Vetorização de Texto e conseguimos estabelecer conexões entre a relação entre os métodos de vetorização BOW e TF-IDF e a relação entre a Suavização de Laplace e o Teorema de Naive-Bayes.

- ## Sobre nosso projeto
     - Por que criamos tantas opções de organização da base de dados?
       - Como nunca é possível prever o que um usuário comum pretende fazer exatamente com a base de dados organizada ou como ele pretende usar-la em sua íntegra pensamo que seria uma ótima adição fazer com que algumas opções retornem dicionários outras retornem listas e outras retornem dataframes
         - Por que criamos 7 filtros diferentes?
           - Com o intuito de criar um código que além de ser útil para esse projeto pudesse também ser usado para qualquer outro projeto usando pandas pensamo que epenas um ou dois filtros nao seriam o suficiente
             - remove_at - tira palavras com @
             - remove_link - Tira palavras com http
             - remove_ponc - Tira pontuação
             - remove_laugh - Tira palavras que tenham mais do que x k's juntos contanto que eles representem no mínimo y% da palavra
             - remove_word_sts - Tira palavras menores do que x
             - remove_num_str - tira palavras com uma sequência de números maiores que x ou que tenham uma quantidade de números que representem mais de y% de uma palavra
             - remove_options - recebe True/False para cada uma dessas funções e caso a função possa receber ou exija parâmetros ela também os recebe
````python
class RemoveWords:
    list_desired_words = [Object_of_Study]
    while True:
        Desired_Study_Words = str(input(
            f"""Enter words you don't want removed individually or separated by space, all words
    entered are case matched to lowercase. Type {Object_of_Study} to leave: """))
        if '' in list_desired_words:
            list_desired_words.remove('')
        if Desired_Study_Words == Object_of_Study:
            break
        elif ' ' in Desired_Study_Words:
            split_input = [j for j in Desired_Study_Words.split()]
            for j in split_input:
                j = j.lower()
                list_desired_words.append(j)
        else:
            list_desired_words.append(Desired_Study_Words.lower())
    print(
        f'Here is a list of length {len(list_desired_words)} with all words that wont be removed {list_desired_words}')

    def __init__(self, dataframe, column_name, show_removed=False):

    def _filter_simple(self, key_word='', length_st=0):

    def remove_at(self):

    def remove_link(self):

    def remove_ponc(self, punks=string.punctuation):
       
    def remove_laugh(self, length_k, length_no_k):

    def remove_word_sts(self, length_s):

    def remove_num_str(self, length_num_c, percent_str_num=100):

    def remove_options(self, **kwargs):
````

- ### Como ele pode ser melhorado:
  - #### Lemmatizing words
  - #### n-grams
  - #### TF-IDF
    - TF-IDF (Term Frequency-Inverse Document Frequency) é um modo de vetorizar textos que podem ser livros, artigos científicos, revistas ou até mesmo ‘tweets’. Vetorizar um texto é o processo de atribuir números para textos. Um exemplo da utilização desse mecanismo no dia a dia é a ferramenta de pesquisa do google e demais navegadores. É possível fazer um paralelo entre a TF-IDF e a Suavização de Laplace, visto que assim como a Suavização de Laplace, este também surgiu para corrigir um problema em outro método, no entanto, nesse caso foi para corrigir um problema na Vetorização de Textos por Bag of Words (BOW). O método BOW vetoriza textos somente conforme a frequência com que cada palavra de uma frase aparece em cada texto analisado. JÁ a TF-IDF também considera a quantidade de vezes em que uma palavra aparece em um conjunto de textos. Ao separar o anagrama TF-IDF no “hífen” obtemos TF, o que equivale ao método BOW, e IDF, que considera a frequência total de cada palavra em todos os textos. A seguir está um ‘code snippet’ com uma ideia incompleta de como codar a TF-IDF e uma imagem do cálculo, com um embedded link para o site usado para entender o que TF-IDF é e como ela pode ser usada e aplicada.
````python
# apos limpar e separar a base de dados em relevante e irrelevante
rel = ['asd356756378fasdf 1232432 aerg aerg', 'asdfas123df lkidrugfyhb  ha ha ha ha ha dfs;gouijhbsr9pdog8', 'asdgfasgdda tf trf tf  import', 'rtuyie567yw6 w465yuw4uy  oi oi oi sys']
irel = ['asdfas123df', 'asd356756378fasdf', 'dsghsdfghs', 'aerg', 'Projetos']
l = rel + irel  # tds os documentos
l_split = [j for s in l for j in s.split()]  # tds as palavras em tds os documentos
l_join = ' '.join(str(n) for n in l)  # tds os documentos como 1
print('l_split', l_split)  # teste
print('l_join', l_join)  # teste
print('l',l)  # teste
frequencia_txt_ind = {}  # dictionary with each documents as a key and a dict with each term on it as a key and its respective frequency as value
for d in l:
    count_dic = {}
    for t in d.split():
        count_t = d.count(t)
        count_dic[t] = count_t
    frequencia_txt_ind[d] = count_dic
frequencia_txt_td = {s: l_join.count(s) for s in l_split}  # cria um dicionario com todas as palavras e suas frquencias no texto inteiro
'agr só faltaria matematica - agr só faltaria matematica - agr só faltaria matematica - agr só faltaria matematica'
print(frequencia_txt_ind)  # mais teste

""" AGORA FALTARIA APENAS USAR OS VALORES EM "frequencia_txt_td" PARA CALCULAR IDF E FAZER A CONTA"""
````
<p align="center">
 <a href="https://towardsdatascience.com/getting-started-with-text-vectorization-2f2efbec6685" >
 <img src="https://raw.githubusercontent.com/RafaelNiccheri/gfjh/main/zdfsg.png?token=AO7T4BXDFZ4FLHVJP4LBPG3BKOHWQ">
  </a>
</p>

### Poderíamos usar esse classificador para gerar mais amostras de treinamento?
Não podemos usar o classificador para gerar novas amostras de treinamento, pois nesse caso, o classificador iria classificar as amostras e ao usa-las para treinar iria obter um acerto de 100% visto que ele está comparando sua classificação com ela mesma ao invés de comparar com uma classificação previa feita de outro modo. Usar o classificador desse modo é igual a fazer uma prova e usar ela mesma como gabarito para checar suas respostas.

### Em quais outros contextos nosso classificador pode ser usado?
O Teorema de Naive-Bayes é muito utilizado como uma técnica de ‘Machine Learning’ classificada como ‘Supervised Learning’, e se sobressai em relação a outras formas de ‘Machine Learning’ quando usado para analisar base de dados menores. Técnicas categorizadas como ‘Unsupervised Learning’ geralmente são mais utilizadas quando o volume de dados é muito alto, pois as mesmas não precisam que sua base de dados de treinamento tenha sido previamente classificada e para conseguir "aprender" procura por padrões nos dados fornecidos. Geralmente essas técnicas necessitam de diversas iterações continuas para conseguirem aprender e obter uma acurácia aceitável. No entanto, as técnicas de ‘Supervised Learning’ como o Teorema de Naive-Bayes recebem uma classificação previa em sua base de dados de treinamento tornando-as muito mais rápidas. O Naive-Bayes citado anteriormente além de ser uma técnica de ‘Supervised Learning’ também é considerada uma das mais simples porem eficazes e rápidas deste grupo quando estamos lidando com base de dados pequenas. Assim, este método é muito utilizado para classificar e-mails como ‘spam’ ou não. Esta implementação do Naive-Bayes não se distancia muito do que é feito para classificar ‘tweets’, mas como e-mail ‘spam’ geralmente compartilham muitas características podemos fazer algumas melhorias que não eram possíveis com ‘tweets’. São estas: fazer uma comparação do endereço de e-mail que enviou um e-mail com uma base de dados contendo endereços falsos de empresas normalmente utilizados, checar se um e-mail contém muitos símbolos de dinheiro, checar se ele contém muitos links ou links considerados inseguros ou até mesmo se ele contém algum Java script ou outros scripts que podem ser usados para infectar computadores.

## Teste de 100 iterações do classificador (passo 6 localizxado no fim do nootebook principal)
Como dito acima, o classificador não obteve um desempenho muito melhor do que 50%. No entanto, seu desempenho também tende a não cair abaixo deste valor, assim é razoável dizer que o mesmo pode até não ser a melhor opção para uma classificação que requer uma precisão muito grande, mas nao deixa de ser uma opção viável para situações em que a precisão não é o mais importante, mas sim a rapidez visto que este método é muito mais rápido do que outros métodos de machine learning com acurácias mais elevadas. Ao analisarmos a histograma abaixo, é possível perceber que mesmo a nao estando muito acima de 52% de acurácia, a maior parte das iterações obteve entre 50% e 54% de acerto. Além disso, é possível perceber que das iterações que obtiveram uma diferença expressiva para a média do que seria rolar um dado, a maior parte esta entre 54% e 57% e a maior diferença para o centro é de 7% advindos de uma dessas iterações positivas citadas. Além disso, também é importante ressaltar que o gráfico mostra que o classificador obteve tres iterações com acurácia por volta de 57% e apenas duas com acurácia de pôr volta de 45%. Esse dado serve como mais um indicador que apesar de o classificador ter um desempenho perto de 50%, ele está no caminho certo e caso as melhorias citadas acima forem implementadas ele tem uma probabilidade grande de aumentar bastante essa acurácia.
<p align="center">
 <img src="https://raw.githubusercontent.com/RafaelNiccheri/gfjh/main/Figure_1.png?token=AO7T4BQO6CE2YYIWG2VD6GDBKSOSO">
</p>

# Conclusão
Nosso classificador obteve em média uma acurácia de 52%, o que não é muito mais preciso do que rodar um dado, no entanto, ao discorrermos sobre o motivo disso chegamos a algumas hipóteses. Primeiro nós acreditamos que um fator decisivo na perda de acurácia é o tamanho da base de dados utilizada. Como nos utilizamos apensa 300 ‘tweets’ para a base de dados Treinamento, o vocabulário de palavras uteis do nosso classificador estava mt pequeno fazendo com que palavra que frases que potencialmente fossem ser classificadas como relevantes acabassem sendo classificadas erroneamente como irrelevantes ou vice-versa. No entanto, essa hipótese apenas explicava o motivo da acurácia estar tao perto de 50%, mas não explicava o motivo de todas as simulações realizadas terem mais ‘tweets’ totais classificados como relevantes (aproximadamente 56%) do que o total de ‘tweets’ relevantes classificados a mao. Foi então que surgiu nossa segunda hipótese, esta discorre sobre a influência que frases de dupla negação ou sarcasmo tem com relação ao desempenho do nosso classificador, nós acreditamos que como o ‘tweeter’ é uma plataforma informal e livre é comum encontrar frases sarcásticas e de dupla negação, estas são geralmente constituídas por palavras relevantes e que transmitem sentido e opiniões importantes, no entanto, as mesmas, neste caso transmitem apenas criticas e opiniões vazias sem relevância alguma para o contexto do estudo o que infla o número de palavras irrelevantes classificas como relevantes.


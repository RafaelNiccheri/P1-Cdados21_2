# P1-Cdados21_2 (Classificador de tweets do Fantastico)
## Conta do tweeter @RNiccheri
#### Esquecemos de colocar docstring para as classes mas tds as funções tem ja.

### quero deixar explicito que nos referimos a nossa opinião sobre o andamento do nosso projeto e nao sobre o projeto proposto pela professora. Tmbem gostaria de deixar claro que existem varios erros de portugues pois ao escrever esta primeira versao nao nos preocupamos com gramatica ou sintaxe do texto.

## Problema Apresentado:
### O problema proposto era como descrito a seguir:
Uma empresa queria reunir tweets sobre um de seus prudotos, no entanto, como o tweeter  é uma das maisores plataformas digitais o nemuro de tweets era muito grande. Entao, era preciso arrumar um modo de separar os tweets que eram relevantes, sendo assim nos teriamos sido contratodos por essa empresa, afim de criar um classicador de tweets relevantes e irrelevantes, e teriamos escolhido utilizar o teorema de Naive-Bayes em conjunto com a Suavização de Laplace para criar este classificador de tweets. 




## Nossa opinião sobre nosso projeto:
Por mais que nosso classificar estaja com um desempenho de +/- 52.5% estamos felizes com o resultado do nosso projeto. Para criar o classificador criamos um novo mudolu para a biblioteca pandas e emoji do zero, o que tornando a maior parte do codigo escrito durante o projeto algo que podera ser reutilizado pelos membros do grupo em outros projetos. Além disso, ao procurar maneiras de melhorar a performance descobrimos tambem novos modos de categirizar textos para programação como a Vetorização de Texto e conseguimos estabelecer conexoes entre a relação entre os metodos de vetorização BOW e TF-IDF e a relação entre a Suavização de Laplace e o Teorema de Naive-Bays

## Branches:
Depois de ter terminado de escrever o codigo para a limpeza dos tweets iniciamos o processo de otimização do codigo. Ele consistia em passar por todas as funçaos e parametros globais das duas classes procurando semelhanças entre as Enherited functions de cada uma delas com o intuito de criar um decorando, uma funçáo ou um metodo global da classe que fosse capaz de executar esta parte semelhante para tds as funcões, deste modo diminuindo a memoria ocupada, o temanho do arquivo e o numero de linhas usadas. Para atingir este objetivo sem correr o risco substituir nossos arquvos funcionais par arquivos com gliches/bugs resultantes de uma optimizaçao incompleta foi criado o branch Optimizing em que eram commitados todos os comits que nao adicionavam usuabilidades novas mas sim corrigiam/melhoravam/atualizavam usuabilidades colocadas em previos commits, ao terminar de trabalhar em cada melhoria, era feito um merge afim de deixar o branch Optimizing sempre o menor numero possivel de comits a frente do branch main para que não fosse perdido mt progresso casa algun arquivo com diferenças substanciais a ultima versao otimizada e um numero de erros expressivo o bastante para considerar sua descontinuaçao fosse comitado.
- ## Sobre nosso projeto
     - Por que criamos tantas opções de organização da base de dados?
       - Como nunca é possivel prever o que um usuario comum pretende fazer exatamente com a base de dados organizada ou como ele pretende usa-la em sua integra achamos que seria uma otima adição fazer com que algumas opções retornem dicionarios outras retornem listas e outras retornem dataframes.
         - Por que criamos 7 filtros diferentes?
           - Com a intuito de criar um codigo que alem de ser util para esse projeto pudesse tambem ser usado para qualquer outro projeto usando pandas achamos que sepenas um ou dois filtros nao seriam o suficiente
             - remove_at - tira palavras com @
             - remove_link - Tira palavras com http
             - remove_ponc - Tira pontuação
             - remove_laugh - Tira palavras que tenham mais do que x k's juntos contanto que eles representem no minimo y% da palavra
             - remove_word_sts - Tira palavras menores do que x
             - remove_num_str - Tira palavras com uma sequencia de numeros maior que x
             - remove_options - recebe True/False para cada uma dessas funcoes e caso a funcáao possa receber ou exija parametros ela tamnem os recebe
<p align="center">
  <img src="https://github.com/RafaelNiccheri/gfjh/blob/main/Captura%20de%20tela%202021-09-16%20220519.png">
</p>

- ### Como ele pode ser melhorado:
  - #### Lemmatizing words
  - #### n-grams
  - #### TF-IDF
TF-IDF (Term Frequency-Inverse Document Frequency) é um modo de vetorizar textos, estes podem ser livros artigos científicos revistas ou até mesmo tweets. Vetorizar um texto é o processo de atribuir números para textos, um exemplo da utilização desse mecanismo no dia a dia é a ferramenta de pesquisa do google e demais browsers. É possível fazer um paralelo entre a TF-IDF e a Suavização de Laplace, uma vez que assim como a Suavização de Laplace, esta também surgiu para corrigir um problema em um outro método, no entanto em seu caso foi para corrigir um problema na Vetorização de Textos por Bag of Words (BOW). O método BOW vetoriza textos somente de acordo com a frequência com que cada palavra de uma frase aparece em cada texto analisado. JÁ a TF-IDF também leva em conta a quantidade de vezes em que uma palavra aparece no conjunto de texto. Ao separar o anagrama TF-IDF no “hífen” obtemos TF, o que equivale ao método BOW, e IDF, o que leva em conta a frequência total de cada palavra em todos os textos. A seguir está um code snippet com uma ideia incompleta de como codar a TF-IDF e uma imagem, um embedded link  para o site usado para entender o que TF-IDF é e como ele pode ser usado e aplicado, do cálculo para realizar TF-IDF.
````python
# apos limpar e separar a base de dados em relevante e irrelevante
rel = ['asd356756378fasdf aerg', 'asdfas123df', 'import', 'sys']
irel = ['asdfas123df', 'asd356756378fasdf', 'dsghsdfghs', 'aerg', 'Projetos']
l = rel + irel
l_split = [j for s in l for j in s.split()]
l_join = ' '.join(str(n) for n in l)
print('l_split', l_split)
print('l_join', l_join)
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
### Documentação:

##### Em Breve...


# Place-Holder text tirado de um outro repositorio meu para ter uma ideia de formatação do read.me

# Simple-Chatty-Bot (complete)

## My opinipon:
If you've never worked with a programing language this project will be a great entry point. It explains verry well the logic behind each line and expands on that by teaching in paralel how to properlly write your code respecting pythons "formating" guide-lines. Eventhought this project is easy for someone with a little of programing expirience it still teaches valuable python etiquette that programers should learn and aply from the start.

## Branches:
I wanted to creat two independent branches, one with the coppy of the folder I worked with and the other only with the .py files but wasnt able to. As it is right now I only need to delete the main branche and coppy this file the both of the independent branches.

## overall opinion:
- Project itself:
  - Targeted at people who have never programed or just started a few days or weeks ago
  - If you've learned the correct way to format your code they have a [PEP-8 code style mini course](https://hyperskill.org/learn/step/5879) and  a [commenting mini course](https://hyperskill.org/learn/step/6081). Things I hadn't lerned about before those two mini couses.
    - I'd never heard of [PEP-8](https://www.python.org/dev/peps/) or any other type of coding stile guide books
    - I never knew the correct spacing between the code line and the comment or how to deal with big comments
  - If you know a little about programing but also haven't heard of those guideline both mini courses toghether wont take more then 20 minuts
  - It's easy to creat a connection between all the different things you're tought
  - The idea to turn all the the different benchmarks you reach into a final project gisves the sensation that what you learned was worth wile
  - As someone diagnosed with ADHD and ADD it's really gruelling to read all the theory presented wich led me to skip all of it exept for the PEP-8 one
- About the option to comit or not to [GitHub](https://github.com/):
  - I would do it even if only privately because it's a good way to keep track of your improvement
  - This being the first project for people who know nouthing about python it should have a walk through for commiting through JetBrains IDE.
    - I've used GitHub before but always have truble using it (specially to creat idependent branches) I could never do it. I already tried all methods I could find.
  
  ## HERE IS MY PROGRESS AS OF WRITING THIS: 
  ![image](https://user-images.githubusercontent.com/62864902/131230794-a84569b3-442e-4623-a4b5-96dc946e6823.png)

<ol>
<li>
<p>A paragraph
with two lines.</p>
<pre><code>indented code
</code></pre>
<blockquote>
<p>A block quote.</p>
</blockquote>
</li>
</ol>

# P1-Cdados21_2 (Classificador de tweets do Fantastico)
## Conta do tweeter @RNiccheri
#### Esquecemos de colocar docstring para as classes mas tds as funções tem ja.

### quero deixar explicito que nos referimos a nossa opinião sobre o andamento do nosso projeto e nao sobre o projeto proposto pela professora. Tmbem gostaria de deixar claro que existem varios erros de portugues pois ao escrever esta primeira versao nao nos preocupamos com gramatica ou sintaxe do texto.

## Problema Apresentado:
###O problema proposto era como descrito a seguir:
Uma empresa queria reunir tweets sobre um de seus prudotos, no entanto, como o tweeter  é uma das maisores plataformas digitais o nemuro de tweets era muito grande. Entao, era preciso arrumar um modo de separar os tweets que eram relevantes, sendo assim nos teriamos sido contratodos por essa empresa, afim de criar um classicador de tweets relevantes e irrelevantes, e teriamos escolhido utilizar o teorema de Naive-Bayes em conjunto com a Suavização de Laplace para criar este classificador de tweets. 




## Nossa opinião sobre nosso projeto:
Por mais que o projeto ainda nao esteja completo, estamos contentes com o progresso realizado e o ritimo em que estamos sendo capazes de atualiza-lo.

## Branches:
Depois de ter terminado de escrever o codigo para a limpeza dos tweets iniciamos o processo de otimização do codigo. Ele consistia em passar por todas as funçaos e parametros globais das duas classes procurando semelhanças entre as Enherited functions de cada uma delas com o intuito de criar um decorando, uma funçáo ou um metodo global da classe que fosse capaz de executar esta parte semelhante para tds as funcões, deste modo diminuindo a memoria ocupada, o temanho do arquivo e o numero de linhas usadas. Para atingir este objetivo foi criado o branch Optimizing em que eram commitados todos os comits que nao adicionavam usuabilidades novas mas sim corrigiam/melhoravam/atualizavam usuabilidades colocadas em previos commits. 

### Explicações gerais sobre nosso projeto:
- Por que criamos tantas opções de organização da base de dados?
  - Como nunca é possivel prever o que um usuario comum pretende fazer exatamente com a base de dados organizada ou c ele pretende usa-la em sua integra achamos que seria uma otima adição fazer com que algumas opções retornem dicionarios outras retornem listas e outras retornem dataframes.
- Por que criamos 7 dataframes?
  - Com o intuito de otimizar ao maximo o desempenho do nosso classificador, uma limpeza so do dataframe nao seria o sufuciente pois nao teriamos parametros de comparacão para saber quao eficiente essa limpeza foi ao que se diz respesto ao desempenho do classificador. Uma limpeza extremamente rigida nem sempre é a melhor opção mas concerteza é uma opção como qualquer outra tambem é, com isso em mente decidimos criar 6 filtros diferentes e um dataframe diferente para cada filtro. No entanto como dito acima, é impossivel prever qual é a melhor combinacao entre essas limpezas e por isso dicidimos tambem criar o 7 dataframe, criado apartir da função **"remove_options"** ele permite que o usuario passe True (Verdadeiro) ou False (Falso) para cada filtro criado, alem de passar os seus parametros é claro, deste modo, é possivel criar 6! dataframes diferentes o que equivale a 720 possibilidades. 
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


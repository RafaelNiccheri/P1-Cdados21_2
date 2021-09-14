import string
import functools
import operator
import emoji
import numpy as np
import pandas as pd

global Object_of_Study
Object_of_Study = input('Input the object of this study below\n>>> ')


class ListWord:
    def __init__(self, column_name="", column_number=-1):
        """

        :param column_number: number of the pandas.DataFrame
        :type column_number: int
        :param column_name: name of the pandas.DataFrame
        :type column_name: str
        """
        self.list_word = []
        self.emoji_list = []
        self.dataframe = 'dataframe'
        self.column_name = str(column_name)
        self.column_number = int(column_number)

    def _b_c_l(self, dataframe, start_list, stop_list, only_word):
        """
        :type dataframe: pandas.DataFrame
        :type start_list: int
        :type stop_list: int
        :type only_word: Boolean
        :param dataframe: pandas.DataFrame
        :param start_list: number of the row
        where the function should start
        :param stop_list: number of the row
        where the function should end
        """
        for i in np.arange(start_list, stop_list):
            splitting_emoji_string = emoji.get_emoji_regexp().split(dataframe[self.column_name][i])
            splitting_grouped_string = [j.split() for j in splitting_emoji_string]
            uniting_sting_lists = functools.reduce(operator.concat, splitting_grouped_string)
            if only_word:
                removing_not_word = [j for j in uniting_sting_lists if j.isalpha()]
                self.list_word += removing_not_word
            else:
                self.list_word += uniting_sting_lists

    def by_column_name(self, dataframe, start_list, stop_list, only_word=False):
        """

        :type dataframe: pandas.DataFrame
        :type start_list: int
        :type stop_list: int
        :type only_word: Boolean
        :param only_word: if True keep only words
        :param dataframe: pandas.Data
        :param start_list: number of the row
        where the function should start
        :param stop_list: number of the row
        where the function should stop
        :return: list of words from specified
        pandas.DataFrame rows and column
        :rtype: list
        """
        if only_word:
            print(
                f"only_word is set to {only_word}. Are you sure you only want to keep words you can get "
                f"back emoji latter")
        self._b_c_l(dataframe, start_list, stop_list, only_word)
        return self.list_word

    def by_column_number(self, dataframe, start_list, stop_list, only_word=False):
        """

        :type dataframe: pandas.DataFrame
        :type start_list: int
        :type stop_list: int
        :type only_word: Boolean
        :param only_word: if True keep only words
        :param dataframe: pandas.DataFrame
        :param start_list: where
        :param stop_list: 
        :return: list of words from specified
        pandas.DataFrame rows and column
        :rtype: list
        """
        for i in np.arange(start_list, stop_list):
            splitting_emoji_string = emoji.get_emoji_regexp().split(dataframe.iloc[i, self.column_number])
            splitting_grouped_string = [j.split() for j in splitting_emoji_string]
            uniting_sting_lists = functools.reduce(operator.concat, splitting_grouped_string)
            if only_word:
                removing_not_word = [j for j in uniting_sting_lists if j.isalpha()]
                self.list_word += removing_not_word
            else:
                self.list_word += uniting_sting_lists
        return self.list_word

    def _l_e(self, dataframe, start_lists, stop_lists):
        """
        :type dataframe: pandas.DataFrame
        :type start_lists: int
        :type stop_lists: int
        :param dataframe: pandas.DataFrame
        :param start_lists: number of the row
        where the function should start
        :param stop_lists: number of the row
        where the function should end
        """
        lista_emo1 = []
        for i in np.arange(start_lists, stop_lists):
            lista_emo1.append(''.join(j for j in dataframe[self.column_name][i] if j in emoji.UNICODE_EMOJI['en']))
            if '' in lista_emo1:
                lista_emo1.remove('')
        for i in lista_emo1:
            lista_emo1_s = list(i)
            for j in lista_emo1_s:
                self.emoji_list.append(j)

    def list_emoji(self, dataframe, start_list, stop_list):
        """

        :param start_list: number of the row
        where the function should start
        :type start_list: int
        :param stop_list: number of the row
        where the function should end
        :type stop_list: int
        :param dataframe: dataframe that will be listed
        :type dataframe: pandas.DataFrame
        :return: list of all emoji in the dataframe
        :rtype: list
        """
        self._l_e(dataframe, start_lists=start_list, stop_lists=stop_list)
        return self.emoji_list

    def lists_all(self, dataframe, c_o_c=False):
        """

        :type c_o_c: Boolean
        :param c_o_c: if True calls count_list_occurrence
        :param dataframe: pandas.DataFrame
        :return: list of all words + emoji in the dataframe.
        :rtype: list.
        """
        self._l_e(dataframe, 0, len(dataframe))
        self._b_c_l(dataframe, 0, len(dataframe), only_word=False)
        if c_o_c:
            c_o_c_l = self.emoji_list + self.list_word
            self.count_list_occurrence(c_o_c_l, dic_obj={}, creat_dataframe=True)
            return self.count_list_occurrence
        else:
            return self.emoji_list + self.list_word

    def c_o_f(self, dataframe):
        """

        :rtype: pandas.DataFrame
        """
        self.lists_all(dataframe, c_o_c=True)
        return self.dataframe

    def count_list_occurrence(self, list_obj, dic_obj=None, creat_dataframe=False):
        """

        :type creat_dataframe: Boolean
        :type list_obj: list
        :type dic_obj: dictionary
        :rtype: dict
        :param creat_dataframe: if True it returns a pandas.DataFrame
        :param list_obj: list of any object type
        :param dic_obj: dictionary in witch to
        count occurrences. If it´s not passed,
        creates a new one. If a existing one is passed
        it will be read as (key:value), (items:occurrences).
        :return: a new dict as (keys:values), (items:occurrences).
        if a existing dict is given it will make a copy of it and alter
        only the copy. If creat_dataframe is True returns a pandas.DataFrame
         created from these new dictionary
        """
        if dic_obj is None:
            dic_obj = {}
        set_dic = set(dic_obj.keys())
        set_list = set(list_obj)
        for pp in set_list:
            if pp not in set_dic:
                dic_obj[pp] = 0
        for z in list_obj:
            dic_obj[z] += 1
        if creat_dataframe:
            new_dataframe = pd.DataFrame.from_dict(dic_obj, orient='index', columns=['# de ocorrências'])
            self.dataframe = new_dataframe
        else:
            return dic_obj


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
        """

        :param show_removed: if True shows a list of all removed words
        :type show_removed: Boolean
        :param dataframe: Receives a pandas DataFrame
        :type dataframe: pandas.DataFrame
        :param column_name: specify the name of the pandas.DataFrame column
        :type column_name: str
        """
        self.column_name = str(column_name)
        self.dataframe = dataframe
        self.data = self.dataframe.to_dict()
        self.remove_all = False
        self.filtered = ''
        self.removed = []
        self.show_removed = show_removed
        self.emo_db = emoji.UNICODE_EMOJI['en']
        self.Object_of_Study = Object_of_Study
        self.new_dic = {}

    def filter_simple(self, key_word='', length_st=0):
        """

        :param key_word: character wich you disere all words containing to be removed
        :type key_word: str
        :param length_st: maximum length of the removed word
        :type length_st: int
        """
        keep_dic = {}
        data2 = self.data[self.column_name]
        self.new_dic = {self.column_name: keep_dic}
        for elements in data2.keys():
            elements_l = elements.lower()
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements_l in RemoveWords.list_desired_words:
                keep_dic[elements] = data2[elements]
            elif length_st > len(elements):
                self.removed.append(elements)
            elif key_word == '@' or key_word == 'http':
                if key_word in elements:
                    self.removed.append(elements)
                else:
                    keep_dic[elements] = data2[elements]
            else:
                keep_dic[elements] = data2[elements]

    def remove_at(self):
        """

        :rtype: pandas.DataFrame
        """
        self.filter_simple(key_word='@')
        if self.remove_all:
            self.data = self.new_dic
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(self.new_dic)

    def remove_link(self):
        """

        :return: dataframe without links
        :rtype: pandas.DataFrame
        """
        self.filter_simple(key_word='http')
        if self.remove_all:
            self.data = self.new_dic
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(self.new_dic)

    def remove_ponc(self, puncs=string.punctuation):
        """

        :param puncs: string of all punctuation marks to be removed
        :type puncs: str
        :return: dataframe without chosen punctuation
        :rtype: pandas.DataFrame
        """
        keep_dic = {}
        self.new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            elements_l = elements.lower()
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements_l in RemoveWords.list_desired_words:
                keep_dic[elements] = data2[elements]
            else:
                # for j in puncs:
                #     if j in elements:
                #         element = elements.replace(j, '')
                #         print(element, elements)
                #         keep_dic[element] = data2[elements]
                removing_puncs = elements.translate({ord(ponc_char): 0 for ponc_char in puncs})
                keep_dic[removing_puncs] = data2[elements]
        if self.remove_all:
            self.data = self.new_dic
        else:
            return pd.DataFrame.from_dict(self.new_dic)

    def remove_laugh(self, length_k, length_no_k):
        """

        :param length_no_k: minimum percentage of the string left after removing k's
        :type length_no_k: int
        :param length_k: minimum length of the laugh that is removed
        :type length_k: int
        :return: dataframe without k's in words with a lot of them in sequence
        :rtype: pandas.DataFrame
        """
        keep_dic = {}
        self.new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            string_nok = ""
            elements_l = elements.lower()
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements_l in RemoveWords.list_desired_words:
                keep_dic[elements] = data2[elements]
            elif 'k' * length_k in elements_l:
                list_wk = list(elements)
                for khas in list_wk:
                    if khas != "k":
                        string_nok += khas
                string_k_percent = (1 - (len(string_nok) / len(elements))) * 100
                if round(string_k_percent) > length_no_k:
                    self.removed.append(string_nok)
                    pass
                else:
                    keep_dic[string_nok] = data2[elements]
            else:
                keep_dic[elements] = data2[elements]
        if self.remove_all:
            self.data = self.new_dic
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(self.new_dic)

    def remove_word_sts(self, length_s):
        """

        :param length_s: minimum length of words
        :type length_s: int
        :return: dataframe without words smaller than length_s
        :rtype: pandas.DataFrame
        """
        self.filter_simple(length_st=length_s)
        if self.remove_all:
            self.data = self.new_dic
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(self.new_dic)

    def remove_num_str(self, length_num_c):
        """

        :param length_num_c: length of sequenced numbers
        in a string required for the string to be removed
        :type length_num_c: int
        :return: pandas.DataFrame without strings with the
        specified minimum length of of sequenced numbers
        :rtype: pandas.DataFrame
        """
        keep_dic = {}
        self.new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            elements_l = elements.lower()
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements_l in RemoveWords.list_desired_words:
                keep_dic[elements] = data2[elements]
            elif len(elements) <= length_num_c:
                keep_dic[elements] = data2[elements]
            else:
                for i in range(0, len(elements)):
                    k = length_num_c
                    k += i
                    if k <= len(elements):
                        slices_el = elements[i:k]
                        try:
                            if int(slices_el):
                                self.removed.append(elements)
                        except Exception:
                            keep_dic[elements] = data2[elements]
        if self.remove_all:
            self.data = self.new_dic
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(self.new_dic)

    def remove_options(self, **options_my_class):
        """

        :param options_my_class: Kwargs that determine what remove_*
        function will be called and give its parameters
        :type options_my_class: dict exemple - remove_options(remove_at={True: '()'}, remove_laugh={True: '(4, 3)'})
        :return: dataframe with filtered index accordance to Kwargs received
        :rtype: pandas.DataFrame
        """
        list_o = ['remove_at', 'remove_link', 'remove_ponc', 'remove_word_sts', 'remove_laugh', 'remove_num_str']
        list_f = ['self.remove_at', 'self.remove_link', 'self.remove_ponc', 'self.remove_word_sts', 'self.remove_laugh',
                  'self.remove_num_str']
        self.remove_all = True
        for choice in list_o:
            choice_tf = list(options_my_class[choice].keys())
            try:
                if choice_tf[0]:
                    getting_pos = list_o.index(choice)
                    choice_ff = list(options_my_class[choice].values())
                    eval(list_f[getting_pos] + str(choice_ff[0]))
                    print(choice, self.removed)
            except Exception:
                continue
        if self.show_removed:
            print('Total', self.removed)
        self.filtered = pd.DataFrame.from_dict(self.new_dic)
        return self.filtered


print('''Classes_funcoes é uma mini biblioteca feita para um projeto de Ciência de Dados com a principal função de
deixar mais fácil a interação entre a biblioteca pandas e a biblioteca emoji (esse era o intuito pelo
menos mas acabamos fazendo uma biblioteca para o projeto inteiro). Além das biblioteca citadas anteriormente,
ela requer as bibliotecas numpy, operator, functools e string. Quase certeza que todas estão disponíveis com pip
install''')

'''MUITO IMPORTANTE!!! COMO EU TIVE USAR ALGUMAS NOTAÇÕES INESPERADAS NESSE TRABALHO RESOLVI COLOCAR AQUI, ALÉM DO
NOTEBOOK PRINCIPAL (QUE ESTÁ AQUI PARA FACILITAR OS TESTES DO CÓDIGO), OS SCRATCHES CRIADOS DURANTE ESTE PROJETO.
PARA QUE ESTES SCRATCHES N FOSSEM EXECUTADOS JUNTO COM O RESTO DO SCRIPT COLOQUEI ELES DENTRO DE UM TRY QUE SEMPRE DA
ERRO E A COPIA DO NOTEBOOK QUE EU ESTAVA USANDO AQUI PARA TESTAR O CÓDIGO DENTRO DE UM EXCEPT EXCEPTION. TALL QUE:

def main()
    try:
        int("abc")
        .
        .
        .
    except Exception:
        código
        .
        .
if __name__ == "__main__":
    main()'''


def main():

    # #from classes_funcoes import *
    # from em_desenvolvimento import *
    # import string
    # import emoji
    # import pandas as pd



    dados_treino = pd.read_excel(f'{Object_of_Study}.xlsx')
    dados_treino_1=dados_treino
    dados_treino

    dados_treino_rel = dados_treino.loc[dados_treino['Unnamed: 1'] == 1]
    dados_treino_rel = dados_treino_rel.reset_index()
    dados_treino_rel = dados_treino_rel.loc[['Treinamento', 'Unnamed: 1']]


    p = ListWord(column_name='Treinamento').c_o_f(dados_treino_rel)
    p.sort_values(by='# de ocorrências', ascending=False)



    mn = RemoveWords(p, '# de ocorrências', show_removed=True)
    mn1 = RemoveWords(p, '# de ocorrências', show_removed=True)
    mn2 = RemoveWords(p, '# de ocorrências', show_removed=True)
    mn3 = RemoveWords(p, '# de ocorrências', show_removed=True)
    mn4 = RemoveWords(p, '# de ocorrências', show_removed=True)
    mn5 = RemoveWords(p, '# de ocorrências', show_removed=True)
    mn6 = RemoveWords(p, '# de ocorrências', show_removed=True)



    #### Antes de filtrar, todos os emojis e a/frase palavra designada como o object_of_study são excluídos da filtragem e colocados de volta na vase de dados. A palavra designada como object_of_study é definhada ao executar o codigo pela primeira vez else paras redefini-la é preciso reiniciar o ‘kernel’.



    print('\n sem palavras com @')
    qremove_at = mn1.remove_at()
    print('\n sem palavras com link')
    qremove_link =mn.remove_link()
    print('\n sem pontuação nas palavras')
    qremove_ponc = mn2.remove_ponc()
    print('\n sem palavras com menos de 3 letras')
    qremove_word_sts = mn3.remove_word_sts(3)
    print('\n sem palavras com mais de 3 ks juntos')
    qremove_laugh = mn4.remove_laugh(2, 5)
    print('\n sem palavras com sequencia de numero da ordem das unidades maior que 3 juntos')
    qremove_num_str = mn5.remove_num_str(3)
    print('\n todos os filtros juntos')
    qremove_options = mn6.remove_options(remove_at={True: '()'}, remove_link={True: '()'},
                                        remove_ponc={True: '()'},remove_laugh={True: '(2, 5)'},
                                        remove_word_sts={True: '(3)'}, remove_num_str={True: '(3)'})




    qremove_at.sort_values(by='# de ocorrências', ascending=False)



    qremove_link.sort_values(by='# de ocorrências', ascending=False)




    qremove_ponc.sort_values(by='# de ocorrências', ascending=False)



    qremove_word_sts.sort_values(by='# de ocorrências', ascending=False)



    qremove_laugh.sort_values(by='# de ocorrências', ascending=False)



    qremove_num_str.sort_values(by='# de ocorrências', ascending=False)



    qremove_options.sort_values(by='# de ocorrências', ascending=False)




    ## frequencia relativa





    qremove_options.sort_values(by='# de ocorrências', ascending=False)

    total_qremove_options = sum(qremove_options['# de ocorrências'])
    pd.DataFrame(qremove_options.index)

    # for frequencia, palavra in (qremove_options['# de ocorrências'], index_qremove_options['index']):
    #     qremove_options['frequência relativa']['palavra'] = frequencia * 100/total_qremove_options



    #### Caso alguma dessas listas de palavras retiradas seja do seu interesse para montar o classificador escolha-a agora. É recomandado escolher alguma lista para monta a base de dados de palavras irrelevantes.

    ##### abaixo estaremos montando nossa base de dados de palavrai irrelevantes. Penas poderão ser usadas palavras removidas do dataframe.







    'muito bom o programa'

    '''
    P(relevante/frase) = (P(muito/relevante) * P(bom/relevante) ... * P(relevante))
    '''

    '''
    EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO
    EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO
    EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO
    EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO - EM DESENVOLVIMENTO
    '''



    print(type(mn))



    mn
    # print(len(qremove_options['# de ocorrências']))



    print(f"""NUMERO DE VEZES QUER APARECE A PALAVRA DEFINIDA NO INPUT DO COMEÇO POR DATAFRAME CRIADO
    
    {sum(qremove_link['# de ocorrências'][[j for j in RemoveWords.list_desired_words]])} qremove_link
    {sum(qremove_at['# de ocorrências'][[j for j in RemoveWords.list_desired_words]])} qremove_at
    {sum(qremove_ponc['# de ocorrências'][[j for j in RemoveWords.list_desired_words]])} qremove_ponc
    {sum(qremove_word_sts['# de ocorrências'][[j for j in RemoveWords.list_desired_words]])} qremove_word_sts
    {sum(qremove_laugh['# de ocorrências'][[j for j in RemoveWords.list_desired_words]])} qremove_laugh
    {sum(qremove_num_str['# de ocorrências'][[j for j in RemoveWords.list_desired_words]])} qremove_num_str
    {sum(qremove_options['# de ocorrências'][[j for j in RemoveWords.list_desired_words]])} qremove_options""")



    qremove_options_1 = qremove_options.sort_values(by='# de ocorrências', ascending=False)
    qremove_options_1=qremove_options_1.loc[qremove_options_1['# de ocorrências'] > 50]
    qremove_options_1

if __name__ == "__main__":
    main()
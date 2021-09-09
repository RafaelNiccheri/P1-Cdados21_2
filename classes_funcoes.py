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

        :type column_number: specify the number of the pandas.DataFrame
        :type column_name: specify the name of the pandas.DataFrame
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
                f"only_word is set to {only_word}. Are you sure you only want to keep only words you can get "
                f"back\nemojis latter")
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

    def _l_e(self, dataframe, start_list, stop_list):
        """
        :type dataframe: pandas.DataFrame
        :type start_list: int
        :type stop_list: int
        :param dataframe: pandas.DataFrame
        :param start_list: number of the row
        where the function should start
        :param stop_list: number of the row
        where the function should end
        """
        lista_emo1 = []
        for i in np.arange(start_list, stop_list):
            lista_emo1.append(''.join(j for j in dataframe[self.column_name][i] if j in emoji.UNICODE_EMOJI['en']))
            if '' in lista_emo1:
                lista_emo1.remove('')
        for i in lista_emo1:
            lista_emo1_s = list(i)
            for j in lista_emo1_s:
                self.emoji_list.append(j)

    def list_emoji(self, dataframe):
        """

        :param dataframe: pandas.DataFrame
        :return: list of all emojis in the dataframe
        :rtype: list
        """
        self.__l_e(dataframe)
        return self.emoji_list

    def lists_all(self, dataframe, c_o_c=False):
        """

        :type c_o_c: Boolean
        :param c_o_c: if True calls count_list_occurrence
        :param dataframe: pandas.DataFrame
        :return: list of all words + emojis in the dataframe.
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
    def __init__(self, dataframe, column_name, show_removed=False):
        """
        :param Object_of_Study: global asked by lib at the execution
        :type Object_of_Study: str
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

    def remove_at(self):
        keep_dic = {}
        new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements == self.Object_of_Study:
                keep_dic[elements] = data2[elements]
            elif '@' in elements:
                self.removed.append(elements)
            else:
                keep_dic[elements] = data2[elements]
        if self.remove_all:
            self.data = new_dic
            self.filtered = pd.DataFrame.from_dict(new_dic)
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(new_dic)

    def remove_link(self):
        """

        :return: dataframe without links
        :rtype: pandas.DataFrame
        """
        keep_dic = {}
        new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements == self.Object_of_Study:
                keep_dic[elements] = data2[elements]
            elif 'http' in elements:
                self.removed.append(elements)
                pass
            else:
                keep_dic[elements] = data2[elements]
        if self.remove_all:
            self.data = new_dic
            self.filtered = pd.DataFrame.from_dict(new_dic)
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(new_dic)

    def remove_ponc(self, puncs=string.punctuation):
        """

        :param puncs: string of all punctuation marks to be removed
        :type puncs: str
        :return: dataframe without chosen punctuation
        :rtype: pandas.DataFrame
        """
        keep_dic = {}
        new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements == self.Object_of_Study:
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
            self.data = new_dic
            self.filtered = pd.DataFrame.from_dict(new_dic)
        else:
            return pd.DataFrame.from_dict(new_dic)

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
        new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            string_nok = ""
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements == self.Object_of_Study:
                keep_dic[elements] = data2[elements]
            elif 'k' * length_k in elements.lower():
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
            self.data = new_dic
            self.filtered = pd.DataFrame.from_dict(new_dic)
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(new_dic)

    def remove_word_sts(self, length_s):
        """

        :param length_s: minimum length of words
        :type length_s: int
        :return: dataframe without words smaller than length_s
        :rtype: pandas.DataFrame
        """
        keep_dic = {}
        new_dic = {self.column_name: keep_dic}
        data2 = self.data[self.column_name]
        for elements in data2.keys():
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements == self.Object_of_Study:
                keep_dic[elements] = data2[elements]
            elif len(elements) < length_s:
                self.removed.append(elements)
                pass
            else:
                keep_dic[elements] = data2[elements]
        if self.remove_all:
            self.data = new_dic
            self.filtered = pd.DataFrame.from_dict(new_dic)
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(new_dic)

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
        new_dic = {self.column_name: keep_dic}

        data2 = self.data[self.column_name]

        for elements in data2.keys():
            if elements in self.emo_db:
                keep_dic[elements] = data2[elements]
            elif elements == self.Object_of_Study:
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
                                pass
                        except Exception:
                            keep_dic[elements] = data2[elements]
        if self.remove_all:
            self.data = new_dic
            self.filtered = pd.DataFrame.from_dict(new_dic)
        else:
            if self.show_removed:
                print(self.removed)
            return pd.DataFrame.from_dict(new_dic)

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
        options_my_class_1 = dict(remove_at={False: '()'}, remove_link={False: '()'}, remove_ponc={False: '()'},
                                  remove_laugh={False: '()'}, remove_word_sts={False: '()'},
                                  remove_num_str={False: '()'})
        self.remove_all = True
        for item in list_o:
            try:
                if options_my_class[item] != options_my_class_1[item]:
                    options_my_class_1[item] = options_my_class[item]
                else:
                    pass
            except Exception:
                pass
        for choice in list_o:
            choice_tf = list(options_my_class_1[choice].keys())
            if choice_tf[0]:
                getting_pos = list_o.index(choice)
                choice_ff = list(options_my_class_1[choice].values())
                eval(list_f[getting_pos] + str(choice_ff[0]))
            else:
                pass
        if self.show_removed:
            print(self.removed)
        return self.filtered


print('''Classes_funcoes é uma mini biblioteca feita para um projeto de Ciência de Dados com a principal função de
deixar mais fácil a interação entre a biblioteca pandas e a biblioteca emoji (esse era o intuito pelo
menos mas acabamos fazendo uma biblioteca para o projeto inteiro). Além das biblioteca citadas anteriormente,
ela requer as bibliotecas numpy, operator, functools e string. Quase certeza que todas estão disponíveis com pip
install''')

'''MUITO IMPORTANTE!!! COMO EU TIVE USAR ALGUMAS NOTAÇÕES INESPERADAS NESSE TRABALHO RESOLVI COLOCAR AQUI, ALÉM DO
NOTEBOOK PRINCIPAL (QUE ESTÁ AQUI PARA FACILITAR OS TESTES DO CÓDIGO), OS SCRATCHES CRIADOS DURANTE ESTE PROJETO.
PARA QUE ESTES SCRATCHES N FOSSEM EXECUTADOS JUNTO COM O RESTO DO SCRIPT COLOQUEI ELES DENTRO DE UM TRY QUE SEMPRE DA
ERRO E A COPIA DO NOTEBOOK QUE EU ESTAVA USANDO AQUI PARA TESTAR O CÓDIGO DENTRO DE UM EXCEPT EXCEPTION. TALL QUE:'''

'''
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
    try:
        int('a')

        class Car:
            """
              blueprint for car
            """
            global TESTES_CLASSES_CARROS1
            global TESTES_CLASSES_CARROS
            TESTES_CLASSES_CARROS = 1

            def __init__(self, model, color, company, speed_limit):
                self.color = color
                self.company = company
                self.speed_limit = speed_limit
                self.model = model
                print(TESTES_CLASSES_CARROS)

            def start(self):
                print("started")
                print(TESTES_CLASSES_CARROS)

            def stop(self):
                print("stopped")
                maruthi_suzuki1 = Car("ertiga", "black", "suzuki", 60)
                TESTES_CLASSES_CARROS1 = maruthi_suzuki1.accelarate()

            def accelarate(self):
                print("accelarating...")

                "accelarator functionality here"

            def change_gear(self, gear_type):
                print("gear changed")
                " gear related functionality here"

        maruthi_suzuki = Car("ertiga", "black", "suzuki", 60)
        maruthi_suzuki.stop()
        print(TESTES_CLASSES_CARROS)

        class Foo:
            def __init__(self, x, y):
                self.x = y
                self.y = x

            def do_this(self):
                print(self.x, self.y)
                # TESTES_CLASSES_CARROS
                pass

            def do_that(self):
                print(self.y, self.x)
                pass

            def __call__(self):
                print("hi")
                self.do_this()
                self.do_that()

        print()
        foo = Foo(1, 2)
        print()
        foo()
        print("hihi")
        foo.do_this()
        qw = '@eorithj'
        print(qw.split('@'))

        import string
        print(type(string.punctuation))
        print(string.punctuation)
        print(list(string.punctuation))
        s = 'abc12321cba'
        print(type(int(s[6])))
        print(s.replace('a', ''))

        class C(object):
            @property
            def x(self):
                "I am the 'x' property."
                print(1)
                return self._x

            @x.setter
            def x(self, value):
                print(2)
                self._x = value

            @x.deleter
            def x(self):
                print(3)
                del self._x

        w = C
        print(w.x)

        # (copied from class doc)

        def self_remove_at():
            print('@')

        def self_remove_link():
            print('http')

        def self_remove_ponc():
            print('ponc')

        def self_remove_word_st3():
            print('word')

        def self_remove_laugh():
            print('haha')

        def self_remove_num_str():
            print('str')

        def func(**options_my_class):
            lista = ['remove_at', 'remove_link', 'remove_ponc', 'remove_word_st3', 'remove_laugh', 'remove_num_str']
            lista_f = ['{self_remove_at()}', '{self_remove_link()}', '{self_remove_ponc()}',
                       '{self_remove_word_st3()}', '{self_remove_laugh()}', '{self_remove_num_str()}']
            options_my_class_1 = dict(remove_at=False, remove_link=False, remove_ponc=False, remove_word_st3=False,
                                      remove_laugh=False, remove_num_str=False)
            for i in lista:
                try:
                    if options_my_class[i] != options_my_class_1[i]:
                        options_my_class_1[i] = options_my_class[i]
                    else:
                        pass
                except Exception:
                    pass
            for choice in lista:
                if options_my_class_1[choice] == False:
                    pass
                else:
                    getting_pos = lista.index(choice)
                    eval(lista_f[getting_pos])

        func(remove_link=True, remove_at=False, remove_ponc=True, remove_word_st3=True, remove_laugh=True,
             remove_num_str=False)

        f'{self_remove_at()}'

        r = 'ófidg111111sdfghjo'

        for i in range(0, len(r)):
            k = 3
            k += i
            if k <= len(r):
                qwert = r[i:k]
                try:
                    if int(qwert):
                        print(qwert)
                except Exception:
                    print(1)

        d = {}
        set_d = d
        print(type(set_d))

        import string
        s = 'abc12321cba!@#$%^&*()_+{}":>?<'
        s1 = 'abc12321cba!@#$%^&*()_+{}":>?<'

        # print(s.replace(list(string.punctuation), ''))
        s1 = [s1.replace(j, '') for j in string.punctuation if s1 not in list(string.punctuation)]
        for j in string.punctuation:
            print(j)
            if j in s:
                s = s.replace(j, '')
        print(s)
        print(s1)

        print(dict(remove_at={False: '()'}, remove_link={False: '()'}, remove_ponc={False: '()'},
                   remove_laugh={False: '()'},
                   remove_word_sts={False: '()'}, remove_num_str={False: '()'}))

        def self_remove_at():
            print(type('@'), '@')

        def self_remove_link():
            print(type('http'), 'http')

        def self_remove_ponc(x):
            print(type(x), x)

        def self_remove_word_sts(x):
            print(type(x), x)

        def self_remove_laugh(x, y):
            print(type(x), type(y), x, y)

        def self_remove_num_str(x):
            print(type(x), x)

        def func(**options_my_class):
            list_o = ['remove_at', 'remove_link', 'remove_ponc', 'remove_word_sts', 'remove_laugh',
                      'remove_num_str']
            list_f = ['self_remove_at', 'self_remove_link', 'self_remove_ponc', 'self_remove_word_sts',
                      'self_remove_laugh',
                      'self_remove_num_str']
            options_my_class_1 = dict(remove_at={False: '()'}, remove_link={False: '()'}, remove_ponc={False: '()'},
                                      remove_laugh={False: '()'}, remove_word_sts={False: '()'},
                                      remove_num_str={False: '()'})
            for i in list_o:
                try:
                    if options_my_class[i] != options_my_class_1[i]:
                        options_my_class_1[i] = options_my_class[i]
                    else:
                        pass
                except Exception:
                    pass
            for choice in list_o:
                # print(list(options_my_class_1[choice].keys()))
                choice_tf = list(options_my_class_1[choice].keys())
                print(choice_tf)
                if choice_tf[0]:
                    # print(list(options_my_class_1[choice].values()), 1)
                    print(options_my_class_1[choice].values())
                    getting_pos = list_o.index(choice)
                    choice_ff = list(options_my_class_1[choice].values())
                    print(choice_ff[0], "choice_ff[0]")
                    print(list_f[getting_pos] + str(choice_ff[0]))
                    eval(list_f[getting_pos] + str(choice_ff[0]))
                else:
                    print(choice_tf[0], 2)
                    pass

        func(remove_at={False: '()'}, remove_link={True: '()'}, remove_ponc={True: '("ponc")'},
             remove_laugh={True: '(3, 4)'}, remove_word_sts={True: '(3)'}, remove_num_str={True: '(3)'})
        length_k = 4
        elements = 'siklauyfhkkkkkkkkkkkkkkkkoilueag'
        stringk = ""
        if 'k' * length_k in elements:
            list_wk = list(elements)
            for khas in list_wk:
                if khas != "k":
                    stringk += khas
            if len(stringk) > 0:
                pass

            print(f"""
            {elements}
            {list_wk}
            {stringk}""")
        print(elements)
        sdd = "hkkkkkkkkkkkkkkkk"
        print(elements)

        def bar():
            global variable
            variable = 'whatever'

        def foo():
            print(variable)

        bar()
        foo()
        import numpy as np
        import pandas as pd

        dados_treino_1 = pd.read_excel('ps5.xlsx')
        dados_treino_1['Treinamento'][1]
        import emoji
        import emojis

        lista_emo = []
        lista_emo1 = []
        lista_emo_split = []
        lista_emo1_split = []
        for i in np.arange(0, len(dados_treino_1)):
            lista_emo.append(
                ''.join(j for j in dados_treino_1['Treinamento'][i] if j in emojis.db.get_emoji_aliases().values()))
            lista_emo1.append(''.join(j for j in dados_treino_1['Treinamento'][i] if j in emoji.UNICODE_EMOJI['en']))

            if '' in lista_emo:
                lista_emo.remove('')
            if '' in lista_emo1:
                lista_emo1.remove('')

        print(lista_emo)
        print(lista_emo1)
        for i in lista_emo:
            lista_emo_s = list(i)
            for j in lista_emo_s:
                lista_emo_split.append(j)
        for i in lista_emo1:
            lista_emo1_s = list(i)
            for j in lista_emo1_s:
                lista_emo1_split.append(j)
        print(f'''lista_emo_split, {lista_emo_split}
        lista_emo_split, {len(lista_emo_split)}
        lista_emo1_split, {lista_emo1_split}
        lista_emo1_split, {len(lista_emo1_split)}
        len(lista_diff), {len(lista_emo1_split) - len(lista_emo_split)}''')

        # print(emoji.UNICODE_EMOJI['en'])
        # print(len(emoji.UNICODE_EMOJI['en']))

        # for 🥇 in emoji.UNICODE_EMOJI['en']:
        #     print(1)
        print(1)
        print(''.join(j for j in lista_emo1_split if j in emoji.UNICODE_EMOJI['en'].keys()))
        # if True:
        #     dados_treino = pd.read_excel('ps5.xlsx')
        #     pd.reset_option("display")
        #
        #     p = ListWord(column_name='Treinamento').c_o_f(dados_treino)
        #     p.sort_values(by='# de ocorrências', ascending=False)
        #
        #     mn = RemoveWords(p, '# de ocorrências')
        #
        #     qremove_link = mn.remove_link()
        #     qremove_at = mn.remove_at()
        #     qremove_ponc = mn.remove_ponc()
        #     qremove_word_st3 = mn.remove_word_st3()
        #     qremove_laugh = mn.remove_laugh()
        #     qremove_num_str = mn.remove_num_str()
        #     qremove_options = mn.remove_options(remove_link=True, remove_at=True,
        #                                         remove_ponc=True, remove_word_st3=True,
        #                                         remove_laugh=True, remove_num_str=True)
        #
        #     print(type(mn))
        #
        #     mn
        #     print(qremove_options['# de ocorrências'][Object_of_Study], qremove_num_str['# de ocorrências'][Object_of_Study])
        #
        #     print(f"""{qremove_link['# de ocorrências'][Object_of_Study]} qremove_link
        #     {qremove_at['# de ocorrências'][Object_of_Study]} qremove_at
        #     {qremove_ponc['# de ocorrências'][Object_of_Study]} qremove_ponc
        #     {qremove_word_st3['# de ocorrências'][Object_of_Study]} qremove_word_st3
        #     {qremove_laugh['# de ocorrências'][Object_of_Study]} qremove_laugh
        #     {qremove_num_str['# de ocorrências'][Object_of_Study]} qremove_num_str""")
        #
        #     qremove_options_1 = qremove_options.sort_values(by='# de ocorrências', ascending=False)
        #     qremove_options_1 = qremove_options_1.loc[qremove_options_1['# de ocorrências'] > 100]
        #     qremove_options_1

        # print()

        # print('''Classes_funcoes é uma mini biblioteca feita para um projeto de Ciência de Dados com a principal função de
        # deixar mais fácil a interação entre a biblioteca pandas e as bibliotecas emoji e emojis (esse era o intuito pelo
        # menos mas acabamos fazendo uma biblioteca para o projeto inteiro). Além das biblioteca citadas anteriormente,
        # ela requer as bibliotecas numpy, operator, functools e string. Quase certeza que todas estão disponíveis com pip
        # install''')
        # w = ['👍', '🙈', '🤡', '😕', '😱', '👍', '✅', '🤷', '♂️', '😂', '😱', '😂', '👏', '🤙', '😎', '😱', '🤰', '💣', '🤣',
        #      '❤️', '🤤', '😥', '❤️', '😉', '☺️', '😂', '🙏', '💰', '🙂', '😝', '😂', '😹', '🤡', '🤣', '😎', '😉', '👍', '🤝',
        #      '😏', '🥺', '🎮', '😏', '⚙️', '😢', '😂', '😭', '😐', '🥺', '😥', '😭', '😔', '🎊', '🎉', '😭', 'we', 'ahem',
        #      'ruim', 'de', 'usar', 'não', 'perde', 'no', 'nem', 'tem', 'isso', 'também', 'posso', 'falar', 'como', 'imagino',
        #      'não', 'sei', 'estado', 'namo', 'com', 'seu', 'que', 'é', 'meu', 'tb', 'golpe', 'ou', 'golpe', 'gosta', 'de',
        #      'não', 'quer', 'me', 'dar', 'seu', 'tlvz', 'quando', 'sair', 'o', 'trailer', 'do', 'novo', 'vai', 'crescer', 'a',
        #      'procura', 'pelo', 'eu', 'comecei', 'jogar', 'yakuza', 'no', 'meu', 'antigo', 'one', 's', 'e', 'achei', 'mto',
        #      'comprei', 'o', 'e', 'tô', 'jogando', 'prey', 'q', 'tem', 'no', 'yakuza', 'like', 'a', 'dragon', 'monster',
        #      'hunter', 'world', 'tbem', 'tem', 'no', 'haahhaha', 'n', 'posso', 'negar', 'que', 'tô', 'loco', 'pra', 'pegar',
        #      'o', 'séries', 'x', 'esse', 'ae', 'tá', 'meio', 'tá', 'certo', 'isso', 'tampa', 'a', 'beleza', 'do', 'vai',
        #      'fazer', 'ano', 'que', 'o', 'foi', 'procura', 'ai', 'nas', 'o', 'preço', 'tem', 'aaa', 'então', 'procura', 'nas',
        #      'casas', 'lá', 'é', 'também', 'n', 'tem', 'magazine', 'bota', 'também', 'pra', 'comprar', 'um', 'tem', 'que',
        #      'importar', 'como', 'é', 'bom', 'viver', 'n', 'sei', 'pq', 'reclamo', 'dungeons', 'dark', 'alliance', 'será',
        #      'lançado', 'em', 'de', 'junho', 'para', 'e', 'trailer', 'e', 'gameplay', 'todas', 'as', 'respostas', 'agora', 'é',
        #      'da', 'apple', 'é', 'que', 'quero', 'é', 'amd', 'é', 'blablabla', 'os', 'a', 'minha', 'estratégia', 'é', 'a',
        #      'xbox', 'e', 'switch', 'já', 'adiei', 'pra', 'uns', 'anos', 'quando', 'os', 'exclusivos', 'de', 'reais',
        #      'custarão', 'uns', 'em', 'ai', 'nintendo', 'já', 'conhecemos', 'por', 'não', 'baixar', 'os', 'mas', 'com',
        #      'playstation', 'dá', 'pra', 'comprar', 'depois', 'mas', 'eu', 'so', 'dei', 'um', 'pro', 'nat', 'e', 'sou',
        #      'carinhosa', 'com', 'o', 'kai', 'o', 'aoyama', 'nem', 'aparece', 'ele', 'nao', 'gosta', 'do', 'meu', 'amor',
        #      'comprou', 'qria', 'jogar', 'a', 'continuação', 'de', 'pau', 'na', 'sua', 'bunda', 'comprou', 'qria', 'jogar', 'a',
        #      'continuação', 'de', 'pau', 'na', 'seu', 'cú', 'comprou', 'qria', 'jogar', 'a', 'continuação', 'de', 'elder',
        #      'pau', 'no', 'seu', 'rabo', 'comprou', 'qria', 'jogar', 'a', 'continuação', 'de', 'pau', 'no', 'seu', 'ânus',
        #      'acho', 'q', 'vem', 'caio', 'gamer', 'aí', 'só', 'falta', 'ganhar', 'um', 'kkkk', 'teoricamente', 'eu', 'tenho',
        #      'os', 'dois', 'em', 'xbox', 'one', 'no', 'então', 'no', 'futuro', 'pretendo', 'ter', 'os', 'dois', 'mas', 'não',
        #      'faço', 'questão', 'de', 'ter', 'o', 'tão', 'cedo', 'rim', 'tá', 'valendo', 'mil', 'vale', 'imagina', 'quantos',
        #      'dá', 'pra', 'comprar', 'perdeu', 'as', 'principais', 'novidades', 'de', 'não', 'se', 'traz', 'as', 'notícias',
        #      'que', 'você', 'precisa', 'saber', 'no', 'primeiro', 'episódio', 'do', 'gen', 'a', 'avaliar', 'o', 'dualsense',
        #      'antes', 'de', 'se', 'gladiarem', 'nas', 'quatro', 'limpando', 'o', 'setup', 'pessoa', 'q', 'presta', 'a', 'gente',
        #      'já', 'sabe', 'que', 'não', 'tvlz', 'uma', 'acho', 'q', 'vou', 'assinar', 'pelo', 'se', 'eu', 'conseguir', 'zerar',
        #      'os', 'jogos', 'q', 'peguei', 'no', 'foda', 'ficar', 'assinando', 'e', 'comprando', 'jogo', 'sem', 'precisar',
        #      'ou', 'ter', 'tempo', 'kkkkk', 'no', 'caso', 'esse', 'é', 'um', 'problema', 'bom', 'queria', 'streamar', 'mas',
        #      'queria', 'streamar', 'a', 'existe', 'alguma', 'maneira', 'sem', 'ser', 'com', 'placa', 'de', 'captura', 'de', 'o',
        #      'fazer', 'e', 'ter', 'na', 'mesma', 'os', 'overlays', 'do', 'streamlabs', 'a', 'chegada', 'de', 'mais', 'stock',
        #      'da', 'está', 'a', 'ajudar', 'a', 'vender', 'mais', 'jogos', 'fui', 'ver', 'esse', 'vídeo', 'e', 'consegue', 'ser',
        #      'mais', 'vergonhoso', 'que', 'só', 'esse', 'corte', 'a', 'notícia', 'é', 'bate', 'recorde', 'nos', 'de', 'lol',
        #      'e', 'nem', 'é', 'um', 'dado', 'da', 'estimativa', 'furada', 'de', 'analista', 'pago', 'ainda', 'soltou', 'um',
        #      'no', 'final', 'se', 'me', 'lembro', 'bem', 'a', 'digital', 'fraude', 'quando', 'recebeu', 'o', 'john', 'linneman',
        #      'e', 'o', 'outro', 'lá', 'falaram', 'que', 'não', 'veio', 'o', 'cabo', 'passado', 'alguns', 'dias', 'eles',
        #      'afirmaram', 'que', 'era', 'o', 'posso', 'estar', 'errado', 'vocês', 'conseguem', 'imaginar', 'o', 'barulho',
        #      'dos', 'verificados', 'e', 'nas', 'redações', 'se', 'tudo', 'isso', 'que', 'ta', 'acontecendo', 'com', 'a',
        #      'marca', 'xbox', 'estivesse', 'acontecendo', 'com', 'a', 'fazendo', 'uma', 'inversão', 'dos', 'aquisição', 'da',
        #      'bethesda', 'pela', 'sony', 'jogos', 'lançamento', 'chegando', 'na', 'psnow', 'mais', 'poderoso', 'joel', 'não',
        #      'era', 'pra', 'você', 'ter', 'vendido', 'o', 'cérebro', 'pra', 'comprar', 'nossa', 'sim', 'cargas', 'fizeste',
        #      'sem', 'por', 'venha', 'aqui', 'vota', 'no', 'os', 'lançamentos', 'de', 'games', 'mais', 'aguardados', 'da',
        #      'terceira', 'semana', 'de', 'março', 'de', 'para', 'xbox', 'xbox', 'series', 'nintendo', 'pc', 'e', 'eu', 'queria',
        #      'mesmo', 'o', 'mas', 'já', 'valeu', 'o', 'a', 'patroa', 'ninguém', 'liga', 'se', 'seu', 'pai', 'vai', 'te', 'dar',
        #      'quatro', 'quarenta', 'celulares', 'e', 'noventa', 'tênis', 'que', 'custam', 'dois', 'mil', 'ninguém', 'liga',
        #      'mesmo', 'é', 'um', 'que', 'eu', 'nunca', 'passaria', 'pra', 'comprem', 'um', 'para', 'a', 'day', 'jogar', 'fifa',
        #      'ogo', 'foi', 'lançado', 'dia', 'no', 'mas', 'nem', 'todo', 'mundo', 'conseguiu', 'baixar', 'as', 'melhorias',
        #      'aqui', 'vemos', 'um', 'ele', 'e', 'joão', 'félix', 'joga', 'para', 'descobrir', 'as', 'capacidades', 'do', 'e',
        #      'se', 'sabe', 'jogar', 'unidades', 'câmera', 'hd', 'para', 'sony', 'demon', 'souls', 'no', 'ta', 'bonito', 'quero',
        #      'jogar', 'ligo', 'meu', 'e', 'atualizou', 'em', 'minutos', 'kkkkkk', 'eu', 'comprei', 'na', 'uma', 'steelbook',
        #      'paguei', 'tentei', 'jogar', 'o', 'jogo', 'na', 'primeira', 'semana', 'de', 'lançamento', 'no', 'sem', 'devolvi',
        #      'e', 'agora', 'depois', 'que', 'tiver', 'certeza', 'que', 'o', 'jogo', 'está', 'em', 'perfeitas', 'eu', 'vou',
        #      'comprar', 'de', 'a', 'psn', 'seria', 'o', 'termômetro', 'se', 'o', 'jogo', 'está', 'ok', 'sem', 'nenhuma',
        #      'perspectiva', 'de', 'comprar', 'um', 'o', 'jeito', 'é', 'jogar', 'pelo', 'acho', 'que', 'vou', 'começar', 'com',
        #      'bloodborne', 'pensando', 'seriamente', 'em', 'começar', 'a', 'juntar', 'dinheiro', 'pra', 'comprar', 'um',
        #      'tomara', 'que', 'a', 'sony', 'lance', 'um', 'com', 'tb', 'ainda', 'vais', 'a', 'tempo', 'de', 'aproveitar',
        #      'descontos', 'imperdíveis', 'numa', 'grande', 'coleção', 'de', 'jogos', 'para', 'a', 'e', 'com', 'a', 'promoção',
        #      'de', 'escolhas', 'disponível', 'na', 'ps', 'rt', 'para', 'trailer', 'de', 'dungeons', 'dark', 'acaba', 'de',
        #      'sair', 'e', 'nos', 'sua', 'gameplay', 'e', 'suas', 'jogo', 'grátis', 'no', 'e', 'por', 'tempo', 'limitado', 'que',
        #      'bizarro', 'pq', 'n', 'compra', 'logo', 'o', 'attack', 'on', 'titan', 'final', 'battle', 'já', 'está', 'o', 'jogo',
        #      'irá', 'contar', 'a', 'história', 'do', 'anime', 'da', 'primeira', 'até', 'a', 'terceira', 'confira', 'o', 'do',
        #      'para', 'essa', 'nova', 'geração', 'do', 'cê', 'acha', 'que', 'faz', 'mais', 'sentido', 'termos', 'de', 'cash',
        #      'mesmo', 'comprar', 'esse', 'ou', 'montar', 'um', 'pc', 'com', 'configurações', 'só', 'queria', 'uma', 'ganha',
        #      'nova', 'gameplay', 'mostrando', 'casa', 'com', 'interior', 'explorável', 'lembrando', 'que', 'o', 'game',
        #      'continua', 'sendo', 'está', 'em', 'no', 'está', 'previsto', 'para', 'ser', 'lançado', 'para', 'xbox', 'series',
        #      'xbox', 'pc', 'e', 'nintendo', 'eu', 'acho', 'que', 'não', 'supera', 'o', 'gow', 'mas', 'espero', 'que', 'eu',
        #      'esteja', 'eu', 'queria', 'muito', 'comprar', 'o', 'antes', 'do', 'lançamento', 'de', 'gow', 'por', 'isso',
        #      'quanto', 'mais', 'vem', 'um', 'só', 'pode', 'trust', 'apresenta', 'os', 'auscultadores', 'gxt', 'compatíveis',
        #      'com', 'e', 'pc', 'motivos', 'para', 'comprar', 'um', 'até', 'o', 'agora', 'o', 'negócio', 'é', 'comprar', 'um',
        #      'pra', 'jogar', 'a', 'parte', 'pq', 'não', 'vai', 'sair', 'pro', 'caralho', 'eu', 'não', 'sabia', 'que', 'isso',
        #      'ocorre', 'no', 'tbm', 'o', 'comercial', 'todo', 'dia', 'da', 'aparecendo', 'eu', 'sou', 'pobre', 'playstation',
        #      'para', 'de', 'me', 'dar', 'gatilho', 'queria', 'poder', 'fechar', 'o', 'jogo', 'no', 'da', 'sala', 'e',
        #      'continuar', 'no', 'mesmo', 'save', 'quando', 'fosse', 'jogar', 'no', 'do', 'quarto', 'é', 'só', 'juntar', 'a',
        #      'porra', 'do', 'e', 'xbox', 'series', 'x', 'com', 'os', 'pc', 'o', 'motivo', 'pode', 'ser', 'o', 'porém', 'a',
        #      'sony', 'é', 'detentora', 'da', 'ip', 'logo', 'poderia', 'já', 'ter', 'feito', 'o', 'patch', 'de',
        #      'diferentemente', 'de', 'dark', 'que', 'é', 'de', 'uma', 'empresa', 'terceira', 'o', 'mesmo', 'roda', 'a', 'no',
        #      'pq', 'tem', 'o', 'fps', 'e', 'pode', 'receber', 'o', 'fps', 'boost', 'burlando', 'o', 'problema', 'o', 'camp',
        #      'salve', 'era', 'plataforma', 'e', 'tinha', 'pensando', 'na', 'minha', 'xicara', 'do', 'q', 'não', 'vou', 'dark',
        #      'alliance', 'novo', 'jogo', 'de', 'rpg', 'ambientado', 'no', 'mundo', 'de', 'dungeons', 'dragons', 'é',
        #      'finalmente', 'é', 'chega', 'em', 'de', 'junho', 'para', 'xbox', 'one', 'e', 'series', 'e', 'pc', 'já', 'estive',
        #      'mais', 'longe', 'de', 'comprar', 'uma', 'xbox', 'series', 's', 'em', 'vez', 'de', 'uma', 'mas', 'ffxvi', 'é',
        #      'mas', 'tão', 'que', 'não', 'dá', 'para', 'esperar', 'eu', 'falo', 'não', 'por', 'ser', 'pois', 'eu', 'não',
        #      'falo', 'assim', 'porque', 'estou', 'louco', 'pra', 'pegar', 'series', 'e', 'ainda', 'não', 'tem', 'um', 'sentido',
        #      'pra', 'em', 'quando', 'eu', 'peguei', 'meu', 'eu', 'ja', 'trago', 'junto', 'com', 'ele', 'breath', 'of', 'de',
        #      'olha', 'o', 'ou', 'ne', 'vai', 'ver', 'vc', 'eh', 'rico', 'vem', 'a', 'primeira', 'parcela', 'do', 'ksks',
        #      'vamos', 'aos', 'fatos', 'por', 'volta', 'de', 'meses', 'de', 'dá', 'para', 'comprar', 'jogo', 'de', 'lançamento',
        #      'de', 'com', 'preço', 'full', 'meses', 'de', 'é', 'o', 'custo', 'de', 'jogo', 'de', 'lançamento', 'do', 'nintendo',
        #      'switch', 'é', 'por', 'isso', 'que', 'os', 'sonystas', 'estão', 'desesperados', 'o', 'cara', 'tava', 'vendendo',
        #      'o', 'a', 'conto', 'eu', 'perguntei', 'pra', 'ele', 'por', 'que', 'o', 'preço', 'tava', 'tão', 'acima', 'do',
        #      'ele', 'colocou', 'a', 'culpa', 'no', 'o', 'dólar', 'tá', 'reais', 'e', 'eu', 'não', 'acho', 'que', 'é', 'pq',
        #      'vai', 'sair', 'a', 'versão', 'de', 'que', 'é', 'cara', 'e', 'não', 'atualiza', 'grátis', 'pra', 'quem', 'pegou',
        #      'na', 'eu', 'tenho', 'ele', 'comprado', 'só', 'que', 'não', 'tinha', 'jogado', 'tô', 'jogando', 'pelo', 'hype',
        #      'da', 'nem', 'dá', 'é', 'gente', 'do', 'flame', 'a', 'única', 'coisa', 'que', 'acho', 'que', 'pode', 'acontecer',
        #      'pra', 'sair', 'esse', 'é', 'a', 'sony', 'querer', 'fazer', 'um', 'remaster', 'desse', 'game', 'pro', 'e', 'tbm',
        #      'uma', 'versão', 'de', 'pc', 'o', 'ta', 'acho', 'que', 'parcelado', 'de', 'nem', 'sinto', 'tanto', 'cara',
        #      'quando', 'vc', 'pegar', 'o', 'por', 'favor', 'jogue', 'pq', 'você', 'vai', 'sentir', 'aquela', 'nostalgia', 'boa',
        #      'e', 'ainda', 'ter', 'uma', 'experiência', 'de', 'nova', 'o', 'tratamento', 'que', 'deram', 'no', 'jogo', 'ficou',
        #      'tv', 'e', 'youtube', 'me', 'torturavam', 'com', 'propagadans', 'incessantes', 'do', 'agora', 'é', 'toda', 'hora',
        #      'falando', 'de', 'o', 'dia', 'mal', 'começou', 'e', 'a', 'pauta', 'já', 'conta', 'novidades', 'do', 'game', 'pass',
        #      'vídeo', 'de', 'divulgação', 'dos', 'jogos', 'do', 'possível', 'game', 'japonês', 'exclusivo', 'da', 'playstation',
        #      'ea', 'play', 'chegando', 'no', 'game', 'pass', 'do', 'pc', 'logo', 'logo', 'agora', 'é', 'só', 'esperar', 'o',
        #      'resto', 'do', 'dia', 'pra', 'ver', 'o', 'que', 'mais', 'pode', 'surgir', 'mano', 'se', 'no', 'celular', 'já', 'é',
        #      'bonito', 'imagine', 'num', 'num', 'xbox', 'series', 'x', 'evento', 'de', 'inicio', 'de', 'temporada', 'de',
        #      'fortnite', 'cap', 'tô', 'doido', 'por', 'uma', 'tv', 'nova', 'e', 'um', 'pra', 'me', 'alienar', 'acho', 'que',
        #      'a', 'sony', 'tinha', 'que', 'adaptar', 'o', 'pra', 'esse', 'design', 'estou', 'com', 'a', 'impressão', 'que', 'o',
        #      'conteúdo', 'de', 'na', 'internet', 'se', 'resume', 'a', 'a', 'até', 'o', 'momento', 'obrigado', 'fazia', 'tempo',
        #      'que', 'eu', 'estava', 'carente', 'de', 'um', 'rpg', 'com', 'classes', 'possibilidades', 'de', 'um', 'farmizinho',
        #      'de', 'aventuras', 'em', 'lugares', 'e', 'você', 'foi', 'exatamente', 'o', 'que', 'eu', 'precisava', 'jogar', 'na',
        #      'hora', 'amando', 'esse', 'jogo', 'rt', 'diversos', 'jogos', 'de', 'e', 'estão', 'em', 'promoção', 'na', 'acho',
        #      'bonitinho', 'a', 'sony', 'me', 'mandando', 'sobre', 'o', 'como', 'se', 'professora', 'brasileira', 'tivesse',
        #      'dinheiro', 'pra', 'tal', 'eu', 'não', 'consigo', 'trocar', 'nem', 'meu', 'notebook', 'pra', 'poder', 'trabalhar',
        #      'direitinho', 'não', 'deixou', 'né', 'outriders', 'para', 'e', 'data', 'de', 'jogabilidade', 'e', 'tudo', 'que',
        #      'você', 'precisa', 'saber', 'eu', 'quando', 'comprar', 'meu', 'playstation', 'me', 'da', 'um', 'de', 'se',
        #      'tivesse', 'ficado', 'em', 'casa', 'o', 'dinheiro', 'da', 'multa', 'comprava', 'rt', 'attack', 'on', 'titan',
        #      'final', 'battle', 'já', 'está', 'o', 'jogo', 'irá', 'contar', 'a', 'história', 'do', 'anime', 'da', 'primeira',
        #      'até', 'a', 'terceira', 'amigo', 'esse', 'jogo', 'tá', 'ficando', 'bom', 'eu', 'tentei', 'ano', 'passado',
        #      'fazendo', 'força', 'mas', 'desisti', 'pq', 'ainda', 'tava', 'todo', 'mas', 'tô', 'pensando', 'em', 'voltar',
        #      'quando', 'lançar', 'o', 'de', 'se', 'vier', 'um', 'eu', 'se', 'não', 'nem', 'o', 'pai', 'me', 'da', 'ai',
        #      'gringa', 'compra', 'um', 'pra', 'day', 'jogar', 'tá', 'me', 'dando', 'dor', 'de', 'cabeça', 'ja', 'pra', 'compra',
        #      'um', 'logo', 'mano', 'akjsajk', 'meu', 'amigo', 'disse', 'q', 'é', 'quase', 'o', 'preço', 'de', 'um', 'e', 'eu',
        #      'real', 'n', 'sei', 'oq', 'valeria', 'mais', 'diga', 'o', 'que', 'você', 'tem', 'a', 'em', 'todos', 'os',
        #      'idiomas', 'que', 'vem', 'pra', 'novas', 'matrículas', 'até', 'participarão', 'do', 'sorteio', 'de', 'um',
        #      'playstation', 'só', 'falei', 'do', 'mod', 'pra', 'dizer', 'que', 'o', 'jogo', 'suporta', 'mais', 'frames',
        #      'tranquilamente', 'sem', 'bugar', 'ou', 'quebrar', 'animação', 'já', 'tá', 'ali', 'prontinho', 'pra', 'fazer', 'é',
        #      'só', 'a', 'sony', 'mas', 'é', 'capaz', 'de', 'acontecer', 'o', 'que', 'você', 'falou', 'mesmo', 'remaster', 'no',
        #      'e', 'pc', 'está', 'muito', 'mas', 'muitíssimo', 'espero', 'que', 'eles', 'estejam', 'fazendo', 'isso', 'pra',
        #      'tentar', 'gerar', 'porque', 'a', 'sony', 'não', 'está', 'me', 'agradando', 'muito', 'do', 'jeito', 'que',
        #      'peguei', 'o', 'por', 'conta', 'dos', 'meus', 'jogos', 'mas', 'também', 'quero', 'jogar', 'mas', 'a', 'dona',
        #      'sony', 'bom', 'não', 'sei', 'do', 'em', 'mas', 'geralmente', 'esse', 'tipo', 'de', 'material', 'vem', 'aberto',
        #      'nas', 'ele', 'usou', 'pra', 'pelo', 'menos', 'espero', 'que', 'tenha', 'sido', 'ou', 'ele', 'é', 'burro',
        #      'imaginem', 'entrar', 'num', 'sorteio', 'para', 'poder', 'comprar', 'uma', 'para', 'trailer', 'de', 'dungeons',
        #      'dark', 'acaba', 'de', 'sair', 'e', 'nos', 'sua', 'gameplay', 'e', 'suas', 'ela', 'só', 'esqueceu', 'de', 'avisar',
        #      'que', 'a', 'sony', 'nao', 'esta', 'lucrando', 'com', 'o', 'a', 'cada', 'vendido', 'é', 'um', 'gxt', 'carus',
        #      'são', 'os', 'novos', 'auscultadores', 'da', 'compatíveis', 'com', 'e', 'pc', 'rt', 'tô', 'doido', 'por', 'uma',
        #      'tv', 'nova', 'e', 'um', 'pra', 'me', 'alienar', 'eu', 'não', 'sou', 'a', 'favor', 'de', 'de', 'bens', 'materiais',
        #      'pq', 'o', 'infinito', 'e', 'o', 'universo', 'ele', 'o', 'espírito', 'piriri', 'mas', 'eu', 'acho', 'que', 'vale',
        #      'mais', 'a', 'pena', 'um', 'console', 'na', 'mão', 'de', 'quem', 'vai', 'usar', 'do', 'que', 'se', 'eu', 'ainda',
        #      'tivesse', 'meu', 'eu', 'teria', 'passado', 'ele', 'num', 'preço', 'acessível', 'pra', 'pegar', 'achei', 'q', 'os',
        #      'preços', 'dos', 'acessórios', 'do', 'seriam', 'mais', 'baixos', 'depois', 'do', 'lançamento', 'do', 'mas', 'um',
        #      'controle', 'de', 'tá', 'reais', 'mais', 'caro', 'do', 'que', 'paguei', 'em', 'ai', 'é', 'só', 'a', 'água',
        #      'bater', 'no', 'bumbum', 'que', 'vcs', 'até', 'se', 'num', 'que', 'eu', 'queria', 'experimentar', 'o', 'adaptive',
        #      'trigger', 'do', 'dizem', 'que', 'em', 'jogo', 'de', 'vc', 'sento', 'o', 'do', 'gatilho', 'rt', 'mais', 'um',
        #      'sorteio', 'meu', 'para', 'estou', 'sorteando', 'e', 'veja', 'como', 'movimentação', 'é', 'que', 'segue',
        #      'vendendo', 'fora', 'os', 'vários', 'jogos', 'a', 'no', 'e', 'caindo', 'pra', 'no', 'series', 'os', 'caras', 'são',
        #      'muito', 'ué', 'kkkk', 'quando', 'mostram', 'dados', 'que', 'o', 'está', 'superior', 'em', 'jogo', 'x', 'vocês',
        #      'se', 'recusam', 'a', 'acreditar', 'também', 'kkkkkkkkk', 'legal', 'que', 'vc', 'se', 'acha', 'depressivo',
        #      'kkkkkkkkkkkkk', 'ja', 'se', 'cortou', 'hoje', 'pq', 'a', 'nao', 'te', 'respondeu', 'que', 'a', 'nao', 'me',
        #      'ksksksksk', 'ja', 'tentou', 'se', 'matar', 'pq', 'seu', 'pai', 'nao', 'quis', 'te', 'comprar', 'um', 'pra', 'vc',
        #      'jovem', 'moderno', 'sadi', 'boi', 'me', 'da', 'nojo', 'pqp', 'esse', 'fone', 'novo', 'é', 'o', 'platinum', 'com',
        #      'outra', 'bem', 'só', 'não', 'dá', 'pra', 'esperar', 'o', 'desempenho', 'de', 'um', 'mas', 'eu', 'uso', 'o',
        #      'tempo', 'tanto', 'pra', 'trampar', 'quanto', 'pro', 'rt', 'dancinha', 'da', 'vitoria', 'segue', 'lá', 'bravo',
        #      'eu', 'acho', 'que', 'antes', 'de', 'dayane', 'precisava', 'muito', 'mais', 'de', 'um', 'mackbook', 'ou', 'um',
        #      'rt', 'eae', 'já', 'compraram', 'a', 'pior', 'versão', 'de', 'outriders', 'por', 'no', 'eu', 'jogarei', 'sem',
        #      'custo', 'adicional', 'day', 'one', 'no', 'só', 'queria', 'elas', 'jogando', 'the', 'last', 'of', 'us', 'no',
        #      'zeus', 'tentando', 'queimar', 'o', 'porra', 'irmao', 'pode', 'comprar', 'um', 'vai', 'pagar', 'multa', 'por',
        #      'ser', 'retardado', 'suspeitei', 'do', 'seficarputoepior', 'nada', 'foi', 'o', 'cristal', 'msm', 'vão', 'dá', 'um',
        #      'pra', 'pro', 'com', 'canal', 'novo', 'na', 'vai', 'rolar', 'lives', 'de', 'e', 'edição', 'de', 'comprei', 'o',
        #      'jogo', 'depois', 'que', 'tinha', 'o', 'tá', 'até', 'hoje', 'na', 'jogando', 'todos', 'os', 'games', 'em',
        #      'destaca', 'demais', 'os', 'só', 'vou', 'jogar', 'qdo', 'tiver', 'update', 'de', 'ou', 'quando', 'não', 'tiver',
        #      'mais', 'nada', 'msm', 'na', 'vdd', 'se', 'alguém', 'vender', 'um', 'riscado', 'vai', 'é', 'ficar', 'mais',
        #      'barato', 'rt', 'aí', 'gente', 'sou', 'bobona', 'em', 'um', 'namoro', 'se', 'eu', 'tiver', 'dinheiro', 'compro',
        #      'mesmo', 'as', 'essa', 'thread', 'das', 'namoradas', 'dando', 'pros', 'um', 'xbox', 'serie', 'x', 'e', 'um', 'pc',
        #      'bala', 'da', 'última', 'geração', 'rt', 'joão', 'félix', 'e', 'joe', 'gomez', 'em', 'playroom', 'e', 'fifa', 'na',
        #      'este', 'é', 'o', 'primeiro', 'episódio', 'da', 'série', 'next', 'mas', 'os', 'jogos', 'estão', 'com', 'o', 'fps',
        #      'precisaria', 'que', 'a', 'própria', 'fs', 'fizesse', 'e', 'acho', 'que', 'não', 'virá', 'tão', 'que', 'acho',
        #      'que', 'é', 'capaz', 'de', 'venderem', 'um', 'remaster', 'de', 'bb', 'pro', 'e', 'pc', 'com', 'nada', 'de', 'fov',
        #      'na', 'porra', 'do', 'vsf', 'fiquei', 'com', 'inveja', 'dos', 'cara', 'ganhando', 'um', 'nintendo', 'switch', 'e',
        #      'rt', 'só', 'o', 'dissipador', 'de', 'calor', 'do', 'já', 'é', 'do', 'tamanho', 'do', 'se', 'fosse', 'familiar',
        #      'encheria', 'o', 'saco', 'o', 'resto', 'da', 'vida', 'perdeu', 'o', 'pir', 'fogo', 'no', 'cu', 'deve', 'vim', 'um',
        #      'tudo', 'pra', 'me', 'dar', 'um', 'como', 'é', 'boa', 'um', 'zero', 'com', 'jogos', 'rt', 'para', 'o', 'por', 'a',
        #      'mor', 'quem', 'me', 'dera', 'poder', 'jogar', 'quando', 'tiver', 'o', 'meu', 'ele', 'será', 'uma', 'compra',
        #      'certa', 'e', 'espero', 'que', 'todos', 'os', 'problemas', 'estejam', 'resolvidos', 'lucro', 'nos', 'primeiros',
        #      'meses', 'como', 'lucro', 'se', 'a', 'própria', 'sony', 'leva', 'prejuízo', 'com', 'cada', 'rt', 'eu', 'não',
        #      'sou', 'a', 'favor', 'de', 'de', 'bens', 'materiais', 'pq', 'o', 'infinito', 'e', 'o', 'universo', 'ele', 'o',
        #      'espírito', 'piriri', 'mas', 'eu', 'acho', 'tem', 'gente', 'mais', 'casual', 'que', 'não', 'sabe', 'nem', 'o',
        #      'que', 'é', 'um', 'xbox', 'series', 'enquanto', 'até', 'a', 'pessoa', 'mais', 'isolada', 'no', 'país', 'a',
        #      'ganhar', 'este', 'passatempo', 'do', 'e', 'com', 'jogos', 'para', 'e', 'game', 'pass', 'me', 'fez', 'parar', 'de',
        #      'jogar', 'demon', 'souls', 'de', 'e', 'agora', 'to', 'jogando', 'the', 'messenger', 'a', 'sony', 'sentiu',
        #      'depois', 'da', 'bethesda', 'ir', 'pro', 'xbox', 'e', 'fazer', 'jogos', 'exclusivos', 'de', 'disse', 'tudo', 'eu',
        #      'graças', 'a', 'deus', 'tenho', 'condições', 'de', 'ter', 'o', 'meu', 'e', 'um', 'pc', 'que', 'rode', 'vários',
        #      'mas', 'sou', 'consolista', 'um', 'xsx', 'vai', 'ser', 'bem', 'no', 'pc', 'eu', 'trampo', 'tanto', 'que', 'quando',
        #      'chega', 'final', 'do', 'dia', 'só', 'quero', 'ligar', 'o', 'console', 'na', 'sala', 'e', 'platinar', 'um', 'game',
        #      'kkkkkk', 'eu', 'acho', 'impressionante', 'como', 'o', 'gamepass', 'do', 'xbox', 'toda', 'hora', 'inclui', 'um',
        #      'milhão', 'de', 'jogos', 'novos', 'e', 'ainda', 'da', 'pra', 'usar', 'no', 'xbox', 'one', 'e', 'no', 'enquanto',
        #      'o', 'da', 'sony', 'só', 'funciona', 'no', 'e', 'ninguém', 'nunca', 'mais', 'teve', 'notícia', 'é', 'imagem', 'de',
        #      'é', 'com', 'você', 'banca', 'o', 'game', 'pass', 'ele', 'vem', 'com', 'a', 'gold', 'e', 'o', 'catálogo', 'para',
        #      'você', 'tenha', 'é', 'bingo', 'enquanto', 'isso', 'você', 'morre', 'em', 'reais', 'em', 'um', 'jogo', 'de', 'o',
        #      'dólar', 'tá', 'a', 'vida', 'tá', 'a', 'conta', 'não', 'fecha', 'e', 'videogame', 'é', 'pense', 'rt', 'nossa',
        #      'arma', 'agora', 'é', 'o', 'bethesda', 'já', 'foi', 'aprovada', 'no', 'carne', 'das', 'casas', 'saiu', 'fone',
        #      'novo', 'pro', 'jogo', 'com', 'fps', 'boost', 'e', 'eu', 'aqui', 'esperando', 'o', 'próximo', 'meme', 'do', 'com',
        #      'o', 'outer', 'adiciona', 'opção', 'de', 'no', 'e', 'xbox', 'series', 'x', 'a', 'plus', 'deve', 'ser', 'lembrada',
        #      'esse', 'ano', 'tbm', 'q', 'desde', 'q', 'lançou', 'o', 'ela', 'vem', 'muito', 'sonhei', 'que', 'eu', 'ganhava',
        #      'um', 'é', 'mais', 'fácil', 'sair', 'um', 'software', 'novo', 'do', 'que', 'vacine', 'seus', 'jogadores', 'do',
        #      'que', 'essas', 'porra', 'trazer', 'a', 'vacina', 'pra', 'cá', 'e', 'foi', 'vocês', 'que', 'removeram', 'e',
        #      'além', 'disso', 'cadê', 'meu', 'de', 'graça', 'seja', 'pelo', 'menos', 'um', 'pouco', 'comunista', 'sony',
        #      'novas', 'confirmadas', 'para', 'esta', 'mereço', 'um', 'não', 'saiu', 'vídeo', 'de', 'comparação', 'com', 'o',
        #      'fez', 'com', 'o', 'pro', 'pensando', 'em', 'comprar', 'um', 'e', 'parcelar', 'em', 'já', 'que', 'parece', 'que',
        #      'não', 'vamo', 'sair', 'tão', 'cedo', 'dessa', 'situação', 'com', 'esses', 'cara', 'aí', 'no', 'poder', 'gg', 'kd',
        #      'meu', 'sua', 'safada', 'gg', 'ein', 'é', 'foda', 'ser', 'a', 'amiga', 'kkkkkkkkkkk', 'obrigado', 'por', 'me',
        #      'chamar', 'de', 'sou', 'eu', 'quem', 'pago', 'tô', 'até', 'esperando', 'o', 'escritório', 'de', 'contabilidade',
        #      'me', 'mandar', 'os', 'documentos', 'pra', 'eu', 'e', 'eu', 'sou', 'mais', 'do', 'pc', 'talvez', 'minha', 'vovó',
        #      'pública', 'do', 'fique', 'com', 'o', 'pra', 'hahaha', 'e', 'isso', 'q', 'e', 'ser', 'dar', 'amor', 'e', 'apoiar',
        #      'dar', 'pra', 'no', 'fim', 'todos', 'virarem', 'contra', 'review', 'de', 'via', 'rt', 'pior', 'que', 'eu', 'acho',
        #      'esse', 'lindo', 'gameplay', 'de', 'creed', 'valhalla', 'o', 'casamento', 'do', 'rei', 'série', 'deste', 'que',
        #      'é', 'um', 'jogo', 'de', 'mundo', 'aberto', 'de', 'ação', 'e', 'aventura', 'desenvolvido', 'pela', 'ubisoft',
        #      'disponível', 'para', 'xbox', 'one', 'e', 'pc', 'e', 'o', 'game', 'está', 'dublado', 'em', 'português', 'do',
        #      'brasil', 'esse', 'vídeo', 'o', 'planalto', 'parece', 'um', 'rapaz', 'como', 'agora', 'há', 'um', 'futuro',
        #      'incerto', 'para', 'o', 'e', 'xbox', 'as', 'devs', 'vão', 'priorizar', 'o', 'switch', 'até', 'se', 'convenceram',
        #      'que', 'a', 'nova', 'geração', 'é', 'de', 'fato', 'um', 'bom', 'negócio', 'hell', 'let', 'baita', 'de', 'um',
        #      'simulador', 'de', 'tiro', 'que', 'o', 'me', 'falou', 'bastante', 'chega', 'no', 'xbox', 'series', 'x', 'e',
        #      'esse', 'macro', 'quanto', 'deve', 'vezes', 'mais', 'problemático', 'e', 'a', 'midia', 'abafou', 'até', 'hj', 'lá',
        #      'no', 'ask', 'playstation', 'tem', 'vídeos', 'do', 'peidando', 'o', 'basicamente', 'não', 'vi', 'quase', 'nenhuma',
        #      'notícia', 'sobre', 'aqui', 'estão', 'a', 'estatísticas', 'das', 'devoluçoes', 'só', 'para', 'não', 'dizerem',
        #      'que', 'tirei', 'do', 'cu', 'a', 'informação', 'mano', 'isso', 'parece', 'aqueles', 'quebra', 'recorde', 'de',
        #      'console', 'mais', 'vendido', 'com', 'o', 'nome', 'eu', 'nem', 'entro', 'nesse', 'mérito', 'porque', 'isso', 'é',
        #      'a', 'parte', 'ultra', 'positiva', 'do', 'gamepass', 'falo', 'de', 'pessoa', 'que', 'quer', 'sei', 'x', 'jogo',
        #      'do', 'as', 'pessoas', 'esquecem', 'que', 'com', 'o', 'tempo', 'os', 'preços', 'vão', 'caindo', 'e', 'elas',
        #      'podem', 'ter', 'todos', 'os', 'consoles', 'sem', 'nenhum', 'problema', 'meu', 'controle', 'do', 'não', 'esta',
        #      'carregando', 'e', 'ja', 'mudei', 'as', 'configurações', 'de', 'fornecer', 'energia', 'de', 'horas', 'para',
        #      'sempre', 'ele', 'não', 'carrega', 'ja', 'testei', 'conectar', 'no', 'pc', 'e', 'tbm', 'não', 'funciona', 'e',
        #      'quero', 'suporte', 'e', 'não', 'acho', 'no', 'seu', 'site', 'o', 'chat', 'online', 'ou', 'numero', 'de',
        #      'telefone', 'a', 'atualização', 'já', 'teve', 'e', 'o', 'ficou', 'de', 'fora', 'rt', 'na', 'verdade', 'foi', 'um',
        #      'pc', 'nintendo', 'switch', 'e', 'xbox', 'eu', 'nem', 'olho', 'muito', 'os', 'vídeos', 'por', 'q', 'não', 'posso',
        #      'comprar', 'um', 'cara', 'eu', 'amei', 'tanto', 'demons', 'souls', 'e', 'eu', 'passei', 'meses', 'jogando', 'só',
        #      'ele', 'todos', 'os', 'tinha', 'amigos', 'americanos', 'e', 'um', 'alemão', 'só', 'pra', 'jogar', 'de', 'longe',
        #      'o', 'game', 'q', 'mais', 'joguei', 'no', 'podiam', 'mandar', 'o', 'esse', 'não', 'volta', 'nunca', 'nas', 'lojas',
        #      'brasileiras', 'wtf', 'no', 'veio', 'a', 'mesma', 'coisa', 'a', 'pessoa', 'que', 'tem', 'um', 'pra', 'jogar',
        #      'fortnite', 'já', 'morreu', 'por', 'dentro', 'ele', 'podia', 'fazer', 'esse', 'vídeo', 'de', 'mó', 'caro',
        #      'apesar', 'de', 'ser', 'um', 'game', 'de', 'octopath', 'traveler', 'é', 'um', 'estilo', 'que', 'me', 'agrada',
        #      'será', 'que', 'chega', 'para', 'eu', 'definitivamente', 'preciso', 'de', 'um', 'antes', 'do', 'lançamento', 'de',
        #      'ragnarok', 'preciso', 'jogar', 'no', 'lançamento', 'o', 'que', 'vai', 'ser', 'sem', 'dúvidas', 'um', 'dos',
        #      'melhores', 'jogos', 'da', 'geração', 'all', 'podem', 'me', 'mas', 'desde', 'que', 'eu', 'comprei', 'não',
        #      'entrou', 'no', 'gamepass', 'nenhum', 'jogo', 'que', 'eu', 'estou', 'então', 'pra', 'mim', 'n', 'faz', 'me',
        #      'ajuda', 'esta', 'em', 'segundo', 'no', 'ranking', 'de', 'mais', 'e', 'o', 'monstro', 'chamado', 'vem',
        #      'destruindo', 'tudo', 'em', 'vendas', 'ja', 'faz', 'anos', 'e', 'não', 'para', 'cade', 'a', 'media', 'fazendo',
        #      'chamada', 'desse', 'reclames', 'do', 'plim', 'plim', 'nessa', 'temp', 'eu', 'vou', 'usar', 'o', 'controle', 'de',
        #      'gulaso', 'de', 'neymar', 'rt', 'hdmi', 'não', 'é', 'necessário', 'para', 'o', 'diz', 'gerente', 'de', 'produto',
        #      'da', 'sony', 'pra', 'fazer', 'fake', 'com', 'resolução', 'dinâmica', 'realmente', 'as', 'vezes', 'eu', 'penso',
        #      'que', 'as', 'merdas', 'que', 'os', 'fanboys', 'do', 'xbox', 'falam', 'vem', 'da', 'propria', 'o', 's', 'iria',
        #      'rodar', 'jogo', 'se', 'os', 'multis', 'fossem', 'para', 'assim', 'como', 'o', 'x', 'seria', 'o', 'sem', 'duvida',
        #      'nenhuma', 'se', 'o', 'fosse', 'overclock', 'rick', 'and', 'morty', 'literalmente', 'já', 'fez', 'ad', 'de',
        #      'graça', 'pra', 'mas', 'mesmo', 'assim', 'quem', 'tá', 'patrocinando', 'a', 'série', 'é', 'pagando', 'pra', 'eles',
        #      'fazerem', 'ad', 'é', 'o', 'mlk', 'vai', 'se', 'vender', 'pras', 'veias', 'la', 'e', 'comprar', 'o', 'ss', 'agora',
        #      'me', 'compra', 'um', 'sonhei', 'que', 'comprei', 'o', 'tô', 'há', 'tanto', 'tempo', 'esperando', 'o', 'q',
        #      'criei', 'um', 'ranço', 'se', 'não', 'quer', 'ser', 'comprado', 'então', 'também', 'não', 'vo', 'compra', 'só',
        #      'queria', 'um', 'agora', 'se', 'alguém', 'me', 'perguntar', 'hoje', 'se', 'estou', 'feliz', 'com', 'o', 'eu',
        #      'vou', 'dizer', 'que', 'então', 'está', 'também', 'ta', 'um', 'nao', 'fede', 'nem', 'atualmente', 'só', 'no',
        #      'aguardo', 'de', 'acabei', 'de', 'pegar', 'o', 'aí', 'vem', 'esse', 'ghostwire', 'pra', 'q', 'eu', 'curti', 'o',
        #      'aesthetics', 'mas', 'não', 'vou', 'fazer', 'a', 'msm', 'coisa', 'q', 'eu', 'fiz', 'com', 'death', 'de', 'comprar',
        #      'um', 'console', 'por', 'causa', 'de', 'um', 'no', 'fim', 'não', 'joguei', 'nem', 'de', 'ds', 'vlw', 'a', 'pena',
        #      'por', 'dbd', 'e', 'beat', 'saber', 'pelo', 'fazendo', 'propaganda', 'na', 'eu', 'ein', 'tenho', 'comprar', 'ou',
        #      'abortar', 'missão', 'eh', 'zuera', 'to', 'tratando', 'como', 'um', 'opala', 'kkkk', 'queria', 'ou', 'até', 'o',
        #      'msm', 'mas', 'tem', 'mta', 'coisa', 'q', 'me', 'prende', 'ao', 'xbox', 'ent', 'vou', 'continuar', 'com', 'ele',
        #      'ai', 'ate', 'eu', 'quero', 'um', 'antes', 'que', 'fosse', 'isso', 'traduziram', 'mto', 'mal', 'a', 'palavra',
        #      'lucro', 'aí', 'era', 'ser', 'receita', 'receita', 'preço', 'x', 'não', 'significa', 'só', 'que', 'se', 'gastou',
        #      'mais', 'dinheiro', 'só', 'que', 'o', 'switch', 'custa', 'e', 'o', 'é', 'dado', 'idiota', 'pra', 'manchete',
        #      'clickbait', 'as', 'vezes', 'é', 'mais', 'fácil', 'só', 'jogar', 'no', 'chão', 'gasolina', 'cara', 'daq', 'a',
        #      'pouco', 'chega', 'no', 'valor', 'do', 'kkk', 'minha', 'mãe', 'veio', 'perguntar', 'quando', 'vou', 'comprar', 'o',
        #      'pode', 'ser', 'um', 'gif', 'da', 'caixa', 'do', 'meu', 'que', 'chegou', 'toda', 'eu', 'amo', 'o', 'meu',
        #      'nintendo', 'switch', 'e', 'curto', 'demais', 'o', 'são', 'todos', 'consoles', 'mas', 'se', 'eu', 'não', 'tivesse',
        #      'nenhum', 'desses', 'e', 'estivesse', 'me', 'decidindo', 'por', 'qual', 'o', 'xbox', 'a', 'opção', 'mais',
        #      'completa', 'e', 'que', 'valoriza', 'sua', 'grana', 'objetivo', 'de', 'ter', 'uma', 'namorada', 'e', 'se', 'casar',
        #      'meu', 'casar', 'com', 'um', 'rt', 'cada', 'dia', 'eu', 'me', 'surpreendo', 'mais', 'com', 'os', 'recursos', 'do',
        #      'movimentação', 'automática', 'mais', 'um', 'sorteio', 'para', 'o', 'está', 'sorteando', 'e', 'veja', 'como',
        #      'contra', 'não', 'há', 'não', 'trouxe', 'mudanças', 'nos', 'alguém', 'me', 'da', 'um', 'rt', 'overwatch', 'agora',
        #      'roda', 'em', 'fps', 'no', 'xbox', 'series', 'x', 'e', 'mas', 'não', 'no', 'mainha', 'quer', 'comprar', 'um',
        #      'mas', 'minha', 'ansiedade', 'é', 'tão', 'grande', 'que', 'tô', 'quase', 'pedindo', 'um', 'msm', 'comprou', 'qria',
        #      'jogar', 'alguma', 'o', 'miseravi', 'não', 'sai', 'da', 'rt', 'entrem', 'no', 'meu', 'tik', 'tok', 'e', 'dêem',
        #      'like', 'no', 'meu', 'vídeo', 'para', 'ganhar', 'uma', 'mano', 'eu', 'to', 'encantado', 'com', 'o', 'dualsense',
        #      'do', 'mas', 'eu', 'quero', 'mandar', 'fazer', 'uma', 'mesa', 'pro', 'então', 'meu', 'dinheiro', 'se', 'resume',
        #      'numa', 'coisa', 'ou', 'q', 'q', 'eu', 'faso', 'china', 'pede', 'empréstimo', 'de', 'reais', 'de', 'vinizin',
        #      'para', 'pagar', 'o', 'do', 'theo', 'não', 'tenho', 'espaço', 'nem', 'muita', 'vontade', 'de', 'depender', 'de',
        #      'um', 'se', 'estragar', 'eu', 'não', 'tenho', 'como', 'sair', 'desesperada', 'catando', 'pecinha', 'pra',
        #      'comprar', 'e', 'pelo', 'menos', 'o', 'ps', 'é', 'completo', 'por', 'si', 'só', 'e', 'não', 'iria', 'me', 'dar',
        #      'tanta', 'dor', 'de', 'o', 'ps', 'eu', 'pego', 'por', 'até', 'o', 'pc', 'por', 'menos', 'de', 'n', 'sei', 'bem',
        #      'o', 'que', 'uma', 'feminista', 'liberal', 'libera', 'tamanho', 'da', 'atualização', 'gb', 'as', 'vezes', 'nem',
        #      'é', 'pelo', 'rt', 'queria', 'um', 'empate', 'nao', 'tem', 'mas', 'tenho', 'certeza', 'que', 'nao', 'sera', 'm',
        #      'a', 'm', 'a', 'microsoft', 'ira', 'fica', 'muito', 'mais', 'proxima', 'acho', 'que', 'sera', 'm', 'a', 'm', 'pra',
        #      'sony', 'ainda', 'mesmo', 'com', 'as', 'merdas', 'dela', 'o', 'pessoal', 'esta', 'hypado', 'pro', 'tá', 'tão',
        #      'que', 'parece', 'até', 'ser', 'furada', 'é', 'uma', 'biblioteca', 'com', 'jogos', 'que', 'tu', 'pode', 'baixar',
        #      'a', 'qualquer', 'momento', 'se', 'tiver', 'só', 'está', 'disponível', 'no', 'não', 'me', 'parece', 'impossível',
        #      'lançarem', 'um', 'smt', 'v', 'maniax', 'no', 'mas', 'da', 'primeira', 'versão', 'acho', 'difícil', 'essa',
        #      'merda', 'tem', 'um', 'problema', 'de', 'junta', 'tudo', 'e', 'deita', 'e', 'os', 'caishits', 'ainda', 'falam',
        #      'que', 'essa', 'coisa', 'é', 'melhor', 'que', 'o', 'tem', 'doente', 'para', 'ganhei', 'ontem', 'fora', 'que', 'a',
        #      'economia', 'de', 'lá', 'é', 'salário', 'mínimo', 'vc', 'compra', 'alguém', 'me', 'dá', 'um', 'series', 'x', 'sou',
        #      'minoria', 'pelo', 'visto', 'kkkkkk', 'eu', 'sei', 'que', 'parecer', 'loucura', 'mais', 'acho', 'que', 'vai',
        #      'ocorre', 'um', 'empate', 'entre', 'o', 'e', 'o', 'xbox', 'series', 'x', 'difícil', 'já', 'está', 'disparando',
        #      'na', 'mas', 'vamos', 'é', 'complicado', 'tirar', 'essas', 'conclusões', 'como', 'se', 'o', 'fosse', 'vou', 'ter',
        #      'mais', 'um', 'ia', 'ajudar', 'a', 'passar', 'o', 'tempo', 'no', 'lockdown', 'n', 'acordei', 'e', 'não', 'vi',
        #      'um', 'na', 'minha', 'cama', 'vo', 'ficar', 'falando', 'do', 'nintendo', 'switch', 'e', 'do', 'p', 'minha', 'vó',
        #      'ate', 'ela', 'adivinhar', 'q', 'eu', 'quero', 'um', 'dos', 'dois', 'te', 'falar', 'que', 'eu', 'acho', 'o',
        #      'series', 's', 'mais', 'interessante', 'que', 'o', 'series', 'x', 'e', 'o', 'quanto', 'ao', 'concordo', 'com',
        #      'mas', 'a', 'empresa', 'deveria', 'ter', 'pois', 'rodar', 'com', 'fps', 'instável', 'é', 'pior', 'que', 'manter',
        #      'no', 'os', 'dois', 'consoles', 'estão', 'parecidos', 'nesse', 'quando', 'um', 'é', 'por', 'por', 'exemplo', 'o',
        #      'crash', 'no', 'do', 'está', 'mas', 'é', 'só', 'em', 'sombras', 'simples', 'o', 'problema', 'da', 'sony', 'de',
        #      'estar', 'na', 'liderança', 'é', 'que', 'duvido', 'e', 'muito', 'ela', 'se', 'mexer', 'pra', 'trazer', 'algo',
        #      'já', 'tem', 'anos', 'de', 'rumor', 'que', 'chegaria', 'o', 'now', 'aqui', 'e', 'fora', 'ainda', 'liberar', 'a',
        #      'plus', 'collection', 'somente', 'para', 'o', 'que', 'houve', 'com', 'o', 'não', 'vai', 'chegar', 'no', 'brasil',
        #      'rt', 'pq', 'q', 'tem', 'um', 'raio', 'tentando', 'acertar', 'um', 'gigante', 'e', 'o', 'valor', 'de', 'um', 'ssd',
        #      'de', 'é', 'o', 'outro', 'kkkk', 'se', 'tiras', 'estes', 'mais', 'a', 'bethesda', 'e', 'perdes', 'mt', 'do',
        #      'catálogo', 'q', 'tornava', 'a', 'ps', 'tão', 'fixe', 'p', 'descobrir', 'outros', 'jogos', 'fora', 'dos', 'daqui',
        #      'a', 'pouco', 'só', 'tens', 'ubisoft', 'na', 'e', 'duvido', 'q', 'lhes', 'falte', 'lançamento', 'da', 'p', 'mim',
        #      'foi', 'n', 'tens', 'quase', 'jogos', 'novos', 'só', 'queria', 'um', 'autografado', 'pelo', 'herói', 'sonysta',
        #      'é', 'flagrado', 'se', 'masturbando', 'na', 'frente', 'de', 'um', 'o', 'fifa', 'no', 'é', 'bom', 'eu', 'curto',
        #      'o', 'pes', 'por', 'causa', 'da', 'juve', 'e', 'da', 'copa', 'da', 'que', 'são', 'exclusivos', 'mas', 'o', 'modo',
        #      'carreira', 'do', 'fifa', 'me', 'e', 'como', 'ainda', 'jogo', 'games', 'tipo', 'horizon', 'zero', 'não', 'sobra',
        #      'tempo', 'pra', 'mais', 'ainda', 'andam', 'se', 'pá', 'que', 'o', 'material', 'do', 'sai', 'isso', 'aí', 'fácil',
        #      'ceo', 'team', 'vikings', 'subs', 'iphone', 'e', 'na', 'loja', 'pois', 'é', 'kfhskdsdfsdf', 'e', 'o', 'tá',
        #      'dando', 'uns', 'então', 'meio', 'que', 'vale', 'a', 'pena', 'preciso', 'pra', 'comprar', 'e', 'pc', 'gamer', 'rt',
        #      'nova', 'tela', 'de', 'carregamento', 'do', 'fortnite', 'no', 'via', 'o', 'ou', 'a', 'pra', 'quem', 'quiser',
        #      'aproveitar', 'os', 'jogos', 'do', 'game', 'tem', 'xbox', 'series', 's', 'no', 'estoque', 'da', 'pra', 'quem',
        #      'quer', 'entrar', 'na', 'nova', 'geração', 'ou', 'já', 'tem', 'um', 'é', 'uma', 'excelente', 'opção', 'de', 'fifa',
        #      'o', 'melhor', 'game', 'jogo', 'de', 'futebol', 'de', 'video', 'game', 'via', 'custando', 'será', 'se', 'devo',
        #      'tu', 'vai', 'ganhar', 'um', 'q', 'eu', 'sei', 'se', 'eu', 'comprar', 'um', 'ao', 'inves', 'd', 'um', 'xbox',
        #      'serie', 'x', 'eu', 'vou', 'estar', 'sendo', 'rt', 'às', 'vezes', 'tudo', 'o', 'que', 'você', 'precisa', 'é',
        #      'sair', 'da', 'zona', 'de', 'conforto', 'e', 'dar', 'um', 'passo', 'em', 'direção', 'aos', 'seus', 'nao', 'vai',
        #      'ter', 'eu', 'ganhando', 'um', 'uma', 'putaria', 'o', 'que', 'tão', 'fazendo', 'com', 'os', 'estoques', 'de', 'só',
        #      'queria', 'que', 'o', 'blaclist', 'rodasse', 'no', 'colocar', 'hd', 'no', 'eu', 'não', 'penso', 'em', 'e', 'se',
        #      'deus', 'vou', 'pegar', 'o', 'xbox', 'novo', 'então', 'vc', 'ia', 'ter', 'um', 'único', 'tlgd', 'pelo', 'andar',
        #      'da', 'carruagem', 'só', 'compro', 'o', 'no', 'lançamento', 'do', 'eu', 'achei', 'q', 'a', 'vida', 'útil', 'do',
        #      'seria', 'grande', 'mas', 'a', 'do', 'deve', 'bater', 'rindo', 'de', 'a', 'sony', 'comprou', 'exclusividade', 'de',
        #      'informação', 'para', 'vocês', 'não', 'citarem', 'que', 'o', 'nintendo', 'switch', 'ficou', 'à', 'frente', 'do',
        #      'passei', 'anos', 'chorando', 'por', 'um', 'ai', 'agora', 'o', 'preço', 'que', 'eu', 'investi', 'nesse', 'pc',
        #      'dava', 'pra', 'ter', 'comprado', 'uns', 'ou', 'um', 'estreia', 'do', 'demon', 'souls', 'impressiona', 'pela',
        #      'experiência', 'do', 'jogo', 'sorriso', 'e', 'mas', 'assim', 'se', 'vc', 'tiver', 'skate', 'e', 'um', 'oi', 'tem',
        #      'um', 'mod', 'no', 'ps', 'que', 'bota', 'o', 'jogo', 'em', 'não', 'tem', 'isso', 'no', 'um', 'laptop', 'seria',
        #      'mais', 'util', 'que', 'um', 'tenho', 'kkkkk', 'até', 'o', 'android', 'tá', 'mais', 'pesado', 'que', 'no',
        #      'dungeons', 'dark', 'alliance', 'será', 'lançado', 'em', 'de', 'junho', 'para', 'e', 'trailer', 'e', 'gameplay',
        #      'um', 'sony', 'japan', 'exibe', 'vídeo', 'com', 'de', 'jogos', 'do', 'consulta', 'com', 'direito', 'a', 'olha',
        #      'que', 'blz', 'rapaz', 'a', 'melhor', 'coisa', 'são', 'os', 'comentários', 'dessa', 'a', 'galera', 'vive', 'em',
        #      'uma', 'realidade', 'agora', 'marrento', 'o', 'ficou', 'de', 'logo', 'o', 'aí', 'não', 'sdds', 'do', 'que',
        #      'ainda', 'não', 'um', 'e', 'uma', 'tv', 'e', 'um', 'joão', 'félix', 'e', 'joe', 'gomez', 'em', 'playroom', 'e',
        #      'fifa', 'na', 'este', 'é', 'o', 'primeiro', 'episódio', 'da', 'série', 'next', 'gen', 'icons', 'something', 'went',
        #      'wrong', 'rt', 'happy', 'birthday', 'chiaki', 'and', 'chihiro', 'desenho', 'bem', 'em', 'cima', 'da', 'hora',
        #      'mas', 'vale', 'que', 'eu', 'consegui', 'a', 'tempo', 'em', 'fazer', 'e', 'rt', 'ganha', 'nova', 'gameplay',
        #      'mostrando', 'casa', 'com', 'interior', 'explorável', 'lembrando', 'que', 'o', 'game', 'continua', 'sendo', 'se',
        #      'quisesse', 'ficar', 'bonito', 'eu', 'comprava', 'um', 'dungeons', 'dark', 'alliance', 'será', 'lançado', 'de',
        #      'junho', 'para', 'e', 'confesso', 'que', 'a', 'temporada', 'do', 'fortnite', 'poderia', 'ter', 'sido', 'vídeo',
        #      'no', 'canal', 'e', 'live', 'feita', 'pra', 'testar', 'o', 'fiz', 'a', 'live', 'pela', 'primeira', 'vez',
        #      'diretamente', 'no', 'a', 'sony', 'ta', 'de', 'parabéns', 'pela', 'qualidade', 'que', 'ele', 'deixei', 'voces',
        #      'via', 'raid', 'com', 'a', 'simpática', 'bom', 'dia', 'a', 'um', 'caralho', 'queria', 'tanto', 'ser', 'rica', 'se',
        #      'viesse', 'um', 'título', 'no', 'ovo', 'de', 'páscoa', 'eu', 'pagava', 'mais', 'que', 'um', 'fácil', 'aquela',
        #      'palhaçada', 'de', 'querer', 'aumentar', 'o', 'gold', 'do', 'foi', 'a', 'galera', 'cobra', 'a', 'galera', 'pede',
        #      'e', 'a', 'ms', 'corre', 'atrás', 'e', 'mas', 'a', 'galera', 'da', 'sony', 'não', 'reclama', 'não', 'acham',
        #      'ruim', 'não', 'poder', 'expandir', 'a', 'memória', 'do', 'ou', 'gravar', 'os', 'jogos', 'novos', 'em', 'hd',
        #      'para', 'não', 'existe', 'uma', 'opção', 'equivalente', 'na', 'rt', 'pior', 'que', 'eu', 'acho', 'esse', 'lindo']
        #
        # dic= {'rumor': 1}
        # print(len(dic))
        # q = count_list_occurrence(w, dic)
        # print(f'''{q}
        # {dic}''')
        # print(len(w), len(set(w)))

        # if True:
        #     import pandas as pd
        #
        #     method_list = [func for func in dir(RemoveWords) if
        #                    callable(getattr(RemoveWords, func)) and not func.startswith("__")]
        #
        #     qazx = dir(RemoveWords)
        #     print(method_list, 'funcs')
        #     dados_treino = pd.read_excel('ps5.xlsx')
        #     # pd.set_option("display.max_rows", 999, "display.max_columns", 999)
        #     pd.reset_option("display")
        #     # dados_treino.Treinamento
        #
        #     # w = ListWord(column_name='Treinamento').lists_all(dados_treino)
        #     # w
        #     p = ListWord(column_name='Treinamento').c_o_f(dados_treino)
        #     print(type(p))
        #     # p = count_list_occurrence(w)
        #     # p = pd.DataFrame.from_dict(p, orient='index', columns=['# de ocorrências'])
        #     # p.sort_values(by='# de ocorrências', ascending=False)
        #
        #     print('ANTES', len(p))
        #     mn = RemoveWords(p, '# de ocorrências')
        #     # mn = mn.remove_at(0, 299, column_name='index')
        #     # print('DEPOIS', len(mn), len(p))
        #     qremove_link = mn.remove_link()
        #     qremove_at = mn.remove_at()
        #     qremove_ponc = mn.remove_ponc()
        #     qremove_word_st3 = mn.remove_word_st3()
        #     qremove_laugh = mn.remove_laugh()
        #     qremove_num_str = mn.remove_num_str()
        #     qremove_options = mn.remove_options(remove_link=True, remove_at=True, remove_ponc=True, remove_word_st3=True,
        #                                         remove_laugh=True, remove_num_str=True)
        import emoji
        import emojis
        # lista_splitting_emoji_string = []
        # lista_splitting_grouped_string = []
        # lista_uniting_sting_lists = []
        lista_emo = []
        lista_emo1 = []
        lista_diff = []
        for i in np.arange(0, len(dados_treino_1)):
            lista_emo.append(
                ''.join(j for j in dados_treino_1['Treinamento'][i] if j in emojis.db.get_emoji_aliases().values()))
            lista_emo1.append(''.join(j for j in dados_treino_1['Treinamento'][i] if j in emoji.UNICODE_EMOJI['en']))
            # splitting_emoji_string = emoji.get_emoji_regexp().split(dados_treino_1['Treinamento'][i])
            # splitting_grouped_string = [j.split() for j in splitting_emoji_string]
            # uniting_sting_lists = functools.reduce(operator.concat, splitting_grouped_string)
            # lista_splitting_emoji_string.append(splitting_emoji_string)
            # lista_splitting_grouped_string.append(splitting_grouped_string)
            # lista_uniting_sting_lists.append(uniting_sting_lists)
            # lista_emo.append(emojis.get(dados_treino_1['Treinamento'][i]))
            if '' in lista_emo:
                lista_emo.remove('')
            if '' in lista_emo1:
                lista_emo1.remove('')

        # print(lista_splitting_emoji_string)
        # print(lista_splitting_grouped_string)
        # print(lista_uniting_sting_lists)
        print(lista_emo)
        print(lista_emo1)
        for i in lista_emo:
            lista_emo_split = (emoji.get_emoji_regexp().split(i))
        for i in lista_emo1:
            lista_emo1_split = (emoji.get_emoji_regexp().split(i))
        print(lista_emo_split)
        print(lista_emo1_split)
        # nb0 = 0
        # nb1 = 0
        # nb2 = 0
        nb3 = 0
        nb4 = 0
        # for j in lista_splitting_emoji_string:
        #     for h in j:
        #         nb0+=emojis.count(h, unique=False)
        # print(nb0)
        #
        # for j in lista_uniting_sting_lists:
        #     for h in j:
        #         nb1+=emojis.count(h, unique=False)
        # print(nb1)
        #
        # for j in lista_splitting_grouped_string:
        #     for h in j:
        #         for q in h:
        #             nb2+=emojis.count(q, unique=False)
        # print(nb2)
        for j in lista_emo:
            nb3 += emojis.count(j, unique=False)
        print(nb3)
        for j in lista_emo1:
            nb4 += emojis.count(j, unique=False)
        print(nb4)
        lista_diff.append([i for i in lista_emo1 if i not in lista_emo])
        print(lista_diff)

        abcdefghijkl = f"{list(emojis.db.get_emoji_aliases().keys())}\n{list(emojis.db.get_emoji_aliases().values())}\n{list(emojis.db.get_emoji_aliases())}"
        # print(abcdefghijkl)
        listaaaaa = []
        for i in list(emojis.db.get_emoji_aliases().values()):
            listaaaaa.append(emojis.db.get_emoji_by_code(i))
        # print(listaaaaa)

        aqwsedfr = list(emojis.db.get_emoji_aliases().keys()) + list(emojis.db.get_emoji_aliases().values())
        print(aqwsedfr)

        lisqa = list(emojis.db.get_emoji_aliases().items())
        print(lisqa)
        print(emoji.get_emoji_regexp())

        print(emoji.emojize(':grinning_face_with_smiling_eyes::snake::thumbs_up_medium_skin_tone:'))
        print(emojis.encode('This is a message with emojis :smile: :snake::thumbsup:🏽'))
        emojisssss = emoji.get_emoji_regexp().split('This is a message with emojis 😄 🐍👍🏽')
        print(type(emojisssss))
        print(emojisssss)

        dados_treino_1 = pd.read_excel('ps5.xlsx')
        dados_treino_1['Treinamento'][1]
        import emoji
        import emojis
        # lista_splitting_emoji_string = []
        # lista_splitting_grouped_string = []
        # lista_uniting_sting_lists = []
        lista_emo = []
        lista_emo1 = []
        lista_diff = []
        for i in np.arange(0, len(dados_treino_1)):
            lista_emo.append(
                ''.join(j for j in dados_treino_1['Treinamento'][i] if j in emojis.db.get_emoji_aliases().values()))
            lista_emo1.append(''.join(j for j in dados_treino_1['Treinamento'][i] if j in emoji.UNICODE_EMOJI['en']))
            # splitting_emoji_string = emoji.get_emoji_regexp().split(dados_treino_1['Treinamento'][i])
            # splitting_grouped_string = [j.split() for j in splitting_emoji_string]
            # uniting_sting_lists = functools.reduce(operator.concat, splitting_grouped_string)
            # lista_splitting_emoji_string.append(splitting_emoji_string)
            # lista_splitting_grouped_string.append(splitting_grouped_string)
            # lista_uniting_sting_lists.append(uniting_sting_lists)
            # lista_emo.append(emojis.get(dados_treino_1['Treinamento'][i]))
            if '' in lista_emo:
                lista_emo.remove('')
            if '' in lista_emo1:
                lista_emo1.remove('')

        # print(lista_splitting_emoji_string)
        # print(lista_splitting_grouped_string)
        # print(lista_uniting_sting_lists)
        print(lista_emo)
        print(lista_emo1)
        for i in lista_emo:
            lista_emo_split = (emoji.get_emoji_regexp().split(i))
        for i in lista_emo1:
            lista_emo1_split = (emoji.get_emoji_regexp().split(i))
        print(lista_emo_split)
        print(lista_emo1_split)
        # nb0 = 0
        # nb1 = 0
        # nb2 = 0
        nb3 = 0
        nb4 = 0
        # for j in lista_splitting_emoji_string:
        #     for h in j:
        #         nb0+=emojis.count(h, unique=False)
        # print(nb0)
        #
        # for j in lista_uniting_sting_lists:
        #     for h in j:
        #         nb1+=emojis.count(h, unique=False)
        # print(nb1)
        #
        # for j in lista_splitting_grouped_string:
        #     for h in j:
        #         for q in h:
        #             nb2+=emojis.count(q, unique=False)
        # print(nb2)
        for j in lista_emo:
            nb3 += emojis.count(j, unique=False)
        print(nb3)
        for j in lista_emo1:
            nb4 += emojis.count(j, unique=False)
        print(nb4)
        lista_diff.append([i for i in lista_emo1 if i not in lista_emo])
        print(lista_diff)

    except Exception:
        import string
        import functools
        import operator
        import emoji
        import emojis
        import numpy as np
        import pandas as pd
        dados_treino = pd.read_excel('ps5.xlsx')
        dados_treino

        p = ListWord(column_name='Treinamento').c_o_f(dados_treino)
        p.sort_values(by='# de ocorrências', ascending=False)

        at_character = RemoveWords(p, '# de ocorrências', Object_of_Study, show_removed=True)
        link = RemoveWords(p, '# de ocorrências', Object_of_Study, show_removed=True)
        ponc = RemoveWords(p, '# de ocorrências', Object_of_Study, show_removed=True)
        word_sts = RemoveWords(p, '# de ocorrências', Object_of_Study, show_removed=True)
        laugh = RemoveWords(p, '# de ocorrências', Object_of_Study, show_removed=True)
        num_str = RemoveWords(p, '# de ocorrências', Object_of_Study, show_removed=True)
        options = RemoveWords(p, '# de ocorrências', Object_of_Study, show_removed=True)

        qremove_at = at_character.remove_at()
        qremove_link = link.remove_link()
        qremove_ponc = ponc.remove_ponc()
        qremove_word_sts = word_sts.remove_word_sts(3)
        qremove_laugh = laugh.remove_laugh(4, 3)
        qremove_num_str = num_str.remove_num_str(3)
        qremove_options = options.remove_options(remove_at={True: '()'}, remove_link={True: '()'},
                                                 remove_ponc={False: '()'}, remove_laugh={True: '(4, 3)'},
                                                 remove_word_sts={True: '(3)'}, remove_num_str={True: '(3)'})

        print(f"""NUMERO DE VEZES QUE A PERECE A PALAVRA PS5 POR DATAFRAME CRIDO (VALE LEMBRAR QUE O DATAFRAME
                        QREMOVE_OPTIONS ESTÁ COM A OPÇÃO REMOVE_PUNC DESLIGADA PELO MOTIVO CITADO ACIMA)

            {qremove_link['# de ocorrências'][Object_of_Study]} qremove_link, num ps5
            {qremove_at['# de ocorrências'][Object_of_Study]} qremove_at, num ps5
            {qremove_ponc['# de ocorrências'][Object_of_Study]} qremove_ponc, num ps5
            {qremove_word_sts['# de ocorrências'][Object_of_Study]} qremove_word_sts, num ps5
            {qremove_laugh['# de ocorrências'][Object_of_Study]} qremove_laugh, num ps5
            {qremove_num_str['# de ocorrências'][Object_of_Study]} qremove_num_str, num ps5
            {qremove_options['# de ocorrências'][Object_of_Study]} qremove_options, num ps5""")

        qremove_options_1 = qremove_options.sort_values(by='# de ocorrências', ascending=False)
        qremove_options_1 = qremove_options_1.loc[qremove_options_1['# de ocorrências'] > 100]
        qremove_options
        qremove_ponc_1 = qremove_ponc.reset_index()
        dados_treino_2 = dados_treino.reset_index()
        listapok = []
        for wordsss in qremove_ponc_1['index']:
            if wordsss not in dados_treino_2['index']:
                listapok.append(wordsss)
        print(listapok)


if __name__ == "__main__":
    main()

# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
#
# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()


import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
lst_r, lst_h = [],[]
random.shuffle(lst)
# print(lst)
lst_r = [1 if el == 'robot' else 0 for el in lst ]
lst_h = [1 if el == 'human' else 0 for el in lst ]
print(pd.DataFrame({'robot': lst_r, 'human': lst_h}))
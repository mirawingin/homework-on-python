# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, 
# которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()

# Да, конечно! мы можем использовать метод pd.get_dummies() для создания one-hot кодирования, 
# но также можно сделать это без него, используя методы pandas. Вот как это можно сделать:
    
import pandas as pd

# Создаем DataFrame
data = pd.DataFrame({'whoAmI': ['robot', 'human', 'robot', 'human', 'robot']})

# Получаем уникальные категории
categories = data['whoAmI'].unique()

# Создаем новый DataFrame для хранения one-hot кодирования
one_hot_encoded = pd.DataFrame()

# Для каждой категории создаем новый столбец и заполняем его значениями
for category in categories:
    one_hot_encoded[category] = (data['whoAmI'] == category).astype(int)

# Выводим результат
print(one_hot_encoded)
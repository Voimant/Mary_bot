from pprint import pprint

import pandas as pd

def dela():
    df = pd.read_excel("/home/voimant/Рабочий стол/Mary_2/source/dela.xlsx")

    # pprint(df.to_dict())
    y = df.to_dict()
    my_dict = {}

    d_key = y['Суть спора']
    value = y['Ссылка на дело']
    count = 0
    for k,v in d_key.items():
        my_dict[v] = value[count]
        count += 1
    return my_dict
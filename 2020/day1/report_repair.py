import numpy as np
import pandas as pd

def find_number(array):
    for i, x in enumerate(array):
        k = i
        while k + 1 < array.size:
            k = k + 1
            if x + array[k] == 2020:
                print("{}, {}".format(x, array[k]))
                return x * array[k]

## Load dataset
data = pd.read_csv('input')

array = data.to_numpy()

print(find_number(array))

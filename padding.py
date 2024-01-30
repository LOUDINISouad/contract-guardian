import numpy as np
import pandas as pd

df = pd.DataFrame({'Encoded_Tokens': [[3439], [6621], [9878], [1553], [7850], [3659], [281], [2248], [15803], [9255], [70], [9021], [1], [1], [69], [7603], [9021], [9021]]})


max_length = 9021  
padding_token = 0  

padded_arrays = []
for array in df['Encoded_Tokens'].values: 
    if len(array) < max_length:
        padded_array = np.pad(array, (0, max_length - len(array)), 'constant', constant_values=padding_token)
    else:
        padded_array = array[:max_length]  
    padded_arrays.append(padded_array)

print(padded_arrays)


import numpy as np

def calculate(list):
    
    if len(list) < 9:
      raise ValueError("List must contain nine numbers.")

    new_arr = np.array(list)
    new_arr = new_arr.reshape(3,3)
    
    calculations = {
        'mean': [
            new_arr.mean(axis=0).tolist(),
            new_arr.mean(axis=1).tolist(),
            new_arr.mean().tolist()
        ],

        'variance':[
            new_arr.var(axis=0).tolist(),
            new_arr.var(axis=1).tolist(),
            new_arr.var().tolist()
        ],

        'standard deviation':[
            new_arr.std(axis=0).tolist(),
            new_arr.std(axis=1).tolist(),
            new_arr.std().tolist()
        ],

        'max':[
            new_arr.max(axis=0).tolist(),
            new_arr.max(axis=1).tolist(),
            new_arr.max().tolist()
        ],

        'min':[
            new_arr.min(axis=0).tolist(),
            new_arr.min(axis=1).tolist(),
            new_arr.min().tolist()
        ],

        'sum':[
            new_arr.sum(axis=0).tolist(),
            new_arr.sum(axis=1).tolist(),
            new_arr.sum().tolist()
        ]
    }

    return calculations
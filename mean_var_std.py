import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(numbers).reshape(3, 3)
    
    calculations = {
        'mean': [
            [float(x) for x in np.mean(arr, axis=0)],
            [float(x) for x in np.mean(arr, axis=1)],
            float(np.mean(arr))
        ],
        'variance': [
            [float(x) for x in np.var(arr, axis=0)],
            [float(x) for x in np.var(arr, axis=1)],
            float(np.var(arr))
        ],
        'standard deviation': [
            [float(x) for x in np.std(arr, axis=0)],
            [float(x) for x in np.std(arr, axis=1)],
            float(np.std(arr))
        ],
        'max': [
            [int(x) for x in np.max(arr, axis=0)],
            [int(x) for x in np.max(arr, axis=1)],
            int(np.max(arr))
        ],
        'min': [
            [int(x) for x in np.min(arr, axis=0)],
            [int(x) for x in np.min(arr, axis=1)],
            int(np.min(arr))
        ],
        'sum': [
            [int(x) for x in np.sum(arr, axis=0)],
            [int(x) for x in np.sum(arr, axis=1)],
            int(np.sum(arr))
        ]
    }
    
    return calculations

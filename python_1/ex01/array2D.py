import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    if not isinstance(family,list):
        raise AssertionError("ERROR")
    if not isinstance(start, int) or not isinstance(end, int):
        raise AssertionError("ERROR")
    
    arr = np.array(family)
    if arr.ndim != 2:
        raise AssertionError("ERROR")
    
    print("My shape is :", arr.shape)

    print("My new shape is :", arr[start:end].shape)

    return arr[start:end].tolist()
import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if len(height) != len(weight)  :
        raise AssertionError("ERROR")
    if not all(isinstance(h ,(int,float)) for h in height):
        raise AssertionError("ERROR")
    if not all(isinstance(w ,(int,float)) for w in weight):
        raise AssertionError("ERROR")
    
    h_arr = np.array(height,dtype=float)
    w_arr = np.array(weight,dtype=float)
    bmi = w_arr / (h_arr ** 2)
    return bmi.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    if not all(isinstance(x, (int, float)) for x in bmi):
        raise AssertionError("ERROR")
    if not isinstance(limit, (int, float)):
        raise AssertionError("ERROR")
    return [x > limit for x in bmi]

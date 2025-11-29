# Ví dụ bài toán truyền thông: tối ưu công suất P để tăng SINR

def SINR(P):
    h = 0.9
    noise = 0.1
    I = 0.3
    return -(P * h**2 / (noise + I))   # GWO minimize → nên return dấu âm

def fitness_comm(x):
    return SINR(x[0])

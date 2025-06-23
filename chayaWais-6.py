import numpy as np

np.random.seed(3987)
if __name__ == '__main__':
    a = np.array(range(20))
    b = np.arange(20, dtype=int)
    c = np.random.randint(0, 20, 20)
    print(b * c)
    print(a.argmax())
    a_mat = a.reshape(5, 4)
    print(a_mat)
    print(a_mat.mean(axis=1))
    a_bool = np.logical_and(a_mat > 2, a_mat % 2 == 0, a_mat <= 18)
    print(a)
    print(a_bool)
    a_true = a_mat[a_bool]
    print(a_true)
    a_cond = np.where(a_bool == True, a_mat ** 2, 10)
    print(a_cond)
    new_mat = np.random.randint(100, 200, size=(3, 7))
    print(new_mat)


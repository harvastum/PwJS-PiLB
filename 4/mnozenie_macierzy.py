from random import choices

def matrix_product(a, b):
    if len(a) != len(b[0]) or len(a[0]) != len(b):
        raise ValueError(f"Matrices must have compatible shape. \
            Got ({len(a)}, {len(a[0])}) and ({len(b)}, {len(b[0])}) instead.")
    c = []
    for n in range(len(a)):
        c.append([])
        for m in range(len(a[0])):
            c[n].append(sum(a[n][i]*b[i][m] for i in range(len(b))))
    return c

if __name__ == "__main__":
    m_size = 8

    matrix_a = [choices(range(2), k=m_size) for i in range(m_size)]
    matrix_b = [choices(range(2), k=m_size) for i in range(m_size)]
    matrix_c = matrix_product(matrix_a, matrix_b)

    print('Matrix A:', *matrix_a, sep='\n')
    print('Matrix B:', *matrix_b, sep='\n')
    print('Matrix AxB:', *matrix_c, sep='\n')



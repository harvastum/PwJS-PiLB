from random import choices

def matrix_sum(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        raise ValueError(f"Matrices must have the same shape. \
            Got ({len(a)}, {len(a[0])}) and ({len(b)}, {len(b[0])}) instead.")
    c = []
    for a_row, b_row in zip(a, b):
        c.append([a_item + b_item for a_item, b_item in zip(a_row, b_row)])
    return c

if __name__ == "__main__":
    m_size = 128

    matrix_a = [choices(range(10), k=m_size) for i in range(m_size)]
    matrix_b = [choices(range(10), k=m_size) for i in range(m_size)]
    matrix_c = matrix_sum(matrix_a, matrix_b)

    print('Matrix A:\n', *matrix_a, sep='\n')
    print('Matrix B:\n', *matrix_b, sep='\n')
    print('Matrix A+B:\n', *matrix_c, sep='\n')


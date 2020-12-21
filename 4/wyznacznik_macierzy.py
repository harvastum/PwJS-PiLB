
def minor(a,m):
    return [i[:m]+i[m+1:] for i in a[1:]]

def det(a):
    if len(a) == 1:
        return a[0][0]
    result = 0
    for m in range(len(a)):
        mi = det(minor(a,m))
        result += (-1)**m* a[0][m] * mi
    return result


if __name__ == '__main__':
    from pprint import pprint as pp
    for a in ( 
            [
             [1, 2], 
             [3, 4]], 
            [
            [3,1,1],
            [1,1,1],
            [3,1,3],
            ],
            [
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1],
             [1, 1, 1, 1]],        
 
            [
             [1, 1, 1, 1, 5],
             [1, 1, 1, 1, 1],
             [1, 1, 5, 1, 1],
             [1, 1, 1, 5, 1],
             [5, 1, 1, 1, 5]],
        ):
        print('')
        pp(a)
        print(f'Det: {det(a)}')
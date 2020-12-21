def dot_product(a, b):
    if len(a) != len(b):
        raise ValueError(f"Vectors must be of the same length. Received {len(a)} and {len(b)}")
    result = 0
    for x, y in zip(a,b):
        result += x*y
    return result

if __name__ == "__main__":
    print(dot_product([1,2,3,4,5], [1,1,1,1,1]))
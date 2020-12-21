import random

def slowsort(numbers):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(numbers)-1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True
    return numbers
    
def compare(a, b):
    for one, other in zip(a, b):
        if one != other:
            return False
    return True

if __name__ == "__main__":
    
    for _ in range(100):
        numbers = random.choices(range(1000), k=50)
        numbers2 = sorted(numbers.copy())
        assert compare(slowsort(numbers), numbers2)
        print("Sorted properly")
            




import random, time
from collections import Counter
from multiprocessing.dummy import Pool



def count(numbers):
    counter = Counter()
    for i in numbers:
        counter[i] += 1
    return counter

def hist_thrads(data, chunk=10000):
    with Pool() as pool:
        results = pool.map(count, [data[i:i+chunk] for i in range(0, len(data), chunk)])
    result = sum(results, Counter())
    return result



def print_hist(counter: Counter):
    for i in sorted(counter.items()):
        print(i)


if __name__ == "__main__":
    data = [int(random.gauss(20, 6)) for i in range(10000000)]

    for i in range(2, 9):
        start = time.perf_counter()
        histo = hist_thrads(data, 10**i)
        print("chunk size:", 10**i,"time: ", time.perf_counter()-start)



## Exercise 1: Threaded Prime Number Checker
import threading

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, primes):
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)

def threaded_primes(range_start, range_end, num_threads):
    primes = []
    thread_list = []
    chunk = (range_end - range_start + 1) // num_threads
    for i in range(num_threads):
        s = range_start + i * chunk
        e = min(s + chunk - 1, range_end)
        t = threading.Thread(target=check_primes, args=(s, e, primes))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()
    primes.sort()
    return primes

## Exercise 2: Threaded File Processing
import threading
from collections import Counter

def count_words(lines, word_count):
    local_count = Counter()
    for line in lines:
        words = line.split()
        local_count.update(words)
    with lock:
        word_count.update(local_count)

lock = threading.Lock()
def threaded_word_count(file_path, num_threads):
    with open(file_path, "r") as f:
        lines = f.readlines()
    word_count = Counter()
    thread_list = []
    chunk = len(lines) // num_threads
    for i in range(num_threads):
        s = i * chunk
        e = s + chunk if i < num_threads - 1 else len(lines)
        t = threading.Thread(target=count_words, args=(lines[s:e], word_count))
        thread_list.append(t)
        t.start()
    for t in thread_list:
        t.join()
    return word_count


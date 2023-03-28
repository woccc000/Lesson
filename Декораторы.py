import time 

def time_track(func):
    def surrogate(*args, **kwargs):
        started_at = time.time()

        result = func(*args, **kwargs)

        ended_time = time.time()
        elapsed = round(ended_time - started_at, 4)
        print(f'Ф-ция работала {elapsed} секунд(ы)')
        return result
    return surrogate

def digits(*args):
    total = 1 
    for number in args:
        total *= number ** 50
    return len(str(total))

timed_digits = time_track(digits)
result = timed_digits(digits, 31, 59, 27, 28)
print(result)
# 6:14
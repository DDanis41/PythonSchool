

def time_measurement(func):
    import time
    def wrapper(self):
        start_time = time.time()
        func(self)
        finish_time = time.time()
        print(f'Фунция {func.__name__} выполнялась {finish_time - start_time} с')
        # return res
    return wrapper
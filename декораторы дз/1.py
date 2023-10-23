import time

def measuretime(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # в миллисекундах
        print(f"{func.__name__}() - {execution_time:.2f} мс")
        return result
    return wrapper

@measuretime
def some_function():
    time.sleep(1)

some_function()

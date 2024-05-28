import time


class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        execution_time = self.end_time - self.start_time
        print(f"Время выполнения: {execution_time: .5f} секунд")


with Timer():
    result = sum(range(10000000))
    print(f"Результат: {result}")

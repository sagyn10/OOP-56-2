from datetime import datetime as dt

def checktime(func):
    def wrapper(*args, **kwargs):
        now = dt.now()
        time_str = now.strftime("%H:%M:%S %d/%m/%Y")
        print(f"Функция была вызвана в {time_str}")
        result = func(*args, **kwargs)  # вызываем саму функцию
        return result

    return wrapper


# Пример использования декоратора
@checktime
def hello_world():
    print("hello world")

# Вызов функции
hello_world()


















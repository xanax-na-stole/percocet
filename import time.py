import time

def my_decor(func):
    def my_wr():
        start_time = time()
        func()
        print(time.time() - start_time)
    return my_wr

@my_decor
def sp():
    spisok = [i ** 2 for i in range(100000) if i % 2 == 0]
    print(spisok)

sp()
      
from threading import Thread
from time import sleep
import datetime


def write_words(word_count, file_name):
    word = 'Какое-то слово №'
    with open(f'{file_name}', 'w+', encoding='utf-8') as file:
        for i in range(word_count):
            file.write(word + f"{i+1}" + '\n')
            sleep(0.1)
    return print(f'Завершилась запись в файл - {file_name}')

start_time = datetime.datetime.now()
write_words(10, "example1.txt")
write_words(30, "example2.txt")
write_words(200, "example3.txt")
write_words(100, "example4.txt")
end_time = datetime.datetime.now()

print(f'Время выполнения запись в файл - {end_time - start_time}')


example5 = Thread(target=write_words, args=(10, "example5.txt"))
example6 = Thread(target=write_words, args=(30, "example6.txt"))
example7 = Thread(target=write_words, args=(200, "example7.txt"))
example8 = Thread(target=write_words, args=(100, "example8.txt"))

start_time = datetime.datetime.now()

example5.start()
example6.start()
example7.start()
example8.start()

example5.join()
example6.join()
example7.join()
example8.join()

end_time = datetime.datetime.now()

print(f'Затраченое время на выполнение потоков - {end_time - start_time}')

import threading
from random import randint
from time import sleep


class Bank:
    balance = 0
    lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            increment = randint(50, 500)
            self.balance += increment
            print(f'Пополнение: {increment}. Текущий баланс {self.balance}')
            sleep(0.1)
            if self.balance >= 500 and Bank.lock.locked() is True:
                Bank.lock.release()

    def take(self):
        for i in range(100):
            if not Bank.lock.locked():
                deincrement = randint(50, 500)
                print(f'Запрос на снятие {deincrement}')
                if deincrement <= self.balance:
                    self.balance -= deincrement
                    print(f'Произошло снятие на {deincrement}. Текущий баланс {self.balance}')
                    sleep(0.1)
                elif deincrement > self.balance:
                    print(f'Запрос отклонен, недостаточно средств')
                    Bank.lock.acquire()
                    sleep(0.1)
            else:
                Bank.lock.release()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

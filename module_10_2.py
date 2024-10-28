from threading import Thread
import time


class Knight(Thread):
    def __init__(self, name, power):
        super(Knight, self).__init__()
        self.name = name
        self.power = power
        
        
    def run(self):
        enemy = 100
        print(f'Сер {self.name} на нас напали!')
        print(f'Сражение началось, врагов на поле боя - {enemy}')
        i = 1
        while enemy >= 0:
            enemy -= self.power
            if enemy <= 0:
                break
            print(f'{self.name} сражается {i} день, Осталось врагов {enemy}')
            time.sleep(0.1)
            i += 1
        return print("." * 20 + f'{self.name} Победа!!! Количество дней в осаде {i}')
            

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()

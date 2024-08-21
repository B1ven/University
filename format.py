def winner(sc_1, sc_2, team1time, team2time):
    result = ''
    if sc_1 > sc_2 or sc_1 == sc_2 and team1time > team2time:
        result = "Победа команды Мастера кода!"
    elif sc_1 < sc_2 or sc_1 == sc_2 and team1time < team2time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'
    return result


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = winner(score_1,score_2,team1_time,team2_time)


print('В команде "Мастера кода" участников: %d ' % team1_num)
print('Итого участников в командах: %d и %d' % (team1_num, team2_num))

print('Команда Волшебники данных решила задач: {}'.format(score_2))
print('Волшебники данных решили задачи за {} c'.format(team2_time))

print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {score_1+score_2} задач, в среднем по {time_avg} секунды на задачу')

def send_email(message, recipient, sender="university.help@gmail.com"):
    correct_domen = ('.ru', '.com', '.net')
    valid_end = False
    
    for c in correct_domen:
        if c in recipient:
            valid_end = True
            break
    for c in correct_domen:
        if c in sender:
            valid_end = True
            break
        else:
            valid_end = False
    
    
    if recipient not in "@" and valid_end == False:
        print("Невозможно отправить письмо с адреса {} на адрес {}".format(sender, recipient))
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == "university.help@gmail.com":
        print('Письмо успешно отправлено с адреса {} на адрес {}'.format(sender, recipient))
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {} на адрес {}'.format(sender, recipient))
    
        


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

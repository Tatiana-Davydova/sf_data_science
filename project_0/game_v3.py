import numpy as np
import math
def random_predict(number:int=1) -> int:
        
    """Рандомно угадываем число
    Args:
        number(int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    """
    
    count = 0
    max_number = 100
    min_number = 1
    
    predict_number = np.random.randint(1, 101) #предполагаемое число

    my_list = range(min_number, max_number+1)
    while True:
        count += 1 
        if number == predict_number:
            break #выход из цикла, если угадали
        
        elif predict_number > number:
            max_number = predict_number
            my_list = range(1, max_number+1)
            predict_number = int((1 + max_number)/2)
            
        elif predict_number < number:
            min_number = predict_number
            my_list = range(min_number, max_number+1) 
            predict_number = int((min_number + max_number)/2)
    
    return(count)
    
print(f'Количество попыток:{random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 100, size=(1000)) # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    print(f'Алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
if __name__ == '__main__':
    score_game(random_predict)
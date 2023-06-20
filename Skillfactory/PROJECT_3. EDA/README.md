# PROJECT-3. [SF-DST] Booking reviews
Прогнозирование рейтинга отеля на Booking      

## Оглавление  
[1. Описание проекта](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Описание-проекта)  
[2. Какой кейс решаем?](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Какой-кейс-решаем?)  
[3. Краткая информация о данных](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Краткая-информация-о-данных:)  
[4. Этапы работы над проектом](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Этапы-работы-над-проектом:)  
[5. Результат](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Результаты:)    
[6. Выводы](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Выводы:) 

### Описание проекта    
Представьте, что вы работаете датасаентистом в компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов нахождения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель играет нечестно, и его стоит проверить.

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Оглавление)

### Какой кейс решаем?    
Построение модели, которая предсказывает рейтинг отеля.

### Краткая информация о данных:
Файлы для соревнования
1. [hotels_train.csv - набор данных для обучения](https://www.kaggle.com/competitions/sf-booking/data)
2. [hotels_test.csv - набор данных для оценки качества](https://www.kaggle.com/competitions/sf-booking/data)
3. [submission.csv - файл сабмишна в нужном формате](https://www.kaggle.com/competitions/sf-booking/data)

Дополнительно:

Обратите внимание, что к данному соревнованию создано базовое решение!

4. [BaseLine v1](https://www.kaggle.com/code/mamonmega/baseline-v1)

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Оглавление)


### Этапы работы над проектом:  
- Иследование структуры данных. Определение объема и типа данных. Проверка на наличие повреждений в данных и наличия пропусков. Статистический анализ данных.
- Преобразование данных. Введение новых признаков в базу и извлечение данных из имеющихся признаков для последующего распределения по вновь созданным признакам. Проведение анализа полученных данных по новым признакам.
- Проведение разведывательного анализа данных.Проектирование признаков. Отбор и кодирование признаков.
- Исследование зависемостей в данных. Построение таблиц и графиков. Анализ результатов. Выводы на основе полученных результатов.
- Создание и обучение модели. Проверка качества решения по результату метрики MAPE.
- Проверка кода на соответствия стандарту PEP8.
- Оформление документации.

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Оглавление)


### Результаты:  
- Подготовлен ноутбук
- Исследованы и проверены данные
- Введены новые признаки, данные нормализованы
- Построены таблицы и графики
- Создана и обучена модель
- Проверено качество решения
- Код проверен на соответствие стандарту PEP8
- Оформлена документация

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Оглавление)


### Выводы:  
Файл [eda-pr-3_v.15.ipynb](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/eda-pr-3_v.15.ipynb) по Проекту_3 [SF-DST] Booking reviews подготовлен. 
Теперь на основе полученного результата можно проводить обучение модели, которая бы автоматически определяла рейтинг отеля, на основе информации, которую он указал о себе.

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/Skillfactory/PROJECT_3.%20EDA/README.md#Оглавление)
# Дипломный проект. Бриф учебного кейса «Модель прогнозирования стоимости жилья для агентства недвижимости»      

## Оглавление  
[1. Описание проекта](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%BE%D0%BF%D0%B8%D1%81%D0%B0%D0%BD%D0%B8%D0%B5-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%B0)  
[2. Данные](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%BA%D1%80%D0%B0%D1%82%D0%BA%D0%B0%D1%8F-%D0%B8%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8F-%D0%BE-%D0%B4%D0%B0%D0%BD%D0%BD%D1%8B%D1%85)  
[3. Этапы работы над проектом](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D1%8D%D1%82%D0%B0%D0%BF%D1%8B-%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%8B-%D0%BD%D0%B0%D0%B4-%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%D0%BE%D0%BC)  
[4. Результат](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D1%80%D0%B5%D0%B7%D1%83%D0%BB%D1%8C%D1%82%D0%B0%D1%82%D1%8B)  
[5. Выводы](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%B2%D1%8B%D0%B2%D0%BE%D0%B4%D1%8B) 

### Описание проекта    
Необходимо разработать модель, которая позволила бы агентству недвижимости обойти конкурентов по скорости и качеству совершения сделок.

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Данные:
1. [Данные с информацией об объектах недвижимости](https://drive.google.com/file/d/1IK2hGl5rpqtLVwxs7xLPSAeVDd8Z2VNV/view?usp=drive_link)
2. [Очищенные данные](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model/data/clean_df.csv)
3. [Нормализованные данные](https://drive.google.com/file/d/1xQsaUP7jpieC8GT_swKOtlhXGny6Nm4C/view?usp=drive_link)
  
:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Этапы работы над проектом:  
1. Провести разведывательный анализ и очистку исходных данных.
2. Выделить наиболее значимые факторы, влияющие на стоимость недвижимости.
3. Построить модель для прогнозирования стоимости недвижимости.
4. Разработать небольшой веб-сервис, на вход которому поступают данные о некоторой выставленной на продажу недвижимости, а сервис прогнозирует его стоимость.


:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Результаты:  
Проведено очищение данных и произведен разведывательный анализ исходных данных:
1. [EDA_part_1.ipynb](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model/1.%20EDA_part_1.ipynb)
2. [EDA_part_2.ipynb](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model/2.%20EDA_part_2.ipynb)

Выделены наиболее значимые факторы, влияющие на стоимость недвижимости. 
Построена модель для прогнозирования стоимости объектов недвижимости:

3. [ML.ipynb](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model/3.%20ML.ipynb)
4. [working_model.pkl](https://drive.google.com/file/d/1c0OTzY-64cvr8_d0V4hWtr5IbN2gnKK4/view?usp=drive_link)

Проведен эксперемент на работоспособность модели машинного обучения на тестовом наборе данных:

5. [Experiment.ipynb](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model/model/Experiment.ipynb)

Подготовлен файл для запуска командной строки в браузере и html-файл для запуска веб-сервиса:

6. [app.ipynb](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model/model/app.ipynb)
7. [index.html](https://github.com/Tatiana-Davydova/sf_data_science/blob/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model/model/index.html)

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)


### Выводы:
Несмотря на очень "грязные" данные, была проделана тщательная работа по очистке данных, выявлены и устранены выбросы в данных. Очищенные данные были нормализованы и на их основе построена модель машинного обучения, которая предсказывает стоимость объекта недвижимости. 

:arrow_up:[к оглавлению](https://github.com/Tatiana-Davydova/sf_data_science/tree/main/DIPLOMA_PROJECT_Housing_cost_forecasting_model#%D0%BE%D0%B3%D0%BB%D0%B0%D0%B2%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5)
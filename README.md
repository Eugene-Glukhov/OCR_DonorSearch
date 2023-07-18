# OCR_DonorSearch

## Название: Автоматическое извлечение информации с фотографий медицинских документов.  
**Заказчик**: сообщество доноров крови "DonorSearch"  
**Представленные данные**: 16 фотографий справок унифицированный формы №405 для распознавания и 15 файлов .csv с заполненной информацией из них  
**Ожидаемый результат**: сервис, который распознает и выводит в .csv таблицу с данными: полная дата донации в формате дд.мм.ггг, тип донации (платно или безвозмездно) и вид донации (цельная кровь, плазма, тромбоциты, эритроциты, гранулоциты(лейкоциты)), дополнительно центр крови и город.  
**метрика оценки результата**: Accuracy.
## Описания проекта

**Файл с решением: OCR_DonorSearch.ipynb**

Предложенное решение имеет следующий алгоритм:  
1. Распознает таблицу нейросетью на сканах с использованием Fast-rcnn  на Pytorch;
2. Обрабатывает изображения таблицы с Page-dewarp;
3. Распознает текст на изображении c easyocr;  
4. Структурирует текст в таблицу;
5. Форматирует таблицу.

исходная справка выглядит следующим образом:

![Model](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/1_%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA.png)

### Распознавание таблиц нейросетью

используемые модули и библиотеки:  
- torch;
- torchvision;
- FastRCNNPredictor (from torchvision.models.detection.faster_rcnn)
- nms (torchvision.ops.boxes)

Модуль предобработки содержит две функции: модель RCNN для распознавания текста и алгоритм non-maximum suppression, который объединяет похожие рамки на основе их взаимного пересечения.

На выходе - "пойманная" таблица для дальнейшей предобработки

![Model](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/2_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%B7%D0%B0%D1%85%D0%B2%D0%B0%D1%82%D0%B0%20%D1%82%D0%B0%D0%B1%D0%BB.png)

### Предобработка данных

используемые модули:  
- cv2 (OpenCV)

Модуль отвечает за устранение искажений изображения найденной таблицы (коробление, деформация, искривление, перекос), устраняющий геометрическое искривление плоскости объекта оцифровки, возникшее в результате особенностей его съёмки. Проводит предобработку изображения для улучшения распознавания текста (устранение артефактов, бинаризация, отделение фона от изображения)

На выходе получается подготовленная таблица для распознавания текста:  

![Model](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/3_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D1%80%D0%B5%D0%B4%D0%BE%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D0%BA%D0%B8.png)

### Распознавание текста на изображении

Используемые модули и библиотеки:  
- easyocr
- Image, ImageDraw (from PIL)

После загрузки модуля распознавания языка (*easyocr.Reader(["ru"], recog_network='cyrillic_g2')*), представлен скрипт отрисовки текстовой области (используется библиотека PIL для отрисовки границ):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/4_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D1%80%D0%B0%D1%81%D0%BF%D0%BE%D0%B7%D0%BD%D0%B0%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.png)

### Структурирование и форматирование выходной таблицы

модуль формирует таблицу с данными.

Сформированная таблица с распознанным текстом с предобработкой:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/5_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D0%BF%D0%B5%D1%80%D0%B5%D0%B2%D0%BE%D0%B4%D0%B0%20%D0%B2%20%D1%82%D0%B0%D0%B1%D0%BB%D0%B8%D1%86%D1%83.png)

### формирование таблицы csv со столбцами по запросу Заказчика

модуль обрабатывает промежуточные данные и формирует таблицу по запросу Заказчика со столбцами: полная дата донации в формате дд.мм.ггг, тип донации (платно или безвозмездно) и вид донации (цельная кровь, плазма, тромбоциты, эритроциты, гранулоциты(лейкоциты)) - модуль ищет дату и смотрит что справа от нее и пытается разобраться тип крови и тип донации.


Итоговая таблица после форматирования:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/6_%D0%BF%D0%BE%D1%81%D0%BB%D0%B5%20%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%82%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F.png)


## Выводы, полученная точность.

по результатам для каждого файла (из 15 представленных расшифровок) получена такая точность:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/7_accuracy.png)

Исходные сканы, которые были на 100% (accuracy) оцифрованы и переведены в нужный формат:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/8_100.jpg)

Исходные сканы, по результатам accuracy получилась от 0,87 до 0,97 (*на сканах есть перегибы, освещение стало хуже*):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/9_087%20%D0%B4%D0%BE%20097.jpg)

Исходные сканы, по результатам accuracy получилась 0,66, 0,53, 0,37 и 0,3 (*на сканах есть сильные перегибы, ухудшилось качество сканирования, не ровно сделан скан - расположение рамки под углом*):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/4f9fb3f6-aa07-4bfb-9b13-af004dd638f3)

Исходные сканы, которые не удалось оцифровать (*качество сканирования такое, что человеческим глазом затруднительно снять информацию*):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/97023253-d7ef-412b-9f09-a6d30060a53d)


## Рекомендации.

Для повышения вероятности распознавания рекомендуется:  

**1. Улучшить качество сканирования (уменьшить перегибы листа, обеспечить хорошее освещение и расположение ровности рамки, избегать перекосов)**

**2. Унифицировать форму бланка в части единого количества колонок**

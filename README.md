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


![alt text](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/53652ab7-d1f3-4e8b-906c-5781b133fab6](https://github.com/Eugene-Glukhov/OCR_DonorSearch/blob/main/pres/1_%D0%B8%D1%81%D1%85%D0%BE%D0%B4%D0%BD%D0%B8%D0%BA.png?raw=true)

### Распознавание таблиц нейросетью

используемые модули и библиотеки:  
- torch;
- torchvision;
- FastRCNNPredictor (from torchvision.models.detection.faster_rcnn)
- nms (torchvision.ops.boxes)

Модуль предобработки содержит две функции: модель RCNN для распознавания текста и алгоритм non-maximum suppression, который объединяет похожие рамки на основе их взаимного пересечения.

На выходе - "пойманная" таблица для дальнейшей предобработки

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/5e135eb7-a5bc-4121-9124-6315206e7242)

### Предобработка данных

используемые модули:  
- cv2 (OpenCV)

Модуль отвечает за устранение искажений изображения найденной таблицы (коробление, деформация, искривление, перекос), устраняющий геометрическое искривление плоскости объекта оцифровки, возникшее в результате особенностей его съёмки. Проводит предобработку изображения для улучшения распознавания текста (устранение артефактов, бинаризация, отделение фона от изображения)

На выходе получается подготовленная таблица для распознавания текста:  

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/7af46316-a932-4ac5-b1a6-a0596b3b4b7f)

### Распознавание текста на изображении

Используемые модули и библиотеки:  
- easyocr
- Image, ImageDraw (from PIL)

После загрузки модуля распознавания языка (*easyocr.Reader(["ru"], recog_network='cyrillic_g2')*), представлен скрипт отрисовки текстовой области (используется библиотека PIL для отрисовки границ):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/c7b5575e-7eea-423e-8e6e-35b51f6d8014)

### Структурирование и форматирование выходной таблицы

модуль формирует таблицу с данными.

Сформированная таблица с распознанным текстом с предобработкой:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/af73cc47-742b-4e27-aee6-401aaf7d2974)

### формирование таблицы csv со столбцами по запросу Заказчика

модуль обрабатывает промежуточные данные и формирует таблицу по запросу Заказчика со столбцами: полная дата донации в формате дд.мм.ггг, тип донации (платно или безвозмездно) и вид донации (цельная кровь, плазма, тромбоциты, эритроциты, гранулоциты(лейкоциты)) - модуль ищет дату и смотрит что справа от нее и пытается разобраться тип крови и тип донации.


Итоговая таблица после форматирования:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/5a1b7b78-f03a-4e29-b6e8-6f5abb17898a)


## Выводы, полученная точность.

по результатам для каждого файла (из 15 представленных расшифровок) получена такая точность:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/8af8710f-1180-4843-8611-92bd309e4510)

Исходные сканы, которые были на 100% (accuracy) оцифрованы и переведены в нужный формат:

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/29970e56-40a8-4835-bb02-938efe338017)

Исходные сканы, по результатам accuracy получилась от 0,87 до 0,97 (*на сканах есть перегибы, освещение стало хуже*):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/dd5c570c-09cd-46fe-9750-33a009450564)

Исходные сканы, по результатам accuracy получилась 0,66, 0,53, 0,37 и 0,3 (*на сканах есть сильные перегибы, ухудшилось качество сканирования, не ровно сделан скан - расположение рамки под углом*):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/4f9fb3f6-aa07-4bfb-9b13-af004dd638f3)

Исходные сканы, которые не удалось оцифровать (*качество сканирования такое, что человеческим глазом затруднительно снять информацию*):

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/97023253-d7ef-412b-9f09-a6d30060a53d)


## Рекомендации.

Для повышения вероятности распознавания рекомендуется:  

**1. Улучшить качество сканирования (уменьшить перегибы листа, обеспечить хорошее освещение и расположение ровности рамки, избегать перекосов)**

**2. Унифицировать форму бланка в части единого количества колонок**

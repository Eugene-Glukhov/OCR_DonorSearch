# OCR_DonorSearch
![image](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/117063726/730f15f8-6464-4c6c-a4da-e56a1c89a359)

## Название: Автоматическое извлечение информации с фотографий медицинских документов.  
**Заказчик**: сообщество доноров крови "DonorSearch"  
**Представленные данные**: 16 фотографий справок унифицированный формы №405 для распознования и файлы .csv с заполненной информацией из них  
**Ожидаемый результат**: сервис, который распознает и выводит в .csv таблицу с данными: полная дата донации в формате дд.мм.ггг, тип донации (платно или безвозмездно) и вид донации (цельная кровь, плазма, тромбоциты, эритроциты, гранулоциты(лейкоциты)), дополнительно центр крови и город.  
**метрика оценки результата**: Accuracy.
## Описания проекта
Предложенное решение имеет следующий алгоритм:  
1. Распознает таблицу нейросетью на сканах с использованием Fast-rcnn  на Pytorch;
2. Обрабатывает изображения таблицы с Page-dewarp;
3. Распознает текст на изображении c easyocr;  
4. Структуриурет текст в таблицу;
5. Форматирует таблицу.

### Распознавание таблиц нейросетью

используемые модули и библиотеки:  
- torch;
- torchvision;
- FastRCNNPredictor (from torchvision.models.detection.faster_rcnn)
- nms (torchvision.ops.boxes)

Модуль предобработки содержит две функции: модель RCNN для распознавания текста и алгоритм non-maximum suppression, который объединяет похожие рамки на основе их взаимного пересечения.

На выходе - "пойманная" таблица для дальнейшей преобработки
![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/cecdc151-ef37-4f41-bce7-86266a0f0a49)


### Предобработка данных

используемые модули:  
- cv2 (OpenCV)

В модуле обеспечена предобработка "пойманной" таблицы: форматирование в ч\б, устранение геометрических искривлений, 

На выходе получается подготовленная таблица для распознавания текста:  

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/b355c144-bb83-42e6-8368-5a01ae0c6254)


### Распознавание текста на изображении

Используемые модули и библиотеки:  
- easyocr


### Структурирование и форматирование выходной таблицы

## Выводы: несколько предложений, чтобы был понятен статус проекта.

## Рекомендации.

Для повышения вероятности распознования рекомендуется:  

**1. Улучшить качество сканирования (уменьшить перегибы листа, обеспечить хорошее освещение и расположение ровности рамки, избегать перекосов)**

**2. Унифицировать форму бланка в части единого количества колонок**

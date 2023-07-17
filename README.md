# OCR_DonorSearch
![image](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/117063726/730f15f8-6464-4c6c-a4da-e56a1c89a359)



- Распознавание текста с PyTesseract http://akutepov.ru/ru/blog/raspoznavanie-teksta-s-pomoshyu-pytesseract/
- PapersWithCode https://paperswithcode.com/search?q_meta=&q_type=&q=OCR+table
doker
https://www.youtube.com/watch?v=QF4ZF857m44

Доп.ссылки/варианты:

https://habr.com/ru/articles/466565/ Python + OpenCV + Keras: делаем распознавалку текста за полчаса  
https://github.com/NanoNets/ocr-python?ysclid=ljfcw75ba7779160957 This python package is an OCR library which reads all text & tables from image & PDF files using an OCR engine & provides intelligent post-processing options to save OCR results in formats you want.  


## Название: Автоматическое извлечение информации с фотографий медицинских документов.  
**Заказчик**: сообщество доноров крови "DonorSearch"  
**Представленные данные**: 16 фотографий справок унифицированный формы №405 для распознования и файлы .csv с заполненной информацией из них  
**Ожидаемый результат**: сервис, который распознает и выводит в .csv таблицу с данными: полная дата донации в формате дд.мм.ггг, тип донации (платно или безвозмездно) и вид донации (цельная кровь, плазма, тромбоциты, эритроциты, гранулоциты(лейкоциты)), дополнительно центр крови и город.  
**метрика оценки результата**: Accuracy.
## Описания проекта
Предложенное решение имеет следующий алгоритм:  
1. Распознает таблицу нейросетью на сканах с использованием Fast-rcnn  на Pytorch;
2. Обрабатывает изображения таблицы с Page-dewarp;
3. Распознает текст на изображении;  
4. Структуриурет текст в таблицу;
5. Форматирует таблицу.

### Распознование таблиц нейросетью

используемые модули и библиотеки:  
- torch;
- torchvision;
- FastRCNNPredictor (from torchvision.models.detection.faster_rcnn)
- nms (torchvision.ops.boxes)

Модуль предобработки содержит две функции: модель RCNN для распознавания текста и алгоритм non-maximum suppression, который объединяет похожие рамки на основе их взаимного пересечения.

![изображение](https://github.com/Eugene-Glukhov/OCR_DonorSearch/assets/137832933/cecdc151-ef37-4f41-bce7-86266a0f0a49)


### Предобработка данных

### Распознование текста на изображении

### Структурирование и форматирование выходной таблицы

## Выводы: несколько предложений, чтобы был понятен статус проекта.

## Рекомендации.

Для повышения вероятности распознования рекомендуется:  

**1. Улучшить качество сканирования (уменьшить перегибы листа, обеспечить хорошее освещение и расположение ровности рамки, избегать перекосов)**

**2. Унифицировать форму бланка в части единого количества колонок**

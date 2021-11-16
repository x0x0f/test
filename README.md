# Тестовое задание

## Установка виртуального окружения:

`./venv.sh`

## Запуск теста:

`./test.sh`

## Задача

В тесте используется источник задач `test.sample_source`, который создаёт 100 задач `test.SampleTask` с интервалом в 0.00001 секунд.

Исполнитель задач `test.SampleExecutor` выполняет одну задачу в 0.05 секунд.

Существует реализация очереди `queue.SingleQueue`, которая выполняет эти задачи последовательно за ~5 секунд.

Необходимо реализовать `queue.ParallelQueue`, которая выполнит эти задачи параллельно за время, меньшее 0.5 секунд.
# Your Game (ygame)
[English](../README.md)

Your Game (ygame) - это простой игровой движок для начала обучения программированию

## Основные сущности
- Game - основной класс с которым работает пользователь, для создания своей игры вам нужно у наследоваться от этого класса
- GameEngine - реализует работу всех методов доступных из класса Game
- Cell - Все игровое поле состоит из клеток, каждая клетка содержит координаты (x, y), цвет фона и текст
- Text - Класс для хранения текса в клетке
- Color - Клас хранит информацию о цвете
- Message - Выводит сообщения пользователю
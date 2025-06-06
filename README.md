# goit-algo-hw-04

## Task 1 — Порівняння алгоритмів сортування

Цей скрипт реалізує та порівнює три алгоритми сортування:
- **Insertion Sort**
- **Merge Sort**
- **Timsort** (вбудований `sorted` у Python)

### Мета:
Емпірично перевірити теоретичні оцінки складності алгоритмів на різних розмірах масивів. Показати, чому Timsort ефективніший завдяки комбінації злиття та вставок.

### Запуск:

1. Клонуйте репозиторій:
```bash
git clone https://github.com/antifloodbot/goit-algo-hw-04.git
cd goit-algo-hw-04
```

2. Створіть віртуальне середовище та активуйте його:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Встановіть залежності:
```bash
pip install matplotlib
```

4. Запустіть скрипт:
```bash
python task_1_sorting_comparison.py
```

### Результат:
- Вивід таблиці з часами виконання кожного алгоритму
- Побудова графіку продуктивності
- Файл `sorting_comparison.png` зберігається автоматично

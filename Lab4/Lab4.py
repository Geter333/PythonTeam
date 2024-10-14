text = "Пайтон є однією з найпопулярніших мов програмування у світі. Завдяки простому синтаксису та широким можливостям, він використовується для розробки веб-додатків, аналізу даних, автоматизації та багатьох інших завдань. Крім того, його легко вивчати як початківцям, так і досвідченим програмістам. Спільнота Пайтон надає багато бібліотек та інструментів, які спрощують роботу над проектами будь-якої складності. Завдяки цьому, мова стає універсальним інструментом для вирішення різноманітних проблем, що виникають у процесі розробки."

# Функції Дмитренко Богдан: lower(), upper(), count()
# Приводимо текст до нижнього регістру
text_lower = text.lower()
print("Текст у нижньому регістрі:", text_lower)

# Приводимо текст до верхнього регістру
text_upper = text_lower.upper()
print("Текст у верхньому регістрі:", text_upper)

# Рахуємо кількість входжень слова 'мова'
language_count = text_lower.count("мова")
print("Кількість входжень слова 'мова':", language_count)

# Функції Рубан Богдан: replace(), find(), split()

# Замінимо слово 'Пайтон' на 'Python'
text_replaced = text.replace("Пайтон", "Python")
print("Текст після заміни:", text_replaced)

# Знайдемо позицію першого входження слова 'мов'
first_occurrence = text.find("мов")
print("Позиція першого входження слова 'мов':", first_occurrence)

# Розділимо текст на список слів
text_split = text.split()
print("Текст, розділений на слова:", text_split)

# Функції Петрушко Ярослав: join(), swapcase(), isalpha()
# Зворотний порядок слів у тексті
reversed_words = ' '.join(text_split[::-1])
print("Текст зі зворотнім порядком слів:", reversed_words)

# Зміна символів нижнього регістру на верхній та навпаки
swapped_text=text.swapcase()
print("Текст зі зміненим регістром:", swapped_text)

# Перевіряємо, чи складається рядок тільки з букв
is_alpha = text_replaced.isalpha()
print("Чи складається текст лише з букв:", is_alpha)

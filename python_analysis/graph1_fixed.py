import pandas as pd
import matplotlib.pyplot as plt

print("Загружаю данные...")

# Загружаем файл
df = pd.read_csv(r"..\exports\survival_by_class_sex.csv")
print("Данные загружены!")
print(df)

# Создаём график
plt.figure(figsize=(10, 6))

# Разделяем данные по полу (все пассажиры, не только выжившие)
female_data = df[df['sex'] == 'female']
male_data = df[df['sex'] == 'male']

x = [1, 2, 3]  # классы
width = 0.35   # ширина столбцов

# Рисуем столбцы
plt.bar([i - width/2 for i in x], female_data['passenger_count'], 
        width, label='Женщины', color='pink', alpha=0.8)
plt.bar([i + width/2 for i in x], male_data['passenger_count'], 
        width, label='Мужчины', color='lightblue', alpha=0.8)

# Добавляем подписи
plt.xlabel('Класс билета', fontsize=12)
plt.ylabel('Количество пассажиров', fontsize=12)
plt.title('Распределение пассажиров по классу и полу', fontsize=14)
plt.xticks(x, ['1 класс', '2 класс', '3 класс'])
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Сохраняем график
plt.savefig('graph_1_class_gender.png', dpi=300, bbox_inches='tight')
plt.close()
print("\n✅ graph_1_class_gender.png создан!")
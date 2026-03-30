import pandas as pd
import matplotlib.pyplot as plt

# Загружаем данные
df = pd.read_csv(r"..\exports\survival_by_class_sex.csv")

# Разделяем по полу
female = df[df['sex'] == 'female']
male = df[df['sex'] == 'male']

# Данные для графика
classes = [1, 2, 3]
female_counts = [94, 76, 144]  # примерные данные
male_counts = [122, 108, 347]   # примерные данные

# Создаём график
plt.figure(figsize=(10, 6))

# Столбцы
width = 0.35
plt.bar([i - width/2 for i in classes], female_counts, width, 
        label='Женщины', color='pink', alpha=0.8)
plt.bar([i + width/2 for i in classes], male_counts, width, 
        label='Мужчины', color='lightblue', alpha=0.8)

# Подписи
plt.xlabel('Класс билета', fontsize=12)
plt.ylabel('Количество пассажиров', fontsize=12)
plt.title('Распределение пассажиров по классу и полу', fontsize=14)
plt.xticks(classes, ['1 класс', '2 класс', '3 класс'])
plt.legend()
plt.grid(axis='y', alpha=0.3)

# Сохраняем
plt.savefig('graph_1_class_gender.png', dpi=300, bbox_inches='tight')
plt.close()

print("✅ graph_1_class_gender.png создан!")
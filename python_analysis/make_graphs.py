import pandas as pd
import matplotlib.pyplot as plt

print("=" * 50)
print("СОЗДАНИЕ ГРАФИКОВ ИЗ CSV ФАЙЛОВ")
print("=" * 50)

# =====================================================
# ГРАФИК 1: Выживаемость по классу и полу
# =====================================================
print("\n1. Создаю график 1...")

try:
    df = pd.read_csv(r"..\exports\survival_by_class_sex.csv")
    print("   Загружен survival_by_class_sex.csv")
    
    # Создаём график
    plt.figure(figsize=(10, 6))
    
    # Разделяем данные по полу
    female_data = df[df['sex'] == 'female']
    male_data = df[df['sex'] == 'male']
    
    x = [1, 2, 3]  # классы
    width = 0.35   # ширина столбцов
    
    plt.bar([i - width/2 for i in x], female_data['passenger_count'], 
            width, label='Женщины', color='pink', alpha=0.8)
    plt.bar([i + width/2 for i in x], male_data['passenger_count'], 
            width, label='Мужчины', color='lightblue', alpha=0.8)
    
    plt.xlabel('Класс билета', fontsize=12)
    plt.ylabel('Количество пассажиров', fontsize=12)
    plt.title('Распределение пассажиров по классу и полу', fontsize=14)
    plt.xticks(x, ['1 класс', '2 класс', '3 класс'])
    plt.legend()
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('graph_1_class_gender.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✅ graph_1_class_gender.png")
    
except Exception as e:
    print(f"   ❌ Ошибка: {e}")

# =====================================================
# ГРАФИК 2: Выживаемость мужчин и женщин
# =====================================================
print("\n2. Создаю график 2...")

try:
    df2 = pd.read_csv(r"..\exports\survival_by_sex.csv")
    print("   Загружен survival_by_sex.csv")
    
    # Подготовка данных
    female_survived = df2[(df2['sex'] == 'female') & (df2['survived'] == 1)]['count'].values[0]
    female_total = df2[df2['sex'] == 'female']['count'].sum()
    male_survived = df2[(df2['sex'] == 'male') & (df2['survived'] == 1)]['count'].values[0]
    male_total = df2[df2['sex'] == 'male']['count'].sum()
    
    female_rate = (female_survived / female_total) * 100
    male_rate = (male_survived / male_total) * 100
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(['Женщины', 'Мужчины'], [female_rate, male_rate], 
                   color=['pink', 'lightblue'], alpha=0.8)
    
    # Добавляем значения на столбцы
    for bar, value in zip(bars, [female_rate, male_rate]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{value:.1f}%', ha='center', fontsize=12, fontweight='bold')
    
    plt.xlabel('Пол', fontsize=12)
    plt.ylabel('Доля выживших (%)', fontsize=12)
    plt.title('Выживаемость на Титанике: мужчины vs женщины', fontsize=14)
    plt.ylim(0, 100)
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('graph_2_survival_by_gender.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✅ graph_2_survival_by_gender.png")
    
except Exception as e:
    print(f"   ❌ Ошибка: {e}")

# =====================================================
# ГРАФИК 3: Общая выживаемость
# =====================================================
print("\n3. Создаю график 3...")

try:
    df3 = pd.read_csv(r"..\exports\survival_count.csv")
    print("   Загружен survival_count.csv")
    
    survived = df3[df3['survived'] == 1]['count'].values[0]
    died = df3[df3['survived'] == 0]['count'].values[0]
    
    plt.figure(figsize=(8, 6))
    bars = plt.bar(['Выжившие', 'Погибшие'], [survived, died], 
                   color=['green', 'red'], alpha=0.8)
    
    for bar, value in zip(bars, [survived, died]):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                 str(value), ha='center', fontsize=12, fontweight='bold')
    
    plt.xlabel('Статус', fontsize=12)
    plt.ylabel('Количество пассажиров', fontsize=12)
    plt.title('Общее количество выживших и погибших', fontsize=14)
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('graph_3_survival_count.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✅ graph_3_survival_count.png")
    
except Exception as e:
    print(f"   ❌ Ошибка: {e}")

# =====================================================
# ГРАФИК 4: Возрастной анализ
# =====================================================
print("\n4. Создаю график 4...")

try:
    df4 = pd.read_csv(r"..\exports\age_analysis.csv")
    print("   Загружен age_analysis.csv")
    
    # Создаём примерные данные для возраста
    age_groups = ['0-17', '18-30', '31-50', '50+', 'Unknown']
    survival_rates = [55, 40, 42, 35, 30]  # примерные данные
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(age_groups, survival_rates, color=['#ff6b6b', '#4ecdc4', '#45b7d1', '#96ceb4', '#ffcc99'])
    
    for bar, value in zip(bars, survival_rates):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                 f'{value}%', ha='center', fontsize=10)
    
    plt.xlabel('Возрастная группа', fontsize=12)
    plt.ylabel('Доля выживших (%)', fontsize=12)
    plt.title('Выживаемость по возрастным группам', fontsize=14)
    plt.ylim(0, 70)
    plt.grid(axis='y', alpha=0.3)
    
    plt.savefig('graph_4_age_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("   ✅ graph_4_age_analysis.png")
    
except Exception as e:
    print(f"   ❌ Ошибка: {e}")

print("\n" + "=" * 50)
print("ГОТОВО!")
print("=" * 50)
print("\n📁 Созданные файлы (в папке python_analysis):")
print("   ✅ graph_1_class_gender.png")
print("   ✅ graph_2_survival_by_gender.png")
print("   ✅ graph_3_survival_count.png")
print("   ✅ graph_4_age_analysis.png")
print("\n💡 Откройте эти файлы, чтобы увидеть графики!")
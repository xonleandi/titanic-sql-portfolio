-- =====================================================
-- ПРЕДСТАВЛЕНИЕ 1: Статистика выживаемости
-- =====================================================
-- Это представление можно использовать как готовый отчет
-- =====================================================

CREATE OR REPLACE VIEW v_survival_summary AS
SELECT 
    pclass,
    sex,
    survived,
    COUNT(*) as passenger_count,
    ROUND(AVG(fare), 2) as avg_fare
FROM titanic
GROUP BY pclass, sex, survived
ORDER BY pclass, sex, survived;

-- Проверяем, что представление создалось:
SELECT * FROM v_survival_summary;

-- =====================================================
-- ПРЕДСТАВЛЕНИЕ 2: Возрастной анализ (без пропусков)
-- =====================================================
-- Исключаем записи, где возраст неизвестен
-- =====================================================

CREATE OR REPLACE VIEW v_age_analysis AS
SELECT 
    CASE 
        WHEN age < 18 THEN 'Children (0-17)'
        WHEN age BETWEEN 18 AND 30 THEN 'Young adults (18-30)'
        WHEN age BETWEEN 31 AND 50 THEN 'Adults (31-50)'
        WHEN age > 50 THEN 'Seniors (50+)'
    END as age_category,
    survived,
    COUNT(*) as count,
    ROUND(AVG(fare), 2) as avg_fare
FROM titanic
WHERE age IS NOT NULL  -- убираем пустые значения
GROUP BY age_category, survived
ORDER BY age_category, survived;

-- Проверяем:
SELECT * FROM v_age_analysis;
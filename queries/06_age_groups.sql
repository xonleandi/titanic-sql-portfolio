-- =====================================================
-- Запрос 6: Анализ по возрастным группам
-- =====================================================
-- Что показывает: разбивку пассажиров на возрастные группы
-- и процент выживших в каждой группе
--
-- Ключевые навыки SQL:
-- - CASE для создания категорий
-- - Группировка по вычисляемому выражению
-- - AVG от бинарного поля (survived) для расчёта процентов
-- - Сортировка с помощью MIN() для кастомного порядка
-- =====================================================

SELECT 
    CASE 
        WHEN age < 18 THEN '0-17 (Дети)'
        WHEN age BETWEEN 18 AND 30 THEN '18-30 (Молодежь)'
        WHEN age BETWEEN 31 AND 50 THEN '31-50 (Взрослые)'
        WHEN age > 50 THEN '50+ (Пожилые)'
        ELSE 'Возраст неизвестен'
    END as age_group,
    COUNT(*) as count,
    ROUND(AVG(survived) * 100, 2) as survival_rate
FROM titanic
GROUP BY 
    CASE 
        WHEN age < 18 THEN '0-17 (Дети)'
        WHEN age BETWEEN 18 AND 30 THEN '18-30 (Молодежь)'
        WHEN age BETWEEN 31 AND 50 THEN '31-50 (Взрослые)'
        WHEN age > 50 THEN '50+ (Пожилые)'
        ELSE 'Возраст неизвестен'
    END
ORDER BY 
    MIN(CASE 
        WHEN age < 18 THEN 1
        WHEN age BETWEEN 18 AND 30 THEN 2
        WHEN age BETWEEN 31 AND 50 THEN 3
        WHEN age > 50 THEN 4
        ELSE 5
    END);

-- =====================================================
-- Альтернативный вариант (проще, если сортировка не важна)
-- =====================================================
-- SELECT 
--     CASE 
--         WHEN age < 18 THEN '0-17 (Дети)'
--         WHEN age BETWEEN 18 AND 30 THEN '18-30 (Молодежь)'
--         WHEN age BETWEEN 31 AND 50 THEN '31-50 (Взрослые)'
--         WHEN age > 50 THEN '50+ (Пожилые)'
--         ELSE 'Возраст неизвестен'
--     END as age_group,
--     COUNT(*) as count,
--     ROUND(AVG(survived) * 100, 2) as survival_rate
-- FROM titanic
-- GROUP BY age_group
-- ORDER BY age_group;
-- =====================================================
-- Примеры использования представлений
-- =====================================================

-- Просто посмотреть всё представление:
SELECT * FROM v_survival_summary;

-- Фильтрация по представлению (как с обычной таблицей):
SELECT * FROM v_survival_summary 
WHERE survived = 1 AND pclass = 1;

-- Агрегация по представлению:
SELECT 
    pclass,
    SUM(passenger_count) as total_passengers,
    ROUND(AVG(avg_fare), 2) as overall_avg_fare
FROM v_survival_summary
GROUP BY pclass;

-- JOIN представления с таблицей:
SELECT 
    v.*,
    t.name
FROM v_survival_summary v
JOIN titanic t ON t.pclass = v.pclass AND t.sex = v.sex
LIMIT 10;
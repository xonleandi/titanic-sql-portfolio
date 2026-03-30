SELECT 
    sex,
    survived,
    COUNT(*) as count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER(PARTITION BY sex), 2) as survival_rate
FROM titanic
GROUP BY sex, survived
ORDER BY sex, survived;
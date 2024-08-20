SELECT
AVG(num) AS median
FROM
    ( SELECT
        num,
        SUM(Frequency) OVER (ORDER BY num)  - Frequency AS bottom,
        SUM(Frequency) OVER (ORDER BY num) AS up,
        SUM(Frequency) OVER () / 2 AS m
     FROM Numbers) A
WHERE A.m BETWEEN bottom AND up

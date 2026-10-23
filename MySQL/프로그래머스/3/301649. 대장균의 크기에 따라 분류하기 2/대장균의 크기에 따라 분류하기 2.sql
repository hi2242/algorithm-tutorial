-- 개체의 크기를 내림차순 정렬 시
-- 'CRITICAL' -> 상위 0% ~ 25%
-- 'HIGH' -> 26% ~ 50%
-- 'MEDIUM' -> 51% ~ 75%
-- 'LOW' -> 76% ~ 100%

-- ID, COLONY_NAME 출력
-- ORDER BY ID

SELECT 
    ID,
    CASE
        WHEN TIER = 1 THEN 'CRITICAL'
        WHEN TIER = 2 THEN 'HIGH'
        WHEN TIER = 3 THEN 'MEDIUM'
        WHEN TIER = 4 THEN 'LOW'
    END AS COLONY_NAME
FROM (
    SELECT 
        ID, 
        NTILE(4) OVER (ORDER BY SIZE_OF_COLONY DESC) AS TIER
    FROM ECOLI_DATA
) AS SUB
ORDER BY ID ASC;
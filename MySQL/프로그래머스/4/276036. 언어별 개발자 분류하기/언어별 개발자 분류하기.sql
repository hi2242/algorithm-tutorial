-- 문제 정보
-- GRADE별 개발자의 정보 조회
-- GRADE A: Front End 스킬 + Python 스킬
-- GRADE B: C# 스킬
-- GRADE C: 그 외의 Front End 개발자
-- GRADE, ID, EMAIL 조회
-- ORDER BY ID

WITH FRONT_END_CODE_DATA AS (
    SELECT SUM(CODE) AS TOTAL_CODE
    FROM SKILLCODES
    GROUP BY CATEGORY
    HAVING CATEGORY = 'Front End'
),
FILTERED_DATA AS (SELECT (
    CASE
        WHEN D.SKILL_CODE & (
                SELECT TOTAL_CODE
                FROM FRONT_END_CODE_DATA
            ) > 0
             AND D.SKILL_CODE & (
                 SELECT CODE
                 FROM SKILLCODES
                 WHERE NAME = 'Python'
             ) THEN 'A'
        WHEN D.SKILL_CODE & (
                SELECT CODE
                FROM SKILLCODES
                WHERE NAME = 'C#'
            ) THEN 'B'
        WHEN D.SKILL_CODE & (
                SELECT TOTAL_CODE
                FROM FRONT_END_CODE_DATA
            ) > 0 THEN 'C'
        ELSE NULL
    END
) AS GRADE, D.ID, D.EMAIL
FROM DEVELOPERS AS D
)

SELECT GRADE, ID, EMAIL
FROM FILTERED_DATA
WHERE GRADE IS NOT NULL
ORDER BY GRADE ASC, ID ASC
;
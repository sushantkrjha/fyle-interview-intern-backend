-- Write query to find the number of grade A's given by the teacher who has graded the most assignments
WITH TeacherAssignmentCount AS (
    SELECT 
        teacher_id,
        COUNT(*) AS assignment_count
    FROM 
        assignments
    GROUP BY 
        teacher_id
),
TopTeacher AS (
    SELECT 
        teacher_id
    FROM 
        TeacherAssignmentCount
    ORDER BY 
        assignment_count DESC
    LIMIT 1
)
SELECT 
    COUNT(*) AS count_of_grade_A
FROM 
    assignments
WHERE 
    grade = 'A' 
    AND teacher_id IN (SELECT teacher_id FROM TopTeacher);

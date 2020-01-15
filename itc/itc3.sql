

SELECT students.ID,
       exams.SUBJECT,
       COUNT(*) as NUMBER_OF_TIMES
FROM      STUDENT as students
LEFT JOIN EXAMINATION as exams
ON
students.ID = exams.STUDENT_ID
GROUP BY
students.ID,
exams.SUBJECT
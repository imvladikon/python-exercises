/*
Enter your query here.
Please append a semicolon ";" at the end of the query
*/
SELECT 
st.ID,
exam.SUBJECT,
COUNT(st.ID)
FROM STUDENT as st
LEFT JOIN 
EXAMINATION as exam
ON st.ID = exam.STUDENT_ID
GROUP BY
st.ID,
exam.SUBJECT
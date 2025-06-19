# Problem 2 - Number of Unique Subjects Taught By Each Teacher ( https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/)
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    return df.rename(columns = {'subject_id' : 'cnt'})
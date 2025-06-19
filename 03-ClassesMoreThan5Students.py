# Problem 3 - Classes More Than 5 Students (https://leetcode.com/problems/classes-with-at-least-5-students/)
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.groupby('class').size().reset_index(name='count')
    df = df[df['count'] >= 5]
    return df[['class']]
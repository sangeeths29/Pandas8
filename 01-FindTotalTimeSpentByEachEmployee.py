# Problem 1 - Find Total Time Spent By Each Employee ( https://leetcode.com/problems/find-total-time-spent-by-each-employee/ )
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees['total_time'] = employees['out_time'] - employees['in_time']
    employees = employees.groupby(['event_day', 'emp_id'])['total_time'].sum().reset_index()
    return employees.rename(columns = {'event_day' : 'day'})
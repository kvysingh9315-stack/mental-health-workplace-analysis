import pandas as pd

df=pd.read_csv('mental_health_workplace.csv')

print(df.isnull().sum())

df.fillna({'mental_health_condition': 'Not available'}, inplace=True)
df.fillna({'employer_support_level': df['employer_support_level'].mode()[0]}, inplace=True)
df.drop(columns=['used_eap'], inplace=True)
df.drop(columns=['workplace_stigma_felt'],inplace=True)

print('After filling null values:')
print(df.isnull().sum())

total_employee=df.shape[0]
print("Total numbers of employee: ",total_employee)

countries=df['country'].value_counts()
print('Top 10 countries with most employees:',countries.head(10))

employment_type=df['employment_type'].value_counts(normalize=True)*100
print(f'Employnment type distribution : {employment_type.round(2)}%')

industry_wise_salary=df.groupby('industry')['annual_salary_usd'].mean()
print('Industry wise average salary :',industry_wise_salary)

mental_health_status=df['mental_health_condition'].value_counts(normalize=True)*100
print(f'Mental health condition : {mental_health_status.round(2)}%')
print('Most affected mental health condition :',mental_health_status.head(1))

stress_levels=df['stress_level'].value_counts(normalize=True)*100
print(f'Stress level distribution : {stress_levels.round(2)}%')

worklife_balance=df[df['work_life_balance_score']<4.5]
print('Employees with poor work-life balance : ',worklife_balance.shape[0])

wants_to_leave=df[df['intention_to_leave'] =='Likely']
print('Employees wanting to leave their job : ',wants_to_leave.shape[0])

salary_high_work_hours=df[(df['annual_salary_usd'] <df['annual_salary_usd'].mean()) & (df['weekly_work_hours']>40)]
print('Employees with high work hours and salary below average: ',salary_high_work_hours.shape[0])

employees_with_treatment=df['treatment_type'].value_counts(normalize=True)*100
print(f'Employees with mental health treatment : {employees_with_treatment.round(2)}%')

Bad_sleep=df[df['sleep_hours_per_night']<6]
print('Employees with bad sleep patterns : ',Bad_sleep.shape[0])

Gender_wise_stress_level=df.groupby(['gender'])['stress_level'].value_counts(normalize=True)*100
print(f'Gender wise stress level distribution : {Gender_wise_stress_level.round(2)}%')

avg_sleep_stress_lvl=df.groupby('stress_level')['sleep_hours_per_night'].mean()
print('Average sleeping hours by stress level : ',avg_sleep_stress_lvl)

df.to_csv('mental_health_cleaned.csv', index=False)
print("CSV exported successfully! ")
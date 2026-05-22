use employee_mental_health;

select *from mental_health_cleaned;

select country ,avg(annual_salary_usd) as average_salary_by_countries
from mental_health_cleaned
group by country
order by average_salary_by_countries desc;

select country,count(*) as total_employees
from mental_health_cleaned
where work_life_balance_score >4.5
group by country
order by total_employees desc;

select industry,count(*) as employees_wants_to_leave
from mental_health_cleaned
where intention_to_leave='Likely'
group by industry
order by employees_wants_to_leave desc;

select industry,count(*) as employees_working_more_than_avg_worktime
from mental_health_cleaned
where weekly_work_hours>(select avg(weekly_work_hours) from mental_health_cleaned)
group by industry
order by employees_working_more_than_avg_worktime desc;

select has_diagnosis,count(*) as employees_diagnosed_with_mental_health_condition
from mental_health_cleaned
where has_diagnosis='Yes'
group by has_diagnosis;

select gender,count(*) as not_satisfied_with_job
from mental_health_cleaned
where job_satisfaction_score <=5.2
group by gender
order by not_satisfied_with_job desc;

select industry,count(*) as employess_with_less_avg_sleep
from mental_health_cleaned
where sleep_hours_per_night<(select avg(sleep_hours_per_night) from mental_health_cleaned)
group by industry
order by employess_with_less_avg_sleep desc;

select job_role,count(*) as employees_with_good_employer_support
from mental_health_cleaned
where employer_support_level='Good' or employer_support_level ='Excellent'
group by job_role
order by employees_with_good_employer_support;

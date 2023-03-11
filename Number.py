# call log file
call_log = [
    ('9898989898', '8989898989', '00:05:23'),
    ('1898989898', '9989898989', '01:00:23'),
    ('2898989898', '7989898989', '00:00:21'),
    ('2898989898', '6989898989', '00:00:23'),
    ('4898989898', '5989898989', '00:01:23'),
    ('5898989898', '4989898989', '00:05:55'),
    ('5898989898', '3989898989', '00:00:23'),
    ('7898989898', '2989898989', '00:02:23'),
    ('8898989898', '1189898989', '00:05:20'),
    ('1098989898', '8459898989', '00:00:23'),
    ('1898989898', '8967898989', '00:00:40'),
    ('2898989898', '8989898989', '00:05:23'),
]

# 1. Find the distinct From Numbers for a day.
distinct_from_numbers = set([call[0] for call in call_log])
print("Distinct From Numbers: ", distinct_from_numbers)

# 2. Find the distinct From Numbers who used the Free Plan. (Call Duration less than 1 min)
free_plan_numbers = set([call[0] for call in call_log if int(call[2].split(':')[0]) < 1])
print("Distinct From Numbers who used Free Plan: ", free_plan_numbers)

# 3. Find the total call duration with respect to From Number
duration_by_number = {}
for call in call_log:
    number = call[0]
    hours, minutes, seconds = map(int, call[2].split(':'))
    duration = hours * 3600 + minutes * 60 + seconds
    if number not in duration_by_number:
        duration_by_number[number] = duration
    else:
        duration_by_number[number] += duration
print("Total call duration with respect to From Number: ", duration_by_number)

# 4. Find the total income for a day. (Cost to be considered for Call Duration greater 1 min)
total_income = 0
for call in call_log:
    duration = int(call[2].split(':')[0]) * 60 + int(call[2].split(':')[1])
    if duration > 1:
        total_income += (duration - 1) * 0.3
print("Total income for a day: ", total_income)

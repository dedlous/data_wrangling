import unicodecsv
import sys
f_handler=open('out.log', 'w')
sys.stdout=f_handler

# enrollments=[]
# f=open('enrollments.csv','rb')
# reader=unicodecsv.DictReader(f)
# for row in reader:
#     enrollments.append(row)
#
# f.close()
#
# with open('enrollments.csv','rb') as f:
#     reader = unicodecsv.DictReader(f)
#     enrollments=list(reader)
#     # for row in reader:
#     #     enrollments.append(row)
# print (enrollments[:6])

import unicodecsv

def read_csv(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        return list(reader)

enrollments = read_csv('enrollments.csv')
daily_engagement = read_csv('daily_engagement.csv')
project_submissions = read_csv('project_submissions.csv')



from datetime import datetime as dt


# 将字符串格式的时间转为 Python datetime 类型的时间。
# 如果没有时间字符串传入，返回 None

def parse_date(date):
    if date == '':
        return None
    else:
        return dt.strptime(date, '%Y/%m/%d')


# 将可能是空字符串或字符串类型的数据转为 整型 或 None。

def parse_maybe_int(i):
    if i == '':
        return None
    else:
        return int(i)

def get_unique_students(data):
    unique_students = set()
    for data_point in data:
        unique_students.add(data_point['account_key'])
    return unique_students

# 清理 enrollments 表格中的数据类型
# 清理 enrollments 表格中的数据类型

for enrollment in enrollments:
    enrollment['cancel_date'] = parse_date(enrollment['cancel_date'])
    enrollment['days_to_cancel'] = parse_maybe_int(enrollment['days_to_cancel'])
    enrollment['is_canceled'] = (enrollment['is_canceled'] == 'TRUE')
    enrollment['is_udacity'] = (enrollment['is_udacity'] == 'TRUE')
    enrollment['join_date'] = parse_date(enrollment['join_date'])


# 清理 engagement 的数据类型
for engagement_record in daily_engagement:
    engagement_record['lessons_completed'] = int(float(engagement_record['lessons_completed']))
    engagement_record['num_courses_visited'] = int(float(engagement_record['num_courses_visited']))
    engagement_record['projects_completed'] = int(float(engagement_record['projects_completed']))
    engagement_record['total_minutes_visited'] = float(engagement_record['total_minutes_visited'])
    engagement_record['utc_date'] = parse_date(engagement_record['utc_date'])


# 清理 submissions 的数据类型
for submission in project_submissions:
    submission['completion_date'] = parse_date(submission['completion_date'])
    submission['creation_date'] = parse_date(submission['creation_date'])

#####################################
#                 3                 #
#####################################

## 将 daily_engagement 表中的 "acct" 重命名为 ”account_key"

for engagement_record in daily_engagement:
    engagement_record['account_key'] = engagement_record['acct']
    del[engagement_record['acct']]

# print (enrollments[:6])
# print (daily_engagement[:6])
#####################################
#                 2                 #
#####################################

## 计算每张表中的总行数，和独立学生（拥有独立的 account keys）的数量
len(enrollments)

unique_enrolled_students=get_unique_students(enrollments)
len(unique_enrolled_students)
print ('len(enrollments)=%d,len(unique_enrolled_students=%d)'%(len(enrollments),len(unique_enrolled_students)))
# print (unique_enrolled_students[:6])
# print (unique_enrolled_students)

len(daily_engagement)
unique_engagement_students=get_unique_students(daily_engagement)
len(unique_engagement_students)
print ('len(daily_engagement)=%d,len(unique_engagement_students=%d)'%(len(daily_engagement),len(unique_engagement_students)))

len(project_submissions)
unique_project_submitters=get_unique_students(project_submissions)
len(unique_project_submitters)
print ('len(project_submissions)=%d,len(unique_project_submitters=%d)'%(len(project_submissions),len(unique_project_submitters)))


# for enrollment in enrollments:
#     student = enrollment['account_key']
#     if student not in unique_engagement_students:
#         print (enrollment)
#         # break


num_problem_students = 0
num_problem_students_is_udacity=0
num_problem_students_data_equal = 0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in unique_engagement_students):
        # and enrollment['join_date'] != enrollment['cancel_date']):
        # print (enrollment)#71
        num_problem_students += 1
        if (enrollment['is_udacity']):
            num_problem_students_is_udacity += 1
        elif (enrollment['join_date'] == enrollment['cancel_date']):
            num_problem_students_data_equal +=1
        else:
            print (enrollment)


not_in_unique_engagement_students=0
# print (unique_enrolled_students)
for enrol in unique_enrolled_students:
    if (enrol not in unique_engagement_students):
        # print(enrol)
        not_in_unique_engagement_students += 1
        # print (enrollments[enrol])
    # student=unique_enrolled_students['account_key']#65

num_problem_students_not_in_daily_engagement=0
for enrollment in enrollments:
    student = enrollment['account_key']
    if (student not in daily_engagement):
        num_problem_students_not_in_daily_engagement +=1

print ('num_problem_students=%d'%num_problem_students)
print ('not_in_enagement_num=%d'%not_in_unique_engagement_students)
print ('num_problem_students_is_udacity=%d'%num_problem_students_is_udacity)
print ('num_problem_students_data_equal=%d'%num_problem_students_data_equal)
print ('num_problem_students_not_in_daily_engagement=%d'%num_problem_students_not_in_daily_engagement)


# for enrollment in enrollments:
#     if enrollment['is_udacity']:
#         print (enrollment)
#     # if enrollment['is_udacity']=='TRUE':
#     #     print (enrollment)

# 为所有 Udacity 测试帐号建立一组 set
udacity_test_accounts = set()
for enrollment in enrollments:
    if enrollment['is_udacity']:
        udacity_test_accounts.add(enrollment['account_key'])
print ('len(udacity_test_accounts)',len(udacity_test_accounts))


# 通过 account_key 删除所有 Udacity 的测试帐号
def remove_udacity_accounts(data):
    non_udacity_data = []
    for data_point in data:
        if data_point['account_key'] not in udacity_test_accounts:
            non_udacity_data.append(data_point)
    return non_udacity_data


non_udacity_enrollments = remove_udacity_accounts(enrollments)
non_udacity_engagement = remove_udacity_accounts(daily_engagement)
non_udacity_submissions = remove_udacity_accounts(project_submissions)

print ('len(non_udacity_enrollments)=',len(non_udacity_enrollments))
print ('len(non_udacity_engagement)=',len(non_udacity_engagement))
print ('len(non_udacity_submissions)=',len(non_udacity_submissions))

# print (non_udacity_enrollments)




paid_students = {}
for enrollment in non_udacity_enrollments:
    if (not enrollment['is_canceled'] or
            enrollment['days_to_cancel'] > 7):
        account_key = enrollment['account_key']
        enrollment_date = enrollment['join_date']
        if (account_key not in paid_students or
                enrollment_date > paid_students[account_key]):
            paid_students[account_key] = enrollment_date
print ('len(paid_students)=%d'%(len(paid_students)))


# def within_one_week(join_date, engagement_date):
#     time_delta = engagement_date - join_date
#     return time_delta.days < 7

def within_one_week(join_date, engagement_date):
    time_delta = engagement_date - join_date
    return time_delta.days >= 0 and time_delta.days < 7

def remove_free_trial_cancels(data):
    new_data = []
    for data_point in data:
        if data_point['account_key'] in paid_students:
            new_data.append(data_point)
    return new_data

paid_enrollments = remove_free_trial_cancels(non_udacity_enrollments)
paid_engagement = remove_free_trial_cancels(non_udacity_engagement)
paid_submissions = remove_free_trial_cancels(non_udacity_submissions)


print ('len(paid_enrollments)=%d'%(len(paid_enrollments)))
print ('len(paid_engagement)=%d'%(len(paid_engagement)))
print ('len(paid_submissions)=%d'%(len(paid_submissions)))

paid_engagement_in_first_week = []
for engagement_record in paid_engagement:
    account_key = engagement_record['account_key']
    join_date = paid_students[account_key]
    engagement_record_date = engagement_record['utc_date']

    if within_one_week(join_date, engagement_record_date):
        paid_engagement_in_first_week.append(engagement_record)

print ('len(paid_engagement_in_first_week)=%d'%(len(paid_engagement_in_first_week)))
# print (paid_engagement_in_first_week)

from collections import defaultdict
engagement_by_account = defaultdict(list)
for engagement_record in paid_engagement_in_first_week:
    account_key = engagement_record['account_key']
    engagement_by_account[account_key].append(engagement_record)

# print (engagement_by_account)
# print (list(engagement_by_account)[:3])


# 创建一个包含学生在第1周在教室所花总时间和字典。键为帐号（account key），值为数字（所花总时间）
total_minutes_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_minutes = 0
    for engagement_record in engagement_for_student:
        total_minutes += engagement_record['total_minutes_visited']
    total_minutes_by_account[account_key] = total_minutes

import numpy as np

# 汇总和描述关于教室所花时间的数据
total_minutes = total_minutes_by_account.values()
# print (total_minutes)
print ('Mean:', np.mean(list(total_minutes)))
print ('Standard deviation:', np.std(list(total_minutes)))
print ('Minimum:', np.min(list(total_minutes)))
print ('Maximum:', np.max(list(total_minutes)))

student_with_max_minutes = None
max_minutes = 0

for student, total_minutes in total_minutes_by_account.items():
    if total_minutes > max_minutes:
        max_minutes = total_minutes
        student_with_max_minutes = student

print ('max_minutes=',max_minutes)

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] == student_with_max_minutes:
        print (engagement_record)



total_lessons_by_account = {}
for account_key, engagement_for_student in engagement_by_account.items():
    total_lessons = 0
    for engagement_record in engagement_for_student:
        total_lessons += engagement_record['lessons_completed']
        total_lessons_by_account[account_key] = total_lessons

total_lessons = total_lessons_by_account.values()
print ('Mean:', np.mean(list(total_lessons)))
print ('Standard deviation:', np.std(list(total_lessons)))
print ('Minimum:', np.min(list(total_lessons)))
print ('Maximum:', np.max(list(total_lessons)))


def group_data(data, key_name):
    grouped_data = defaultdict(list)
    for data_point in data:
        key = data_point[key_name]
        grouped_data[key].append(data_point)
    return grouped_data

engagement_by_account = group_data(paid_engagement_in_first_week,
                                   'account_key')

def sum_grouped_items(grouped_data, field_name):
    summed_data = {}
    for key, data_points in grouped_data.items():
        total = 0
        for data_point in data_points:
            total += data_point[field_name]
        summed_data[key] = total
    return summed_data

total_minutes_by_account = sum_grouped_items(engagement_by_account,
                                             'total_minutes_visited')

def describe_data(e):
    data=list(e)
    print ('Mean:', np.mean(data))
    print ('Standard deviation:', np.std(data))
    print ('Minimum:', np.min(data))
    print ('Maximum:', np.max(data))


import matplotlib.pyplot as plt
import numpy as np

# Summarize the given data
def describe_data(e):
    data=list(e)
    print ('Mean:', np.mean(data))
    print ('Standard deviation:', np.std(data))
    print ('Minimum:', np.min(data))
    print ('Maximum:', np.max(data))
    plt.hist(data)
    plt.show()

describe_data(list(total_minutes_by_account.values()))


lessons_completed_by_account = sum_grouped_items(engagement_by_account,
                                                 'lessons_completed')
describe_data(list(lessons_completed_by_account.values()))

for engagement_record in paid_engagement:
    if engagement_record['num_courses_visited'] > 0:
        engagement_record['has_visited'] = 1
    else:
        engagement_record['has_visited'] = 0


days_visited_by_account = sum_grouped_items(engagement_by_account,
                                            'has_visited')
describe_data(list(days_visited_by_account.values()))



######################################
#                 11                 #
######################################

## 创建两个付费学生第1周的互动数据列表（engagement）。第1个包含通过项目的学生，第2个包含没通过项目的学生。

subway_project_lesson_keys = ['746169184', '3176718735']

pass_subway_project = set()

for submission in paid_submissions:
    project = submission['lesson_key']
    rating = submission['assigned_rating']

    if ((project in subway_project_lesson_keys) and
            (rating == 'PASSED' or rating == 'DISTINCTION')):
        pass_subway_project.add(submission['account_key'])

print (len(pass_subway_project))

passing_engagement = []
non_passing_engagement = []

for engagement_record in paid_engagement_in_first_week:
    if engagement_record['account_key'] in pass_subway_project:
        passing_engagement.append(engagement_record)
    else:
        non_passing_engagement.append(engagement_record)

print ('len(passing_engagement)=',len(passing_engagement))
print ('len(non_passing_engagement)=',len(non_passing_engagement))





passing_engagement_by_account = group_data(passing_engagement,
                                           'account_key')
non_passing_engagement_by_account = group_data(non_passing_engagement,
                                               'account_key')

print ('non-passing students:')
non_passing_minutes = sum_grouped_items(
    non_passing_engagement_by_account,
    'total_minutes_visited'
)

describe_data(non_passing_minutes.values())

print ('passing students:')
passing_minutes = sum_grouped_items(
    passing_engagement_by_account,
    'total_minutes_visited'
)
describe_data(passing_minutes.values())

print ('non-passing students:')
non_passing_lessons = sum_grouped_items(
    non_passing_engagement_by_account,
    'lessons_completed'
)
describe_data(non_passing_lessons.values())

print ('passing students:')
passing_lessons = sum_grouped_items(
    passing_engagement_by_account,
    'lessons_completed'
)
describe_data(passing_lessons.values())

print ('non-passing students:')
non_passing_visits = sum_grouped_items(
    non_passing_engagement_by_account,
    'has_visited'
)
describe_data(non_passing_visits.values())

print ('passing students:')
passing_visits = sum_grouped_items(
    passing_engagement_by_account,
    'has_visited'
)
describe_data(passing_visits.values())


import seaborn as sns

plt.hist(non_passing_visits.values(), bins=8)
plt.xlabel('Number of days')
plt.title('Distribution of classroom visits in the first week ' +
          'for students who do not pass the subway project')

plt.hist(passing_visits.values(), bins=8)
plt.xlabel('Number of days')
plt.title('Distribution of classroom visits in the first week ' +
          'for students who pass the subway project')
plt.show()
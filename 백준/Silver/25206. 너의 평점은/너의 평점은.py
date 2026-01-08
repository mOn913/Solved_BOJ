score_dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0,
             'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}

sum = 0 # (학점 X 과목평점)의 합
grade_sum = 0 # 학점의 총합

for i in range(20):
    subject_score_grade = list(input().split())
    if subject_score_grade[2] == "P":
        continue
    sum += float(subject_score_grade[1]) * score_dic[subject_score_grade[2]]
    grade_sum += float(subject_score_grade[1])
    
print(f"{sum / grade_sum:.6f}")

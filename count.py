import os
counter=0
with open (r'C:\Users\13394\Desktop\text-file-process-jerrymajerry-master\text-file-process\log_files\201811123021.log',encoding='utf-8')as f:
    for line in f:
        student=line.split(',')[1]
        student_id=student[10:]
        if student_id=='23021':
            counter=counter+1
print(counter)
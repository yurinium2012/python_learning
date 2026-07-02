previous_num = 0

for current_num in range(11):
       total = current_num + previous_num
       print("current number:",current_num,
             "previous number:",previous_num,
             "Sum:", total)
       previous_num = current_num
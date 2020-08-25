import random
grade = random.uniform(0,100)
if grade >=60:
    if grade >=90:
        print("优秀")
    elif 70<= grade <=80:
        print("良")
    else:
        print("一般")
elif grade <= 30:
    print("找家长")
else:
    print("下课来一趟")
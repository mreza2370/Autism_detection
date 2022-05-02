import random
import numpy as np
length=len(data[0:])
rows=[j for j in range(length)]
data_ex=data.copy()
lebel_ex=label.copy()
selected_rows=[]
i=0
while(True):
    while(True):
        length2=len(rows)
        random_num=random.randint(0,length2-1)
        random_row=rows[random_num]
        if random_row not in selected_rows:
            selected_rows.append(random_row)
            rows.remove(rows[random_num])
            break
     
    data_ex[i]=data[random_row]
    lebel_ex[i]=label[random_row]
    i+=1
    if i%10000==0:
      print(i)
    if i==length:
        break   

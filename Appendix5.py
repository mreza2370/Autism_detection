

data_final=data_ex.copy()
for i in range(len(data_ex[0:])):
    average=max(data_ex[i])-min(data_ex[i])
    if average==0:
        pass
    else:
        data_final[i]=data_ex[i]/average
    if i%10000==0:
        print(i)

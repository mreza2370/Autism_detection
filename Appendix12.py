
test_loss, test_acc = myModel. evaluate(data_final,lebel_ex)
test_labels_p = myModel. predict(data_final)
import numpy as np
test_labels_p = np. argmax(test_labels_p, axis=1)

def evaluate(lebel_ex,test_labels_p): 
  import sys
  if len(lebel_ex)!=len(test_labels_p): 
    return('Error sizes dont match')
    #sys. exit()
  Tp=0
  Fp=0
  #length=len(lebel_ex)/10
  #process=0
  for i in range(len(lebel_ex)): 
    if lebel_ex[i]. argmax()!=test_labels_p[i]: 
        Fp+=1
    else: 
        Tp+=1
   # if (i+1)%length==0: 
     # process+=1
      #processed=process*10
      #print('%s percents done'%processed)
  recall=Tp/len(test_labels_p)
  accuracy=recall
  precision=Tp/(Tp+Fp)
  F1=(2*(precision*recall))/(precision+recall)
  print('True Positives :  ',Tp,'  ','False Positives :  ',Fp)
  print('Recall : ',recall)
  print('accuracy : ',accuracy)
  print('precision : ',precision)
  print('F1 measurement : ',F1)

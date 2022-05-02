import numpy as np
import random
from dtaidistance import dtw
from dtaidistance import dtw_visualisation as dtwvis

# Our Pre-Processing function
    
def equalize(t,a): 
  ta= len(t)-len(a)
  at= len(a)-len(t)
  if ta>0: 
        t=equalize_matrix2(t,ta,a)
  elif at>0: 
        t=equalize_matrix(t,at,a)
  else: 
        pass
  
  return[t,a]
  
  
def distance(a,b): 
  if len(a)==len(b): 
      d= len(a)
      dis_matrix=[]
      for num in range(d): 
          single_dis=abs(a[num]-b[num])
          dis_matrix. append(single_dis)
      return(dis_matrix)
      
  else: 
      raise NameError('given lists dont have same length') 

def equalize_matrix2(matrix,number,compare_matrix): 
    e_matrix=matrix. copy()
    import random
    import math
    import numpy as np
    conditions = math. factorial(len(e_matrix))/(math. factorial(number)*math. factorial(len(e_matrix)-number))
    samples=[]
    all_t_matrixes=[]
    dis_value=[]
    num_e_matrix=[i for i in range(len(e_matrix))]
    while(True): 
          x=random. sample(num_e_matrix,number)
          x. sort()
          if x not in samples: 
                samples. append(x)
          if len(samples)==conditions: 
                break
    for sample in samples: 
          t_matrix=matrix. copy()
          for s_num,s in enumerate(sample): 
                t_matrix. remove(t_matrix[s-s_num])
          distancee = distance(t_matrix,compare_matrix)
          distancee=np. mean(distancee)
          t_matrix. append(distancee)
          all_t_matrixes. append(t_matrix)
    for a in all_t_matrixes: 
          dis_value. append(a[-1: ])
    selected_matrix=all_t_matrixes[np. argmin(dis_value)]
    selected_matrix=selected_matrix[0: -1]

    return selected_matrix
  
def equalize_matrix(matrix,number,compare_matrix): 
    e_matrix=[]
    for place in range(len(matrix)): 
          if place == len(matrix)-1: 
                break
          e_matrix. append((matrix[place]+matrix[place+1])/2)
          
    for end_place in range(number): 
          e_matrix. append(matrix[len(matrix)-1])
          
    for start_place in range(number): 
          e_matrix. insert(0,matrix[0])  
         
    selected_matrix = best_places(e_matrix,number,matrix,compare_matrix)
    return selected_matrix

  
      

def best_places(e_matrix,number,matrix,compare_matrix): 
    import random
    import math
    import numpy as np
    conditions = math. factorial(len(e_matrix))/(math. factorial(number)*math. factorial(len(e_matrix)-number))
    samples=[]
    all_t_matrixes=[]
    dis_value=[]
    num_e_matrix=[i for i in range(len(e_matrix))]
    while(True): 
          x=random. sample(num_e_matrix,number)
          x. sort()
          if x not in samples: 
                samples. append(x)
          if len(samples)==conditions: 
                break
    for sample in samples: 
          t_matrix=matrix. copy()
          first_numbers=[n for n in range(number)]
          for s_num,s in enumerate(sample): 
              if s in first_numbers: 
                  t_matrix. insert(s,e_matrix[s])
              else: 
                  t_matrix. insert(s+1+s_num-number,e_matrix[s])
          distancee = distance(t_matrix,compare_matrix)
          distancee=np. mean(distancee)
          t_matrix. append(distancee)
          all_t_matrixes. append(t_matrix)
    for a in all_t_matrixes: 
          dis_value. append(a[-1: ])
    selected_matrix=all_t_matrixes[np. argmin(dis_value)]
    selected_matrix=selected_matrix[0: -1]
    return selected_matrix
    
#Function to generate data
def classA(y_points): 
    y_dtat=y_points. copy()
    num=random. randint(0,3)
    s_num=[]
    selected=[]
    for i in range(num): 
        rand=random. randint(0,19)
        while(True): 
            if rand not in selected: 
                selected. append(rand)
                s_num. append(rand)
                break
            else: 
                rand=random. randint(0,19)
    for s in s_num: 
        y_dtat[s]=random. gauss(0,1)
    return(y_dtat)
        
def classB(y_points): 
    y_dtat=y_points. copy()
    num=random. randint(4,7)
    s_num=[]
    selected=[]
    for i in range(num): 
        rand=random. randint(0,19)
        while(True): 
            if rand not in selected: 
                selected. append(rand)
                s_num. append(rand)
                break
            else: 
                rand=random. randint(0,19)
    for s in s_num: 
        y_dtat[s]=random. gauss(0,1)
    return y_dtat
        
        
def classC(y_points): 
    y_dtat=y_points. copy()
    num=random. randint(8,11)
    s_num=[]
    selected=[]
    for i in range(num): 
        rand=random. randint(0,19)
        while(True): 
            if rand not in selected: 
                selected. append(rand)
                s_num. append(rand)
                break
            else: 
                rand=random. randint(0,19)
    for s in s_num: 
        y_dtat[s]=random. gauss(0,1)
    return y_dtat
        
def classD(y_points): 
    y_dtat=y_points. copy()
    num=random. randint(12,15)
    s_num=[]
    selected=[]
    for i in range(num): 
        rand=random. randint(0,19)
        while(True): 
            if rand not in selected: 
                selected. append(rand)
                s_num. append(rand)
                break
            else: 
                rand=random. randint(0,19)
    for s in s_num: 
        y_dtat[s]=random. gauss(0,1)
    return y_dtat   
    
    
def classE(y_points): 
    y_dtat=y_points. copy()
    num=random. randint(16,19)
    s_num=[]
    selected=[]
    for i in range(num): 
        rand=random. randint(0,19)
        while(True): 
            if rand not in selected: 
                selected. append(rand)
                s_num. append(rand)
                break
            else: 
                rand=random. randint(0,19)
    for s in s_num: 
        y_dtat[s]=random. gauss(0,1)
    return y_dtat
# function to measure distances between an original and an equalized track
def measaure_distance(equalized_track,gt): 
    if len(equalized_track)!=len(gt): 
        assert "lenghts not match"
    all_dist=0
    for index,item in enumerate(equalized_track): 
        all_dist+=abs(item-gt[index])
    return(all_dist)
def compute_error(reps=100): 
    errors={'ours': 0,'dtw': 0}
    for function in ['classA','classB','classC','classD','classE']: 
        for rep in range(reps): 
            dataE=[]
            number=1
            y_points=[0 for i in range(20)]
            for i in range(number): 
                outp=globals()[function](y_points)
                dataE. append(outp)
            #############################
            modified_dataE=dataE[0]. copy()
            for i in range(number): 
                for r in range(2): 
                    modified_dataE. remove(modified_dataE[random. randint(0,16)])

            path = dtw. warping_path(modified_dataE, y_points)
            dtwvis. plot_warping(modified_dataE, y_points, path)

            selected_track={}
            selected_anno=[]
            for p in path: 
                if p[0] not in selected_track: 
                    selected_track[p[0]]=[]
                selected_track[p[0]]. append(p[1])

            equlized_track=[]
            for sel_tra in selected_track: 
                for number in range(len(selected_track[sel_tra])): 
                    equlized_track. append(modified_dataE[sel_tra])

            equlized_mat=equalize(modified_dataE, y_points)

            errors['ours']+=measaure_distance(equlized_track,dataE[0])

            errors['dtw']+=measaure_distance(equlized_mat[0],dataE[0])
    return(errors)
res=compute_error()

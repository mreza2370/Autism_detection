# Pre-Processing
        

    
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
          dis_matrix.append(single_dis)
      return(dis_matrix)
      
  else:
      raise NameError('given lists dont have same length') 




def equalize_matrix2(matrix,number,compare_matrix):
    e_matrix=matrix.copy()
    import random
    import math
    import numpy as np
    conditions = math.factorial(len(e_matrix))/(math.factorial(number)*math.factorial(len(e_matrix)-number))
    samples=[]
    all_t_matrixes=[]
    dis_value=[]
    num_e_matrix=[i for i in range(len(e_matrix))]
    while(True):
          x=random.sample(num_e_matrix,number)
          x.sort()
          if x not in samples:
                samples.append(x)
          if len(samples)==conditions:
                break
    for sample in samples:
          t_matrix=matrix.copy()
          for s_num,s in enumerate(sample):
                t_matrix.remove(t_matrix[s-s_num])
          distancee = distance(t_matrix,compare_matrix)
          distancee=np.mean(distancee)
          t_matrix.append(distancee)
          all_t_matrixes.append(t_matrix)
    for a in all_t_matrixes:
          dis_value.append(a[-1:])
    selected_matrix=all_t_matrixes[np.argmin(dis_value)]
    selected_matrix=selected_matrix[0:-1]

    return selected_matrix
  




def equalize_matrix(matrix,number,compare_matrix):
    e_matrix=[]
    for place in range(len(matrix)):
          if place == len(matrix)-1:
                break
          e_matrix.append((matrix[place]+matrix[place+1])/2)
          
    for end_place in range(number) :
          e_matrix.append(matrix[len(matrix)-1])
          
    for start_place in range(number) :
          e_matrix.insert(0,matrix[0])  
         
    selected_matrix = best_places(e_matrix,number,matrix,compare_matrix)
    return selected_matrix

  
      

def best_places(e_matrix,number,matrix,compare_matrix):
    import random
    import math
    import numpy as np
    conditions = math.factorial(len(e_matrix))/(math.factorial(number)*math.factorial(len(e_matrix)-number))
    samples=[]
    all_t_matrixes=[]
    dis_value=[]
    num_e_matrix=[i for i in range(len(e_matrix))]
    while(True):
          x=random.sample(num_e_matrix,number)
          x.sort()
          if x not in samples:
                samples.append(x)
          if len(samples)==conditions:
                break
    for sample in samples:
          t_matrix=matrix.copy()
          first_numbers=[n for n in range(number)]
          for s_num,s in enumerate(sample):
              if s in first_numbers:
                  t_matrix.insert(s,e_matrix[s])
              else:
                  t_matrix.insert(s+1+s_num-number,e_matrix[s])
          distancee = distance(t_matrix,compare_matrix)
          distancee=np.mean(distancee)
          t_matrix.append(distancee)
          all_t_matrixes.append(t_matrix)
    for a in all_t_matrixes:
          dis_value.append(a[-1:])
    selected_matrix=all_t_matrixes[np.argmin(dis_value)]
    selected_matrix=selected_matrix[0:-1]
    return selected_matrix
    

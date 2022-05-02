def distance(a,b):
  if len(a)==len(b):
      d= len(a)
      dis_matrix=[]
      for num in range(d):
          single_dis=(((a[num][0]-b[num][0])**2)+((a[num][1]-b[num][1])**2))**0.5
          dis_matrix.append(single_dis)
      return(dis_matrix)
      
  else:
      raise NameError('given lists dont have same length')
      
# Interpolation for equalization
def interpolate(t,a):
  ta= len(t)-len(a)
  at= len(a)-len(t)
  if ta>0 and ta<=5:
        a=equalize_matrix(a,ta,t)
  elif at>0 and at<=5:
        t=equalize_matrix(t,at,a)
  elif ta >= 6 or at >= 6:
      t='stop'
      a='stop'
  else:
        pass
  
  return[t,a]
  
  
  
def equalize_matrix(matrix,number,compare_matrix):
    e_matrix=[]
    for place in range(len(matrix)):
          if place == len(matrix)-1:
                break
          e_matrix.append([(matrix[place][0]+matrix[place+1][0])/2,(matrix[place][1]+matrix[place+1][1])/2])
    for end_place in range(number) :
          e_matrix.append(matrix[len(matrix)-1])
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
          for s in sample:
                t_matrix.insert(s+1,e_matrix[s])
          distancee = distance(t_matrix,compare_matrix)
          distancee=np.mean(distancee)
          t_matrix.append(distancee)
          all_t_matrixes.append(t_matrix)
    for a in all_t_matrixes:
          dis_value.append(a[-1:])
    selected_matrix=all_t_matrixes[np.argmin(dis_value)]
    selected_matrix=selected_matrix[0:-1]
    return selected_matrix

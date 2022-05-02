import random
import numpy as np
import os
import matplotlib.pyplot as plt
#import keras

def make_noise_line(orig_points,level):
    points=orig_points.copy()
    min_noise=20*(level-1)
    max_noise=20*(level)
    noise_num=random.randint(min_noise,max_noise)
    selected_indices=random.sample(range(0,len(points)), noise_num)
    for index in selected_indices:
        noise_val_x=random.randint(-5,5)
        noise_val_y=random.randint(-5,5)
        points[index][0]=points[index][0]+noise_val_x
        points[index][1]=points[index][1]+noise_val_y
    return(points)
    
def make_noise_circle(orig_points,level):
    points=orig_points.copy()
    min_noise=20*(level-1)
    max_noise=20*(level)
    noise_num=random.randint(min_noise,max_noise)
    selected_indices=random.sample(range(0,len(points)), noise_num)
    for index in selected_indices:
        noise_val_x=random.randint(-10,10)
        noise_val_y=random.randint(-10,10)
        points[index][0]=points[index][0]+noise_val_x
        points[index][1]=points[index][1]+noise_val_y
    return(points) 

def make_noise_square(orig_points,level):
    points=orig_points.copy()
    min_noise=20*(level-1)
    max_noise=20*(level)
    noise_num=random.randint(min_noise,max_noise)
    selected_indices=random.sample(range(0,len(points)), noise_num)
    for index in selected_indices:
        noise_val_x=random.randint(-10,10)
        noise_val_y=random.randint(-10,10)
        points[index][0]=points[index][0]+noise_val_x
        points[index][1]=points[index][1]+noise_val_y
    return(points)  
""" 
#lines    
mo_lines=make_noise_line(lines[25],4)    
x_points=[]
y_points=[]
for cp in mo_lines:
    x_points.append(cp[0])
    y_points.append(cp[1])
axes = plt.gca()
axes.set_xlim([-10,210])
axes.set_ylim([-5,5])
plt.plot(x_points,y_points)   
 
#circles
mo_lines=make_noise_circle(circles[33],5)    
x_points=[]
y_points=[]
for cp in mo_lines:
    x_points.append(cp[0])
    y_points.append(cp[1])
axes = plt.gca()
axes.set_xlim([-5,205])
axes.set_ylim([0,110])
plt.plot(x_points,y_points)   
        
#squares
mo_lines=make_noise_square(squares[9],1)    
x_points=[]
y_points=[]
for cp in mo_lines:
    x_points.append(cp[0])
    y_points.append(cp[1])
axes = plt.gca()
axes.set_xlim([-10,110])
axes.set_ylim([-5,55])
plt.axis('off')
plt.plot(x_points,y_points)   
#plt.close()
    
"""   
    
    
def create_circle(x,y):
    computed_points=[]
    radius=100
    first_x=x-radius
    last_x=x+radius
    while(True):
        selected_x=first_x+1
        if selected_x >= last_x:
            break
        selected_y=np.sqrt((radius**2)-(selected_x-x)**2)+y
        computed_points.append([selected_x,selected_y])
        first_x=selected_x
    return(computed_points)

def create_line(x,y):
    computed_points=[]
    num=200
    last_x=x+num
    first_x=x
    while(True):
        if first_x==last_x:
            break
        computed_points.append([first_x+1,y])
        first_x+=1
    return(computed_points)

def create_square(x,y,length):
    computed_points=[]
    current_y=y
    for i in range(50):
        computed_points.append([x,current_y+1])
        current_y=current_y+1
    current_x=x
    for i in range(100):
        computed_points.append([current_x+1,current_y])
        current_x=current_x+1
    for i in range(50):
        computed_points.append([current_x,current_y-1])
        current_y=current_y-1
    return(computed_points)
    
    

    
circles=[]
for iteration in range(2500):
    circles.append(create_circle(100,0))

lines=[]
for iteration in range(2500):
    lines.append(create_line(0,0))

squares=[]
for iteration in range(2500):
    squares.append(create_square(0,0,200))
        
for level in [1,2,3,4,5]:
    try:
        os.mkdir('all') 
    except:
        pass
    for index,circle in enumerate(circles[500*(level-1):500*(level)]):
        mo_lines=make_noise_circle(circle,level)    
        x_points=[]
        y_points=[]
        for cp in mo_lines:
            x_points.append(cp[0])
            y_points.append(cp[1])
        axes = plt.gca()
        axes.set_xlim([-5,205])
        axes.set_ylim([0,110])
        plt.figure()
        plt.axis('off')
        plt.plot(x_points,y_points)
        plt.savefig('all/circle{}_level{}.png'.format(index,level))
        plt.close()
    for index,line in enumerate(lines[500*(level-1):500*(level)]):
        mo_lines=make_noise_line(line,level)    
        x_points=[]
        y_points=[]
        for cp in mo_lines:
            x_points.append(cp[0])
            y_points.append(cp[1])
        axes = plt.gca()
        axes.set_xlim([-10,210])
        axes.set_ylim([-5,5])
        plt.figure()
        plt.axis('off')
        plt.plot(x_points,y_points) 
        plt.savefig('all/line{}_level{}.png'.format(index,level))
        plt.close()
    for index,square in enumerate(squares[500*(level-1):500*(level)]):
        mo_lines=make_noise_square(square,level)    
        x_points=[]
        y_points=[]
        for cp in mo_lines:
            x_points.append(cp[0])
            y_points.append(cp[1])
        axes = plt.gca()
        axes.set_xlim([-10,110])
        axes.set_ylim([-5,55])
        plt.figure()
        plt.axis('off')
        plt.plot(x_points,y_points) 
        plt.savefig('all/square{}_level{}.png'.format(index,level))
        plt.close()
        

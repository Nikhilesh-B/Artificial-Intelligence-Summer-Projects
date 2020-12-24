 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:54:05 2020
pla.py intaking the data processing it and working from there. 
@author: Nick
"""

import pandas as pd 
data = {}
import numpy as np
import plot_db as plt
import sys 



def main(IN, OUT):
    
    
    df = pd.read_csv(IN, header=None)
    ## now running the perceptron alogirthm that will iterate through and update weights writing to the 
    #file as necessary 
    
    
    
    
    m = [0,0,0]
    x = [1,2,3]
    
    lst = []
    
    
    with open(OUT,"w") as f:
        f.write("w1,w2,w_naught\n")
        while(x != m): 
          x = m.copy()
          for index, row in df.iterrows(): 
              y_i = row[2]
              x_1 = row[0]
              x_2 = row[1]
              #print(x_1, x_2,y_i)
              f_x = np.sign(x_1*m[0]+x_2*m[1]+m[2]) 
              if (y_i*f_x<=0):
                  m[0] = m[0]+y_i*x_1
                  m[1] = m[1]+y_i*x_2
                  m[2] = m[2]+y_i
                  f.write(str(m[0])+","+str(m[1])+","+str(m[2])+"\n")
        f.close()
    
        
    plt.visualize_scatter(df,feat1=0, feat2=1, labels=2,weights=m,title='')


main(sys.argv[1],sys.argv[2])


    






import math
import numpy as np
from math import factorial

def erlang(A, m):
    L = (A ** m) / factorial(m)
    sum_ = 0
    for n in range(m + 1): sum_ += (A ** n) / factorial(n)
    block=(L / sum_)
    return block 
    
    
def getacell(pb, x):
    left = 0
    right = 1000

    # Perform binary search to find the minimum offered load with the desired blocking probability
    while True:
        mid = (left + right) / 2
        b = erlang(mid, x)
        if abs(b - pb) < 0.0001:
            return mid
        elif b > pb:
            right = mid
        else:
            left=mid
            
Pb = 0.001
total_slots = 8
slots_per_user = 2
No_channels = 125
Area = 450  # in Km2
Population = 1000000  # number of subscribers per city
l = 10  # calls per day
Call_duration = 1  # in minutes
ci = 6.25



sectoring_level=eval(input("Sectoring level(60,120,180):"))
Max_channels=eval(input("Maximum number of channels:"))
TDM=eval(input("TDM slots:"))

n=360/sectoring_level
N=(ci*n)/3
cluster_number=(Area*Population)/(Max_channels*math.sqrt(3))
channels_per_cluster=No_channels/cluster_number
Number_trunks=math.floor((channels_per_cluster/N)*TDM)
x = Number_trunks*n
a_user=l*Call_duration
a_cell=getacell(x,Pb)
y=a_cell/n
subscribers_cell=a_user/a_cell
total_subscribers=Area/Population
total_cells=total_subscribers/subscribers_cell
print(total_cells)
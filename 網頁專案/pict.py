# import matplotlib.pyplot as plt
# list1 = ['北投','萬華','文山']
# list2 = [30.5,44.5,44.7]
# plt.bar(list1,list2)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
font = {'family' : 'DFKai-SB',
'weight' : 'bold',
'size'  : '16'}
plt.rc('font', **font) # pass in the font dict as kwargs
plt.rc('axes',unicode_minus=False)
x = np.linspace(0, 10, 1000)
y = np.sin(x)
z = np.cos(x**2)
plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)
plt.plot(x,z,"b--",label="$cos(x^2)$")
plt.xlabel("x軸")
plt.ylabel("y軸")
plt.title("標題")
plt.ylim(-1.2,1.2)
plt.legend()
plt.show()
import numpy as np
data=np.asarray(data)
label=np.asarray(label)
data=data.reshape(5*number,100)
label=label.reshape(5*number,5)


data = data.astype('float32')
label = label.astype('float32')

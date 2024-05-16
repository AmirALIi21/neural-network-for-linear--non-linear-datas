hey there , this code is based on neural network to predict for linear and non-linear datas and it shows the result on a chart . if the dots are colser to the line it means 
the model is working great and if they are far away from it then it means the model is not working properly . 
the code is prety easy to understand and it dose have comment for better understanding , altough i think you might wanna know more about the reshape and the numbers you have to 
use for those sections .
in line 19 we have : print(x_train.shape,x_test.shape,y_train.shape,y_test.shape)
which show's us the shape of our data in this format :for example:  (69998,16)
so if you have a extra dimension it might look like :(69998, 16, 1)
although you can give the data dimension you can that in lines 22 ,23.
in line 27 : inputs=Input(shape=(7,)) for the example I said befor I put 16 instead of 7 (the second number of the print in line 19).

at last you change batch size and the epoch as you wish 

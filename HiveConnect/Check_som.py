def fun(x,y,z):
    print(x,y,z)

tuple_vec = (1,0,1)
fun(*tuple_vec)

dict_vec = {'x':1,'y':2,'z':3}
fun(**dict_vec)
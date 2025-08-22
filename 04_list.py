## list = podemos hacer acciones de (operaciones propias list) ##

my_list= list()
my_other_list=[]

my_list =[20,30,40,50,60,60,"fabith"]
print(len(my_list))

my_other_list=[35, 1.70, "BZuluaga"]
print(my_other_list)
print(type(my_other_list))

print(my_list.count(60))
print(my_list[0], my_list[3], my_list[-1])

print(my_list + my_other_list)

## elementos de una lista(es mutable)
my_other_list.append("fabithBZ")
my_other_list.insert(1, "GRIS")
my_other_list.remove("GRIS")
print(my_other_list)

my_list.remove(60)
print(my_list)

##operaciones propias con arreglos
my_list.pop() # solo - elimina el ultimo valor / elimina segun el indice quele pases ejm(2)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()
print(my_new_list)

my_list.clear()
print(my_list)

my_new_list.reverse()
print(my_new_list)

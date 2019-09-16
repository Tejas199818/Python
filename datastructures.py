def my_list():
    bike=['R15','RC 200','Duke 200','RTR 200']
    print("My bike list are : ",bike)
    bike.append('Kawasaki 300')
    print("Let me add Kawasaki 300 to my list \n",bike)
    bike.remove('RTR 200')
    print("I don't need RTR 200 in my list \n",bike)
    print("I have",len(bike),"bikes in my list")
    bike.remove('Kawasaki 300')
    print("Lets pop out Kawasaki since it's not in my budget\n",bike)
    bike.sort()
    print("My bike list in order\n",bike)
    print("\n\n")
my_list()
    
def my_tuple():
    game=('COD','PUBG','CS-GO')
    print("This is my tuple\n",game)
    print("CS-GO is",game.index('CS-GO'),"rd in my list")
    game+=('DOTA',)
    print("Let me add DOTA to my tuple",game)
    print("There are",len(game),"games in my tuple")
    print("\n\n")
my_tuple()
    
def abc2():
    print("DICTIONARY:")
    a={0:"Konichiwa",1:"Ohaiyo",2:"Kawaii",3:"Baka",4:"konoyaro",5:"Utsukushi",6:"Arigatho"}
    inp=int((input("Enter a number from 0 to 6\n")))
    print(a[inp])
    print("\n\n")
abc2()

def abc4():
    print("SETS:")
    a={0,1,2}
    b={2,3,4}
    print("Intersection",a&b)
    print()
    print("Union",a|b)
    print()
    print("A==B?",a==b)
    print()
    print("A-B",a-b)
    print()
    print("B-A",b-a)
    print()
    print("\n\n")
abc4() 

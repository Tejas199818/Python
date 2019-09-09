def my_list():
    bike=['R15','RC 200','Duke 200','RTR 200']
    print("My bike list are : ",bike)
    bike.append('Kawasaki 300')
    print("Let me add Kawasaki 300 to my list \n",bike)
    bike.remove('RTR 200')
    print("I don't need RTR 200 in my list \n",bike)
    print("I have",len(bike),"bikes in my list")
    bike.pop('Kawasaki 300')
    print("Lets pop out Kawasaki since it's not in my budget\n",bike)
    bike.sort()
    print("My bike list in order\n",bike)
    
def my_tuple():
    game=('COD','PUBG','CS-GO')
    print("This is my tuple\n",game)
    print("CS-GO is",game.index('CS-GO'),"rd in my list")
    game+=('DOTA',)
    print("Let me add DOTA to my tuple",game)
    print("There are",len(game),"games in my tuple")
    

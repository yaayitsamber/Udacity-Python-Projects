#first argument is start number, second number will count down to but not include,
#third number adds to the start number, or in this case with the (-) will subtract!
#Just a lil bit of practice! could have used reversed(range(100)):
def bottles_polyjuice():
    for x in range(99, 0, -1):
        print( str(x) + " Bottles of Polyjuice potion on the wall")
        print
        print( str(x) + " Bottles of Polyjuice potion")
        print
        print( "Take one down, pass it around.")
        print
        if x > 1:
            print( str(x - 1) + " Bottles of Polyjuice Potion on the wall")
            print
        elif x == 1:
            print( str(x) + " Bottle of Polyjuice Potion left on the wall")

bottles_polyjuice()

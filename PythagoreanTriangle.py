side_1 = raw_input("Enter triangle side 1")
side_2 = raw_input("Enter triangle side 2")
side_3 = raw_input("Enter triangle side 3")
hypotenuse = max(side_1,side_2,side_3)
a = min(side_1, side_2, side_3)
b = (int(hypotenuse) - int(a))

print int(hypotenuse)**2
print int(a)**2
print int(b)**2
if int(hypotenuse)/2 == 0 :
    print ("NOPE")
else:
    print ("Right on")

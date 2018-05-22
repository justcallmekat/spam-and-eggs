#This program will create a calculator that can compute the area of a circle and triangle
print "Shape Calculator Waking Up...\n"
option = str.upper(raw_input("Choose a shape. Enter 'C' for circle or 'T' for triangle: \n"))
if option == 'C':
  radius = float(raw_input("Input the radius: \n "))
  area = 3.14159 * radius**2
  print "The area is %s" % area
  
elif option == 'T':
  base = float(raw_input("Input the base: \n"))
  height = float(raw_input("Input the height: \n"))
  area = 0.5 * base * height
  print "The area is %s" % area
else:
  print "You've entered an invalid shape"

print "Shape Calculator is going back to sleep..."

h = float(input("Enter the x - coordinate of center of circle"))
k = float(input("Enter the y - coordinate of center of circle"))
x = float(input("Enter the x - coordinate of arbitary point"))
y = float(input("Enter the y - coordinate of arbitary point"))
r = float(input("Enter the radius of circle"))
if (x - h ) ** 2 + (y - k) **  2 - r ** 2 > 0 :
          print("Point is outside the circle")
elif (x - h ) ** 2 + (y - k) **  2 - r ** 2 == 0 :
          print("Point is on the circle")
else :
          print("Point is inside the circle")

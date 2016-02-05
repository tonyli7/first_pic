import math

pic = open("pic.ppm","w+")

info="P3 %d %d %d \n"
xres=500
yres=500
cmax=255

info=info%(xres,yres,cmax)

for x in range(0,500):
    line=""
    for y in range(0,500):
        pix="%d %d %d "
        
        red=(x+y)%255
        green=math.fabs(x-y)%255
        blue=(x*y)%255

        pix=pix%(red, green, blue)
        line+=pix
    line+="\n"
    info+=line

pic.write(info)
pic.close()

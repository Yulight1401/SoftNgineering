import project1

def run():
    result = 0
    result2 = 0
    functionx = 0
    x = [0,0,0]
    y = [0,0,0]
    p = [{x: 0,y: 0,z: 0},{x: 0,y: 0,z: 0},{x: 0,y: 0,z: 0}]

    while(x[1] <= 2 ):
        while(y[1] <= 2):
            while(x[0] <= 2):
                while(y[1] <=2):
                    p[0].x = x[0]
                    p[0].y = y[0]
                    functionx = result
                    result = 0
                    result += project1.radius(0)*project1.radius(0)
                    if result < functionx:
                        result = functionx

    print "resultone is" , result

    while(x[1] <= 2 ):
        while(y[1] <= 2):
            while(x[0] <= 2):
                while(y[1] <=2):
                    p[0].x = x[0]
                    p[0].y = y[0]
                    functionx = result
                    result = 0
                    result += project1.radius(0)*project1.radius(0)
                    if result < functionx:
                        result = functionx
                    if result2 == result:
                        print 'x1 is',x[0], 'y1 is', y[0], 'x2 is', x[1],'y2 is',y[1]
                        break


run()

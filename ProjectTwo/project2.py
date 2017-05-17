import math

#
def radius(i, p):
    m = 1000
    min = []
    min[0] = fabs(p[i].x - 0)
	min[1] = fabs(p[i].y - 0)
	min[2] = fabs(p[i].x - 2)
	min[3] = fabs(p[i].y - 2)

    for j in 4 :
		if mi[j] < m :
			m = mi[j]

    if i != 0 :
        for j in i :
            m = math.min(m, math.sqrt((p[i].x - p[j].x)*(p[i].x - p[j].x) + (p[i].y - p[j].y)*(p[i].y - p[j].y)) - radius(j))

    if m <= 0 :
        m = 0
        return m
    else:
        return m

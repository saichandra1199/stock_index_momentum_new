import csv,numpy

fil = open('returns.csv', 'w')
writer = csv.writer(fil)

for i in range(1,30):
    k = numpy.random.randint(10,5000)
    j = i + k
    writer.writerow([j])
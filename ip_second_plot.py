import pylab

principal  = 1000
interest   = 0.053
years      = 20
values 	 = []

for i in range(years + 1):
	values.append(principal)
	principal += principal * interest

pylab.figure(1)
pylab.plot(range(years + 1), values)
pylab.show()

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
pylab.title("5.3% interest on 1000 dollars saving, 20 years")
pylab.xlabel("Years 0 to 20")
pylab.ylabel("Principal")
pylab.show()

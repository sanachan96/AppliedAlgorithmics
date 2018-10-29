import time340

print("Initial test")
time = time340.TimeSpan(1, 2, 3)
print(time)
time2 = time340.TimeSpan(-10, 4, 1.5)
print(time2)
time33 = time340.TimeSpan(3923, -39, 5)
print(time33)


print("Only seconds")
time4 = time340.TimeSpan(60)
print(time4)
time6 = time340.TimeSpan(59)
print(time6)
time7 = time340.TimeSpan(5604)
print(time7)
print("time5")
time5 = time340.TimeSpan(2, 3, 4)
print(time5)
print("testing add")
time5 += time
print(time5)
time5 -= time
print(time5)

print("Testing Unary Negation")
timeA = time340.TimeSpan(3,2,5)
timeB = -timeA
print(timeA)
print(timeB)
time1010 = time
time1010 -= timeB
print(time1010)
print("")


print("Testing equality")
timeC = time340.TimeSpan(4, 39, 4)
print(timeC)
timeD = time340.TimeSpan(830, 39, 4)
print(timeD)
print("timeD is equal to timeC = " + str(timeD == timeC))
print(timeD != timeC)
timeD = time340.TimeSpan(6, 39, 7)
print("new timeD = " + str(timeD))
print("timeC is less than timeD = " + str(timeC < timeD))
print(timeC <= timeD)
print(timeC > timeD)
print(timeC >= timeC)

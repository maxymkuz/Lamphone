# This is python script that we have written in order to read
# input that we get from our photoresistor, and then
# plot the results and afterwards we can clearly see all the fluctuations of the lamp
import serial
import time
import matplotlib.pyplot as plt

# set up the serial line
ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(0.1)

# Read and record the data
time1 = time.time()
data = []
s = time.time()
for i in range(2000):
    b = ser.readline()  # read a byte string
    string_n = b.decode()  # decode byte string into Unicode
    string = string_n.rstrip()  # remove \n and \r
    # print(string)
    integer = int(string)  # convert string to integer
    # print(flt)
    data.append(integer)  # add to the end of data list
    time.sleep(0.01)  # wait (sleep) 0.01 seconds
ser.close()
print(time.time() - time1)
for line in data:
    print(line)

# show the data
plt.plot(data)
plt.xlabel('Time (miliseconds)')
plt.ylabel('Potentiometer Reading')
plt.title('Potentiometer Reading vs. Time')
plt.show()
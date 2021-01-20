# Progress

### Device setup
As you have suggested, in order to focus light on the sensor from one direction,
we have constructed  a tube covered with duct tape that does not let the light through and is fixed 
on top of our photoresistor.

![our device-1](https://github.com/UKU-mentoring-abench/lamphone-1/blob/main/media/device-1.jpg)
![our device-2](https://github.com/UKU-mentoring-abench/lamphone-1/blob/main/media/device-2.jpg)

### Experiment
We conducted real time experiments on a hanging light bulb. Then we used obtained data from the sensor in Python script to make a fluctuations plot
where we can clearly see the fluctuations and how they go out.

![plot](https://github.com/UKU-mentoring-abench/lamphone-1/blob/main/media/lamp_fluctuations.png) 

### Problems
1. We need do adjust sensitivity of photo resistor, because it transfers light brightness in a too wide range.
2. Maximal sensor frequency that we have managed to get is 2-3 measurements 100 microseconds(0.0002 seconds) (which would not be enough to detect brightness fluctuations caused by sound in range 20-20000 Hz)

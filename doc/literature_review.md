## Ways of gathering data:
### 1) Camera
- First way to get sound from a video is to analuze vibrations of the surfaces of some lightweight objects, like a bag of chips or leafs, or balloon. 
- The problem is, in order to capture all the frequencies(especially high frequencies) of the sound, we need high-speed cameras. 
- It should be able to film more than 1500-2000+ frames per second. Also, processing of such a high frame rate video requires a looot of computational power, and the algorithm is hard to write.
### 2) Optical sensor
- When sound hits the surface of the bulb, the amount of light at different angles is different.
- In order to retrieve speech, we need our input device to have a precision of few millidegrees(10^-3 degrees)
- Also, This method requires some kind of telescope to direct the light from the lamp into an electro-optical sensor. Then we can convert measurements from sensor to digital data using Analog-to-digital Converter(ADC), and then process it.
- The bigger lens the telescope— the better. The telescope with a bigger diameter is able to capture and focus on the optical sensor more light.
### 3) Laser microphone
- We can point a laser at an object and then analyze object’s response to sound.
- Can be built using a laser pointer, an NPN PhotoTransistor, a headphone amp, and a handful of miscellaneous electronics parts.
- Hard to get a clear audio signal it is imperative that the angle of the laser beam be close to 90 degrees to the surface of the window.

## Need to be aware of in the future:
- Google cloud speech API
- Algorithms of processing gathered data (Bandstop filtering, Normalization, Noise reduction, e.t.c.)

### First steps
 - Choose a way to gather data
 - Get fist data and try to process it

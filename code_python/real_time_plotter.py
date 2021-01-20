import serial
import time
import matplotlib.pyplot as plt
import numpy as np


class SerialPort:
    """ A class for all kinds of manipulations with data from serial port"""

    def __init__(self, serialPort="/dev/ttyACM0", baudRate=115200,
                 plotLength=100):
        self.port = serialPort
        self.baud = baudRate
        self.plotMaxLength = plotLength
        self.plotLength = plotLength
        self.serialConnection = serial.Serial(self.port, self.baud, timeout=4)
        time.sleep(0.1)
        self.y_data = []
        self.x_time = []

    @staticmethod
    def us_to_ms(mu):
        """Function to convert microseconds to milliseconds"""
        return mu / 1000

    def readValue(self):
        """Reads a single value and it's time in us from the serial port"""
        # read and decode byte string into Unicode
        string_n = self.serialConnection.readline().decode()
        if len(string_n) <= 0:
            print("Null string")
            return
        try:
            # converting both values to int to plot later, and removing \n and \r
            value, time_us = tuple(map(int, string_n.rstrip().split()))
            time_ms = self.us_to_ms(time_us)
            # print(string_n, end="")
            if value > 1000:
                print("sth wrong", string_n)
                return

            self.y_data.append(value)
            self.x_time.append(time_ms)
        except:
            print(string_n, "failure")

    def close(self):
        self.serialConnection.close()
        print('Disconnected from stm32')

    def time_normalize(self):
        self.x_time = list(map(lambda x: x - self.x_time[0], self.x_time))

    def plot(self, plotLength):
        """ Plots exactly $plotLength values from com port """
        self.x_time = self.x_time[-plotLength:]
        self.y_data = self.y_data[-plotLength:]
        self.time_normalize()
        print(f"Min: {min(self.y_data)}\nMax: "
              f"{max(self.y_data)}\nDifference: {max(self.y_data) - min(self.y_data)}")
        # print(self.x_time)
        plt.plot(self.x_time, self.y_data)
        plt.xlabel('Time (miliseconds)')
        # plt.ylabel('Potentiometer Reading')
        plt.ylabel('Time, when the diode is up, microseconds')

        plt.title('Time, when the diode is up vs. Time')
        plt.show()
        # plt.style.use('fivethirtyeight')
        # ani = FuncAnimation(plt.gcf(), self.animate, interval=1000)
        #
        # plt.tight_layout(


def convert_to_wav(s):
    # print(s.x_time)
    print(s.y_data)
    time_ms = s.x_time[-1]
    wav_wave = s.y_data
    samplerate = 1000 * len(s.y_data) / time_ms

    print("_" * 20, min(s.y_data), max(s.y_data))

    # scaling the wave:
    # wav_wave = list(map(lambda x: int((x - min(wav_wave)) *
    #                                (65000 / max(wav_wave))) - 32767, wav_wave))

    wav_wave = np.int16(wav_wave)
    print(wav_wave)
    scaler = 30000 / max([abs(min(wav_wave)), max(wav_wave)])
    wav_wave *= int(scaler)
    print("scaler:", scaler)
    # scaling around the mean
    mean = sum(wav_wave) / len(wav_wave)
    print(wav_wave)

    print("Mean:", mean, len(wav_wave))
    wav_wave = wav_wave - int(mean)

    # wav_wave = list(map(lambda x: int(x * scaler), wav_wave))
    # wav_wave = list(map(lambda x: int((x - min(wav_wave)) *
    #                                (65000 / max(wav_wave))), wav_wave))

    print(wav_wave)

    print("samplrate:", samplerate, int(samplerate))
    print(type(wav_wave[0]))

    # converting to wav
    import scipy
    from scipy import io
    from scipy.io import wavfile
    scipy.io.wavfile.write("received.wav", int(samplerate), wav_wave)


def main():
    s = SerialPort()
    times = 20000

    for i in range(times):
        s.readValue()

    s.plot(times)

    convert_to_wav(s)


if __name__ == '__main__':
    main()

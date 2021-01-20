import numpy as np
import sounddevice as sd
import json
import pickle
import matplotlib.pyplot as plt
from scipy.io import wavfile


def wav_to_digital(path):
    samplerate, data = wavfile.read(path)
    print(samplerate)
    length = data.shape[0] / samplerate
    print(f"length = {data.shape[0] / samplerate}s")

    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data, label="Left channel")
    plt.legend()
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")
    # plt.show()

    data = data.tolist()  # convert ndarray to usual list

    # scaling the data:
    scaler = 15000 / max([abs(min(data)), max(data)])
    # data *= int(scaler)
    data = list(map(lambda x: int(x * scaler), data))
    # print(data)

    data = list(map(lambda x: x + 32768 // 2, data))
    print(data)

    print("scaler:", scaler)

    to_json = {"samplerate": samplerate,
               "data": data}
    print(max(data))
    print(min(data))
    with open("../data/data.json", 'w', encoding="utf-8") as f:
        json.dump(to_json, f)

    return data, samplerate


def digital_to_wav(samplerate, path, play=True):

    with open(path, "r") as read_file:
        wav_wave = json.load(read_file)['data']
        wav_wave = list(map(lambda x: x - 32767, wav_wave))

        # Proper scaling if we need one:
        wav_wave = np.int16(wav_wave / np.max(np.abs(wav_wave)) * 32767)

    # Save a numpy array to the file if we need it:
    with open('../data/input.pkl', 'wb') as f:
        pickle.dump(wav_wave, f)
        # wav_wave = pickle.load(f)

    if play:
        sd.default.samplerate = samplerate
        print(samplerate)
        print(wav_wave)
        print(type(wav_wave[0]))
        sd.play(wav_wave, blocking=True)

    return wav_wave


if __name__ == '__main__':
    # digital_to_wav(1000, "../data/data.json", True)
    wav_to_digital("../data/semchyshyn.wav")

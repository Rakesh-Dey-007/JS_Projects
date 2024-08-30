from scipy.io.wavfile import write
import wavio as wv
import sounddevice as sound

freq = 44100

duration = 10

recording = sound.rec(int(duration*freq),
                      samplerate=freq, channels=2)

sound.wait()
write("recording.wav", freq, recording)
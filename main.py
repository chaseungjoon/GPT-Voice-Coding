import openai
import pyaudio
import wave
import os
import signal

def speech_to_text(param):
    openai.api_key = '본인의 API Key'
    response = openai.Audio.transcribe(
        model = 'whisper-1',
        file = param,
        temperature = 0.2
    )
    return response['text']

def chat_completion(param):
    openai.api_key = '본인의 API Key'
    response = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {'role': 'system', 'content': ''},
            {'role': 'user', 'content': 'convert the following text into fitting python syntax : '+param+', Give me only the code'}
        ],
        temperature = 0.2
    )
    return response['choices'][0]['message']['content']

FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "output.wav"

audio = pyaudio.PyAudio()

# Open microphone stream
stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording started, \nCtrl+C to stop Recording")

# Record audio until keyboard interrupt
frames = []
interrupted = False

def interrupt_handler(signal, frame):
    global interrupted
    interrupted = True

# Listen for keyboard interrupt
signal.signal(signal.SIGINT, interrupt_handler)

while not interrupted:
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording finished")

# Stop recording and close stream
stream.stop_stream()
stream.close()
audio.terminate()

# Save recorded audio to WAV file
if os.path.exists(WAVE_OUTPUT_FILENAME):
    os.remove(WAVE_OUTPUT_FILENAME)
waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
waveFile.setnchannels(CHANNELS)
waveFile.setsampwidth(audio.get_sample_size(FORMAT))
waveFile.setframerate(RATE)
waveFile.writeframes(b''.join(frames))
waveFile.close()

audio2 = open("프로젝트 파일 디렉토리/output.wav", "rb")

with open('new.py', 'w') as file:
    file.write(chat_completion(speech_to_text(audio2)))
print("Your .py file has been created.")

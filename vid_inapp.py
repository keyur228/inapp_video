import moviepy.editor as mp
import speech_recognition as sr

# Load the video
video_path = input("Enter the path to the video file: ")
video = mp.VideoFileClip(video_path)

# Extract audio from the video
audio_file = video.audio
audio_file.write_audiofile("output.wav")

# Load the newly converted audio file
r = sr.Recognizer()
with sr.AudioFile("output.wav") as source:
    audio_data = r.record(source)

# Convert audio to text
try:
    text = r.recognize_google(audio_data)
    print("Transcribed text from the video:\n", text)
except sr.UnknownValueError:
    print("Could not understand audio.")
except sr.RequestError:
    print("Could not request results; check your network connection.")

import librosa
import os

path = os.getenv('dancey')
path = path + 'Fotonovela_lib.mp3'
print(path)
y, sr =librosa.load(path)

tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

tempo = int(tempo)
print(f'Estimated tempo: {tempo} beats per minute'.format(tempo))

beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(beat_times)

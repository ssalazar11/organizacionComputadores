from pydub import AudioSegment
import numpy as np
import threading
import argparse

parser=argparse.ArgumentParser()
parser.add_argument("-s","--opcion",action="store_true", help="Sea ejecutado sequencial")
parser.add_argument("archivoUno", help="Primer archivo mp3")
parser.add_argument("archivoDos", help="Segundo archivo mp3")
args=parser.parse_args()

dirArchivoUno=args.archivoUno
dirArchivoDos=args.archivoDos

if args.opcion:
    audioUno=AudioSegment.from_mp3(dirArchivoUno)
    audioDos=AudioSegment.from_mp3(dirArchivoDos)
    duracionTotal=max(len(audioUno), len(audioDos))

    mezcla=audioUno.overlay(audioDos[:duracionTotal])
    mezcla.export("mezcla.mp3", format="mp3")



song_mix = int()

def treat_song(song, least):

    global song_mix

    time = least - len(song)

    silence = AudioSegment.silent(duration=time)

    song += silence
    
    song = song[:least]

    sample = np.array(song.get_array_of_samples())

    g = 0.5

    sample = (sample * g).astype(np.int16)

    song_mix += sample

def musicmixer(file1, file2):
    new_song = None
    arr = []

    Song1 = AudioSegment.from_mp3(file1)
    Song2 = AudioSegment.from_mp3(file2)
    arr.append(Song1)
    arr.append(Song2)

    least = max(len(Song1), len(Song2))

    for i in range(len(arr)):

        thread = threading.Thread(target=treat_song, args=(arr[i], least))
        thread.start()
        thread.join()


    new_song = AudioSegment(data=song_mix.tobytes(), 
                            sample_width=Song1.sample_width,
                            frame_rate=Song1.frame_rate,
                            channels=Song1.channels)
    
    new_song.export("new_song.mp3", format="mp3")

file1 = dirArchivoUno
file2 = dirArchivoDos

musicmixer(file1, file2)



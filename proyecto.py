from pydub import AudioSegment

audioUno=AudioSegment.from_file("archivos/Kendrick_Lamar_HUMBLE_.mp3", format="mp3")
audioDos=AudioSegment.from_file("archivos/FEEL.mp3", format="mp3")

audioData=audioUno.get_array_of_samples()

print(len(audioData))
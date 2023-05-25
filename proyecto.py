from pydub import AudioSegment

audioUno=AudioSegment.from_file("archivos/Kendrick_Lamar_HUMBLE_.mp3", format="mp3")
audioDos=AudioSegment.from_file("archivos/FEEL_.mp3", format="mp3")

audioData=audioUno.get_array_of_samples()
audioDataDos=audioDos.get_array_of_samples()

for i in range(len(audioDos)):
    f=i*1000
    resultado=audioUno[:f]+audioDos[:f]


resultado.export("resultado.mp3", format="mp3")
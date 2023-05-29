from pydub import AudioSegment


audioUno=AudioSegment.from_mp3("archivos/Kendrick_Lamar_HUMBLE_.mp3")
audioDos=AudioSegment.from_mp3("archivos/FEEL_.mp3")
duracionTotal=max(len(audioUno), len(audioDos))

mezcla=audioUno.overlay(audioDos[:duracionTotal])



mezcla.export("mezcla.mp3", format="mp3")
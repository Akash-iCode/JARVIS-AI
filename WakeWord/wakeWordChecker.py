import struct
import pyaudio
import pvporcupine

class isHotWordCalled:
    
    def __init__(self, access_key, keywords):
        self.porcupine = pvporcupine.create(access_key=access_key, keywords=keywords)
        self.pa = pyaudio.PyAudio()
        self.audio_stream = self.pa.open(rate=self.porcupine.sample_rate,
                            channels=1,
                            format=pyaudio.paInt16,
                            input=True,
                            frames_per_buffer=self.porcupine.frame_length)
        
    def __del__(self):
        if self.porcupine is not None:
            self.porcupine.delete()

        if self.audio_stream is not None:
            self.audio_stream.close()

        if self.pa is not None:
                self.pa.terminate()
    
    def is_keyword_detected(self):
        pcm = self.audio_stream.read(self.porcupine.frame_length)
        pcm = struct.unpack_from("h" * self.porcupine.frame_length, pcm)

        keyword_index = self.porcupine.process(pcm)

        if keyword_index >= 0:
            return True
        else:
            return False

from re import X
import streamlit as st
import json
import pyaudio
from vosk import Model, KaldiRecognizer
import pandas as pd
import numpy as np


st.markdown("# Vosk")
st.sidebar.header("vosk")







useVoice = st.checkbox('voise')

# TODO save to session storage
result = ''
st.write('result' + result)

if useVoice:
    # model = Model(r"C:\Users\ymalakhova\projects\streamlit_app\vosk-model-small-en-us-0.15")
    model = Model(lang="en-us")
    recognizer = KaldiRecognizer(model, 16000)    
    mic = pyaudio.PyAudio()
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    while useVoice:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            cur_result = json.loads(recognizer.Result())
            print(len(cur_result['text']))
            print(len(result))
            if len(cur_result['text']) and len(result):
                result = result + ' ' + cur_result['text']
            elif len(cur_result['text']) and not len(result):
                result = cur_result['text']

            print('CURRENT RESULT', cur_result)
            print('RESULT', result)
            st.write('result inside if' + result)
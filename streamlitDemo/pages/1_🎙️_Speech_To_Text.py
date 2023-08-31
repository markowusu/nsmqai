import streamlit as st
import os
from utility import DEMO_AUDIO_3_PATH, NO_API_SET_FLAG, get_stt_api, realtime_audio_file_STT, realtime_audio_recording_STT, autoplay_audio

st.set_page_config(page_title="Speech To Text Demo", page_icon="🎙️", layout="wide")

st.markdown("# Speech To Text Demo🎙️")
st.write(
    """
    This demo illustrates a real time transcription of the Speech To Text Model of the NSMQ AI. 
    Try out an audio sample or test with a live recording of your own voice!
    """
)

# with open(DEMO_AUDIO_3_PATH, "rb") as audio_file:
#     print("Demo Audio 3")

# dir_path = os.path.dirname(os.path.realpath(__file__))
# print(dir_path)


# print("======")
# file_stats = os.stat(DEMO_AUDIO_3_PATH)      
# print(file_stats)
# print(f'File Size in Bytes is {file_stats.st_size}')
# print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
# print("======")

# print("========2")
# cwd = os.getcwd()
# print(cwd)

# path_to_find = os.listdir()
# st.title(path_to_find)
# print("========2")

# print("=======3")
# file_path = cwd+"/streamlitDemo"+DEMO_AUDIO_3_PATH

# with open(file_path):
#     print("Finally")


# print("======1")
# file_stats = os.stat(dir_path)      
# print(file_stats)
# print(f'File Size in Bytes is {file_stats.st_size}')
# print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')
# print("======1")



if get_stt_api() == NO_API_SET_FLAG:
    st.warning('Please setup the STT API endpoint on the API Setup page', icon="⚠️")

sampleAudioTab, liveRecordingTab = st.tabs(["AUDIO SAMPLE", "TEST LIVE RECORDING"])

with sampleAudioTab:
    if st.button('Start Transcribing Sample'):
        autoplay_audio(DEMO_AUDIO_3_PATH)
        realtime_audio_file_STT(DEMO_AUDIO_3_PATH)


with liveRecordingTab:
    realtime_audio_recording_STT()


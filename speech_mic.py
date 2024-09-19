import os
import time
import azure.cognitiveservices.speech as speechsdk
import tempfile
from dotenv import load_dotenv

load_dotenv()

stop_flag = False
diarize_text = ""
def conversation_transcriber_recognition_canceled_cb(evt: speechsdk.SessionEventArgs):
    print('Canceled event {}'.format(evt))
    print('Canceled event')
    
def conversation_transcriber_session_stopped_cb(evt: speechsdk.SessionEventArgs):
    print('SessionStopped event')
def conversation_transcriber_transcribed_cb(evt: speechsdk.SpeechRecognitionEventArgs):
    global diarize_text
    if evt.result.reason == speechsdk.ResultReason.RecognizedSpeech:
        if evt.result.speaker_id and evt.result.speaker_id != "Unknown":
            # calculate start end time, convert into second.
            start_time = getFormattedTime(evt.result._offset/10000000)
            end_time = getFormattedTime(
                    (evt.result._offset + evt.result.duration)/10000000)
            print(f"{evt.result.speaker_id} ({start_time}-{end_time}): {evt.result.text}\n")
            diarize_text = f"{evt.result.speaker_id} ({start_time}-{end_time}): {evt.result.text}\n"
            return diarize_text
        # ``print('\tText={}'.format(evt.result.text))
        # print('\tSpeaker ID={}'.format(evt.result.speaker_id))``
    elif evt.result.reason == speechsdk.ResultReason.NoMatch:
        print('\tNOMATCH: Speech could not be TRANSCRIBED: {}'.format(
            evt.result.no_match_details))
def conversation_transcriber_session_started_cb(evt: speechsdk.SessionEventArgs):
    print('SessionStarted event',format(evt))
    global diarize_text
    diarize_text = ""
        
    
def recognize_from_mic():
    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    speech_config.speech_recognition_language="en-US"
    
    
    audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
    # audio_config = speechsdk.audio.AudioConfig(filename=temp_filename)
    print("speak on mic :")
    
    # print("Speak into your microphone.")
    conversation_transcriber = speechsdk.transcription.ConversationTranscriber(
        speech_config=speech_config, audio_config=audio_config)
    
    global stop_flag
    transcribing_stop = False
    def stop_cb(evt: speechsdk.SessionEventArgs):
        # """callback that signals to stop continuous recognition upon
        # receiving an event `evt`"""
        # print('CLOSING on {}'.format(evt))
        nonlocal transcribing_stop
        transcribing_stop = True
    # Connect callbacks to the events fired by the conversation transcriber
    conversation_transcriber.transcribed.connect(
        conversation_transcriber_transcribed_cb)
    conversation_transcriber.session_started.connect(
        conversation_transcriber_session_started_cb)
    conversation_transcriber.session_stopped.connect(
        conversation_transcriber_session_stopped_cb)
    conversation_transcriber.canceled.connect(
        conversation_transcriber_recognition_canceled_cb)
    # stop transcribing on either session stopped or canceled events
    conversation_transcriber.session_stopped.connect(stop_cb)
    conversation_transcriber.canceled.connect(stop_cb)
    conversation_transcriber.start_transcribing_async()
    # Waits for completion.
    while not transcribing_stop:
        time.sleep(.5)
        # conversation_transcriber.stop_transcribing_async()
    conversation_transcriber.stop_transcribing_async()


def getFormattedTime(seconds=0):
    s_min, s_sec = divmod(seconds, 60)
    # s_hr, s_min = divmod(s_min, 60)
    return "%0d:%02d" % (s_min, s_sec)

    
def stop():
    global stop_flag
    stop_flag = True
    
recognize_from_mic()      

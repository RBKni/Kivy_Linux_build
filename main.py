from kivy.app import App

from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout

from kivy.uix.textinput import TextInput

from android.storage import primary_external_storage_path

from jnius import autoclass

from plyer import vibrator

import plyer # IOS

import os



# err = ""

# try:

#     from plyer import audio

# except Exception as e:

#     err = str(dir(plyer))  # str(e)



# Recorder Classes

MediaRecorder = autoclass('android.media.MediaRecorder')

AudioSource = autoclass('android.media.MediaRecorder$AudioSource')

OutputFormat = autoclass('android.media.MediaRecorder$OutputFormat')

AudioEncoder = autoclass('android.media.MediaRecorder$AudioEncoder')

Context = autoclass('android.content.Context')

activity = autoclass('org.kivy.android.PythonActivity').mActivity



class Recorder:

    def __init__(self, filename):

        filename_without_ext = os.path.splitext(filename)[0]

        filename_with_mp3_ext = f"{filename_without_ext}.mp3"

        self.file_path = os.path.join(activity.getExternalFilesDir(None).getAbsolutePath(), filename_with_mp3_ext)



    def start(self):

        self._recorder = MediaRecorder()

        self._recorder.setAudioSource(AudioSource.MIC)

        self._recorder.setOutputFormat(OutputFormat.MPEG_4)

        self._recorder.setAudioEncoder(AudioEncoder.HE_AAC)

        self._recorder.setAudioChannels(1)  # 單通

        self._recorder.setAudioEncodingBitRate(128000)

        self._recorder.setAudioSamplingRate(44100)

        self._recorder.setOutputFile(self.file_path)

        self._recorder.prepare()

        self._recorder.start()



    def stop(self):

        if self._recorder:

            self._recorder.stop()

            self._recorder.release()

            self._recorder = None



class MyApp(App):

    def build(self):

        layout = BoxLayout(orientation='vertical')

        self.textinput = TextInput()

        self.audio = Recorder("audio.mp3")

        btn_start = Button(text='start')

        btn_stop = Button(text='stop')

        btn_start.bind(on_press=self.start_recording)

        btn_stop.bind(on_press=self.do_stop)

        layout.add_widget(self.textinput)

        layout.add_widget(btn_start)

        layout.add_widget(btn_stop)

        return layout



    def start_recording(self, instance):

        self.audio.start()

        self.textinput.text = "start"

        vibrator.vibrate(0.2)



    def do_stop(self, instance):

        self.audio.stop()

        if self.check_file_exists():

            self.textinput.text = "File saved: " + self.audio.file_path

            vibrator.vibrate(0.2)

        else:

            self.textinput.text = "File not saved"

        print("File path:", self.audio.file_path)

        print("File exists:", self.check_file_exists())



    def check_file_exists(self):

        return os.path.isfile(self.audio.file_path)



if __name__ == "__main__":

    MyApp().run()

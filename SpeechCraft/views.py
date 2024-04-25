from django.shortcuts import render
from googletrans import Translator
import speech_recognition as sr
from gtts import gTTS
import os



# List of supported languages and their codes
languages = {
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'english': 'en',
    'zulu': 'zu', 'marathi': 'mr',
}



def text_to_voice(request):
    supported_languages = {
        'en': 'English',
        'mr': 'Marathi',
        'hi': 'Hindi',
        'ja': 'Japanese',
        'es': 'Spanish',
        'fr': 'French',
        'de': 'German',
        'it': 'Italian',
        'zh': 'Chinese',
        'ko': 'Korean',
        'ru': 'Russian',
    }


    converted_text = ''

    if request.method == 'POST':
        if 'text' in request.POST:
            # Text-to-Text conversion
            text = request.POST.get('text', '')
            selected_language = request.POST.get('language', 'en')

            if text:
                try:
                    # Text-to-Speech
                    translator = Translator()
                    translated_text = translator.translate(text, dest=selected_language).text
                    myobj = gTTS(text=translated_text, lang=selected_language, slow=False)
                    save_path = 'static/speech.mp3'
                    myobj.save(save_path)
                    converted_text = translated_text
                except Exception as e:
                    print(f"Error during conversion: {e}")

    context = {'converted_text': converted_text, 'supported_languages': supported_languages}
    return render(request, 'SpeechCraft/home.html', context)


def convert(request):
    return render(request,'SpeechCraft/converter.html')

# def voice_to_text(request):
#     converted_text = ''

#     if request.method == 'POST':
#         form = AudioForm(request.POST, request.FILES)
#         if form.is_valid():
#             language = form.cleaned_data.get('language')  # Use get() method for safe access
#             audio_file = request.FILES.get('audio_data')  # Use get() method for safe access
#             if language and audio_file:
#                 try:
#                     recognizer = sr.Recognizer()
#                     with sr.AudioFile(audio_file) as source:
#                         audio_data = recognizer.record(source)
#                         converted_text = recognizer.recognize_google(audio_data, language=language)
#                 except sr.UnknownValueError:
#                     converted_text = "Speech could not be understood"
#                 except sr.RequestError as e:
#                     converted_text = f"Could not request results; {e}"
#             else:
#                 converted_text = "Invalid form data"
#     else:
#         form = AudioForm()

#     return render(request, 'SpeechCraft/voice_to_text.html', {'form': form, 'converted_text': converted_text})


# def voice_to_voice(request):
#     translated_audio_path = None

#     if request.method == 'POST':
#         form = AudioForm(request.POST, request.FILES)
#         if form.is_valid():
#             source_language = form.cleaned_data['source_language']
#             target_language = form.cleaned_data['target_language']
#             audio_file = request.FILES['audio_data']
#             try:
#                 recognizer = sr.Recognizer()
#                 translator = Translator()

#                 with sr.AudioFile(audio_file) as source:
#                     audio_data = recognizer.record(source)
#                     text = recognizer.recognize_google(audio_data, language=source_language)
#                     translated_text = translator.translate(text, src=source_language, dest=target_language).text

#                     tts = gTTS(text=translated_text, lang=target_language, slow=False)
#                     translated_audio_path = 'static/translated_audio.mp3'
#                     tts.save(translated_audio_path)
#             except Exception as e:
#                 print(f"Error during conversion: {e}")
#     else:
#         form = AudioForm()

#     return render(request, 'SpeechCraft/voice_to_voice.html', {'form': form, 'translated_audio_path': translated_audio_path})
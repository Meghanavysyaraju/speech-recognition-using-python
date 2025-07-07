import speech_recognition as sr

def speech_to_text():
    """
    Performs speech recognition using the default microphone and Google Speech Recognition.

    Returns:
        str: The recognized text, or an error message if recognition fails.
    """
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Speak Anything:")
            r.adjust_for_ambient_noise(source)  # Added to handle background noise
            audio = r.listen(source)

        text = r.recognize_google(audio)
        print("You said: {}".format(text))
        return text

    except sr.UnknownValueError:
        print("Sorry, could not understand what you said.")
        return "Recognition Error: Unable to recognize speech"

    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return f"Recognition Error: {e}"

    except Exception as e:  # Added a general exception block for safety
        print(f"An unexpected error occurred: {e}")
        return f"Error: {e}"

if __name__ == "__main__":
    recognized_text = speech_to_text()

import sys
import subprocess

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

install("numpy")
install("pandas")
install("matplotlib")
install("seaborn")
install("scikit-learn")
install("keras")
install("opencv-python")
install("imutils")
install("pytesseract")
install("pyautogui")
install("pyperclip")
install("speechrecognition")
install("pyttsx3")
install("pywhatkit")
install("pyjokes")
install("pywikihow")
install("wikipedia")
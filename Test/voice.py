import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import pygame

class VoiceAssistantApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Голосовой помощник")
        self.root.geometry("400x300")
        
        # Инициализация движка для синтеза речи
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 150)  # Скорость речи
        
        # Инициализация распознавателя речи
        self.recognizer = sr.Recognizer()
        
        # Создание интерфейса
        self.create_widgets()
        
        # База данных "пользователей" (для примера)
        self.users = {
            "иван": {"action": self.open_user_ivan, "info": "Открываю профиль Ивана"},
            "мария": {"action": self.open_user_maria, "info": "Открываю профиль Марии"},
            "дмитрий": {"action": self.open_user_dmitry, "info": "Открываю профиль Дмитрия"}
        }
    
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Голосовой помощник", font=('Arial', 16))
        self.label.pack(pady=20)
        
        self.btn_listen = tk.Button(self.root, text="Говорить", command=self.listen_command)
        self.btn_listen.pack(pady=10)
        
        self.text_output = tk.Text(self.root, height=8, width=40)
        self.text_output.pack(pady=10)
    
    
    
    def speak(self, text):

        def play_audio(filename):
            pygame.mixer.init()
            try:
                sound = pygame.mixer.Sound(filename)
                sound.play()
                pygame.time.wait(int(sound.get_length() * 1000))  # Ждём окончания
            except Exception as e:
                print(f"Ошибка: {e}")

        """Воспроизводит WAV-файл вместо синтеза речи"""
        audio_files = {
        "Привет, я ваш голосовой помощник": "привет.wav",
        "Открываю профиль Ивана": "Open.mp3",
        "До свидания!": "Back.mp3",
        }
    
        if text in audio_files:
            play_audio(audio_files[text])
        else:
            print(f"Аудиофайл для фразы '{text}' не найден")
        
    
    def listen_command(self):
        """Слушать и распознавать команду"""
        with sr.Microphone() as source:
            self.text_output.insert(tk.END, "Слушаю...\n")
            self.root.update()  # Обновляем интерфейс
            
            audio = self.recognizer.listen(source)
            
            try:
                command = self.recognizer.recognize_google(audio, language="ru-RU").lower()
                self.text_output.insert(tk.END, f"Вы сказали: {command}\n")
                self.process_command(command)
                
            except sr.UnknownValueError:
                self.speak("Я вас не понял")
            except sr.RequestError:
                self.speak("Проблемы с доступом к сервису распознавания")
    
    def process_command(self, command):
        """Обработка команд"""
        # Проверяем команды на открытие пользователей
        for user in self.users:
            if user in command:
                self.users[user]["action"]()
                self.speak(self.users[user]["info"])
                return
        
        # Другие команды
        if "открой браузер" in command:
            webbrowser.open("https://www.yandex.ru")
            
        elif "время" in command:
            # Здесь можно добавить получение времени
            self.speak("Извините, эта функция пока не реализована")
        elif "пока" in command or "выход" in command:
            self.speak("До свидания!")
            self.root.after(1000, self.root.destroy)
        else:
            self.speak("Я не понял вашу команду")
    
    # Методы для открытия пользователей (можно заменить на реальные действия)
    def open_user_ivan(self):
        messagebox.showinfo("Пользователь", "Открыт профиль Ивана\nID: 12345")
    
    def open_user_maria(self):
        messagebox.showinfo("Пользователь", "Открыт профиль Марии\nID: 67890")
    
    def open_user_dmitry(self):
        messagebox.showinfo("Пользователь", "Открыт профиль Дмитрия\nID: 54321")

if __name__ == "__main__":
    root = tk.Tk()
    app = VoiceAssistantApp(root)
    root.mainloop()
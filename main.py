class Device:
    def __init__(self):
        print("Створено пристрій")

class Phone(Device):
    def __init__(self):
        self.phone_number = "0687362734"
        super().__init__()

    def call(self):
        print("Дзвінок на номер", self.phone_number)

class Camera(Device):
    def __init__(self):
        self.camera = "48 мп"
        super().__init__()

    def take_photo(self):
        print("Фото зроблено. Камера:", self.camera)

class MusicPlayer(Device):
    def __init__(self):
        self.music = "Улюбленна музика"
        super().__init__()

    def play_music(self):
        print("Відтворюється", self.music)

class Smartphone(Phone, Camera, MusicPlayer):
    def __init__(self):
        super().__init__()
        print("Створюємо смартфон")

my_phone = Smartphone()
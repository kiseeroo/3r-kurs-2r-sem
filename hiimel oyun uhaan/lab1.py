import random

class Dog:
    def __init__(self, rooms):
        self.rooms = rooms  
        self.rows = len(rooms)
        self.cols = len(rooms[0])
        self.life = 2
        self.row = 0
        self.col = 0
        self.hungry = True
        self.dirty = False
        self.direction = 1 
        self.empty_count = 0    

    def lose_life(self):
        self.life -= 1
        if self.life > 0:
            print(f"Нохой нэг амь алдаж, үлдсэн амь: {self.life}")
        else:
            print("Нохой бүх амьдралаа алдаж, нас барлаа.")

    def dog_state(self):
        room = self.rooms[self.row][self.col]
        print(f"\nНохой [{self.row}][{self.col}] өрөөнд ({room}) байна.")

        if room == "food":
            print("Нохой хоол идэж байна.")
            self.hungry = False
            self.empty_count = 0  

        elif room == "bed":
            if not self.hungry:
                print("Нохой хоол идээд унтсан тул үхлээ!")
                self.lose_life()
            else:
                print("Нохой унтаж байна.")
                self.hungry = True
            self.empty_count = 0  

        elif room == "toy":
            if self.hungry:
                print("Нохой өлсгөлөн үедээ тоглосон тул амь алдав!")
                self.lose_life()
            else:
                print("Нохой тоглож байна.")
                self.hungry = True  
            self.empty_count = 0  

        elif room == "bath":
            print("Нохой усанд орж байна.")
            self.dirty = False  
            self.empty_count = 0  

        elif room == "park":
            if self.dirty:
                print("Нохой бохир байсан тул гадаа гараад өвчин тусаж үхлээ!")
                self.lose_life()
            else:
                print("Нохой гадаа салхилж байна.")
            self.empty_count = 0  

        elif room == "empty":
            print("Хоосон өрөөнд орлоо.")
            self.empty_count += 1  

        if self.empty_count >= 2:  
            print("Хоосон өрөөнд дарааллан орсон тул амь алдлаа!")
            self.lose_life()

    def reset_position(self):
        self.row = 0
        self.col = 0
        self.hungry = True
        self.   dirty = False
        print("\nНохой амжилттай эхлэлд очлоо!")

    def move(self):
        while self.life > 0 and self.row < self.rows:
            self.dog_state()
            
            if 0 <= self.col + self.direction < self.cols:
                self.col += self.direction
            else:
                self.row += 1
                if self.row < self.rows:
                    self.direction *= -1  

        if self.life > 0:
            print("\nНохой амьд гарлаа!")
            self.reset_position()  
        else:
            print("\nНохой бүх амьдралаа алдсан тул тоглоом дууслаа.")

features = ["food", "bed", "bath", "toy", "park", "empty"]
N = int(input("Мөрийн тоог оруулна уу: "))
M = int(input("Баганын тоог оруулна уу: "))

rooms = [[random.choice(features) for _ in range(M)] for _ in range(N)]

dog = Dog(rooms)
dog.move()

import random

class Environment:
    def __init__(self, rooms):
        self.rooms = rooms
        self.rows = len(rooms)
        self.cols = len(rooms[0])

    def get_room(self, row, col):
        return self.rooms[row][col]

    def is_valid_move(self, row, col):
        return 0 <= row < self.rows and 0 <= col < self.cols

class Dog:
    def __init__(self, environment):
        self.environment = environment
        self.rows = environment.rows
        self.cols = environment.cols
        self.life = 2
        self.row = 0
        self.col = 0
        self.hungry = True
        self.dirty = False
        self.empty_count = 0    
        self.bone_found = False
        self.room_counter = 0  

    def lose_life(self):
        self.life -= 1
        if self.life > 0:
            print(f"Нохой нэг амь алдаж, үлдсэн амь: {self.life}")
        else:
            print("Нохой бүх амьдралаа алдаж, нас барлаа.")

    def dog_state(self):
        room = self.environment.get_room(self.row, self.col)
        print(f"\nНохой [{self.row}][{self.col}] өрөөнд ({room}) байна.")

        if room == "bone":
            print("Нохой яс оллоо! Ялалт!")
            self.bone_found = True
        elif room == "food":
            print("Нохой хоол идэж байна.")
            self.hungry = False
            self.empty_count = 0  
        elif room == "bath":
            print("Нохой усанд орж байна.")
            self.dirty = False  
            self.empty_count = 0  
        elif room == "bed" and not self.hungry:
            print("Нохой хоол идээд унтсан тул үхлээ!")
            self.lose_life()
        elif room == "toy" and self.hungry:
            print("Нохой өлсгөлөн үедээ тоглосон тул амь алдав!")
            self.lose_life()
        elif room == "park" and self.dirty:
            print("Нохой бохир байсан тул гадаа гараад өвчин тусаж үхлээ!")
            self.lose_life()
        elif room == "empty":
            print("Хоосон өрөөнд орлоо.")
            self.empty_count += 1  
        else:
            print("Нохой аюулгүй байна.")
            self.empty_count = 0

        if self.empty_count >= 3:  
            print("Хоосон өрөөнд дарааллан орсон тул амь алдлаа!")
            self.lose_life()

    def move(self):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # baruun, doosoho, zuun, deeshee
        while self.life > 0 and not self.bone_found:
            self.dog_state()
            self.room_counter += 1  

            if self.bone_found:
                break

            best_move = None
            for dr, dc in directions:
                new_row, new_col = self.row + dr, self.col + dc
                if self.environment.is_valid_move(new_row, new_col):
                    next_room = self.environment.get_room(new_row, new_col)
                    if next_room == "bone":
                        best_move = (new_row, new_col)
                        break
                    elif next_room == "food" and self.hungry:
                        best_move = (new_row, new_col)
                    elif next_room == "bath" and self.dirty:
                        best_move = (new_row, new_col)
                    elif next_room == "empty" and best_move is None:
                        best_move = (new_row, new_col)

            if best_move:
                self.row, self.col = best_move
            else:
                self.row, self.col = random.choice([(self.row + dr, self.col + dc) for dr, dc in directions if self.environment.is_valid_move(self.row + dr, self.col + dc)])

        if self.bone_found:
            print(f"\nНохой ялаа! Яс олсон тул тоглоом дууслаа. Нохой {self.room_counter} өрөөний дараа яс оллоо.")
        else:
            print(f"\nНохой бүх амьдралаа алдсан тул тоглоом дууслаа. Нохой {self.room_counter} өрөөний дараа үхлээ.")

features = ["food", "bed", "bath", "toy", "park", "empty"]

N = int(input("Мөрийн тоог оруулна уу: "))
M = int(input("Баганын тоог оруулна уу: "))

rooms = [[random.choice(features) for _ in range(M)] for _ in range(N)]

bone_row = random.randint(0, N - 1)
bone_col = random.randint(0, M - 1)
rooms[bone_row][bone_col] = "bone"

environment = Environment(rooms)
dog = Dog(environment)

dog.move()

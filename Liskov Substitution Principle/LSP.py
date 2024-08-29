class Flyable():
    def __init__(self) -> None:
        pass
    def fly(self):
        return "I'm fliying hight"
    

class Bird():
    def __init__(self) -> None:
        pass
    def makeSound(self):
        return "Pio Pio"
        

class Eagle(Flyable, Bird):
    def __init__(self) -> None:
        super().__init__()
    
    def accion(self) -> str:
        return f'{self.makeSound()} {self.fly()}'

class Penguin(Bird):
    def __init__(self) -> None:
        pass

    def accion(self) -> str:
        return self.makeSound()


class BirdWatcher():
    def __init__(self) -> None:
        pass

    def watchBirdFly(self, bird: Flyable):
        print(bird.fly())

if __name__ == "__main__":
    eagle = Eagle();
    penguin = Penguin()

    watcher = BirdWatcher()

    watcher.watchBirdFly(eagle) 

class Developer():
    def writeCode(self) -> str:
        return "Hello world!!"

class FrontEndDeveloper(Developer):
    def __init__(self) -> None:
        super().__init__()
    
    def writeCode(self) -> str:
        return "<h1> Hello World!! </h1>"
        
class BackEndDeveloper(Developer):
    def __init__(self) -> None:
        super().__init__()
    
    def writeCode(self) -> str:
        return "cout << Hello world!! << endl;"
        

if __name__ == "__main__":
    developers = list()
    
    frontDev  = FrontEndDeveloper();
    backDev = BackEndDeveloper()

    developers.append(frontDev)
    developers.append(backDev)

    for dev in developers:
        print(dev.writeCode());

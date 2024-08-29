class Worker():
    def __init__(self, puesto: str) -> None:
        self.puesto = puesto

    def work(self)-> str:
        return f"Trabajar {self.puesto}"

class Reporter():
    def __init__(self, puesto: str) -> None:
        self.puesto = puesto

    def report(self)-> str:
        return f"Reportar {self.puesto}"

class Administrator():
    def __init__(self, puesto: str) -> None:
        self.puesto = puesto

    def administrate(self) -> str:
        return f"Administrar {self.puesto}"


class Developer(Worker, Reporter):
    def __init__(self) -> None:
        super().__init__("Developer")
    

class Manager(Reporter, Administrator):
    def __init__(self) -> None:
        super().__init__("Manager")



if __name__ == "__main__":
    dev = Developer()
    pm = Manager()

    print(dev.work())
    print(dev.report())

    print(pm.report())
    print(pm.administrate())

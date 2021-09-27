class animal:
    def eat(self):
        print("eat")


class mammal(animal):
    def walk(self):
        print("walk")


class fish(animal):
    def swim(self):
        print("swim")


moka = mammal()
moka.eat()
moka.walk()

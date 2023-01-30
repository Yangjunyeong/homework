class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, breed):
        self.name = name
        print(f'{self.name}이(가) 탄생')
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1
    
    def __del__(self):
        Doggy.num_of_dogs -= 1
        print(f'{self.name}야 죽지마 ㅠㅠㅠㅠㅠ')

    def bark(self):
        print(f'{self.name}의 개짖는 소리~~')
    @classmethod
    def get_status(cls):
        print(f'현재 개의 수는 {cls.num_of_dogs}')
        print(f'태어난 개의 수는 {Doggy.birth_of_dogs}')
    
'''d1 = Doggy('예솜이','푸들')
d2 = Doggy('흰둥이','시고르잡종')
Doggy.get_status()
d1.bark()
del d2
Doggy.get_status()
d3 = Doggy('너구리','진돗개')
Doggy.get_status()
input()'''




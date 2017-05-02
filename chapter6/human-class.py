class HumanName:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name

taro = HumanName()
taro.setName("Taro")
print(taro.getName())

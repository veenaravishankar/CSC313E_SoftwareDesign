class PlayerProfile:
    def __init__(self, player_name, max_health):
        self.player_name = player_name
        self.__health = max_health
        self.max_health = max_health
        self._level = 1

    def __str__(self):
        return (f"------Player:{self.player_name} -----\nLevel:"
                f"{self._level}\nHealth: {self.__health}/{self.max_health}")

    def get_health(self):
        return self.__health

    def set_health(self,new_value):
        if new_value< 0:
            self.__health = 0
        elif new_value > self.max_health:
            self.__health = self.max_health
        else:
            self.__health = new_value


player1 = PlayerProfile('Kratos',150)
print(player1)
#print(player1.__health)
current_health = player1.get_health()
player1.set_health(current_health-30)
print(player1)
#this should not be accessible!
print(player1._level)
player1._level = -10

print(player1)



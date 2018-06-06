

def main():

    class food:

        total_foods = 0

        def __init__(self, name):

            self.name = name

            self.calories = 0

            self.foodgroup = ""

            food.total_foods +=1

        def _del_(self):
            food.total_foods-=1

        def __str__(self):

            return "{}".format(self.name)

        def get_total():

            return food.total_foods
        
        def record(self):

            return "Food {0} is a {2} with {1} calories.".format(self.name, self.calories, self.foodgroup)

    food1 = food("Carrot Stew")
    food1.calories = 210
    food1.foodgroup = "Vegtables"

    food2 = food("Buttered Toast")
    food2.calories = 100
    food2.foodgroup ="Grains"

    print(food.get_total())

    del food2

    print (food.get_total())



main()
            
            

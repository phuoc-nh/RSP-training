import heapq

class Food:
    def __init__(self, food, rating):
        self.food = food
        self.rating = rating

    def __lt__(self, other):
        if self.rating == other.rating:
            return self.food < other.food
        
        return self.rating > other.rating
    
    def __str__(self):
        return '{}, {}'.format(self.food, self.rating)
# Example list of Food objects for testing
# foods = [
#     Food("apple", 5),
#     Food("ax", 5),
#     Food("carrot", 7),
#     Food("date", 7),
#     Food("eggplant", 3),
#     Food("fig", 5),
#     Food("grape", 7)
# ]

# # Sort the foods using your __lt__ function
# heapq.heapify(foods) 
# print('>>',heapq.heappop(foods))
# for f in foods:
#     print(f.food, f.rating)

# store food and rating in a hash map for instant update
# store cuisine -> heap of food to get highest rating
# store food cuisine to update according cuisine when we update food rating

class FoodRatings(object):

    def __init__(self, foods, cuisines, ratings):
        """
        :type foods: List[str]
        :type cuisines: List[str]
        :type ratings: List[int]
        """
        # cuisine: heap [{rating, food}]
        # difficult to update
        self.food_rating = {}
        self.food_cuisine = {}
        self.cuisine_foods = {}
        
        for i in range(len(foods)):
            self.food_rating[foods[i]] = ratings[i]
            self.food_cuisine[foods[i]] = cuisines[i]
            
            if cuisines[i] not in self.cuisine_foods:
                self.cuisine_foods[cuisines[i]] = []
            
            self.cuisine_foods[cuisines[i]].append(Food(foods[i], ratings[i]))
            
        for k in self.cuisine_foods:
            heapq.heapify(self.cuisine_foods[k])
            
        # print(self.food_rating)
        # print(self.food_cuisine)
        # print(self.cuisine_foods)
        

    def changeRating(self, food, newRating):
        """
        :type food: str
        :type newRating: int
        :rtype: None
        """
        self.food_rating[food] = newRating
        # update in cuisine heap as well
        cuisine = self.food_cuisine[food]
        foods = self.cuisine_foods[cuisine]
        
        heapq.heappush(foods, Food(food, newRating))

    def highestRated(self, cuisine):
        """
        :type cuisine: str
        :rtype: str
        """
        
        foods_cuisine = self.cuisine_foods[cuisine]
        
        while True:
            food = foods_cuisine[0]
            if food.rating != self.food_rating[food.food]:
                # stale data in heap
                heapq.heappop(foods_cuisine)
            else:
                return foods_cuisine[0].food
        
        # on top of the heap the rating maybe stale
        # double check it with food rating map
        
foods = ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"]
cuisines = ["korean", "japanese", "japanese", "greek", "japanese", "korean"]
ratings = [9, 12, 8, 15, 14, 7]

# # Your FoodRatings object will be instantiated and called as such:
obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


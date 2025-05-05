import random
kenyan_balanced_diets = [
    ["Ugali", "Sukuma wiki", "Fried eggs", "Banana", "Avocado"],
    ["Githeri (maize & beans)", "Spinach", "Pawpaw slices", "Groundnuts"],
    ["Boiled nduma (arrowroot)", "Scrambled eggs", "Terere (amaranth)", "Orange"],
    ["Chapati", "Ndengu (green grams)", "Cabbage stew", "Banana", "Avocado"],
    ["Rice", "Lentil curry", "Steamed sukuma wiki", "Mango"],
    ["Sweet potatoes", "Boiled eggs", "Mrenda", "Watermelon", "Groundnuts"],
    ["Matoke (green banana stew)", "Beef stew (small portion)", "Spinach", "Pineapple"],
    ["Ugali", "Fried omena (silver fish)", "Kale", "Avocado", "Passion fruit"],
    ["Rice", "Fried peas", "Cabbage", "Papaya", "Sunflower oil (used lightly)"],
    ["Boiled maize"," njahi (black beans)", "Terere", "Mango", "Roasted groundnuts"]
]
what_to_eat = random.choice(kenyan_balanced_diets)
kenyan_diets = [
    {
        "name": "Ugali",
        "ingredients": ["4 cups water", "2.5 cups maize flour", "Salt (optional)"],
        "recipe": "Boil water, add maize flour gradually while stirring, cook until firm, simmer for 5 minutes."
    },
    {
        "name": "Sukuma Wiki",
        "ingredients": ["1 bunch sukuma wiki", "1 onion", "2 tomatoes", "2 tbsp oil", "Salt"],
        "recipe": "Fry onions, add tomatoes, add sukuma and salt, cook for 5–7 minutes."
    },
    {
        "name": "Fried Eggs",
        "ingredients": ["5 eggs", "1 onion (optional)", "Salt", "Black pepper", "2 tbsp oil"],
        "recipe": "Beat eggs with salt and pepper, fry in oil with onions (optional) until firm."
    },
    {
        "name": "Githeri",
        "ingredients": ["2 cups boiled maize", "2 cups boiled beans", "1 onion", "2 tomatoes", "Salt", "Oil"],
        "recipe": "Fry onions and tomatoes, add maize and beans, season and simmer for 10 minutes."
    },
    {
        "name": "Spinach",
        "ingredients": ["1 bunch spinach", "1 onion", "Salt", "Oil"],
        "recipe": "Fry onion in oil, add spinach and salt, cook for 5–7 minutes."
    },
    {
        "name": "Arrowroot (Nduma)",
        "ingredients": ["5–6 arrowroots", "Water", "Salt"],
        "recipe": "Wash, peel and boil for 25–30 minutes with salt until soft."
    },
    {
        "name": "Scrambled Eggs",
        "ingredients": ["5 eggs", "Salt", "Oil"],
        "recipe": "Beat eggs, cook while stirring constantly until curds form."
    },
    {
        "name": "Terere (Amaranth)",
        "ingredients": ["1 bunch terere", "1 onion", "1 tomato", "Salt", "Oil"],
        "recipe": "Fry onion and tomato, add terere and salt, cook for 5–7 minutes."
    },
    {
        "name": "Chapati",
        "ingredients": ["3 cups flour", "1 cup warm water", "1 tsp salt", "1 tbsp oil", "Oil for frying"],
        "recipe": "Mix ingredients, knead dough, roll into circles, fry until golden."
    },
    {
        "name": "Ndengu (Green Grams)",
        "ingredients": ["2 cups boiled ndengu", "1 onion", "2 tomatoes", "Garlic", "Salt", "Oil"],
        "recipe": "Fry onion, garlic, tomato; add ndengu and simmer for 10 minutes."
    },
    {
        "name": "Cabbage Stew",
        "ingredients": ["1 medium cabbage", "1 onion", "2 tomatoes", "Salt", "Oil"],
        "recipe": "Fry onion and tomato, add cabbage and salt, cook for 10 minutes."
    },
    {
        "name": "Lentil Curry",
        "ingredients": ["2 cups lentils", "1 onion", "2 tomatoes", "Garlic", "Ginger", "Spices", "Salt", "Oil"],
        "recipe": "Boil lentils, fry onion, garlic, ginger, spices and tomatoes, add lentils and simmer."
    },
    {
        "name": "Sweet Potatoes",
        "ingredients": ["5–6 sweet potatoes", "Water", "Salt"],
        "recipe": "Wash, peel and boil for 20–30 minutes until soft."
    },
    {
        "name": "Boiled Eggs",
        "ingredients": ["5 eggs", "Water"],
        "recipe": "Boil eggs in water for 8–10 minutes, cool and peel."
    },
    {
        "name": "Mrenda (Jute Mallow)",
        "ingredients": ["1 bunch mrenda", "1 tsp baking soda (optional)", "1 onion", "Salt", "Oil"],
        "recipe": "Boil mrenda, add baking soda (optional), fry with onion and salt."
    },
    {
        "name": "Matoke",
        "ingredients": ["10 green bananas", "1 onion", "2 tomatoes", "Salt", "Oil"],
        "recipe": "Fry onions and tomatoes, add bananas and water, simmer until soft."
    },
    {
        "name": "Beef Stew",
        "ingredients": ["½ kg beef", "1 onion", "2 tomatoes", "Garlic", "Salt", "Oil"],
        "recipe": "Boil beef until soft, fry onion and tomato, add beef, simmer with broth."
    },
    {
        "name": "Fried Omena",
        "ingredients": ["2 cups omena", "Warm water", "1 onion", "1 tomato", "Oil"],
        "recipe": "Soak and rinse omena, fry with onion and tomato until crispy."
    },
    {
        "name": "Fried Peas",
        "ingredients": ["2 cups green peas", "1 onion", "1 tomato", "Salt", "Oil"],
        "recipe": "Boil peas, fry with onion and tomato, stir and season."
    },
    {
        "name": "Njahi (Black Beans)",
        "ingredients": ["2 cups boiled njahi", "1 onion", "2 tomatoes", "Garlic", "Salt", "Oil"],
        "recipe": "Fry onion, tomato and garlic, add njahi, simmer for 10 minutes."
    }
]
def recipeis():
    for i in what_to_eat:
        found = False
        for k in kenyan_diets:
            if k["name"].strip().lower() == i.strip().lower():
                print(k["name"])
                arrg= " ".join(k["ingredients"])
                print("ingredients:",arrg)
                rec = "".join(k["recipe"])
                print("recipe",rec)
                found = True
        if k["name"].strip().lower() not in  i.strip().lower():
                print("recipeis for {} not found".format(i))


def main():
    while True:
        print("print exit to exit")
        user_input=input("yes/no would you like me to surgest what to eat: ").lower()
        if not isinstance(user_input,str):
            raise TypeError("please enter yes or no")
        if user_input == "yes":
            food = "".join(what_to_eat)
            print(food)
            recipeis_input = input("yes/no would you llike thier recipies").lower()
            if not isinstance(recipeis_input,str):
                raise TypeError("please enter yes or no")
            if recipeis_input == "yes":
                recipeis()
            if recipeis_input == "no":
                break
        if user_input == "no":
            break
        if user_input == "exit":
            break
        
main()


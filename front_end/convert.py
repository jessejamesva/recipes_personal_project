import json

f = open('tasty-test-sm.json',)

recipes = json.load(f)

results = []

for recipe in recipes['results']:
    ingredients = []
    for i in recipe['sections'][0]['components']:
        item =  i['raw_text']
        item = item.replace('(see recipe above)', '')
        if item != 'n/a':
            ingredients.append(item)

    instructions = []
    for j in recipe['instructions']:
        instructions.append(j['display_text'])


    dict = {
        'name' : recipe['name'],
        'img_url': recipe['thumbnail_url'],
        'rating': recipe['user_ratings']['score'],
        'servings': recipe['num_servings'],
        'description': recipe['description'],
        'video_url': recipe['original_video_url'],
        'ingredients': ingredients,
        'instructions': instructions,
        'slug': recipe['slug']
    }
    results.append(dict)

f.close()

dict = {
    'results' : results
}
# json_object = json.dumps(dict, indent = 4)
# print(json_object)

with open('cleaned_recipes.json', 'w') as outfile:
    json.dump(dict, outfile)
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        ingredient_to_recipe, in_degree = defaultdict(set), Counter()
        for rcp, ingredient in zip(recipes, ingredients):
            for ing in ingredient:
                ingredient_to_recipe[ing].add(rcp)
            in_degree[rcp] = len(ingredient)
            
        ans = []
        for ing in supplies:
            for rcp in ingredient_to_recipe.pop(ing, set()):
                in_degree[rcp] -= 1
                if in_degree[rcp] == 0:
                    supplies.append(rcp)
                    ans.append(rcp)
        return ans


# Restaurant API for Mobile App
## User Guide
User login feature provided by "api-auth" Rest-Framework feature and User credentials provided at the end of ReadMe or create your own user through DefaultRouter provided index (Users endpoint)

This API has been developed according to instructions made, it includes all features stated even more
1. Way to list owner's restaurants... owners/{pk}/restaurants
2. List of restaurants by districts ... districts/{pk}/restaurants
3. list of restaurants by sectors ... sectors/{pk}/restaurants
4. list of restaurants by rating ... restaurants/?rating={:int} (any integer value)
5. list of dishes by restaurants ... restaurants/{pk}/dishes
6. And other endpoints for every model; Users, Districts, Sectors, Owners, Restaurants, Dishes, Ingredients, and Pictures

#### NOTE: Ingredients are recorded separately and linked to Dish using ManyToManyField, Dish Pictures are added  to the Dish after (Picture store dish as ForeignKey field), and one dish can have as many pictures as you want, you can explore more as you use API.

1. Link to Postman Collection : (JSON Link) https://www.getpostman.com/collections/816cab3bf50c65b17bf1
2. Link to the Hosted Web API : http://ndizihiwe.azurewebsites.net/
### Testing Credentials

1. Username : "Nomiso"
2. Password : "123"

## Thank you

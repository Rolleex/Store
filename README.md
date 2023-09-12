# Store
 Hello! This repository contains the code for a store project for portfolio. Here, I will describe the main parts of the code and its functionality.

 ## How to Use

1. Clone the repository to your local computer.
2. Install the necessary dependencies.
3. Create and configure a virtual environment.
4. Launch the application and enjoy its functionality.


# Install 
```
pip install -r requirements.txt
```
Dont forget about 
```
python manage.py makemigrations
python manage.py migrate
```
## Dependencies

The list of dependencies can be found in the requirements.txt file.
____
![image](https://github.com/Rolleex/Store/assets/26228130/5c65af07-3e13-427a-87e4-da21b8ba736e)
____
## Settings
Edit the settings.py file to set up your database and other settings.

# How the Application Works
The application consists of several main components:

### Item Shop View
File: shop/views.py
Simple index func. Display of items and the form of adding to the cart

```
http://127.0.0.1:8000/
```
### Navbar
File: templates/inc/nav.html
____
![image](https://github.com/Rolleex/Store/assets/26228130/26594530-ea7f-4566-a2ec-001f0dc4d811)
____
Based on Bootsrap. Home button, list of categoryes, seach form and user with cart detail

### Sidebar

File: templates/inc/sidebaer.html
File: shop/views.py

We have sidebar for categoryes view. All categoryes we take from context_processors.py
Class CategoryView(View) have a get request for filter items and render on index page.
```
http://127.0.0.1:8000/category/<int:pk>
```
____
![image](https://github.com/Rolleex/Store/assets/26228130/e1cbd60a-f82c-4f8a-80ea-839da3e7c58b)
____
### Search 
File: shop.view.py 

The search is based on the ORM. We pass in the context with filter(title__icontains=q) where q its a request form

## User Registration
File: user_profile/views.py

Here, the user registration process is described. In the register method, POST requests are processed to create a new user and an associated profile. Get methood render register page with RegisterForm. After registration, we are redirected to the profile edit page
```
http://127.0.0.1:8000/register/
```
### Edit 
File: user_profile/views.py
On func register we create User and Profile for our users. Now with methood POST we add Profile info like a name, address and photo. 
```
http://127.0.0.1:8000/edit/
```
### Login and Logout
File: user_profile/views.py

Just login_user func with Post methood and check for validation. 
Default func logout, with redirect on login page
```
http://127.0.0.1:8000/login/
```
## Cart
File: cart/cart.py 

- Initialization: Initialize the cart instance with a user session to store cart data.

- Iterate Through Items: The iter method allows you to iterate through items in the cart, fetching relevant product information.

- Add Items: Easily add items to the cart, specifying the product and desired quantity. You can also choose to update the quantity of an existing item.

- Calculate Total Price: The get_total_price method computes the total price of all items in the cart.

- Remove Items: Remove items from the cart using the remove method.

- Clear Cart: Clear the entire cart with the clear method.

### Add Item to cart

File: cart/views.py
On Index page we have CartAddForm. Func cart_add take pk of product and quantity. Next we check for valid and add to request session cart this product. For add we use add on Cart class(cart/cart.py)

### Cart Item remove
File: cart/views.py 

On cart detail page we can remove some items from the cart list. We have remove func on Cart class(cart/cart.py) 

### Cart detail list
Just render our cart list, bassed on the session.

## Make Order
File: orders/views.py

For now we need input some data to create our order. methood Post take request.POST and create our order with ORM. and we clear cart







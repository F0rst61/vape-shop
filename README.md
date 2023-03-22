# [Vape Attitude](https://easyvape.herokuapp.com/)

EasyVape is a E-Commerce webpage, produced as my final project in [CodeInstitute](https://codeinstitute.net/global/). This is a fullstack website, which "sells" Vapes and E-Juices DHe by EasyVape, which is a fictional company.

The main technologies used were HTML, CSS, JS, Jquery, Python and Django. All images were created using [Dall-E-2](https://openai.com/dall-e-2/)

<img src="https://github.com/gioZAK/easy_vape/blob/1a012a31e3a82345e0cf7346b98fc98ff0967919/docs/ss/responsive-img-easy-vape.png">
 
[Click here](https://easyvape.herokuapp.com/) to visit the deployed website.


---

# Table of contents

1. [Website presentation](#website-presentation)
2. [Structure](#structure)
3. [UX](#ux)
4. [User Stories](#user-stories)
5. [Agile Workflow](#agile-workflow)
6. [Business Plan](#business-plan)
7. [Technologies Used](#technologies-used)    
8. [Testing](#testing)
9. [Deployment](#deployment)
10. [Credits](#credits)

## Website presentation

In this section, I want to show you how to navigate this website, how to check for products, add products, check out, how to add a review, add to products to the wishlist and fill the contact form.

### Home

This is the Home Page, it includes the navigation bar, a jumbotron image with an invitation to shop and the footer.

<details>
<summary>
Home Page Image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/991f111d0027fc5f231878ee8414ec5b9dce2c03/docs/ss/home-page.png">
</details>

### Navigation Bar

In the Navigation Bar the user is able to user the search bar, check for products, access the contact form, check his bag and by clicking on the account, he can access his profile and wishlist.

<details>
<summary>
Nav-Bar Image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/991f111d0027fc5f231878ee8414ec5b9dce2c03/docs/ss/nav-bar-search.png">
</details>

<details>
<summary>
Search-Bar Results Image
</summary>
This is the result if the user searchs for "mint" in the search bar.
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/search-bar-result.png">
</details>

<details>
<summary>
Account Image
</summary>
Here you can access your Profile, Wishlist. Register, Login or Logout.
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-access.png">
</details>

### Products

Here is the product list page, the user is able to see a list of products and choose which one he is interested.

<details>
<summary>
Products List image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/all_products.png">
</details>

### Products Detail

Here in the Product Detail page, the user is able to select the product quantity, add it to the bag, add to the wishlist and write a review.

<details>
<summary>
Product Image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/991f111d0027fc5f231878ee8414ec5b9dce2c03/docs/ss/product-detail.png">
</details>

### Adding Products to the Bag

Inside the Product Detail page, the user can add products to the bag, by clicking on the add to the bag

<details>
<summary>
Product Image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/991f111d0027fc5f231878ee8414ec5b9dce2c03/docs/ss/product-detail.png">
</details>

After this, go to the bag icon on the top left, here in the bag page, you can increase the quantity or remove the products.
If the user is satisfied he can click on Secure Checkout to be redirected to the checkout page.

<details>
<summary>
Bag Page Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/bag-1.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/bag-2.png">
</details>

### Checkout

Here in the Checkout Page, the user is able to see his order items and total.
To complete the checkout you need to fill in the necessary forms.
If you want to test your purchase you can type "4242 4242 4242 4242" in the card field, Stripe will know this is a test

<details>
<summary>
Checkout Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/checkout.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/checkout-success.png">
</details>

Also, the user will receive an email with the purchase information.

<details>
<summary>
Checkout Email Image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/order-confirmation-email.png">
</details>

### Contact Form

If needed, the user can also write a Contact form. 
The site owner will be able to read in the admin page and he will also receive a email with your name and subject.

<details>
<summary>
Contact Form Image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/contact-form.png">
</details>

### Wishlist

In the product detail page the user can add a product to the wishlist. In order to access the wishlist, you can click on manage wishlist or in the account menu in the top left of the nav bar.
Inside the Wishlist page you can see your favorite products there and remove them if necessary. 

<details>
<summary>
Wishlist Images
</summary>
Click on "Add to Wishlist" button <br />
<img src="https://github.com/gioZAK/easy_vape/blob/991f111d0027fc5f231878ee8414ec5b9dce2c03/docs/ss/product-detail.png">
In order to access your wishlist click on the "Manage Wishlist" <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-access-product-detail.png">
Or you can click here. <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-access.png">
This is your wishlist page <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist.png">
In order to remove click on the "Remove from Wishlist" Button. <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-remove-item-1.png">
<br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-remove-item-2.png">
</details>

### Reviews

Inside the product detail page, the user can also add a review, which will be posted after the admin analyzes the review.

<details>
<summary>
Review Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/add-review.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/review-submited.png">
</details>

### Footer

The footer can be found on the bottom of every page. Here the user can access our [facebook](https://www.facebook.com/profile.php?id=100089498293818) and instagram or twitter, which were not created. The user can also see how to reach us and where to find, which are "fake" locations. And also, the user can subscribe to our Newsletter by adding his email and clicking on the subscribe button.

<details>
<summary>
Footer Image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/footer.png">
</details>

## Structure

### Wireframe

Wireframe created using [Balsamiq](https://balsamiq.com/)


<details>
<summary>
Wireframe Home
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/wireframe/home-wireframe.png">
</details>

<details>
<summary>
Wireframe Products List
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/wireframe/product-list-wireframe.png">
</details>

<details>
<summary>
Wireframe Product Detail
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/wireframe/product-detail-wireframe.png">
</details>

<details>
<summary>
Wireframe Bag
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/wireframe/bag-wireframe.png">
</details>
</details>

<details>
<summary>
Wireframe Checkout
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/wireframe/checkout-wireframe.png">
</details>
</details>

<details>
<summary>
Wireframe Profile
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/wireframe/profile-wireframe.png">
</details>
</details>


### Data Scheme

#### ERD

Here is the entity relationship diagram (ERD), showing the relationships between the various models used int his project.

<details>
<summary>
ERD image
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ERD/models.png">
</details>
</details>


## UX

### Site User Goal

- Quickly identify what the website is about
- Search for Products
- Add Products and Manage products in the bag
- Secure Checkout, provided by Stripe
- Register for an account
- Subscribe to a newsletter
- Add a review
- Add products to a wishlist
- Contact the site owner via the contact form.
- Receive confirmation of the purchase

### Site Owner Goal

- Sell items online
- Add new products and categories easily.
- Manage user reviews to avoid malicious comments.
- Read user contact form in the admin panel.
- Receive payment securely via Stripe.

## Agile Workflow

This project was created using Agile techniques during development, such as:

- User stories: displayed using GitHub Issues.
- MoSCoW method: by adding a priority to each issue and display it using tags.
- ToDo, In Progress and Done: using the GitHub Kanban board.

You can access the Kanban board that was used during the project development [here](https://github.com/users/gioZAK/projects/11).
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/kanban-ss.png">

You can access the list of issues/user stories used during the development of this project [here](https://github.com/gioZAK/easy_vape/issues?q=is%3Aissue+is%3Aclosed)
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/userstr-ss.png">


[Back to Table of contents](#table-of-contents)

## User Stories

### View a list of Products

- As a user I can View a list of products so that I can select some to purchase.

### View product detail

- As a user I can view selected product detail so that I can get more information about the product.

### View the purchase total

- As a User I can view the purchase total so that keep control of how much I am about to spend.

### Account Register

- As a user I can register for an account so that have a personal account and view my profile.

### Login/Logout

- As a user I can easily login or logout so that Access my profile or logout my account.

### Email Confirmation

- As a user I can receive an email confirmation so that verify that my account registration was successful.

### Personalized user profile

- As a user I can have a personalized profile so that view order history, confirmation and save payment information.

### Sort the list of products

- As a user I can sort the list of products so that easily identify the best rated, best priced and categorically sorted products.

### Sort a specific category of product

- As a user I can sort a specific category of product so that find the best priced or best-rated product in a specific category, or sort the product by category name.

### Sort multiple categories of products simultaneously

- As a user I can sort multiple categories of products simultaneously so that find the best-priced or best-rated products across broad categories, such as vapes or e-liquid.

### Search Products

- As a user I can search products so that find a specific product.

### Select quantity of product

- As a user I can select quantity of product so that decide how many I want to purchase.

### View items in my bag

- As a user I can view items in my bag so that identify the total cost of my purchase and all items I will receive.

### Adjust items in the bag

- As a user I can adjust items in the bag so that easily make changes to my purchase.

### Order Confirmation

- As a user I can view the order confirmation so that certify that my order was successful.

### Checkout Email Confirmation

- As a user I can receive a email confirmation after checkout so that keep a record of my purchase.

### Payment Information

- As a user I can easily enter my payment information so that checkout quickly.

### Add products

- As a store owner I can add a product so that display items in my website.

### Edit/Update Product

- As a Store Owner I can Edit/Update Product so that change products price, description, image and other criteria.

### Delete a Product

- As a Store Owner I can Delete a Product so that remove items that are no longer for sale.

### Add Products to a Wishlist

- As a user I can add products to a Wishlist so that I can save my favorite products.

### Remove Products from Wishlist

- As a user I can Remove Products from Wishlist so that delete unwanted items from there.

### Write a Review

- As a user I can write a review so that I can tell others user about my experience with the purchased item.

### Read Reviews

- As a user I can read reviews so that I can have more information about the item I am about to purchase.

### Delete Review

- As a user I can Delete a review so that change my review if needed.

### Contact Form

- As a user I can write a form so that I can contact the owner.

## Business Plan

### Business Model

Vape Attitude uses Business-to-Consumer(B2C) retail model. This website is the online platform where the company connects it's products with the costumers. All Vapes and E-Liquids are produced by Vape Attitude and sold on the webpage.

The Customer Orders from the Website, the Website sends the Order Request to the Warehouse and from the Warehouse the Order is sent to the Customer.

#### Products

We currently offer 21 Products, which are divided into these Categories; MODS, PODS, E-Juices with Nicotine and Without Nicotine.

 - 7 Vapes
    - Which 4 are MODS, with price ranging from 90 Euros to 120 Euros.
    - Which 2 are PODS, with price ranging from 45 Euros to 66 Euros.

- 14 E-Juices
    - Which 7 contain Nicotine, with price ranging from 5 Euros to 6.50 Euros.
    - Which 7 do not cotain Nicotine, with price ranging from 3.50 euros to 4 Euros.

#### Delivery

Our products are sent directly to the user location, the delivery fee is 10% percent of the Product Total Price. But, if the user spends more than 80 Euros we offer Free Delivery.

#### Marketing

Since Facebook has one of the highest numbers of users worldwide, we opted to create a Facebook page to connect with our users.

<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/FB/EV-FB.png">

Also, users can subscribe to our Newsletter by filling out the form found on the bottom of the page, provided by MailChimp.

#### Search Engine Optimisation

In order to improve the SEO, I have added a sitemap.xml and robots.txt to the website.

## Technologies Used

### Main Tech

 - HTML5
 - CSS
 - [JavaScript](https://www.javascript.com/)
 - [Django](https://www.djangoproject.com/) 
 - [Bootstrap](https://getbootstrap.com/)

[Back to Table of contents](#table-of-contents)

### Applications, Libraries and Platforms

- Git
    - Used for version control to commit to Git and Push to GitHub.
- Gitpod
    - Used as the IDE to write all the code used in this project.
- Github
    - GitHub is used to store the projects code after being pushed from Git.
- Heroku
    - Used to deploy the application.
- Google Fonts
    - Used to import the fonts.
- FontAwesome
    - Used to import icons.
- Balsamiq Wireframes
    - Used to create the project's wireframe.
- Amazon Web Services
    - Used to host all images and static files.
- Django AllAuth
    - Used to deal with user account registration.
- Chrome DevTool
    - Used to debug and test new styles.
- ChatGTP
    - Used to debug.
- Dall-E-2
    - Used to create all Images.


## Testing
- I have used a combination of automated test and manual testing.

### CSS Testing
- Tested with [Jigsaw](https://jigsaw.w3.org/css-validator/)
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/css-w3-valid.png">

### HTML Testing
- Tested with [Validator.w3](https://validator.w3.org/nu/#textarea)
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/w3-html-valid.png">


[Back to Table of contents](#table-of-contents)

### Manual Testing
 - Here is the sequence of manual test I have applied to check if all applications work.

#### As a user I want to register.

- Steps: 
    1. Click on the Account Menu, on the top left.
    2. Select Register.
    3. Fill up the form.
    4. Check your e-mail.
    5. Click on the link and confirm.

- Outcome:
    - Pass. User is now registered and able to login.

Graphic Example Below.

<details>
<summary>
User Register Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/register-testing-sign-up.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/register-testing-sign-up-submitted.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/register-testing-email.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/register-testing-email-confirm.png">
</details>

#### As a user I want to recover my password.

- Steps: 
    1. Click on the Account Menu, on the top left.
    2. Select Login.
    3. Click on "Forgot Password"
    4. Check your e-mail.
    5. Click on the link.
    6. Add new Password.

- Outcome:
    - Pass. User has a new password and able to log in.

Graphic Example Below.

<details>
<summary>
User Password Recovery Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-sign-in-page.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/password-reset-page.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/password-reset-email.png">
</details>

#### As a user I want to Login.

- Steps: 
    1. Click on the Account Menu, on the top left.
    2. Select Login.
    3. Fill up the Sign In Form.
    4. Click on the Sign in Button.

- Outcome:
    - Pass. User is now logged in.

Graphic Example Below.

<details>
<summary>
User Sign In Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-sign-in-page.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-sign-in-success.png">
</details>

#### As a user I want to Logout.

- Steps: 
    1. Click on the Account Menu, on the top left.
    2. Select Logout.
    3. Click on Sign Out

- Outcome:
    - Pass. User is now logged out.

Graphic Example Below.

<details>
<summary>
User Logout Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-sign-out.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-sign-out-success.png">
</details>

#### As a user I want to view a list of products and sort by Price (Low to High).

- Steps: 
    1. In the Nav Bar, select the Category wanted.
    2. Inside the Product Detail page, on the top left Click on Sort By.
    3. Select Price (low to high)

- Outcome:
    - Pass. User can see the product list and sort it by price.

Graphic Example Below.

<details>
<summary>
Product List and Sorting Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/nav-bar-search.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/all_products.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-product-sorting.png">
</details>

#### As a user I want to view the product detail.

- Steps: 
    1. In the Product List Page.
    2. Click on the wanted Product.

- Outcome:
    - Pass. User can see the product detail page.

Graphic Example Below.

<details>
<summary>
Product Detail Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/all_products.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/product-detail.png">
</details>

#### As a user I want to add product to the bag.

- Steps: 
    1. In the Product Detail Page.
    2. Select the amount needed.
    3. Click on Add to Bag.

- Outcome:
    - Pass. User is able to Add the Product to the Bag.

Graphic Example Below.

<details>
<summary>
Add to Bag Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/product-detail.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-add-to-bag.png">
</details>

#### As a user I want to view my bag and increase the quantity of the product.

- Steps: 
    1. On the top left of the page, click on the bag icon.
    2. Select the quantity needed.
    3. Click on Update.

- Outcome:
    - Pass. User is able to view his bag and increase the item amount.

Graphic Example Below.

<details>
<summary>
Add to Bag Testing Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-bag.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-bag-updated.png">
</details>

#### As a user I want to Checkout and Receive a Confirmation.

- Steps: 
    1. In the bag page, click Secure Checkout.
    2. Fill up the form.
    3. Click on Confirm Order.
    4. Check Email.

- Outcome:
    - Pass. User is able to Checkout and receives a Confirmation E-mail.

Graphic Example Below.

<details>
<summary>
Checkout Success Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-checkout.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-checkout-success.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-checkout-email.png">
</details>

#### As a user I want to add products to my Wishlist.

- Steps: 
    1. In the Product Detail Page.
    2. Click on Add to Wishlist.

- Outcome:
    - Pass. User is able to add product to the Wishlist.

Graphic Example Below.

<details>
<summary>
Add to Wishlist Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/991f111d0027fc5f231878ee8414ec5b9dce2c03/docs/ss/product-detail.png">
</details>


#### As a user I want to view my Wishlist and Remove items from there.

- Steps: 
    1. Either:
        - Click on Manage Wishlist on the Product Detail
        - Or on the top left in the account icons click on Wishlist.
    2. Click on Remove from the Wishlist.

- Outcome:
    - Pass. User is able to view the Wishlist and delete products from there.

Graphic Example Below.

<details>
<summary>
Views and Remove items from Wishlist Images
</summary>
In order to access your wishlist click on the "Manage Wishlist" <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-access-product-detail.png">
Or you can click here. <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-access.png">
This is your wishlist page <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist.png">
In order to remove click on the "Remove from Wishlist" Button. <br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-remove-item-1.png">
<br />
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/wishlist-remove-item-2.png">
</details>

#### As a user I want to add a Product Review.

- Steps: 
    1. In the Product Detail Page.
    2. On the bottom there is a Review Form, write your review there.
    3. Click Submit review

- Outcome:
    - Pass. User is able to add a review.

Graphic Example Below.

<details>
<summary>
Add Product Review Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/add-review.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/review-submited.png">
</details>

#### As a Admin I want to moderate the reviews and see the review posted.

- Steps: 
    1. Go to the Admin Dashboard.
    2. Click on Reviews.
    3. Check the Is Approved Box.
    4. Review is now posted.

- Outcome:
    - Pass. Admin is able to moderate reviews and see the review posted.
    - All users can see the review now.

Graphic Example Below.

<details>
<summary>
Moderate Review Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-admin-reviews.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-admin-reviews-success.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-review-display.png">
</details>

#### As a user I want to delete my own Product Review.

- Steps: 
    1. In the Product Detail Page.
    2. Click on the Delete Button.
        - Only the owner of the review is able to see this button.

- Outcome:
    - Pass. User is able to delete his own review.

Graphic Example Below.

<details>
<summary>
Delete Review Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-review-display.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-review-delete.png">
</details>

#### As a user I want to send a Contact Form.

- Steps: 
    1. On the middle of the Nav Bar, click on Contact Us.
    2. Fill up the Contact Form.
        - If the user logged in his email will be displayed there already.

- Outcome:
    - Pass. User is able to send a form.

Graphic Example Below.

<details>
<summary>
Contact Form Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/ss/contact-form.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-contact-success.png">
</details>

#### As a Admin I want to read the Contact Form send by the users.

- Steps: 
    1. Site Owner has received a Email after form submission.
    2. Go to the Admin dashboard.
    3. Click on Contacts
    4. Click on the Name of the contact form you want to read.

- Outcome:
    - Pass. Admin is able to read the Contact Form.

Graphic Example Below.

<details>
<summary>
Admin Contact Form Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-contact-form-admin.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-contact-form-admin-full.png">
</details>

#### As a Site Owner I want to Add new Product.

- Steps: 
    1. Either:
        - Go to the Admin Dashboard.
        - Access Product Management in the Accounts Icon.
    2. In the Product Management.
    3. Fill up the form.

- Outcome:
    - Pass. Site Owner is able to Add a new product.

Graphic Example Below.

<details>
<summary>
Site Owner Add Product - Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-add-product.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-add-product-success.png">
</details>

#### As a Site Owner I want to Edit a Product.

- Steps: 
    1. Go to the Product Detail Page or the Product List.
    2. Click on Edit.
        - Only SuperUsers can see this option
    3. Fill up the form with the necessary changes


- Outcome:
    - Pass. Site Owner is able to Edit a Product.

Graphic Example Below.

<details>
<summary>
Site Owner Edit Product - Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-add-product-success.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-edit-product.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-edit-product-success.png">
</details>

#### As a Site Owner I want to Delete a Product.

- Steps: 
    1. Go to the Product Detail Page or the Product List.
    2. Click on Delete.
        - Only SuperUsers can see this option

- Outcome:
    - Pass. Site Owner is able to Delete the product.

Graphic Example Below.

<details>
<summary>
Site Owner Delete Product - Images
</summary>
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/testing-edit-product-success.png">
<img src="https://github.com/gioZAK/easy_vape/blob/main/docs/testing/product-deleted-success.png">
</details>

[Back to Table of contents](#table-of-contents)

## Deployment
- In order to Deploy this project:
    1. Either fork or clone this project.
    2. Heroku Setup.
    3. AWS Setup.

### Forking

- In order to Fork this repository:

    1. Access your GitHub account and find the relevant repository.
    2. Click on 'Fork' on the top right of the page.
    3. You will find a copy of the repository in your own Github account.

### Clone

- In order to Clone this repository:

    1. Create repository where you will work with this clone.
    2. Copy "https://github.com/gioZAK/easy_vape.git".
    3. Run the directory you want the clone to be.
    6. In your IDE's terminal type 'git clone' and the paste the URL you just copied.
    7. Press Enter.
    8. You now have a local clone.

### Heroku.

- To setup with Heroku:

   1. Create an account at heroku.com.
   2. Create a new app, add app name and your region.
   3. Click on create app.
   4. Go to "Settings".
   5. Under Config Vars, add your sensitive data.
   6. Now go to your IDE and connect your enviroment with heroku.
   7. heroku login -i.
   8. Then run the following command: heroku git:remote -a your_app_name_here.
   9. Finally: git push heroku main.

### Amazon Web Services.

- To setup with AWS:

    1. Create an account at [AWS](https://aws.amazon.com/).
    2. Navigate to the IAM application and create a user and group.
    3. Set the AmazonS3FullAccess for the user and copy the AWS ACCESS and SECRET keys as config vars to your workspace and Heroku.
    4. Create a new Bucket within the S3 application with an appropriate name.
    5. Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc). 
    6. If Needed Documentation at https://aws.amazon.com/s3/.

## Credits

### Code Institute
- I have relied on the Code Institute Boutique Ado Walktrough Project in order to make my own.
- Special Thanks to the Code Institute staff for the support throughout the course.

### ChatGPT
- I have used [ChatGPT](https://chat.openai.com/chat) as a tool to debug and to guide me on how to apply new functionalities.

### Dall-E-2
- I have created all images using [Dall-E-2](https://openai.com/dall-e-2/)

[Back to Table of contents](#table-of-contents)
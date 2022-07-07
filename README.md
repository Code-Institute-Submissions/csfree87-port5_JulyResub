# La Terre

![home page all screen sizes](/media/mockup.png)

[Link to deployed website](https://laterre.herokuapp.com/)

LaTerre is an e-commerce store located online but based out of Stockholm, Sweden. We sell candles, soaps, lotions and fragrences based on scents of the earth. 
On the website registered users can make make purchases, view shopping bags, view orders, manage profiles, contact us, and register for a newsletter.


# Table Of Contents

-   [User Experience](#user-experience)
-   [Features](#features)
-   [Technologies Used](#technologies-used)
-   [Testing](#testing)
-   [Deployment](#deployment)
-   [Credits](#credits)

## User Experience

-   [User Stories](#user-stories)
-   [The Scope Plane](#the-Scope-plane)
-   [The Structure Plane](#the-structure-plane)
-   [The Surface Plane](#the-surface-plane)


### User Stories

The purpose of the website is for users to make view and purchase scented products online such as those mentioned above.
Each product will come with a specialized look, price, and description.

User stories managed via Issues/(projects) via github.
![User stories](/media/userstory1.png)
![User stories](/media/userstory2.png)


### The Scope Plane

Users want to be able to easily make an account, view/edit profile information, easily search and view product and product details and make purchases. Finally they want to be able to review orders, receive emails, subscribe to newsletters or contact us.
The shop owner wants to be able to manage (add/edit/delete) products and users from the admin system/or product management page..

### The Structure Plane

The website will have the following structure for visitors (not users):
- Log-in/Register: allows the visitor to either log-in or register as a new user
- Contact us
- Shop Now (view products)

On top of these pages, a user will have access to:
- My Profile: from this page, a user can manage their profile information (ph. number, first and last name) and see previous orders
- Log-out: used to simply log-out of the current session

An admin user will also have access to:
- Product Management: this section will allow them to create, update or delete products
- User Management: this section will allow them to create, update or delete users
- Order management: this section allows the admin to see orders and fullfil

The Database structure is as follows:
![DB Schema](/media/dbschema.png)
- For each User, the system creates a new UserProfile (1-1 relationship) to store additional information
- Each Product is connected to a Category (many-1), 
- Each order will create an orderline and order status


### The Surface Plane

The color palette of the website will be:
rgb(213, 195, 173), black: #000; rgb(174, 96, 47); beige;

The general structure and features are inspired by Boutique Ado, but customized to suit a more earthy tone

## Features

-   [Existing Features](#existing-features)
-   [Features Left to Implement](#features-left-to-implement)
 
### Existing Features

![features](/media/userstory1.png)
![features](/media/userstory2.png)

## Technologies Used

### Languages and Frameworks

- HTML for the basic structure of the website
- CSS for some custom styling of the website
- [JQuery](https://code.jquery.com/) to initiate some interactive elements of the bootstrap framework
- [Bootstrap](https://getbootstrap.com/) v5.1 for some pre-formatted styling
- [Django](https://www.djangoproject.com/) high-level Python web framework for back-end development
- [Python] language used for back-end development



### Applications

- [Gitpod](https://gitpod.io/) to develop the project
- [GitHub](https://github.com/) for version control
- [Heroku](https://www.heroku.com) to deploy the project
- [Heroku Postgres](https://www.heroku.com/postgres) for the database of the deployed version on Heroku
- [Fontawesome](https://fontawesome.com/) for the use of icons
- [Stripe](https://stripe.com/) for the payment system
- [AWS](https://aws.amazon.com/) for hosting the media used on the website
- [MailChimp](https://mailchimp.com) for a subscribe to newsletter popup on home page


## Testing

The application functionalities were tested in three different scenarios:

1. Visitor
	- As a visitor, I was able to complete a view products
	- As a visitor, I was able to subscribe to newsleter
	- When trying to access the management pages or the profile page as a normal visitor, I am redirected to the login page
	- As a visitor I can register as a new user from the Register page

2. User
	- As a user, I can access using the login page and sign out using the logout page 
    - As a normal user, I was able to complete a purchase of the products I like 
        using stripe payment test card: 4242 4242 4242 4242 
	- After completing the order, I received the confirmation email
	- I can access the My Profile page, see my orders and update my details
	
3. Admin
	- As a user, I can access using the login page and sign out using the logout page
    - As an admin user I can make a purchase
	- As an admin user I can update my contact details
	- As an admin user I can access all pages of the website
	- As an admin user I can create/edit/delete products
	- As an admin user I can create/edit/delete orders
    - As an admin user I can create/edit/delete users

I used the following validators to check my Javascript:

Manual tests used on all the following pages:
- https://laterre.herokuapp.com/
- https://laterre.herokuapp.com/accounts/login/
- https://laterre.herokuapp.com/accounts/signup/
- https://laterre.herokuapp.com/accounts/logout/
- https://barbers-flo.herokuapp.com/checkout/1/3/3713/
- https://barbers-flo.herokuapp.com/checkout/checkout-success/12
- https://barbers-flo.herokuapp.com/profile/
- https://barbers-flo.herokuapp.com/bag/
- https://barbers-flo.herokuapp.com/management/products/

[JS Validator](https://jshint.com/)

### Bugs

- Pop up newsletter subscription doesn't always work, but does on the first attempt.
- Email confirmation seems to work with testemails created online, but not consistently with real emails
- Webhook 2 step checkout worked initially, does not at the moment. 
- The reservations page for superusers had the date field set to gg/mm/yyyy once a date was submitted. This was due to the format of a variable (expected date, passed string instead).
- The logic of the booking system was incorrect as it would allow to book 2+ consecutive slots (e.g. for a treatment lasting 1 hour) even if only 30 minutes were available. Changed the logic to show available slots based on the duration of the chosen treatment.

## Deployment

[Link to deployed website](https://laterre.herokuapp.com/)

This project was developed using GitPod, pushed to GitHub and deployed using Heroku.

To deploy to Heroku from the GitHub repository, the following steps were taken:

1. Go to heroku.com and log in
2. Click on "Create new app"
3. Go to Deploy > Deployment method > Github
4. Go to Settings > Config vars and add variables
5. Git add / commit / push Procfile and requirements.txt files
6. Enable postgres with Heroku, along with secret key, disable collect static and install whitenoise for static files
7. Click on Deploy branch

### How to run this project locally

To clone this project into Gitpod you will need:

1. A Github account
2. Use the Chrome browser

Then follow these steps:

1. Install the Gitpod Browser Extension for Chrome
2. After installation, restart the browser
3. Log into Gitpod with your gitpod account
4. Navigate to the Project GitHub repository
5. Click the green GitPod button in the top right corner of the repository
6. This will trigger a new gitpod workspace to be created

To work on the project code within a local IDE such as VSCode, Pycharm etc:

1. Follow this link to the [GitHub repository](https://github.com/csfree87/port5/)
2. Click on the Code button
3. In the drop-down, copy the URL that you see in the HTTPs tab
4. In your local IDE, open the terminal
5. Change the current working directory to the location where you want the cloned directory to be made
6. Type git clone and paste the URL you copied in Step 3
7. Press Enter. Your local clone will be created.

## Credits
The content of the deployment section of this readme.md was mostly taken from boutique ado module.
The steps of the e-commerce functions outlined by Boutique Ado
The products name and description are original


### Images
- [Pexels](https://pexels.com) for images used for products and home page

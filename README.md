![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# La Terre

![home page all screen sizes](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/website-different-viewports.JPG)

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

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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
![DB Schema](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/db-schema.png)
- For each User, the system creates a new UserProfile (1-1 relationship) to store additional information
- Each Product is connected to a Category (many-1), 

- [Home Page Wireframe](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/home-page-wireframe.png)

### The Surface Plane

The color palette of the website will be:
![Color Palette](https://raw.githubusercontent.com/matteofiorini92/barbers/master/media/readme-media/color-palette.png)
The general structure and features are inspired by Boutique Ado, but customized to suit a more earthy tone

## Features

-   [Existing Features](#existing-features)
-   [Features Left to Implement](#features-left-to-implement)
 
### Existing Features

| User Story ID |     AS A/AN    |                        I WANT TO BE ABLE TO...                       |                                             FEATURE                                             |
|:--------------|:---------------|:---------------------------------------------------------------------|:------------------------------------------------------------------------------------------------|
|             1 | Customer/Guest | View a list of treatments                                            | Any user can see the list of treatments by going to the Book Now section                        |
|             2 | Customer/Guest | View a calendar of available dates                                   | Any user can see the list of available dates by going to the Book Now section                   |
|             3 | Customer/Guest | View a list of barbers                                               | Any user can see the list of barbers by going to the Book Now section                           |
|             4 | Customer/Guest | View a list of available times                                       | Any user can see the list of available times by going to the Book Now section                   |
|             5 | Guest          | Easily register for an account                                       | Guests can register from the Register section                                                   |
|             6 | Customer       | Easily login or logout                                               | Customers can log-in / log-out from the log-in / log-out sections of the website                |
|             7 | Customer       | Easily recover my password in case I forget it                       | Customers can reset their password by clicking on the Forgot Password? button                   |
|             8 | Customer       | Receive an email confirmation after registering                      | A confirmation email is sent to the customer after registering                                  |
|             9 | Customer       | See the list of my past appointments                                 | From the My Profile page a customer can see their 5 most recent reservations                    |
|            10 | Customer/Guest | Easily select the treatment, date, time and barber of my reservation | Customers can go to the Book Now section and easily select Treatment, Date, Barber and Time     |
|            11 | Customer/Guest | Easily enter my payment information                                  | At the last step of the booking process, the user can enter their CC details                    |
|            12 | Customer/Guest | Feel my personal and payment information is safe and secure          | The payment is processed via Stripe which is PCI compliant Level 1 (highest)                    |
|            13 | Customer/Guest | View an order confirmation after checkout                            | After checkout, the customer is redirected to a confirmation page with the order confirmation   |
|            14 | Customer/Guest | Receive an email confirmation after checking out                     | After checkout, the customer receives a confirmation email                                      |
|            15 | Shop Owner     | Add a type of treatment                                              | From the management section, the shop owner can create new treatments                           |
|            16 | Shop Owner     | Edit/update a treatment                                              | From the management section, the shop owner can edit existing treatments                        |
|            17 | Shop Owner     | Delete a treatment                                                   | From the management section, the shop owner can delete existing treatments                      |
|            18 | Shop Owner     | Add a barber                                                         | From the management section, the shop owner can create new barbers                              |
|            19 | Shop Owner     | Edit/update a barber                                                 | From the management section, the shop owner can edit existing barbers                           |
|            20 | Shop Owner     | Delete a barber                                                      | From the management section, the shop owner can delete existing barbers                         |
|            21 | Shop Owner     | See a specific day's list of reservations                            | From the management section, the shop owner can see the list of reservations for a specific day |


### Features Left to Implement

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

I used the following validators to check my HTML, CSS and JavaScript code:

[HTML Validator](https://validator.w3.org/)
[CSS Validator](https://jigsaw.w3.org/css-validator/)
<p>
    <a href="https://jigsaw.w3.org/css-validator/check/referer">
        <img style="border:0;width:88px;height:31px"
            src="https://jigsaw.w3.org/css-validator/images/vcss-blue"
            alt="Valid CSS!" />
    </a>
</p>

They were both used on all the following pages:
- https://barbers-flo.herokuapp.com/
- https://barbers-flo.herokuapp.com/accounts/login/
- https://barbers-flo.herokuapp.com/accounts/signup/
- https://barbers-flo.herokuapp.com/booking/
- https://barbers-flo.herokuapp.com/booking/1/
- https://barbers-flo.herokuapp.com/booking/1/2022-01-14
- https://barbers-flo.herokuapp.com/booking/1/2022-01-14/3
- https://barbers-flo.herokuapp.com/checkout/1/3/3713/
- https://barbers-flo.herokuapp.com/checkout/checkout-success/12
- https://barbers-flo.herokuapp.com/profile/
- https://barbers-flo.herokuapp.com/management/reservations/
- https://barbers-flo.herokuapp.com/management/new_treatment/
- https://barbers-flo.herokuapp.com/management/get_treatment/
- https://barbers-flo.herokuapp.com/management/new_barber/
- https://barbers-flo.herokuapp.com/management/get_barber/

[JS Validator](https://jshint.com/)

[PEP8 Validator](http://pep8online.com/)

### Bugs

- When the project was started the file structure was incorrect (barbers > barbers_flo > Apps instead of barbers > Apps). The project was working fine in development but didn't work correctly once deployed because of this bug. Fixed by correcting the file structure.
- The function that makes new availability slots if needed was called every time the calendar page was loaded. If the page was loaded twice in a short timeframe, availability slots would have been created twice.
The same function was moved to a separate custom command that is run daily by Heroku Scheduler. Also, the function initially created the same slots for all barbers, so a newly created barber would only have availability slots for the end of the calendar.
- Wrongly named the constant EMAIL_HOST_PASSWORD caused emails not to be sent. Correcting the constant name fixed the issue.
- The reservations page for superusers had the date field set to gg/mm/yyyy once a date was submitted. This was due to the format of a variable (expected date, passed string instead).
- The logic of the booking system was incorrect as it would allow to book 2+ consecutive slots (e.g. for a treatment lasting 1 hour) even if only 30 minutes were available. Changed the logic to show available slots based on the duration of the chosen treatment.

## Deployment

[Link to deployed website](https://barbers-flo.herokuapp.com/)

This project was developed using GitPod, pushed to GitHub and deployed using Heroku.

To deploy to Heroku from the GitHub repository, the following steps were taken:

1. Go to heroku.com and log in
2. Click on "Create new app"
3. Go to Deploy > Deployment method > Github
4. Go to Settings > Config vars and add variables
5. Git add / commit / push Procfile and requirements.txt files
6. Enable automatic deployments from Heroku
7. Click on Deploy branch
8. Create a public bucket in Amazon Web Services (AWS) S3
9. Create user, user group and policy in AWS to allow access to the bucket 
10. Add Config Vars in Heroku to use user's credentials to access AWS

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

1. Follow this link to the [GitHub repository](https://github.com/matteofiorini92/barbers)
2. Click on the Code button
3. In the drop-down, copy the URL that you see in the HTTPs tab
4. In your local IDE, open the terminal
5. Change the current working directory to the location where you want the cloned directory to be made
6. Type git clone and paste the URL you copied in Step 3
7. Press Enter. Your local clone will be created.

## Credits
The content of the deployment section of this readme.md was mostly taken from [this webinar](https://www.youtube.com/watch?v=7BteidgLAyM).
The steps of the booking system are inspired by the [Resurva](https://resurva.com/) booking system for barbers used by these two websites:
The treatments name and description are inspired by [this website](https://tweedbarbers.com/)
- [CutThroat](https://cutthroatbarbershop.resurva.com/)
- [Turk's](https://turksbarbershop.ie/)


### Images
- For images and icons I used [Unsplash](https://unsplash.com/) and [Iconfinder](https://www.iconfinder.com/)

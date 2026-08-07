# Testing

[Return to Óðrerir Meadery README.md](./README.md)

## Manual Testing

Manual testing was prioritized over automated testing to maximize development efficiency within the current project scope. Hand-testing proved significantly faster to execute while ensuring full functional coverage; however, automated test suites are scheduled for the next development phase to support future scalability and feature expansions.

### base.html | Header and Footer

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Logo navigation link to to home page (index.html) upon clicking | User redirected to index.html | Working |
| Navbar "Home" navigation to index.html | User redirected to index.html | Working |
| Navbar "Products" mega menu dropdown > navigation to categorised products.html | User redirected to products.html | Working |
| Navbar "Flavour Sandbox" navigation to flavour_sandbox.html | User redirected to flavour_sandbox.html | Working |
| Navbar "About" navigation to About section in index.html from all pages in site | User redirected to About section | Working |
| Navbar "Add Product" navigation to add_product.html (superuser only) | User redirected to add_product.html | Working |
| Log In navigation within nav bar to login.html | User redirected to login.html | Working |
| Register navigation within nav bar to signup.html | User redirected to signup.html | Working |
| Logged in user - Log out navigation within nav bar to logout.html | User redirected to logout.html | Working |
| Admin user - Navigation to djangos admin page | User redirected to the django admin page | Working |
| Welcome message in navigation for logged in user | User is presented with personalised welcome message in nav bar | Working |
| Contact company link to modal | Modal pop up to contact company | Working |
| Successfully send a message to company after submitting | Email sent to company with users message | Working (antivirus shield turned off) |
| Navigation to company socials | User is redrected to company socials | Working |
| Policy modal buttons bring up policies | User is presented with the policies modal | Working |

### Account pages | Login, Logout, Register

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| User able to input email or username and password and log in | User is successfully logged in to site | Working |
| User able to select "Forgot your password" to change password | User redirected to allauths change password page | Working |
| User able to select Remember Me to stay logged in on net visit | User is succesfully remembered and logged in upon next visit | Working |
| Redirect user to register in login page | User can click on REGISTER HERE to be taken to signup page | Working |
| User able to input a username, email and password and create an acoount | User can successfully create an account to the site | Working |
| User can redirect to login page if they already have an account | User redirected to the login page | Working |
| User can select to logout of the site | User can succesfully logout of the site | Working |

### index.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| User can click Shop now for navigation to products.html | User redirected to products.html | Working |
| User can select type of mead and then click shop all to be taken to a categorised products.html | User is redirected to categorised products.html | Working |
| Most popular produts carousel functions and user can click the item to be tkaen to specfific product_detail.html | User redirected to product_detail.html | Working |

### products.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Paginated list of all products is generated | User is presented with a paginated list of all products in the database | Working |
| Paginated list can be sorted | Sort function succeessfully sorts list on A-Z, Z-A, Price (low) and Price (high) | Working |
| User can see next page of the list | Clicking "Next" or "Previous" succcesfully navigates user in the paginated list | Working |
| Redirection to specific product page | Clicking on a product card redirects user to specific product page | Working |

### product_detail.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Upon clicking specific product link, relevant product page can be viewed | Successfully renders a product specific page | Working |
| Admin bility to update product | "Edit" button pops out modal form to update product and successfully submit | Working |
| Admin ability to delete product from the database | "Delete" button pops out delete confirmation modal which removes product from database | Working |
| User can select different volumes and the price changes accordingly | Clicking on volume options dynamically updates price | Working |
| User can increase and decrease quantity of product | Clicking on + or - buttons changes quantity amounts to be added | Working |
| User can add item to basket | Clicking "add to basket" adds specified volume (if applicable) and quantity to users basket | Working |

### add_product.html (superuser only)

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Admin ability to submit a new product | Admin is able to submit a new product to the database | Working |
| Ability to attach a relevant image to lore or entity | User is able to attach image to entry/entity | Working |

### flavour_sandbox.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Paginated list of all ideas is generated | User is presented with a paginated list of all approved ideas in the database | Working |
| Paginated list can be sorted | Sort function succeessfully sorts list on most liked, newest to oldest and vice versa | Working |
| User can see next page of the list | Clicking "Next" or "Previous" succcesfully navigates user in the paginated list | Working |
| Redirection to specific idea page | Clicking on a product card redirects user to specific idea page | Working |
| Users can "like" a specific idea within the list | Clicking on the like icon "likes" the idea increasing the amount of likes by 1. Reverse function also removes a like | Working |

### idea_detail.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Upon clicking specific idea link, relevant idea page can be viewed | Successfully renders a idea specific page | Working |
| Ability to update idea | "Edit" button pops out modal form to update idea and successfully submit for review | Working |
| Ability to delete idea from the database | "Delete" button pops out delete confirmation modal which then deletes the idea | Working |
| Ability to leave a comment | Comment text area at the bottom of page + post button successfuly submits comment for review | Working |
| Ability to update user specific comment | "Edit" button successfully updates the bottom comments section to reflect the comment is being updated | Working |
| Ability to delete user specific comment | "Delete" button pops out delete confirmation modal and successfully deletes comment | Working |
| Ability to reply to a previous comment | "Reply" button reveals text area to reply to specific comment and submitting sends it for review | Working |

### basket.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Clicking basket icon redirects user to basket.html | Successfully renders users basket page | Working |
| Viewable basket summary with totals breakdown | Successfully renders a baset summary with subtotal, delivery cost and gross total of basket | Working |
| Ability to update quantity or delete items from basket | Users are able to update quantities and delete items from ther basket | Working |
| Ability to go to checkout page | Clicking "check out" redirects user to checkout page | Working |

### checkout.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Order summary viewable on checkout page | Order sumary successfully renders on checkout page, detailing items and prices (per volume) as a totals breakdown | Working |
| Ability to add in and submit delivery information | Users are able to add in delivery information to the checkout form and also save to their profile if they wish to do so | Working |
| Stripe payment implementation | Users are able to purchase the items in their basket using stripe payments | Working |
| Successful order confirmation | Users are redirected to an order confirmation page with order details upon successful payent of their order as well as receiving an order confirmatin email | Working |

### profile.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| After navigating to profile page, user can update delivery information | User is able to submit the form to update default delivery information | Working |
| User can see previous orders in their profile | Users can see all past orders and cllikc on the order number to see previous checkout_success page with order details | Working |

## User Story Validation

The implemented features directly satisfy the criteria defined in the [User Stories](./README.md/#user-stories) during the strategy phase. All user stories have been fully delivered, with the exception of those deferred in the [Scope Plane](./README.md/#scope-plane) for future release.

## Validator Testing

### HTML

- [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
  - base.html | [Result](./documentation/images/testing/base-html-test.png)
    - 48/49 hidden messages related to django specific tags. 1/49 due to h6 tag used before h5 which is being used as a spacing element in navbar menu
  - index.html.html | [Result](./documentation/images/testing/index-html-test.png)
    - Hidden messages relate to django specific tags with one relating to heading skips as this a product name heading in the popular carousel which required a smaller heading.
  - products.html | [Result](./documentation/images/testing/products-html-test.png)
    - Hidden messages relate to django specific tags with one relating to heading skips as this a product name heading which required a smaller heading.
  - product_detail.html | [Result](./documentation/images/testing/product-detail-html-test.png)
    - Hidden messages relate to django specific tags
  - add_product.html | [Result](./documentation/images/testing/add-product-html-test.png)
    - Hidden messages relate to django specific tags
  - flavour_sandbox.html | [Result](./documentation/images/testing/flavour-sandbox-html-test.png)
    - Hidden messages relate to django specific tags with one relating to heading skips as a smaller heading was required.
  - idea_detail.html | [Result](./documentation/images/testing/idea-detail-html-test.png)
    - Hidden messages relate to django specific tags with one relating to heading skips as a smaller heading was required.
  - comment_thread.html | [Result](./documentation/images/testing/comment-thread-html-test.png)
    - Hidden messages relate to django specific tags
  - basket.html | [Result](./documentation/images/testing/basket-html-test.png)
    - Hidden messages relate to django specific tags
  - checkout.html | [Result](./documentation/images/testing/checkout-html-test.png)
    - Hidden messages relate to django specific tags
  - checkout_success.html | [Result](./documentation/images/testing/checkout-success-html-test.png)
    - Hidden messages relate to django specific tags
  - profile.html | [Result](./documentation/images/testing/profile.html-test.png)
    - Hidden messages relate to django specific tags
  - 404.html | [Result](./documentation/images/testing/404-html-test.png)
    - All messages related to django relevant code not recognised by validator.
  - 500.html | [Result](./documentation/images/testing/500-html-test.png)
    - All hidden messages related to django relevant code not recognised by validator.
  - toast_success.html | [Result](./documentation/images/testing/toast-success-html-test.png)
    - All hidden messages related to this being an include, and djangp relevant code.
  - toast_error.html | [Result](./documentation/images/testing/toast-error-html-test.png)
    - All hidden messages related to this being an include, and having no head element.
  - toast_info.html | [Result](./documentation/images/testing/toast-info-html-test.png)
    - All hidden messages related to this being an include, and having no head element.
  - toast_warning.html | [Result](./documentation/images/testing/toast-warning-html-test.png)
    - All hidden messages related to this being an include, and having no head element.

### CSS Warnings from this validator are all dynamic nature warnings as well as vendor extension warnings

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
  - base.css | [Result](./documentation/images/testing/base-css-test.png)
    - Warnings from this validator are all dynamic nature warnings as well as vendor extension warnings
  - basket.css | [Result](./documentation/images/testing/basket-css-test.png)
  - checkout.css | [Result](./documentation/images/testing/checkout-css-test.png)
  - flavour_sandbox.css.css | [Result](./documentation/images/testing/flavour-sandbox-css-test.png)
    - Warnings from this validator are all dynamic nature warnings
  - products.css | [Result](./documentation/images/testing/products-css-test.png)
    - Warnings from this validator are all dynamic nature warnings
  - profile.css | [Result](./documentation/images/testing/profile-css-test.png)

### JavaScript

- [JSHint](https://jshint.com/) - JavaScript Validator
  - base.js | [Result](./documentation/images/testing/base-js-test.png)
    - Warning related to bootstap element
  - basket.js | [Result](./documentation/images/testing/basket-js-test.png)
    - Warnings related to $ not being recognised by jshint.
  - stripe_elements.js | [Result](./documentation/images/testing/stripe-elements-js-test.png)
    - Warnings related to $ and Stripe not being recognised by jshint.
  - flavour_sandbox.js | [Result](./documentation/images/testing/flavour-sandbox-js-test.png)
    - Warnings related to bootstap element, $ not being recognised by jshint and toggleReply being unused, however this function is called in hte html.
  - products.js | [Result](./documentation/images/testing/products-js-test.png)
    - Warnings related to $ not being recognised by jshint.

### Python

All custom Python and Django codebase files were rigorously tested and validated using **Flake8** to ensure strict adherence to **PEP 8** style guidelines and code quality standards.

## Further Testing

This site was designed for and tested across the following web browsers:
    - Google Chrome
    - Microsoft Edge
    - Mozilla Firefox
    - Opera
    - Safari

### Lighthouse Testing


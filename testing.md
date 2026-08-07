# Testing

[Return to Óðrerir Meadery README.md](./README.md)

## Manual Testing

Manual testing was prioritized over automated testing to maximize development efficiency within the current project scope. Hand-testing proved significantly faster to execute while ensuring full functional coverage; however, automated test suites are scheduled for the next development phase to support future scalability and feature expansions.

### base.html | Header and Footer

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Logo navigation link to home page (index.html) upon clicking | User redirected to index.html | Working |
| Navbar "Home" navigation to index.html | User redirected to index.html | Working |
| Navbar "Products" mega menu dropdown > navigation to categorised products.html | User redirected to products.html | Working |
| Navbar "Flavour Sandbox" navigation to flavour_sandbox.html | User redirected to flavour_sandbox.html | Working |
| Navbar "About" navigation to About section in index.html from all pages in site | User redirected to About section | Working |
| Navbar "Add Product" navigation to add_product.html (superuser only) | User redirected to add_product.html | Working |
| Log In navigation within navbar to login.html | User redirected to login.html | Working |
| Register navigation within nav bar to signup.html | User redirected to signup.html | Working |
| Logged in user - Log out navigation within nav bar to logout.html | User redirected to logout.html | Working |
| Admin user - Navigation to Django's admin page | User redirected to the django admin page | Working |
| Welcome message in navigation for logged in user | User is presented with personalised welcome message in nav bar | Working |
| Contact company link to modal | Modal pop up to contact company | Working |
| Successfully send a message to company after submitting | Email sent to company with user's message | Working (antivirus shield turned off) |
| Navigation to company socials | User is redirected to company socials | Working |
| Policy modal buttons bring up policies | User is presented with the policies modal | Working |

### Account pages | Login, Logout, Register

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| User able to input email or username and password and log in | User is successfully logged in to site | Working |
| User able to select "Forgot your password" to change password | User redirected to allauths change password page | Working |
| User able to select Remember Me to stay logged in on net visit | User is successfully remembered and logged in upon next visit | Working |
| Redirect user to register in login page | User can click on REGISTER HERE to be taken to signup page | Working |
| User able to input a username, email and password and create an account | User can successfully create an account to the site | Working |
| User can redirect to login page if they already have an account | User redirected to the login page | Working |
| User can select to logout of the site | User can succesfully logout of the site | Working |

### index.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| User can click "Shop Now" for navigation to products.html | User redirected to products.html | Working |
| User can select type of mead and then click "Shop All" to be taken to categorised products.html | User is redirected to categorised products.html | Working |
| Most popular products carousel functions and user can click the item to be taken to specific product_detail.html | User redirected to product_detail.html | Working |

### products.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Paginated list of all products is generated | User is presented with a paginated list of all products in the database | Working |
| Paginated list can be sorted | Sort function successfully sorts list on A-Z, Z-A, Price (low) and Price (high) | Working |
| User can see next page of the list | Clicking "Next" or "Previous" succesfully navigates user in the paginated list | Working |
| Redirection to specific product page | Clicking on a product card redirects user to specific product page | Working |

### product_detail.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Upon clicking specific product link, relevant product page can be viewed | Successfully renders a product-specific page | Working |
| Admin ability to update product | "Edit" button pops out modal form to update product and successfully submit | Working |
| Admin ability to delete product from the database | "Delete" button pops out delete confirmation modal which removes product from database | Working |
| User can select different volumes and the price changes accordingly | Clicking on volume options dynamically updates price | Working |
| User can increase and decrease quantity of product | Clicking on + or - buttons changes quantity amounts to be added | Working |
| User can add item to basket | Clicking "add to basket" adds specified volume (if applicable) and quantity to user's basket | Working |

### add_product.html (superuser only)

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Admin ability to submit a new product | Admin is able to submit a new product to the database | Working |
| Admin ability to attach a relevant image to product | Admin is able to attach image to product | Working |

### flavour_sandbox.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Paginated list of all ideas is generated | User is presented with a paginated list of all approved ideas in the database | Working |
| Paginated list can be sorted | Sort function successfully sorts list on most liked, newest to oldest and vice versa | Working |
| User can see next page of the list | Clicking "Next" or "Previous" succesfully navigates user in the paginated list | Working |
| Redirection to specific idea page | Clicking on a product card redirects user to specific idea page | Working |
| Users can "like" a specific idea within the list | Clicking on the like icon "likes" the idea increasing the amount of likes by 1. Reverse function also removes a like | Working |

### idea_detail.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Upon clicking specific idea link, relevant idea page can be viewed | Successfully renders a idea-specific page | Working |
| Ability to update idea | "Edit" button pops out modal form to update idea and successfully submit for review | Working |
| Ability to delete idea from the database | "Delete" button pops out delete confirmation modal which then deletes the idea | Working |
| Ability to leave a comment | Comment text area at the bottom of page + post button successfully submits comment for review | Working |
| Ability to update user specific comment | "Edit" button successfully updates the bottom comments section to reflect the comment is being updated | Working |
| Ability to delete user specific comment | "Delete" button pops out delete confirmation modal and successfully deletes comment | Working |
| Ability to reply to a previous comment | "Reply" button reveals text area to reply to specific comment and submitting sends it for review | Working |

### basket.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Clicking basket icon redirects user to basket.html | Successfully renders user's basket page | Working |
| Viewable basket summary with totals breakdown | Successfully renders a basket summary with subtotal, delivery cost and gross total of basket | Working |
| Ability to update quantity or delete items from basket | Users are able to update quantities and delete items from their basket | Working |
| Ability to go to checkout page | Clicking "check out" redirects user to checkout page | Working |

### checkout.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| Order summary viewable on checkout page | Order summary successfully renders on checkout page, detailing items and prices (per volume) as a totals breakdown | Working |
| Ability to add in and submit delivery information | Users are able to add in delivery information to the checkout form and also save to their profile if they wish to do so | Working |
| Stripe payment implementation | Users are able to purchase the items in their basket using stripe payments | Working |
| Successful order confirmation | Users are redirected to an order confirmation page with order details upon successful payment of their order as well as receiving an order confirmation email | Working |

### profile.html

| **FUNCTION & EXPECTED OUTCOME** | **TESTING RESULT** | **STATUS** |
| --- | --- | --- |
| After navigating to profile page, user can update delivery information | User is able to submit the form to update default delivery information | Working |
| User can see previous orders in their profile | Users can see all past orders and click on the order number to see previous checkout_success page with order details | Working |

## User Story Validation

The implemented features directly satisfy the criteria defined in the [User Stories](./README.md/#user-stories) during the strategy phase. All user stories have been fully delivered, with the exception of those deferred in the [Scope Plane](./README.md/#scope-plane) for future release.

## Validator Testing

### HTML

- [W3C Markup Validator](https://validator.w3.org/#validate_by_input)
  - base.html | [Result](./documentation/images/testing/base-html-test.png)
    - 48/49 hidden messages related to django specific tags. 1/49 due to h6 tag used before h5 which is being used as a spacing element in navbar menu
  - index.html | [Result](./documentation/images/testing/index-html-test.png)
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
  - flavour_sandbox.css | [Result](./documentation/images/testing/flavour-sandbox-css-test.png)
    - Warnings from this validator are all dynamic nature warnings
  - products.css | [Result](./documentation/images/testing/products-css-test.png)
    - Warnings from this validator are all dynamic nature warnings
  - profile.css | [Result](./documentation/images/testing/profile-css-test.png)

### JavaScript

- [JSHint](https://jshint.com/) - JavaScript Validator
  - base.js | [Result](./documentation/images/testing/base-js-test.png)
    - Warning related to bootstrap element
  - basket.js | [Result](./documentation/images/testing/basket-js-test.png)
    - Warnings related to $ not being recognised by jshint.
  - stripe_elements.js | [Result](./documentation/images/testing/stripe-elements-js-test.png)
    - Warnings related to $ and Stripe not being recognised by jshint.
  - flavour_sandbox.js | [Result](./documentation/images/testing/flavour-sandbox-js-test.png)
    - Warnings related to bootstrap element, $ not being recognised by jshint and toggleReply being unused, however this function is called in the html.
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

- [Home](./documentation/images/testing/home-lighthouse.png)
  - The Google Lighthouse audit for the homepage (index.html) demonstrates strong overall scores across core metrics. The slight reduction in the Performance score is primarily driven by the Largest Contentful Paint (LCP) metric, resulting from media image load times and network overhead from external CDNs and AWS S3 storage. Because these load times fall within an acceptable baseline for a media-rich page, no further modifications were made.
- [Products](./documentation/images/testing/products-lighthouse.png)
  - Similarly, this page achieved high scores across Accessibility, Best Practices, and SEO. The lower Performance score is driven primarily by the Largest Contentful Paint (LCP) metric, resulting from the same external CDN dependencies and AWS S3 media rendering factors identified on the homepage.
- [Product Detail](./documentation/images/testing/product-detail-lighthouse.png)
  - Consistent with the previous pages, this audit achieved strong results across Accessibility, Best Practices, and SEO. While the Performance metric remained lower due to the same external media asset factors, it demonstrated a slight improvement compared to the homepage score.
- [Flavour Sandbox](./documentation/images/testing/flavour-sandbox-lighthouse.png)
  - Reflecting the positive trends of previous pages, this audit recorded high overall scores across Accessibility, Best Practices, and SEO. The Performance metric showed a slight improvement over earlier tested pages, though it remained influenced by the same external asset delivery factors.
- [Idea Detail](./documentation/images/testing/idea-detail-lighthouse.png)
  - Consistent with the homepage audit, performance remained impacted by external asset loading, while Accessibility, Best Practices, and SEO metrics scored consistently high.
- [Basket](./documentation/images/testing/basket-lighthouse.png)
  - Consistent with previous pages, this audit maintained high scores across Accessibility, Best Practices, and SEO, while demonstrating a notable improvement in the overall Performance score.
- [Checkout](./documentation/images/testing/checkout-lighthouse.png)
  - Consistent with previous pages, this audit maintained high scores across Accessibility, Best Practices, and SEO, while demonstrating a notable improvement in the overall Performance score.
- [Checkout Success](./documentation/images/testing/checkout-success-lighthouse.png)
  - Consistent with previous pages, this audit maintained high scores across Accessibility, Best Practices, and SEO, while demonstrating a notable improvement in the overall Performance score.
- [Profile](./documentation/images/testing/profile-lighthouse.png)
  - Consistent with the homepage audit, performance remained impacted by external asset loading, while Accessibility, Best Practices, and SEO metrics scored consistently high.
- [Log In](./documentation/images/testing/login-lighthouse.png)
  - Consistent with previous pages, this audit maintained high scores across Accessibility, Best Practices, and SEO, while demonstrating a notable improvement in the overall Performance score.
- [Log Out](./documentation/images/testing/logout-lighthouse.png)
  - Consistent with previous pages, this audit maintained high scores across Accessibility, Best Practices, and SEO, while demonstrating a notable improvement in the overall Performance score.
- [Register](./documentation/images/testing/register-lighthouse.png)
  - Consistent with the homepage audit, performance remained impacted by external asset loading, while Accessibility, Best Practices, and SEO metrics scored consistently high.

## Bugs and Fixes

The following section outlines the key issues identified during active development and formal testing, along with the corresponding fixes implemented to resolve them:

### Navbar Toggle & Dropdown Focus Persistence

- **Issue:** Navbar togglers and dropdown menu items retained browser focus states after being clicked/closed, leaving active outlines until clicked elsewhere on the page.
- **Resolution:** Added custom JavaScript event listeners to explicitly invoke `.blur()` on toggler and dropdown elements upon click interactions.

### Unwanted Horizontal Overflow

- **Issue:** Occasional horizontal scrolling appeared across viewports when toggling Chrome DevTools or resizing windows.
- **Resolution:** Applied `max-width: 100%` to `html, body` in the main CSS stylesheet.

### Product Pagination Controls Not Rendering

- **Issue:** Pagination navigation links failed to display on the product list page.
- **Root Cause:** The Django view context was missing required paginator state attributes.
- **Resolution:** Updated `views.py` context dictionary to explicitly deliver `page_obj`, `is_paginated`, `sort`, and `direction` variables to the template.

### Incorrect Volume Selector Display on Merchandise

- **Issue:** Product volume options were incorrectly rendering on non-beverage items like accessories and merchandise.
- **Resolution:** Wrapped volume input fields in Django template conditional tags (`{% if %}`) targeting relevant categories, using Django's `|stringformat:"s"` filter to ensure string comparison consistency.

### Accessory Display Errors in Basket View

- **Issue:** Non-volume accessory products were failing to render correctly inside the shopping basket summary.
- **Resolution:** Refactored the `basket_contents` context processor logic to parse items lacking volume attributes.

### Basket Removal Triggering 403 CSRF Forbidden Error

- **Issue:** Clicking the basket removal icon returned a `403 Forbidden` response (`POST /basket/remove/<id>/`).
- **Root Cause:** The external JavaScript file was unable to resolve Django's `csrfToken` context variable directly.
- **Resolution:** Updated the JS removal handler to read the `csrfmiddlewaretoken` value directly from the DOM form input prior to dispatching the POST request.

### Global Quantity Decrement Disabling

- **Issue:** Reducing any single product quantity to `1` disabled the decrement (`-`) button across **all** items present in the basket.
- **Root Cause:** JavaScript selection logic targeted controls solely by `item_id`, incorrectly grouping distinct line items.
- **Resolution:** Updated DOM selection logic to evaluate a unique composite key matching both `item_id` and `volume`.

### Silent Failure on Stripe Checkout Form

- **Issue:** Submitting the Stripe checkout form caused input fields to disappear without completing processing or displaying confirmation.
- **Root Cause:** Deprecated jQuery `$.trim()` usage triggered a silent JavaScript runtime exception during payload preparation.
- **Resolution:** Refactored string trimming logic to use standard JavaScript native `.trim()` and `.val().trim()`.

### Pagination Resetting Active Category Filters

- **Issue:** Clicking pagination page numbers stripped active category filters, preserving only current sorting parameters.
- **Resolution:** Implemented a custom Django template tag (`url_replace`) to dynamically retain existing query parameters (category, search, sorting) across pagination link generation.

## Future Improvements & Known Bugs

Future iterations of the platform will prioritize enhancing user engagement, refining administrative workflows, and addressing minor technical optimizations flagged during initial testing. Key planned enhancements include:

- **Expanded Social Authentication:**
  - Integrate additional OAuth providers (such as Google, Facebook, and GitHub) through Django Allauth to streamline the sign-up and login process, reducing friction for new users.

- **User-Submitted Flavour Concepts:**
  - Enhance the community feature by allowing authenticated users to upload custom image assets alongside their product idea submissions, creating a richer and more engaging user-generated content experience.

- **Comprehensive Product Reviews & Feedback:**
  - Expand the current star-rating functionality into a full review system, enabling verified customers to leave written comments, structured feedback, and detailed user reviews on product pages.

- **Automated Content Moderation Workflow:**
  - Implement administrative moderation queues and automated checks for user-submitted content (such as reviews and flavour proposals) to ensure platform safety and brand compliance prior to public display.

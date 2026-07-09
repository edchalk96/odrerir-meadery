# Óðrerir Meadery

## By Ed Chalk

[View the live project here](PLACEHOLDER)

[View the repository here](https://github.com/edchalk96/mimirs_index/tree/main)

![Responsive website image](PLACEHOLDER)

## Table of Contents

1. [Background](#background)
2. [User Experience (UX) | The 5 Planes](#user-experience-ux--the-5-planes)
    1. [Strategy Plane](#strategy-plane)
    2. [Scope Plane](#scope-plane)
    3. [Structure PLane](#structure-plane)
    4. [Skeleton Plane](#skeleton-plane)
    5. [Surface PLane](#surface-plane)
3. [Technologies Used](#technologies-used)
4. [Testing](#testing)
5. [Deployment](#deployment)
6. [Credits](#credits)

---

## Background

Óðrerir Meadery is a conceptual e-commerce website dedicated to selling various types of craft mead (honey wine) and accessories to a UK-based audience (ages 18+). Developed as Milestone Project 4 for the Code Institute Full-Stack Web Development diploma, this site serves as a proof of concept. However, it has been built to commercial standards so it can be deployed as a live e-commerce store if the business goes live in the future.

---

## User Experience (UX) | The 5 Planes

The planning and development of the Óðrerir Meadery website followed the core principles of UX design, utilizing Jesse James Garrett's framework from The Elements of User Experience. To ensure a thorough and well-structured design process, this framework was supplemented by Urooj Qureshi’s practical "Five Planes Method" alongside the Code Institute curriculum. The site was built progressively by applying these five planes in distinct, sequential stages:

1. The Strategy Plane
2. The Scope Plane
3. The Structure Plane
4. The Skeleton Plane
5. The Surface Plane

---

### Strategy Plane

#### *Project Goals*

The primary objective of the Óðrerir Meadery website is to provide a seamless, secure e-commerce experience where customers can purchase craft mead in various volumes, manage personalized accounts, and browse curated brand accessories. Beyond sales, the beautifully designed platform serves as a powerful marketing tool to celebrate the traditional heritage of mead-making while elevating the brand's online presence. Additionally, the site fosters community engagement by offering a dedicated channel for customers to request or suggest new mead flavors, directly involving them in the company’s future product development. In order to achieve these project goals, the site will implement the following core features, mapped to the user experience:

- **Dynamic E-Commerce Storefront & Catalog**: A robust product catalog allowing users to filter and sort mead products by type and flavor profile with dedicated product detail pages showcasing detailed tasting notes and descriptions.

- **Secure Authentication & User Profiles**: Custom user registration and secure login functionality, giving customers a personalised dashboard to manage their delivery addresses, save payment preferences, and view past order histories.

- **Intuitive Shopping Cart & Checkout Pipeline**: A persistent shopping cart that calculates item subtotals dynamically, paired with a secure, multi-step checkout pipeline integrated with a reliable payment processor (such as Stripe) to handle transaction validation and email order confirmations.

- **Flavor Sandbox & Innovation Hub**: An interactive community submission portal where registered users can submit custom mead flavor ideas, view submissions from other users, and upvote or comment on community-suggested blends.

- **Administrative Control Panel (Content Management)**: A secure backend administrative interface allowing the meadery staff to easily manage product stock levels, make updates to products and update pricing and review flavour submissions.

#### *User Stories*

The primary objective for customers visiting the site is to seamlessly explore the meadery's diverse product range, learn about the rich history of mead-making, and discover the brand's unique origin story. Beyond browsing, users require an intuitive, secure pathway to purchase products, alongside an interactive space where they can actively engage with the company by proposing new flavor concepts.

##### First Time User Goals

- As a First-Time Visitor, I want to immediately understand the core identity and product offerings of Óðrerir Meadery upon landing on the homepage, so that I can quickly decide if the brand appeals to me.
- As a First-Time Visitor, I want to experience a clean, intuitive navigation layout, so that I can effortlessly explore the site's content, product lines, and interactive features without confusion.
- As a First-Time Visitor, I want to easily register for a secure personal account, so that my details are saved for future convenience and I can track potential order history as a returning customer.
- As a First-Time Visitor, I want to learn about the heritage of mead-making and the company’s background, so that I can appreciate the brand's craftsmanship, build trust, and feel confident making a purchase.
- As a First-Time Visitor, I want to see clear customer reviews, testimonials, or product ratings, so that I can verify the quality of the products before committing to a purchase.
- As a First-Time Visitor, I want to easily locate the company's contact information, privacy policy, and social media links, so that I can verify the legitimacy and authenticity of the business.
- As a First-Time Visitor, I want to encounter a clear age-verification process, so that I am assured the platform operates legally and responsibly regarding the sale of alcohol (18+).
- As a First-Time Visitor, I want to navigate the site seamlessly on my mobile device or tablet, so that I have a high-quality user experience regardless of the device I am using.
- As a First-Time Visitor, I want to see clear information regarding shipping costs, delivery times, and return policies before entering the checkout pipeline, so that there are no unexpected surprises at payment.
- As a First-Time Visitor, I want to clearly see visible trust signals (such as accepted payment badges like Stripe, Visa, or Mastercard) in the footer or checkout, so that I feel secure entering my payment information on a new site.

##### Returning Visitor Goals

- As a Returning Visitor, I want to securely log in and out of my account, so that I can easily manage my personal profile and protect my data.
- As a Returning Visitor, I want to view a detailed history of my previous orders, so that I can track past purchases and easily identify products I want to reorder.
- As a Returning Customer, I want the ability to filter and sort products by flavour profile so that I can quickly locate my preferred mead without unnecessary scrolling.
- As a Returning Customer, I want to receive clear order confirmation both immediately on-screen and via an automated email upon a successful checkout, so that I have instant reassurance of my transaction.
- As a Returning Customer, I want to submit custom flavour suggestions to a dedicated portal, so that I can actively engage with the brand and share my ideas with the community.
- As a Returning Customer, I want to view, comment on, and upvote flavour suggestions submitted by other community members, so that I can interact with fellow mead enthusiasts and see popular community trends.
- As a Returning Customer, I want to easily update my saved shipping addresses and account details from my profile dashboard, so that I don't have to re-enter them during subsequent checkouts.
- As a Returning Visitor, I want my shopping basket to persist and save its contents even if I close the browser and return later, so that I don't lose the items I intended to buy.
- As a Returning Customer, I want to see a history of my approved or pending flavour submissions within my profile, so that I can keep track of the ideas I have contributed to the community.

##### Site Administrator Goals

- As a Store Administrator, I want to add, edit, or delete products directly from the front-end or a dedicated management dashboard, so that I can maintain accurate inventory levels and pricing without altering the source code.
- As a Site Administrator, I want the authority to review, approve, or delete customer flavour suggestions and user comments, so that I can moderate the community platform and ensure all public content aligns with brand guidelines.
- As a Business Owner, I want to sort or filter customer flavour suggestions by the highest number of community upvotes, so that I can easily identify the most popular trends and make data-driven decisions on future product batches.

---

### Scope Plane

The scope of the Óðrerir Meadery platform was strictly defined by translating the strategic objectives established in the Strategy Plane into tangible functional requirements. To ensure a viable, highly functional Minimum Viable Product (MVP), an Opportunities Matrix was utilized to mathematically evaluate each proposed feature against two core metrics: User/Business Importance and Technical Feasibility.

The initial assessment yielded a balanced aggregate score of 53 for Importance and 58 for Feasibility (updated to reflect the modification). During this scoping process, a specific feature (Product Reviews) evaluating poorly at a 2 for Importance and a 2 for Feasibility was deliberately removed from the immediate roadmap. As this feature carried both low importance to the user and low technical feasibility, this represented a high-risk allocation of development time for minimal reward. By stripping away this low-value complexity, development efforts were strictly optimized around the high-value, high-feasibility threshold. This calculated adjustment ensures that the MVP remains streamlined and achievable within the project timeline, successfully prioritising core commercial requirements—such as secure authentication, product CRUD functionality, and a secure checkout flow—while safely deferring non-essential mechanics to future development phases.

#### Opportunities Matrix

| **Opportunity**                                       | **Importance** | **Viability/Feasibility** | **Total Score** |
| ----------------------------------------------------- | :------------: | :-----------------------: | :-------------: |
| **User Authentication (Login/Out)**                   | 5              | 5                         | 10              |
| **User Profile (inc. Delivery info & Order history)** | 5              | 5                         | 10              |
| **Responsive Storefront and Navigation**              | 5              | 5                         | 10              |
| **Product Catalog**                                   | 5              | 5                         | 10              |
| **Full Admin CRUD (Products)**                        | 5              | 5                         | 10              |
| **Product Ratings**                                   | 4              | 4                         | 8               |
| **Product Reviews**                                   | 2              | 2                         | 5               |
| **Shopping Basket & Stripe Checkout**                 | 5              | 5                         | 10              |
| **Company Contact Form**                              | 3              | 5                         | 8               |
| **Flavour Sandbox - Community Suggestions**           | 3              | 4                         | 7               |
| **Community Socials (Likes & Comments)**              | 3              | 4                         | 7               |
| **Community Moderation (Admin Approval)**             | 3              | 4                         | 7               |
| **Admin Moderation Dashboard**                        | 5              | 5                         | 10              |
|                                                       | **53**         | **58**                    |                 |

#### Feature List

- **User Authentication (Login/Out)**

    A secure system utilizing robust verification to allow users to register, log in, and log out of their personal accounts safely, protecting their data and gating member-only features.

- **User Profile (inc. Delivery info & Order history)**

    A personalized customer dashboard where users can manage their default shipping details for a faster checkout, while maintaining a clear view of their past transaction history.

- **Responsive Storefront and Navigation**

    A fully optimized, mobile-first user interface featuring fluid navigation and layout structures, ensuring a seamless and visually engaging experience across all screen sizes.

- **Product Catalog**

    An intuitive digital storefront that showcases the meadery's product range, allowing users to browse items, read detailed descriptions, and filter or sort products by flavour profile.

- **Full Admin CRUD (Products)**

    An administrative feature enabling authorized site managers to Create, Read, Update, and Delete products directly from the front-end to maintain real-time inventory and pricing accuracy.

- **Product Ratings**

    An interactive feedback system that allows customers to view and assign ratings to individual meads (after confirmed purchase), providing social proof to help guide future purchasing decisions.

- **Shopping Basket & Stripe Checkout**

    A dynamic, persistent shopping basket that accurately handles item totals, paired with a secure, production-ready checkout pipeline integrated with the Stripe payment gateway.

- **Company Contact Form**

    A clean, accessible communication channel allowing users to seamlessly send inquiries, feedback, or support requests directly to the meadery's administration team.

- **Flavour Sandbox - Community Suggestions**

    An engaging community portal where authenticated users can submit custom mead flavour concepts, allowing members to interact directly with the brand's creative process.

- **Community Socials (Likes & Comments)**

    A social interactive layer built into the Flavour Sandbox, enabling community members to comment on and upvote or like other users' flavour submissions to highlight popular trends.

- **Community Moderation (Admin Approval)**

    A secure backend control gate that allows site administrators to review, approve, or reject user-submitted flavours and comments before they are published to the public site.

- **Admin Moderation Dashboard**

    A secure, centralized backend interface leveraging built-in Django Administration features, configured specifically to allow site managers to efficiently moderate community engagement, manage database models, and oversee user interactions.

---

### Structure Plane

The Structure Plane defines how the platform’s functional requirements and technical features are organised to create a cohesive user experience. For the Óðrerir Meadery website, this involved designing an intuitive informational architecture and user flow that allows visitors to navigate seamlessly between commercial spaces and community features. To support this front-end layout, a robust relational database schema was architected to handle complex data relationships securely. The sections below detail the structural layout of the site, alongside the database architecture, Entity Relationship Diagrams (ERDs), and the combination of core Django frameworks and custom-built data models implemented to power the sites functionality.

#### Site Layout & User Flows

- **Landing/Homepage**

    The homepage is designed to immediately capture the user's attention with an engaging, clean layout that introduces the brand without overwhelming the visitor. It features an educational section outlining the rich history and various types of mead, alongside a curated promotional section highlighting the site's most popular or clearance products. To ensure strict legal compliance for alcohol sales in the UK market, a secure age-verification modal triggers immediately upon the initial site load, restricting access to users under the age of 18.

- **Global Navigation Bar**

    To ensure seamless and intuitive exploration of the platform, a fixed navigation bar is present at the top of every page. This persistent layout choice allows users to effortlessly access different areas of the site from any scroll depth, maintaining an optimised user experience across mobile, tablet, and desktop viewports.

- **Product Catalogue**

    Accessible directly from the global navigation menu, the product catalogue dynamically displays the meadery's inventory. Users can navigate straight to filtered product views dedicated to specific mead styles or browse the company's range of related accessories, providing a highly focused and frictionless shopping experience.

- **The Flavour Sandbox**

    Serving as the platform's primary community engagement hub, this dedicated page provides an interactive space where authenticated users can actively pitch their own mead concepts. Members can fill out a custom submission form, view concepts designed by other enthusiasts, leave feedback via comments, and upvote or like their favorite recipes.

- **Global Footer & Utility Modals**

    A uniform footer anchors the bottom of every page, containing active social media links (Facebook, Instagram, YouTube, and TikTok) alongside recognised trust signals and payment verification badges. To prevent users from losing their place in the shopping pipeline, the footer utilises interactive modals to cleanly display essential company documentation—including the contact form, delivery protocols, and refund policies—without forcing a page reload.

- **Administrative Product Management Panel**

    Built specifically for staff members and superusers, this restricted interface features a custom front-end form that facilitates full CRUD functionality. Authorized administrators can seamlessly create new items, adjust pricing, update descriptions, and manage live stock levels. To maintain platform security, the link to this management area is strictly gated and will only appear in the navigation bar if a logged-in account possesses superuser credentials.

#### Database Architecture

The website utilises Neon, a serverless cloud infrastructure, to host and manage its robust PostgreSQL relational database. This serverless approach ensures high availability, automatic scaling, and optimal performance for the sites data layer.

To support the core commercial and community functionality across the site, the database architecture integrates a combination of built-in Django frameworks and bespoke, custom-built models. The data schema outlined below illustrates how these entities interact to securely manage user authentication, e-commerce transactions, and community interactions:

##### *User*

The platform utilizes the standard Django User model in tandem with the Django-Allauth package to securely manage user registration, authentication, and session states (logging in and out). To ensure data integrity and establish a secure shopping environment, email verification is configured as a mandatory requirement upon account creation. When a new user registers, an automated verification email is dispatched to their provided address. The user must successfully verify their email before the system grants authorization to sign in, complete commercial transactions, or actively participate in the community Flavour Sandbox. This strict authentication gate protects the platform from automated spam accounts while ensuring a verified user base for community interactions.

- username | Charfield

    Utilises Django's native validation to enforce database uniqueness with a maximum limit of 150 characters. This required field accepts alphanumeric characters alongside underscores (_), at symbols (@), plus signs (+), periods (.), and hyphens (-) during account creation.

- email | EmailField

    Leverages Django's built-in email format validation to ensure syntactic accuracy. This field is explicitly configured as a mandatory requirement within the application settings to facilitate the mandatory account verification process.

- password | CharField

    Enforces Django's core password hashing and validation security standards. To prevent input errors and align with secure authentication protocols, the default Django-Allauth signup flow requires users to input their chosen password twice to confirm accuracy.

##### UserProfile | [ERD](PLACEHOLDER)

The application features a bespoke UserProfile model that shares a one-to-one relationship with Django's native User model. Upon account creation, the system pulls through the authenticated user's credentials to initialize a personalised profile dashboard. This model is specifically architected to allow users to securely save and update a default shipping address for an optimised, single-click checkout experience, while automatically maintaining a detailed, persistent ledger of their transactional order history.

- user | OneToOneField

    Establishes a direct, unique relationship with Django's native User model, ensuring that every registered user is allocated exactly one corresponding profile dashboard.

- default_mobile_number | CharField

    Stores the user's preferred telephone contact number, utilizing an optional character field to accommodate various international and domestic formatting standards.

- default_street_address1 | CharField

    Captures the primary line of the user's shipping address, such as the house number and street name, which is mandatory for physical order fulfillment.

- default_street_address2 | CharField

    Provides an optional secondary text field to accommodate supplementary delivery information, such as apartment numbers, suite details, or building names.

- default_town_or_city | CharField

    Stores the city or town name required to accurately route shipments during the logistics and delivery process.

- default_county | CharField

    An optional field used to record the specific region or county, ensuring regional accuracy for domestic UK addresses.

- default_postcode | CharField

    Captures the alphanumeric postal or ZIP code required to calculate accurate shipping and validate geographical delivery data.

- default_country | CountryField

    Utilises a specialized country dropdown field to map the user's geographic location securely, ensuring compatibility with global shipping standards.

##### Product | [ERD](PLACEHOLDER)

The bespoke Product model serves as the central database repository for the digital storefront, storing comprehensive commercial data and structural inventory metadata for every item in the meadery's catalogue. Beyond standard e-commerce attributes like pricing and stock levels, this model incorporates dedicated fields to classify items by their specific mead type and distinct flavour profile. By structuring these granular data points at the database level, the platform can efficiently power front-end query filtering and sorting algorithms, enabling users to navigate the digital storefront seamlessly based on their taste preferences and honey-wine styles.

- sku | CharField

    Stores a unique Stock Keeping Unit (SKU) code for each item, acting as a primary alphanumeric identifier to ensure precise inventory tracking and product management.

- name | CharField

    Captures the commercial name of the specific product, configured with a character limit suitable for clean display titles across the digital storefront.

- mead_type | CharField

    Utilises a predefined list of choices to classify the product by its specific traditional or historical honey-wine category, enabling accurate front-end catalogue filtering.

- flavour_profile | CharField

    Records a descriptive string detailing the primary taste notes and aromatic qualities of the product to guide customer buying decisions.

- honey | CharField

    Uses a dropdown selection of choices to track the specific varietal of honey used during fermentation, highlighting the authentic craftsmanship of the meadery.

- description | TextField

    Provides a flexible text field for comprehensive product narratives, tasting notes, and ingredient breakdowns to fully inform prospective buyers.

- volume | IntegerField

    Stores the fluid volume of the product bottle using a set of preconfigured choices, allowing the storefront to cleanly display standard commercial measurements.

- price | DecimalField

    Records the retail price of the item using a fixed-precision decimal format, ensuring financial accuracy and consistent currency rendering at checkout.

- rating | DecimalField

    Maintains a calculated average rating value updated by customer feedback, providing reliable social proof directly on the product catalogue.

- image_url | URLField

    Stores an optional absolute web address linking to externally hosted product imagery (AWS), offering flexibility in content delivery network asset management.

- image | ImageField

    Facilitates direct administrative file uploads to store high-resolution product imagery within the application's media storage structures.

- stock_level | IntegerField

    Tracks the real-time numerical quantity of the product available in inventory, driving automated stock status flags and preventing overselling at checkout.

##### Order | [ERD](PLACEHOLDER)

The bespoke Order model serves as the primary data ledger for capturing and finalizing all e-commerce transactions on the platform. Upon a successful checkout, the model automatically generates a unique, permanent tracking number, tallies purchasing metrics, and calculates delivery costs and grand totals. This transactional snapshot is securely bound to the user's account, allowing them to instantly access their purchase history via their profile dashboard, while safely holding independent delivery address details specifically for that shipment.

- order_number | CharField

    Automatically generates a unique, permanent alphanumeric string that serves as the primary reference key for tracking and managing the transaction.

- user_profile | ForeignKey

    Establishes a relational link to the UserProfile model, mapping the completed invoice directly to the customer's account dashboard while allowing for guest checkouts if left blank.

- full_name | CharField

    Captures the complete name of the recipient intended for the shipping label to ensure accurate courier delivery.

- email | EmailField

    Records the buyer's contact email address, which is utilized by the system to dispatch automated purchase confirmations and tracking updates.

- phone_number | CharField

    Stores the recipient's telephone number, providing logistics partners with a direct line of contact for delivery notifications or shipping updates.

- country | CountryField

    Utilises a standardized country field to record the destination nation, ensuring accurate tax calculation and international shipping compliance.

- postcode | CharField

    Captures the alphanumeric postal or ZIP code required to calculate accurate shipping and validate geographical delivery data.

- town_or_city | CharField

    Records the specific city or town destination required for accurate parcel sorting and distribution.

- street_address1 | CharField

    Stores the mandatory primary line of the delivery address, typically capturing the house number, building name, or street details.

- street_address2 | CharField

    An optional field used to provide supplementary delivery details, such as apartment numbers, suite identifiers, or specific unit drop points.

- county | CharField

    An optional field used to capture regional county or state designations to ensure geographic alignment for domestic deliveries.

- date | DateTimeField

    Automatically timestamps the exact moment the transaction is successfully completed, establishing a reliable chronological timeline for order fulfillment.

- delivery_cost | DecimalField

    Records the calculated cost of shipping for the transaction based on basket values, using decimal formatting.

- order_total | DecimalField

    Maintains a fixed-precision decimal tally of the cumulative cost of all items in the order before shipping charges are applied.

- grand_total | DecimalField

    Combines the order_total and delivery_cost fields into a definitive final figure representing the absolute total billed amount.

- original_bag | TextField

    Stores a serialized text string representing the exact structure of the user's shopping cart at the moment of checkout, acting as a crucial backup ledger.

- stripe_pid | CharField

    Records the unique payment intent identifier generated by the Stripe API, securely linking the local database order directly to the processed financial transaction.

##### OrderLineItem | [ERD](PLACEHOLDER)

The bespoke OrderLineItem model acts as an essential intermediary mapping table that tracks individual products and their specific quantities within a single, broader transaction. By establishing relationships between the Order and Product models, this data architecture breaks down a large order into distinct, row-by-row line items. This precise structural layout is what enables the system to dynamically compile and render historical user profile orders.

- order | ForeignKey

    Establishes a relational link back to the main Order model, grouping individual purchased items securely under a single order number.

- product | ForeignKey

    Creates a direct reference to the specific entry in the Product model, capturing all relevant details of the item selected by the customer.

- volume_ordered | ForeignKey

    References the chosen size variation from the Product model, ensuring that the specific bottle volume selected at the time of purchase is accurately recorded.

- quantity | IntegerField

    Stores the exact numerical count of this specific item ordered by the customer, which is used to manage stock subtraction and calculate pricing totals.

- line_item_total | DecimalField

    Maintains a fixed-precision decimal calculation of the subtotal for this specific row, automatically multiplying the product's unit price by the quantity ordered.

##### FlavourSandbox | [ERD](PLACEHOLDER)

The bespoke FlavourSandbox model functions as the data foundation for the platform's interactive community hub, letting authenticated users submit and pitch their own unique mead recipes or flavor ideas. It captures user concepts systematically, structuring raw text submissions alongside specific product categorizations like honey varietals and target flavour profiles. To ensure the storefront remains safe and aligned with brand guidelines, the model includes a built-in moderation gate, allowing administrators to review and approve community ideas before they are dynamically published to the public feed.

- user | ForeignKey

    Links the flavor concept directly to the authenticated standard Django User model, identifying the specific community creator while maintaining referential integrity if an account is managed.

- title | CharField

    Captures the distinct, creative name of the user-submitted mead concept, limited to a standard character length for clean layout headings on the community board.

- addition | CharField

    Stores a text string detailing any supplementary ingredients, fruits, or spices the user proposes adding to their mead recipe (such as vanilla, berries, or oak chips).

- flavour_profile | ForeignKey

    Establishes a relational link to existing categories within the Product model, allowing the community pitch to be mapped against established taste classifications.

- honey | ForeignKey

    References the predefined honey choices in the Product model, enabling the user to select the authentic, specific botanical honey base required for their creation.

- content | TextField

    Provides an unrestricted text area where the creator can elaborate on their brewing vision, explain their inspiration, or write detailed tasting notes for the community.

- approved | BooleanField

    Acts as a crucial administrative moderation flag that defaults to false, preventing user submissions from appearing live on the platform until a site superuser explicitly reviews and approves the content.

- likes | ManyToManyField

    Establishes a many-to-many relationship with the standard Django User model, enabling authenticated members to upvote or "like" their favourite concepts while tracking engagement data to power popularity sorting.

##### SandboxComment | [ERD](PLACEHOLDER)

The bespoke SandboxComment model works in tandem with the FlavourSandbox architecture to provide an interactive, structured discussion space beneath each user-submitted recipe concept. To cultivate deep community engagement, the database schema supports multi-layered conversation threads, allowing users to converse dynamically. Additionally, the model utilizes internal metadata rules to automatically sort the discussion layout chronologically, ensuring that the conversational timeline flows naturally for readers.

- sandbox_post | ForeignKey

    Establishes a relational link back to the parent FlavourSandbox model, ensuring each comment is anchored securely to its corresponding community pitch.

- user | ForeignKey

    Maps the comment directly to the standard Django User model, identifying the contributing member while tracking community authorship across the board.

- body | TextField

    Provides an expansive, flexible text area that handles the raw text input of the user's feedback, question, or review.

- approved | BooleanField

    Functions as a defensive administrative moderation switch, requiring site superusers to verify and approve the text before it is published live to the platform.

- created_on | DateTimeField

    Automatically applies a high-precision timestamp the exact moment a comment is submitted, driving the chronological sorting order of the thread.

- parent | ForeignKey ('self')

    Utilises a self-referential relationship to link a comment back to another comment, enabling the platform to render cleanly nested, direct replies to individual responses.

---

### Skeleton Plane

#### Wireframes

The initial layout and structural blueprint of the platform were designed using [Canva's Online Wireframe Tool](https://www.canva.com/online-whiteboard/wireframes/). These wireframes served as an essential visual guide, defining the foundational information architecture and user flow across every page before any front-end development began.

Adhering to a mobile-first philosophy, each interface was systematically drafted across multiple viewport breakpoints—specifically tailored for mobile, tablet, and desktop screens. This proactive planning phase ensured that cross-device scalability, component positioning, and user experience (UX) responsiveness were deeply embedded into the platform's core design from the outset.

The conceptual wireframes for each page layout are presented below:

- **Home Page** | [View](PLACEHOLDER)
- **Products** | [View](PLACEHOLDER)
- **Flavour Sanbox** | [View](PLACEHOLDER)
- **Basket** | [View](PLACEHOLDER)

### Surface Plane

The architecture and visual identity of the Óðrerir Meadery platform are heavily inspired by two core themes: the honeybee—the vital catalyst in mead production—and Norse mythology, the historical culture intimately tied to the legendary heritage of honey wine. Every design element, from the typography to the curated colour palette, was intentionally selected to reflect these thematic roots. Crucially, this aesthetic is balanced with strict UX design principles, ensuring a seamless user journey that guides visitors effortlessly from discovery to conversion, ultimately driving sales and fostering long-term customer loyalty.
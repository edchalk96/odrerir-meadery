# Database Schema

## *User*

The platform utilizes the standard Django User model in tandem with the Django-Allauth package to securely manage user registration, authentication, and session states (logging in and out). To ensure data integrity and establish a secure shopping environment, email verification is configured as a mandatory requirement upon account creation. When a new user registers, an automated verification email is dispatched to their provided address. The user must successfully verify their email before the system grants authorization to sign in, complete commercial transactions, or actively participate in the community Flavour Sandbox. This strict authentication gate protects the platform from automated spam accounts while ensuring a verified user base for community interactions.

- username | Charfield

    Utilises Django's native validation to enforce database uniqueness with a maximum limit of 150 characters. This required field accepts alphanumeric characters alongside underscores (_), at symbols (@), plus signs (+), periods (.), and hyphens (-) during account creation.

- email | EmailField

    Leverages Django's built-in email format validation to ensure syntactic accuracy. This field is explicitly configured as a mandatory requirement within the application settings to facilitate the mandatory account verification process.

- password | CharField

    Enforces Django's core password hashing and validation security standards. To prevent input errors and align with secure authentication protocols, the default Django-Allauth signup flow requires users to input their chosen password twice to confirm accuracy.

## UserProfile | [ERD](./documentation/images/user-profile-erd.png)

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

## Product | [ERD](./documentation/images/product-erd.png)

The bespoke Product model serves as the central database repository for the digital storefront, storing comprehensive commercial data and structural inventory metadata for every item in the meadery's catalogue. Beyond standard e-commerce attributes like pricing and stock levels, this model incorporates dedicated fields to classify items by their specific mead type and distinct flavour profile. By structuring these granular data points at the database level, the platform can efficiently power front-end query filtering and sorting algorithms, enabling users to navigate the digital storefront seamlessly based on their taste preferences and honey-wine styles.

- sku | CharField

    Stores a unique Stock Keeping Unit (SKU) code for each item, acting as a primary alphanumeric identifier to ensure precise inventory tracking and product management.

- name | CharField

    Captures the commercial name of the specific product, configured with a character limit suitable for clean display titles across the digital storefront.

- mead_type | CharField

    Utilises a predefined list of choices to classify the product by its specific traditional or historical honey-wine category, enabling accurate front-end catalogue filtering.

- ingredients | ArrayField

    Stores a flexible list of text strings detailing the raw ingredients used in the brew, allowing for clean, dynamic rendering of component lists on the product page.

- description | TextField

    Provides a flexible text field for comprehensive product narratives, tasting notes, and ingredient breakdowns to fully inform prospective buyers.

abv | DecimalField

    Records the Alcohol By Volume percentage of the mead using a fixed-precision decimal, ensuring exact legal and consumer compliance formatting (e.g., 14.5%).

- price | DecimalField

    Records the retail price of the item using a fixed-precision decimal format, ensuring financial accuracy and consistent currency rendering at checkout.

- image_url | URLField

    Stores an optional absolute web address linking to externally hosted product imagery (AWS), offering flexibility in content delivery network asset management.

- image | ImageField

    Facilitates direct administrative file uploads to store high-resolution product imagery within the application's media storage structures.

- stock_level | IntegerField

    Tracks the real-time numerical quantity of the product available in inventory, driving automated stock status flags and preventing overselling at checkout.

- clearance | BooleanField

    Functions as an administrative toggle to mark specific items for stock liquidation, enabling the system to dynamically apply discount badging or filter products into a dedicated clearance section.

- most_popular | BooleanField

    Acts as a manual flag for site administrators to highlight high-selling or trending items, pushing them to prominent positions like homepage feature sections or top-tier catalog sorting.

## Order | [ERD](./documentation/images/order-erd.png)

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

## OrderLineItem | [ERD](./documentation/images/order-line-item-erd.png)

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

## FlavourSandbox | [ERD](./documentation/images/flavour-sandbox-erd.png)

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

## SandboxComment | [ERD](./documentation/images/sandbox-comment-erd.png)

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

Overview:
eKart is a comprehensive e-commerce platform developed using Python and Django, designed to provide a seamless shopping experience for users. The platform incorporates robust user authentication, a secure payment gateway, and automated email notifications upon order placement. Leveraging MySQL for the database backend and HTML/CSS for the front-end design, eKart ensures a reliable and user-friendly interface for online shopping.

Key Features:

1. User Authentication:
   - Registration and Login: Users can create an account or log in to their existing accounts securely. The registration process includes email verification to ensure the validity of user credentials.
   - Password Management: Secure password storage using hashing, with options for password reset via email.

2. Product Browsing and Search:
   - Product Catalog: Browse a wide range of products categorized systematically. Each product listing includes detailed descriptions, images, and pricing information.
   - Search Functionality: Advanced search options to find products quickly using keywords, categories, or filters.

3. Shopping Cart:
   - Add to Cart: Users can add products to their shopping cart and review their selections before proceeding to checkout.
   - Cart Management: Update quantities, remove items, and view the total cost dynamically.

4. Payment Integration:
   - Secure Checkout: Integration with popular payment gateways to facilitate secure online transactions.
   - Order Summary: Before finalizing the purchase, users receive a detailed order summary with all pertinent information.

5. Order Management:
   - Order Confirmation: Upon successful payment, users receive an order confirmation email detailing the order information and expected delivery date.
   - Order Tracking: Users can track the status of their orders through their account dashboard.

6. Email Notifications:
   - Order Confirmation Email: Automated emails sent to users confirming their order details immediately after the purchase.
   - Account Notifications: Emails for account-related activities such as password changes or updates to personal information.

Technologies Used:

- Backend:
  - Python: The core programming language used for developing the application logic.
  - Django: A high-level Python web framework that enables rapid development and clean, pragmatic design.
  - MySQL: A relational database management system for storing user data, product information, and order details.

- Frontend:
  - HTML/CSS: The foundational technologies for structuring and styling the web pages, ensuring a responsive and visually appealing user interface.

Technical Architecture:

- Django Models: Define the database schema for users, products, orders, and other entities.
- Views and Templates: Handle the rendering of web pages and manage user interactions with the application.
- Forms and Validation: Secure and validate user input for forms, including registration, login, and checkout processes.
- Email Backend: Configure Django’s email backend to send automated emails using SMTP.


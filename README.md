Blog Website Mini Project
A robust, full-functional blog application built with Django, focusing on clean architecture, relational database management, and structured CRUD operations. 

This project was developed with a backend-first philosophy to demonstrate data integrity and scalable system design.
Backend ArchitectureThis project is built with a backend-first approach, prioritizing modularity and efficient data handling. 
Key technical highlights include:
Relational Data Modeling:
Implemented clear ForeignKey relationships between User, Blog, and Favblog models to manage user-specific data and content associations. 
Structured CRUD Operations: 
Built a complete cycle for blog management (Create, Read, Update, Delete) using both Django Class-Based Views and function-based views for flexible logic handling. 
Scalable Routing: Utilized a clean URL configuration pattern that separates blog, authentication, and favorite management paths for better maintainability.
Dynamic Data Rendering:
Developed robust view logic to handle server-side rendering of database objects into templates. 
Core FeaturesBlog Management:
Full CRUD functionality allowing users to create, view, edit, and delete blog content.  Interactive Favorites System: Logic-heavy "Add to Favorites" feature that links user profiles to specific blog entries, demonstrating mastery of many-to-one relationships.
User Authentication: 
Integrated with Django's contrib.auth system to manage user identity and profile-specific data interactions.




Installation
Clone the repository:

Bash
git clone https://github.com/chetzz-devop/Blog-fullfunctional-Backend-Miniproject.git
cd Blog-fullfunctional-Backend-Miniproject
Code snippet

2.  **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
```[cite: 1]

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
```[cite: 1]

4.  **Apply migrations**:
    ```bash
python manage.py migrate
```[cite: 1]

5.  **Start the development server**:
    ```bash
python manage.py runserver
```[cite: 1]

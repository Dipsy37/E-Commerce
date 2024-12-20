# E-Commerce Site

This is a simple e-commerce site built with Django.

## Project Structure

wsgi.py
manage.py
README.md
store/
    __init__.py
    __pycache__/
    admin.py
    apps.py
    migrations/
        __init__.py
        __pycache__/
        0001_initial.py
    models.py
    static/
        store/
            styles.css
    templates/
        store/
            customer_list.html
            order_list.html
    
    
    views.py
    wsgi.py
manage.py
README.md
store/
    __init__.py
    __pycache__/
    admin.py
    apps.py
    migrations/
        __init__.py
        __pycache__/
        0001_initial.py
    models.py
    static/
        store/
            styles.css
    templates/
        store/
            customer_list.html
            order_list.html
    
    
    views.py

    ## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Dipsy37/E-Commerce.git
    cd ecommerce
    ```
2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate/ps1  
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```
5. Run the development server:
    ```sh
    python manage.py runserver
    ```
6. Open your browser and go to `http://127.0.0.1:8000/` to see the site.

## Project Details

### URLs

- The main URLs are defined in [ecommerce/urls.py](ecommerce/ecommerce/urls.py).
- The store app URLs are defined in [store/urls.py](ecommerce/store/urls.py).

## Views

- The views for the store app are defined in [store/views.py](ecommerce/store/views.py).

### Templates

- The templates for the store app are located in [store/templates/store/](ecommerce/store/templates/store/).

### Static Files

- The static files for the store app are located in [store/static/store/](ecommerce/store/static/store/).
### Tests

- The tests for the store app are defined in [store/tests.py](ecommerce/store/tests.py).


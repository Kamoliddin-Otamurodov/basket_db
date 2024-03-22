# basket_db
# Basketball Players Database (basket_db)

Basket_DB is a project that serves as a basketball players database implemented using Django Rest Framework (DRF). It allows users to perform various CRUD (Create, Read, Update, Delete) operations on basketball players data through a RESTful API.

## Features

- Create, retrieve, update, and delete basketball player records
- Perform CRUD operations on player data via a RESTful API
- Utilizes Django Rest Framework for building the API endpoints
- Provides authentication and authorization mechanisms for secure access

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Kamoliddin-Otamurodov/basket_db.git
   ```

2. Navigate to the project directory:

   ```bash
   cd basket_db
   ```

3. Change to the core directory (if your project structure requires it):

   ```bash
   cd core
   ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Perform Django database migrations:

   ```bash
   python manage.py migrate
   ```

## Usage

1. Start the Django development server:

   ```bash
   python manage.py runserver
   ```

2. Access the API endpoints through your preferred HTTP client (e.g., browser, curl, Postman, etc.):

   - To view the list of available API endpoints and interact with the basketball players data, navigate to `http://127.0.0.1:8000/players/`.
   - Perform CRUD operations using appropriate HTTP methods (GET, POST, PUT, DELETE) on the API endpoints.

## Authentication and Authorization

- The API endpoints may require authentication and authorization for certain operations.
- By default, DRF provides session authentication and token authentication. Ensure you are authenticated with valid credentials to access restricted endpoints.

## Dependencies

- Python 3.x
- Django
- Django Rest Framework

## Contributing

Contributions are welcome! If you would like to contribute to this project, please feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

- [Kamoliddin Otamurodov](https://github.com/Kamoliddin-Otamurodov)

## Acknowledgments

Special thanks to all contributors and anyone who uses this project! Your feedback and suggestions are appreciated.
# 📚 Book Shop API

A simple Book Shop REST API built with **FastAPI**, **SQLAlchemy**, **Pydantic**, and **JWT authentication**.

This project was built as a learning project to practice backend development with Python and FastAPI.

---

## 🚀 Features

- 📚 Book CRUD operations
- 👤 User registration
- 🔐 User login
- 🎟️ JWT authentication
- 🔑 Password hashing with Argon2
- 📦 Pydantic request and response validation
- 🗄️ SQLite database
- 🧩 SQLAlchemy ORM
- 📖 Automatic API documentation with Swagger UI

---

## 🛠️ Technologies

- Python
- FastAPI
- Uvicorn
- SQLAlchemy
- Pydantic
- SQLite
- PyJWT
- pwdlib
- Argon2

---

## 📁 Project Structure

```text
book_shop/
│
├── app/
│   │
│   ├── books/
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── service.py
│   │
│   ├── users/
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── service.py
│   │
│   ├── core/
│   │   ├── deps.py
│   │   └── security.py
│   │
│   ├── database.py
│   └── main.py
│
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/siyametj/book_shop_api.git
```

Move into the project:

```bash
cd book_shop_api
```

Create a virtual environment:

```bash
python3 -m venv venv
```

Activate it:

### Linux / macOS

```bash
source venv/bin/activate
```

### Windows

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the API

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## 📖 API Documentation

FastAPI automatically provides interactive API documentation.

### Swagger UI

```text
http://127.0.0.1:8000/docs
```

### ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

## 📚 Book API

The API provides endpoints for managing books.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | Get all books |
| GET | `/books/{book_id}` | Get a specific book |
| POST | `/books/` | Create a book |
| PUT | `/books/{book_id}` | Update a book |
| DELETE | `/books/{book_id}` | Delete a book |

---

## 👤 Authentication API

The API also provides user authentication.

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register a new user |
| POST | `/auth/login` | Login and receive an access token |

Authentication uses **JWT access tokens**.

---

## 🗄️ Database

The project currently uses **SQLite** as the database.

SQLAlchemy is used as the ORM for database operations.

The database tables are created when the application starts.

---

## 🔐 Authentication

Passwords are hashed before being stored in the database.

The project uses:

- Argon2 for password hashing
- JWT for authentication tokens

---

## 🎯 Project Goal

The main goal of this project is to learn and practice:

- FastAPI
- REST API development
- HTTP methods
- Path parameters
- Query parameters
- Request and response models
- Pydantic validation
- Database integration
- Authentication
- JWT
- Password hashing
- API architecture

---

## 📌 Status

🚧 Learning project

The project is still under development and may receive new features and improvements.

---

## 👨‍💻 Author

**Siyam**

GitHub:

https://github.com/siyametj

---

## 📄 License

This project is licensed under the MIT License.

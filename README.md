# 🛒 Store Management REST API

A modern, high-performance RESTful API built with **FastAPI**, **SQLAlchemy**, and **SQLite** for managing e-commerce store products.

---

## ✨ Features

- **Full CRUD Operations**:
  - `POST /products`: Create a new product.
  - `GET /products`: Retrieve all existing products.
  - `GET /products/{product_id}`: Retrieve a single product by ID.
  - `PUT /products/{product_id}`: Update an existing product.
  - `DELETE /products/{product_id}`: Remove a product from the database.
- **Data Validation & Serialization**: Managed using Pydantic models.
- **Persistent Storage**: ORM database layer backed by SQLite (`store.db`) using SQLAlchemy.
- **Automated API Documentation**: Interactive OpenAPI documentation provided via Swagger UI and ReDoc.

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **Framework**: FastAPI
- **Server**: Uvicorn (ASGI)
- **ORM**: SQLAlchemy
- **Database**: SQLite
- **Validation**: Pydantic

---

## 📂 Project Structure

```text
├── database.py       # Engine initialization and database session dependency (get_db)
├── models.py         # SQLAlchemy ORM database models
├── main.py           # FastAPI application routes, endpoints, and Pydantic schemas
├── store.db          # Local SQLite database file (generated automatically, git-ignored)
├── .gitignore        # Ignored files (virtual environments, database, cache)
└── README.md         # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Set up a virtual environment (Recommended)

- **Windows**:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- **macOS / Linux**:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy
```

### 4. Run the development server

```bash
uvicorn main:app --reload
```

The API server will run at: `http://127.0.0.1:8000`

---

## 📖 API Documentation

Once the server is running, explore the interactive documentation:

- **Swagger UI (Interactive Docs)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔌 API Endpoints Summary

| Method   | Endpoint                 | Description                       |
| :------- | :----------------------- | :-------------------------------- |
| `POST`   | `/products`              | Create a new product              |
| `GET`    | `/products`              | Retrieve all products             |
| `GET`    | `/products/{product_id}` | Retrieve a specific product by ID |
| `PUT`    | `/products/{product_id}` | Update product details            |
| `DELETE` | `/products/{product_id}` | Delete a product                  |

### Example Product Payload (`POST` / `PUT`)

```json
{
  "name": "Wireless Mechanical Keyboard",
  "price": 89.99,
  "description": "RGB backlit wireless mechanical keyboard with blue switches",
  "stock": 15
}
```

### Example Successful Response

```json
{
  "message": "Product created successfully",
  "product": {
    "id": 1,
    "name": "Wireless Mechanical Keyboard",
    "price": 89.99,
    "description": "RGB backlit wireless mechanical keyboard with blue switches",
    "stock": 15
  }
}
```

---

## 📦 Dependencies

To install all the required packages at once, run:

```bash
pip install -r requirements.txt
```

# 📚 Book Shop API

A RESTful API for managing a book shop, including books inventory, orders, and customer management.

## Features

- 📖 Book Management (Create, Read, Update, Delete)
- 🛒 Shopping Cart & Orders
- 👥 User Management & Authentication
- 📊 Inventory Tracking
- 💳 Payment Integration

## Getting Started

### Prerequisites

- Node.js
- npm or yarn
- Database (MongoDB/PostgreSQL)

### Installation

```bash
git clone https://github.com/siyametj/book_shop_api.git
cd book_shop_api
npm install
```

### Configuration

Create a `.env` file in the root directory:

```env
PORT=3000
DATABASE_URL=your_database_url
JWT_SECRET=your_secret_key
```

### Running the API

```bash
npm start
```

The API will be available at `http://localhost:3000`

## API Endpoints

### Books
- `GET /api/books` - Get all books
- `GET /api/books/:id` - Get book by ID
- `POST /api/books` - Create new book
- `PUT /api/books/:id` - Update book
- `DELETE /api/books/:id` - Delete book

### Orders
- `GET /api/orders` - Get all orders
- `POST /api/orders` - Create new order
- `GET /api/orders/:id` - Get order by ID

### Users
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - User login
- `GET /api/users/:id` - Get user profile

## Technologies Used

- **Backend**: Node.js, Express.js
- **Database**: MongoDB
- **Authentication**: JWT
- **Validation**: Joi

## License

MIT License - See LICENSE file for details

## Author

**siyametj**

---

Feel free to customize this README with your specific details!

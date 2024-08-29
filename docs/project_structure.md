## Key Principles for Structuring Projects
### In building FastAPI applications, it’s crucial to follow these best practices:

- **Separation of Concerns:**
Separate different aspects of your FastAPI project, such as routes, models, and business logic, for clarity and maintainability.

- **Modularization:**
Break down your FastAPI application into reusable modules to promote code reusability and organization.

- **Dependency Injection:**
Decouple components by implementing dependency injection, which allows for more flexible and testable code in FastAPI using libraries like fastapi.Dependencies.

- **Testability:**
Prioritize writing testable code in FastAPI applications by employing strategies like dependency injection and mocking to ensure robust testing and quality assurance.

---

### Structuring Format

1. **Structuring based on File-Type:**
In this approach, files are organized by type (e.g., API, CRUD, models, schemas, routers) as represented by FastAPI itself.
*This structure is more suitable for microservices or projects with fewer scopes:*

2. *Structuring based on Module-Functionality:*

    We organize our files based on package functionality for example authentication sub-package, users sub-package.

    The module-functionality structure is better suited for _monolithic projects_ containing numerous domains and modules. By grouping all file types required by a single sub-package, it improves development efficiency.
    This structure is suggested by the [fastapi-best-practices](https://github.com/zhanymkanov/fastapi-best-practices) GitHub repository (8.4k ⭐).
    In this structure, Each package has its own router, schemas, models, etc.

### Our Choice:
As we are developing a secure authentication and authorization system, we assume that this is a microservice, and we will not make it scalable monolithic adding other business logics. If needed, we will make another service depending upon the business. for now the focus is entirely on Authentication, Authorization and security with high performance.
therefore we opt <span style="color: yellow ;">**_File-Type Structure_.**</span>

```
Authapp
├── app/
│   ├── __init__.py
│   ├── main.py                # Main FastAPI application
│   ├── dependencies.py        # Dependency injection functions
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── auth.py            # Authentication-related routes
│   │   ├── users.py           # User-related routes
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py            # User model
│   │   ├── token.py           # Token model
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py            # Pydantic models for user-related data
│   │   ├── token.py           # Pydantic models for token-related data
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth.py            # Authentication and authorization logic
│   │   ├── user.py            # Business logic related to users
│   ├── db/
│   │   ├── __init__.py        # Database initialization and connection
│   │   ├── database.py        # Database session and engine configuration
│   ├── internal/
│   │   ├── __init__.py
│   │   ├── admin.py           # Internal admin utilities and routes
├── docs/
│   ├── README.md                  # Project documentation
├── env/
│   ├── .env.dev               # Development environment variables
│   ├── .env.prod              # Production environment variables
│   ├── .env.local             # Local environment variables
├── requirements/
│   ├── base.txt               # Base dependencies
│   ├── local.txt              # Development-specific dependencies
│   ├── prod.txt               # Production-specific dependencies
├── alembic/
│   ├── env.py                 # Alembic environment configuration
│   ├── README                 # Alembic README file
│   ├── versions/              # Database migration scripts
│   │   ├── 1234_init.py       # Initial migration script
├── alembic.ini                # Alembic configuration file

```

### ORM Selection:
We could use ORMAR because.
- getting an async ORM that can be used with async frameworks (fastapi, starlette etc.)
- getting just one model to maintain - you don't have to maintain pydantic and other orm models (sqlalchemy, peewee, gino etc.)

### Ormar is built with:
- sqlalchemy core for query building.
- databases for cross-database async support.
- pydantic for data validation.

But we are going with SqlAlchemy because its feature rich and mature.
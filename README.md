# Task Manager - PostgreSQL Project

## Features
-  Create tasks
-  List all tasks
-  Update task status
-  Delete tasks
-  Search tasks

## Prerequisites
- Python 3.8+
- PostgreSQL 12+
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/arthiccc/task-manager-postgres.git
cd task-manager-postgres
```
2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
```
4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your database credentials
```
5. Create database and run migrations:
```bash
chmod +x scripts/setup.sh
./scripts/setup.sh
```
## Usage
Run the application:
```bash
python scripts/run.py
```

Commands:
- `1` - Add a new task
- `2` - List all tasks
- `3` - Update task status
- `4` - Delete a task
- `5` - Search tasks
- `6` - Exit

## Database Schema
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    status VARCHAR(20) DEFAULT 'pending',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
## Project Structure
```bash
├── config/         # Database configuration
├── db/             # SQL schema and seed files
├── src/            # Application source code
└── scripts/        # Setup and run scripts
```
## License
MIT License - see LICENSE file for details.




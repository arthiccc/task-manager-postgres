from config.database import Database
from tabulate import tabulate

class TaskManager:
    def __init__(self):
        self.db = Database()
        self.db.connect()

    def add_task(self, title, description, status='pending'):
        """Add a new task"""
        query = """
            INSERT INTO tasks (title, description, status)
            VALUES (%s, %s, %s)
            RETURNING id, title, created_at
        """
        result = self.db.execute_query(query, (title, description, status))
        print(f"✅ Task created successfully! ID: {result[0]['id']}")
        return result[0]

    def list_tasks(self):
        """List all tasks"""
        query = """
            SELECT id, title, description, status, 
                   created_at, updated_at
            FROM tasks
            ORDER BY created_at DESC
        """
        tasks = self.db.execute_query(query)
        
        if not tasks:
            print("No tasks found.")
            return
        
        table_data = [
            [
                task['id'],
                task['title'][:30],
                task['status'],
                task['created_at'].strftime('%Y-%m-%d %H:%M')
            ]
            for task in tasks
        ]
        
        print("\n" + tabulate(
            table_data,
            headers=['ID', 'Title', 'Status', 'Created'],
            tablefmt='grid'
        ))

    def update_status(self, task_id, new_status):
        """Update task status"""
        query = """
            UPDATE tasks
            SET status = %s
            WHERE id = %s
            RETURNING id, title, status
        """
        result = self.db.execute_query(query, (new_status, task_id))
        
        if result:
            print(f"✅ Task {task_id} updated to '{new_status}'")
        else:
            print(f"❌ Task {task_id} not found")

    def delete_task(self, task_id):
        """Delete a task"""
        query = "DELETE FROM tasks WHERE id = %s RETURNING id"
        result = self.db.execute_query(query, (task_id,))
        
        if result:
            print(f"✅ Task {task_id} deleted successfully")
        else:
            print(f"❌ Task {task_id} not found")

    def search_tasks(self, keyword):
        """Search tasks by keyword"""
        query = """
            SELECT id, title, description, status
            FROM tasks
            WHERE title ILIKE %s OR description ILIKE %s
        """
        tasks = self.db.execute_query(query, (f'%{keyword}%', f'%{keyword}%'))
        
        if not tasks:
            print(f"No tasks found matching '{keyword}'")
            return
        
        for task in tasks:
            print(f"\nID: {task['id']}")
            print(f"Title: {task['title']}")
            print(f"Description: {task['description']}")
            print(f"Status: {task['status']}")
            print("-" * 50)

    def close(self):
        """Close database connection"""
        self.db.disconnect()

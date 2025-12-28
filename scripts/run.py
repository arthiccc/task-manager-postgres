#!/usr/bin/env python3

import sys
from src.task_manager import TaskManager

def print_menu():
    print("\n" + "="*50)
    print("📝 TASK MANAGER")
    print("="*50)
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Update task status")
    print("4. Delete a task")
    print("5. Search tasks")
    print("6. Exit")
    print("="*50)

def main():
    tm = TaskManager()
    
    try:
        while True:
            print_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                title = input("Task title: ").strip()
                description = input("Description: ").strip()
                status = input("Status (pending/in_progress/completed) [pending]: ").strip() or 'pending'
                tm.add_task(title, description, status)
                
            elif choice == '2':
                tm.list_tasks()
                
            elif choice == '3':
                task_id = int(input("Enter task ID: "))
                new_status = input("New status (pending/in_progress/completed): ").strip()
                tm.update_status(task_id, new_status)
                
            elif choice == '4':
                task_id = int(input("Enter task ID to delete: "))
                confirm = input(f"Are you sure you want to delete task {task_id}? (yes/no): ")
                if confirm.lower() == 'yes':
                    tm.delete_task(task_id)
                    
            elif choice == '5':
                keyword = input("Enter search keyword: ").strip()
                tm.search_tasks(keyword)
                
            elif choice == '6':
                print("\n👋 Goodbye!")
                break
                
            else:
                print("❌ Invalid choice. Please try again.")
                
    except KeyboardInterrupt:
        print("\n\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        tm.close()

if __name__ == "__main__":
    main()

import sqlite3

class DatabaseConnection:
    """Context manager for database connections"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        """Open database connection"""
        self.connection = sqlite3.connect(self.db_name)
        return self.connection
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Close database connection"""
        if self.connection:
            self.connection.close()
        return False

# Example usage
if __name__ == "__main__":
    # Use the context manager to query the database
    with DatabaseConnection('users.db') as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users')
        results = cursor.fetchall()
        for row in results:
            print(row)

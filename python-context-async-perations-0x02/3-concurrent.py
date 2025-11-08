import asyncio
import aiosqlite

# Async function to fetch all users
async def async_fetch_users():
    """Fetch all users from the database asynchronously"""
    async with aiosqlite.connect('users.db') as db:
        async with db.execute('SELECT * FROM users') as cursor:
            results = await cursor.fetchall()
            print("All users:")
            for row in results:
                print(row)
            return results

# Async function to fetch users older than 40
async def async_fetch_older_users():
    """Fetch users older than 40 from the database asynchronously"""
    async with aiosqlite.connect('users.db') as db:
        async with db.execute('SELECT * FROM users WHERE age > 40') as cursor:
            results = await cursor.fetchall()
            print("\nUsers older than 40:")
            for row in results:
                print(row)
            return results

# Function to run both queries concurrently
async def fetch_concurrently():
    """Execute both fetch operations concurrently using asyncio.gather"""
    # Use asyncio.gather to run both queries concurrently
    results = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    return results

# Main execution
if __name__ == "__main__":
    # Run the concurrent fetch
    asyncio.run(fetch_concurrently())

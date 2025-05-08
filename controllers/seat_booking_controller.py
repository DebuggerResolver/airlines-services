import asyncio
from utils.database_connector import DatabaseConnection

class SeatBookingStrategy:
    @staticmethod
    @staticmethod
    async def book_single_seat(username):
        conn =  DatabaseConnection()
        conn=await conn.get_connection_pool()
        update_query = '''
            WITH one_row AS (
                SELECT seat_id FROM seat
                WHERE user_name IS NULL
                ORDER BY seat_id
                for update skip locked
                LIMIT 1
            )
            UPDATE seat SET user_name = $1
            WHERE seat_id IN (SELECT seat_id FROM one_row)
        '''
        async with conn.acquire() as con:
            await con.execute(update_query, username)

    @staticmethod
    async def book_random_seats():
        tasks = [
            SeatBookingStrategy.book_single_seat(f'user_{i}')
            for i in range(1, 121)
        ]
        results = await asyncio.gather(*tasks, return_exceptions=True)

        for i, result in enumerate(results, 1):
            if isinstance(result, Exception):
                print(f"Task {i} raised an exception: {result}")


if __name__ == '__main__':
    asyncio.run(SeatBookingStrategy.book_random_seats())
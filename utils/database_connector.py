
import os
import logging
import asyncpg
from dotenv import load_dotenv
load_dotenv()  
logger=logging.getLogger("uvicorn")

class DatabaseConnection:
  def __init__(self):
    self.conn_pool=None
    
  async def create_connection_pool(self):
    try:
      self.conn_pool=await asyncpg.create_pool(
        dsn=os.getenv("DATABASE_URL"), min_size=1, max_size=10)
    except Exception as e:
      logger.info(f"Error creating connection pool: {e}")
      raise e
  
  async def get_connection_pool(self):
    if self.conn_pool is None:
      await self.create_connection_pool()
    return self.conn_pool
  
  async def close_connection_pool(self):
    if self.conn_pool is not None:
      try:
        await self.conn_pool.close()
      except Exception as e:
        logger.info(f"Error closing connection pool: {e}")
        raise e
      self.conn_pool=None
      logger.info("Connection pool closed successfully.")
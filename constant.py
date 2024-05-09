from dotenv import load_dotenv
import os


load_dotenv()

DEBUG : bool = False if os.getenv("ENVIRONMENT") == "production" else True
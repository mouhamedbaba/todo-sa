from dotenv import load_dotenv
import os



load_dotenv()

DEBUG : bool = False if os.getenv("ENVIRONMENT") == "production" else True


COLORS = [
    "#22C55E",
    "#3B82F6",
    "#EAB308",
   "#8B5CF6",
"#64748B",
 "#0F172A",
 "#000000",
"#22D3EE",
   "#EC4899",
 "#F97316"
 
    ]

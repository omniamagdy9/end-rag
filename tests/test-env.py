from dotenv import load_dotenv 
import os
from pathlib import Path

# env_path=Path(__file__).parent.parent /"data"/"raw"/".env"
# استخدم ال path  بالطريقة دي احسن من ان اجيبه من على pc from properties  علشان ميكونش  related only to me when i share it with someone else (the right approach to be absolute)
env_path=Path(__file__).parent.parent /".env"
load_dotenv() 
model=os.getenv("QWEN_MODEL")
print(f"QWEN_MODEL: {model}")
Recommended solution: Use Python 3.11
For your Generative AI Architect learning, I recommend keeping Python 3.15 installed and creating a separate environment with Python 3.11 for CrewAI.
Step 1 — Install Python 3.11
Download Python 3.11 from:
Python official downloadsDuring installation, select Add Python to PATH if available.
Step 2 — Check installed Python versions
Open Windows PowerShell or CMD and run:
py -0p


You should see something similar to:
-3.15  C:\...\Python315\python.exe
-3.11  C:\...\Python311\python.exe


Step 3 — Create a virtual environment
Navigate to your project folder and execute:
py -3.11 -m venv crewai_env


Activate the environment.

For CMD:
crewai_env\Scripts\activate.bat


For PowerShell:
.\crewai_env\Scripts\Activate.ps1


Step 4 — Upgrade pip
python -m pip install --upgrade pip setuptools wheel


Step 5 — Install CrewAI
python -m pip install --upgrade crewai crewai-tools


Step 6 — Verify installation
python --version
python -m pip show crewai
python -m pip show crewai-tools
python -m pip check


Expected Python version:
Python 3.11.x


If all packages install successfully, test importing CrewAI:
from crewai import Agent, Task, Crewprint("CrewAI installed successfully!")
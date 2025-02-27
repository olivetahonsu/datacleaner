# datacleaner
An interactive and intuitive tool for data cleaning in Python.

---

## Features 
✅ Detects and summarises missing values 📊  
✅ Interactive prompts for handling missing data ✨  
✅ Supports dropping or imputing missing values (mean, median, mode, custom fill) 🔄  
✅ Progress bars for long operations ⏳  
✅ Color-coded outputs using `rich` 🎨  
✅ Preview cleaned data before saving 👀  
✅ Export and clear logs for debugging 📝  

## Installation 
Here’s how you can install and use the **datacleaner** package.  

---

## 1. Installing via `pip` (Recommended)  
Users can install it using:  
```sh
pip install datacleaner
```
 
---

## 2. Installing from GitHub  
Users can install it directly from my GitHub repo:  
```sh
pip install git+https://github.com/olivetahonsu/datacleaner.git
```

---

## 3. Installing Manually (From Source Code)  
For users who want to clone the repository:  

### Step 1: Clone the repo  
```sh
git clone https://github.com/olivetahonsu/datacleaner.git
cd datacleaner
```

### Step 2: Create a virtual environment (Optional but recommended)  
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### Step 3: Install the package locally  
```sh
pip install .
```

---

## 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## 4. Usage

Once installed, users can run commands like:  

```sh
datacleaner check-missing data.csv
datacleaner clean data.csv
datacleaner export-logs logs_backup.log
datacleaner clear-logs
```

Check for missing values:  
```sh
python src/cli.py check-missing data.csv
```  

Clean data interactively:  
```sh
python src/cli.py clean data.csv
```  

Export logs:  
```sh
python src/cli.py export-logs logs_backup.log
```  

Clear logs:  
```sh
python src/cli.py clear-logs
```

## Contributions
Contributions are welcome! Feel free to submit issues and pull requests. 🚀  


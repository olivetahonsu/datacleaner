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
```sh
pip install -r requirements.txt
```

## Usage
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


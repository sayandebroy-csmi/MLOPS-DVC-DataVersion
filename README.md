# MLOPS-DVC-DataVersion

A hands-on project demonstrating **Data Versioning** using [DVC (Data Version Control)](https://dvc.org/) with a local S3-like remote storage.

## 📋 Overview

This repository showcases how to version your datasets alongside your code using DVC. It demonstrates:
- Initializing DVC in a Git repository
- Setting up a remote storage for data
- Tracking and versioning data files
- Switching between different data versions

## 🛠️ Prerequisites

- Python 3.x
- Git
- pip

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd MLOPS-DVC-DataVersion
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Project Setup Flow

### Step 1: Initialize the Project

```bash
# Create and add your code (mycode.py generates sample CSV data)
python mycode.py

# Commit initial code to Git
git add .
git commit -m "Initial commit with code"
git push
```

### Step 2: Initialize DVC

```bash
# Install DVC
pip install dvc

# Initialize DVC in the repository
dvc init
```
This creates `.dvc/` directory and `.dvcignore` file.

### Step 3: Configure Remote Storage

```bash
# Create a directory for local S3-like storage
mkdir -p s3

# Add the remote storage
dvc remote add -d myremote s3/
```

### Step 4: Track Data with DVC

```bash
# Stop Git from tracking the data folder
git rm -r --cached 'data'
git commit -m "Stop tracking data folder"

# Add data folder to DVC tracking
dvc add data/
```
This creates `data.dvc` - a small metadata file that Git tracks instead of the actual data.

### Step 5: Push Data to Remote

```bash
# Stage the DVC files for Git
git add .gitignore data.dvc

# Commit and push data to DVC remote
dvc commit
dvc push

# Commit changes to Git (v1 of data)
git add .
git commit -m "v1: Initial data version"
git push
```

## 🔄 Creating New Data Versions

### Version 2 & Beyond

1. **Modify your data** (update `mycode.py` to add new rows)

2. **Check what changed**
   ```bash
   dvc status
   ```

3. **Commit and push new version**
   ```bash
   dvc commit
   dvc push
   git add .
   git commit -m "v2: Added new data entries"
   git push
   ```

4. Repeat for subsequent versions (v3, v4, etc.)

## ⏪ Switching Between Data Versions

```bash
# View commit history
git log --oneline

# Checkout a specific version
git checkout <commit-hash>

# Pull the corresponding data version
dvc pull

# Return to latest version
git checkout master
dvc pull
```

## 📁 Project Structure

```
MLOPS-DVC-DataVersion/
├── data/                  # Data directory (tracked by DVC)
│   └── sample_data.csv
├── s3/                    # Local remote storage (simulates S3)
│   └── files/
├── .dvc/                  # DVC configuration
├── data.dvc               # DVC tracking file for data/
├── mycode.py              # Script to generate sample data
├── requirements.txt       # Python dependencies
├── projectflow.txt        # Step-by-step project flow
└── README.md
```

## 📊 Sample Data

The project uses a simple CSV with employee information:

| Name    | Age | City        |
|---------|-----|-------------|
| Alice   | 24  | New York    |
| Bob     | 30  | Los Angeles |
| Charlie | 22  | Chicago     |
| David   | 35  | Houston     |

New rows are added in each version to demonstrate data versioning.

## 🔗 Useful Commands

| Command | Description |
|---------|-------------|
| `dvc init` | Initialize DVC in a repository |
| `dvc add <path>` | Start tracking a file/folder |
| `dvc push` | Push data to remote storage |
| `dvc pull` | Pull data from remote storage |
| `dvc status` | Show changes in tracked data |
| `dvc commit` | Save current state of tracked data |

## 📚 Resources

- [DVC Documentation](https://dvc.org/doc)
- [DVC GitHub Repository](https://github.com/iterative/dvc)

## 📝 License

This project is for educational purposes.

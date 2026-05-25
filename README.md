# Insurance Risk Analytics

This project focuses on analyzing insurance risk using a modular data pipeline and version control.

## Data Pipeline & Versioning
This project uses **DVC (Data Version Control)** to manage datasets efficiently without bloating the Git repository.

### Prerequisites
- Install DVC: `pip install dvc`

### How to reproduce the data pipeline
1. **Clone the repository:** `git clone <repository-url>`
2. **Pull the tracked data:** Run the following command to download the data from the configured DVC remote:
   ```bash
   dvc pull
   

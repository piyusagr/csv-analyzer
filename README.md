
# CSV Analyzer

CSV Analyzer is a Django-based web application designed to analyze CSV files and generate statistical insights along with visualizations. This application processes numeric data and provides histogram plots for the uploaded dataset.

---

## Features

- Upload and analyze CSV files.
- Generate histograms for numeric columns.
- View and download plots in a user-friendly interface.
- Built-in error handling for invalid or missing files.

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8+ 
- Django 4.x
- Matplotlib 3.x

---

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/piyusagr/csv-analyzer.git
   cd csv-analyzer
   ```

2. **Set Up a Virtual Environment**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Settings**
   - Update the `settings.py` file to set up `MEDIA_ROOT` and `MEDIA_URL`:
     ```python
     MEDIA_ROOT = BASE_DIR / "media"
     MEDIA_URL = "/media/"
     ```
   - Ensure static files and media files are properly configured for your environment.

5. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

---

## Usage

1. **Run the Development Server**
   ```bash
   python manage.py runserver
   ```

2. **Access the Application**
   - Open your browser and navigate to: `http://127.0.0.1:8000/`.

3. **Upload and Analyze CSV Files**
   - Upload a CSV file containing numeric data.
   - The application will generate histograms for numeric columns.

---

## Example Directory Structure

```plaintext
csv-analyzer/
├── analysis/
│   ├── views.py
│   ├── models.py
├── media/
│   ├── Numeric_hist.png
│   ├── Numeric-2_hist.png
|   ├── Weekend_days.csv
├── csv_analyzer/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── templates/
│   ├── upload.html
│   ├── results.html
├── manage.py
├── requirements.txt
└── README.md
```

---

## Troubleshooting

1. **Media Files Not Found**
   - Ensure that `MEDIA_ROOT` and `MEDIA_URL` are correctly set in `settings.py`.
   - Verify that files are saved in the correct directory under `MEDIA_ROOT`.

2. **Matplotlib Warnings**
   - Add the following to disable GUI backends for Matplotlib:
     ```python
     import matplotlib
     matplotlib.use('Agg')
     ```

3. **Server Errors**
   - Check the server logs for detailed error messages.

---

## Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.


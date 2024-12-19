from django.shortcuts import render
from csv_analyzer.settings import MEDIA_ROOT, MEDIA_URL
from .forms import CSVUploadForm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import os
import re
from django.conf import settings  

def upload_file(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['file']
            file_path = os.path.join(settings.MEDIA_ROOT, csv_file.name)
            
            with open(file_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            # Read and process CSV
            df = pd.read_csv(file_path)
            context = analyze_csv(df, file_path)
            context['MEDIA_URL'] = settings.MEDIA_URL 
            return render(request, 'results.html', context)
    else:
        form = CSVUploadForm()
    return render(request, 'upload.html', {'form': form})


# def analyze_csv(df, file_path):


    # Basic analysis
    first_rows = df.head().to_html(classes='table table-bordered')
    summary_stats = df.describe().transpose().to_html(classes='table table-hover')

    # Handle missing values
    missing_summary = df.isnull().sum().to_frame(name='Missing Values').to_html(classes='table table-striped')

    # Visualization: Histogram for numerical columns
    numerical_cols = df.select_dtypes(include=['number']).columns
    plots = []
    for col in numerical_cols:
        # plt.figure()
        sns.histplot(df[col].dropna(), kde=True)
        plt.title(f'Histogram of {col}')
        
        # Sanitize column name for file path
        sanitized_col_name = re.sub(r'[^\w\-_\. ]', '_', col)  # Replace invalid characters with underscores
        plot_path = os.path.join(MEDIA_ROOT, f'{sanitized_col_name}_hist.png')
        
        plt.savefig(plot_path)
        plt.close()
        plots.append(os.path.relpath(plot_path, MEDIA_ROOT))

    return {
        'first_rows': first_rows,
        'summary_stats': summary_stats,
        'missing_summary': missing_summary,
        'plots': [os.path.join(MEDIA_URL, plot) for plot in plots]
    }

def analyze_csv(df, file_path):
    # Basic analysis
    first_rows = df.head().to_html(classes='table table-bordered')
    summary_stats = df.describe().transpose().to_html(classes='table table-hover')

    # Handle missing values
    missing_summary = df.isnull().sum().to_frame(name='Missing Values').to_html(classes='table table-striped')

    # Visualization: Histogram for numerical columns
    numerical_cols = df.select_dtypes(include=['number']).columns
    plots = []

    for col in numerical_cols:
        # Create histogram using Seaborn
        plot = sns.histplot(data=df, x=col, kde=True)
        plot.set_title(f'Histogram of {col}')

        # Sanitize column name for file path
        sanitized_col_name = re.sub(r'[^\w\-_\. ]', '_', col)  # Replace invalid characters with underscores
        plot_path = os.path.join(MEDIA_ROOT, f'{sanitized_col_name}_hist.png')

        # Save the figure directly via Seaborn
        plot.get_figure().savefig(plot_path)
        plt.close(plot.get_figure())  # Close the figure to free memory

        plots.append(os.path.relpath(plot_path, MEDIA_ROOT))

    return {
        'first_rows': first_rows,
        'summary_stats': summary_stats,
        'missing_summary': missing_summary,
        'plots': [os.path.join(MEDIA_URL, plot) for plot in plots]
    }

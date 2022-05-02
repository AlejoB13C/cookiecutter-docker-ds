# {{ cookiecutter.project_name }}

{{ cookiecutter.project_description }}
Created by: {{ cookiecutter.full_name }} @{{ cookiecutter.github_username }}
  
## Installation guide

Please read [install.md](install.md) for details on how to set up this project.

## Project Organization

    ├── LICENSE
    ├── README.md               <- The top-level README for developers using this project.  
    ├── install.md              <- Detailed instructions to set up this project.  
    ├── auto-install.py         <- File to auto set up environment and extensions for this project.  
    ├── tasks.py                <- Invoke with commands like `notebook`.  
    ├── setup.py                <- Makes project pip installable (pip install -e .)  
    │                               so {{ cookiecutter.__package_name }} can be imported.  
    ├── requirements.txt        <- The requirements file for reproducing the analysis environment using `pip`.  
    ├── environment.yml         <- The requirements file for reproducing the analysis environment using `conda`.  
    │  
    ├── .env                    <- The file for project environment variables.  
    ├── .gitignore  
    ├── .here                   <- File that will stop the search if none of the other criteria  
    │                         apply when searching head of project.  
    │  
    ├── references              <- Data dictionaries, manuals, and all other explanatory materials.  
    │  
    ├── reports                 <- Generated analysis as HTML, PDF, LaTeX, etc.  
    │   └── figures             <- Generated graphics and figures to be used in reporting.  
    │  
    ├── models                  <- Trained and serialized models, model predictions, or model summaries.  
    │  
    ├── data      
    │   ├── external            <- Data from third party sources.  
    │   ├── interm              <- Intermediate data that has been transformed.  
    │   ├── processed           <- The final, canonical data sets for modeling.  
    │   └── raw                 <- The original, immutable data dump.  
    │  
    ├── notebooks               <- Jupyter notebooks. Naming convention is a number (for ordering),  
    │   │                       the creator's initials, and a short `-` delimited description, e.g.  
    │   │                       `1.0-jqp-initial-data-exploration`.  
    │  
    └── {{ cookiecutter.__package_name }}   <- Source code for use in this project.  
        ├── __init__.py         <- Makes {{ cookiecutter.__package_name }} a Python module.  
        │  
        ├── data                <- Scripts to download or generate data.  
        │   └── make_dataset.py  
        │  
        ├── features            <- Scripts to turn raw data into features for modeling.  
        │   └── build_features.py  
        │  
        ├── models              <- Scripts to train models and then use trained models to make  
        │   │                       predictions.  
        │   ├── train_model.py  
        │   └── predict_model.py  
        │  
        ├── utils               <- Scripts to help with common tasks.  
        │   └── paths.py        <- Helper functions to relative file referencing across project.  
        │  
        └── visualization       <- Scripts to create exploratory and results oriented visualizations.  
            └── visualize.py  
  
---
Project based on the [cookiecutter conda data science project template](https://github.com/AlejoB13C/cookiecutter-docker-ds).
# Cookiecutter Docker Data Science

_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work making use of docker containers._

## Requirements
- [pip](https://pypi.org/project/pip/)

- [Cookiecutter 2.0.2](https://github.com/cookiecutter/cookiecutter)
    Recommended first create a venv to use cookiecutter.
    ```bash
    wget -P ~/.cookie/ https://github.com/cookiecutter/cookiecutter/archive/refs/tags/2.0.2.tar.gz && cd ~/.cookie/ && tar -xf 2.0.2.tar.gz && pip install -e cookiecutter-2.0.2/
    ```


## Resulting directory structure

    ├── LICENSE
    ├── README.md               <- The top-level README for developers using this project.  
    ├── install.md              <- Detailed instructions to set up this project.  
    ├── auto-install.py         <- File to auto set up environment and extensions for this project.  
    ├── tasks.py                <- Invoke with commands like `notebook`.  
    ├── setup.py                <- Makes project pip installable (pip install -e .)  
    │                               so {{ cookiecutter.project_module_name }} can be imported.  
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
    │   └── 0.0-{{ cookiecutter.__name_initials  }}-{{ cookiecutter.__project_slug }}.ipynb  
    │  
    └── {{ cookiecutter.__package_name }}   <- Source code for use in this project.  
        ├── __init__.py         <- Makes {{ cookiecutter.project_module_name }} a Python module.  
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
  
## Contributing guide

All contributions, bug reports, bug fixes, documentation improvements, enhancements and ideas are welcome.

---
Project based on the [cookiecutter conda data science project template](https://github.com/jvelezmagic/cookiecutter-conda-data-science).
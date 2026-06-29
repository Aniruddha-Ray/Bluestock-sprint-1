import os

files = [
    "README.md",
    "requirements.txt",
    ".env",
    ".gitignore",
    "Makefile",

    "db/schema.sql",

    "src/__init__.py",
    "src/etl/__init__.py",
    "src/etl/loader.py",
    "src/etl/validator.py",
    "src/etl/normaliser.py",
    "src/etl/config.py",

    "tests/__init__.py",
    "tests/etl/__init__.py",
    "tests/etl/test_loader.py",
    "tests/etl/test_validator.py",
    "tests/etl/test_normaliser.py",

    "notebooks/exploratory_queries.sql",

    "data/raw/.gitkeep",
    "data/processed/.gitkeep",

    "output/.gitkeep",

    "logs/.gitkeep",

    "docs/.gitkeep"
]

for filepath in files:
    directory = os.path.dirname(filepath)

    if directory != "":
        os.makedirs(directory, exist_ok=True)

    if not os.path.exists(filepath):
        with open(filepath, "w") as f:
            pass

print("Project structure created successfully!")
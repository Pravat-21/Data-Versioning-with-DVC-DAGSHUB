# Step-by-step process of versioning data with DVC & DagsHub:

- **step-1:**
    - Suppose we want to do a project. so I assume that we create all the necessary folders & files with help of coockiecutter template and of course created a virtual environment (although it is not mandetory but it's a good practice to do.)
    - Now assume that we are in that project folder with in virtual environment.

- **step-2:**
    - Do a inital commit after initialized with git & DVC.(assuming that dvc is already installed & git it configured.)
    - If DVC is not installed then-
        -   ```
            pip install dvc
            ```
    - otherwise initialize with the project folder
        -   ```
             git init
             ``` 
        -   ```
            dvc init
            ```
    - then tracked those file with DVC which we want to (here only data folder will be tracked)
        -   ```
            dvc add data/
            ```
    
    


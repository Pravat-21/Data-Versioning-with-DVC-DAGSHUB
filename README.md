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
    - then do the following--
        -   ```
            git add .
            git commit -m "your commit"
            git branch -M main
            git remote add origin <your git repo address>
            git push -u origin main
            ```
- **step-3:**
    - Write your code & test it by using-
        -   ```
            python yourfile_name.py
            ```
    - Here in first version of code I have droped `state_province`,`country`; these two columns.
    - Now it's time to add remote location for data versioning.

    - **STEPS FOR DOING THE DATA VERSIONING IN DAGSHUB:** 
        - First create a accout in `DagsHub` using `GitHub` (we have a choice with `Google` also but here we login with `GitHub` for our benifits.)

        - Connect with your project repo with `DagsHub` (for details how to do that click here)

         - (if `dvc[dagshub]` is not installed then first install it)
            -   ```
                pip install dvc[dagshub]
                ```

        - Next setup your `DVC` with lthe remote location of `DagsHub` (for details how to do that click here)
        -After connecting with `DagsHub`check about DVC --
            -   ```
                dvc status
                ```
            -   ```
                dvc commit
                ```
       


    
    


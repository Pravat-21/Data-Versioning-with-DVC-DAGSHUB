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
        - After dvc commit we can push all the files to git & data to our remote location
            
            -   ```
                git add .
                git commit -m "your commit 2"
                git push
                ```
            -   ```
                dvc push -r origin
                ```
**First version of the code & data has been successfully tracked.**

---------------------------------------------------------------------------------------------------------------
### Creating the second version of the code & data:
- **step-3:**
    - write your second version of code.
    - Test it again.
    - Now we need again do code & data versioning in the same manner
    -   ```
        dvc status
        dvc commit
        ```
        ```
        git status
        ```
        It must show that data.dvc has been modified along with other updated files & folders.

        ```
        git add .
        git commit -m "your commit for second version of code"
        git push
        ```
        Now push the data into remote location.
        ```
        dvc push -r origin
        ```
**Second version of the code & data has been successfully tracked.**

---------------------------------------------------------------------------------------------------------------
## **Now it's the time to check**
- Suppose we want to go the previous version of the project. To do that --
    -   ```
        git log --oneline
        ```
        It will show all the commits.




       


    
    


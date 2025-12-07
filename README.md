# **Step-by-step process of versioning data with DVC & DagsHub:**

- **step-1:**
    - Suppose we want to do a project. so I assume that we create all the necessary folders & files with help of `coockiecutter` template and of course created a virtual environment (although it is not mandetory but it's a good practice to do.)
    - Now assume that we are in that project folder with in virtual environment.

- **step-2:**
    - Do a inital commit after initialized with `GIT` & `DVC`.(assuming that dvc is already installed & git it configured.)
    - If DVC is not installed then-
        ```
        pip install dvc
        ```
    - otherwise initialize with the project folder
        ```
        git init
        ``` 
        ```
        dvc init
        ```
    - then do the following--
        ```
        git add .
        git commit -m "your inital commit"
        git branch -M main
        git remote add origin <your git repo address>
        git push -u origin main
        ```
- **step-3:**
    - Write your code & test it by using-
        ```
        python yourfile_name.py
        ```
    - Here in first version of code I have droped `state_province`,`country`; these two columns.
    - Now it's time to add remote location for data versioning.

    - **STEPS FOR DOING THE DATA VERSIONING IN DAGSHUB:** 
        - First create a accout in `DagsHub` using `GitHub` (we have a choice with `Google` also but here we login with `GitHub` for our benifits.)

        - Connect with your project repo with `DagsHub`

         - (if `dvc[dagshub]` is not installed then first install it)
            ```
            pip install dvc[dagshub]
            ```

        - Next setup your `DVC` with the remote location of `DagsHub`.
            - Go to the remote in the `DagsHub` repo then in DVC section where protocal is being set to `HTTP`.
            - Then copy the following command into our project terminal
                ```
                dvc remote add -d origin https://dagshub.com/<user_name>/<repo_name>.dvc
                dvc remote modify origin --local auth basic
                dvc remote modify origin --local user <user_name>
                dvc remote modify origin --local password your_token 232323.........
                ```

        - After connecting with `DagsHub`check about DVC --
            ```
            dvc status
            ```
        - then tracked those file with DVC which we want to (here only data folder will be tracked)
            ```
            dvc add data/
            ```
        - After dvc commit we can push all the files to git & data to our remote location
            
            ```
            git add .
            git commit -m "your commit 2"
            dvc push 
            git push
            ```
            
**First version of the code & data has been successfully tracked.**

---------------------------------------------------------------------------------------------------------------
### Creating the second version of the code & data:
- **step-3:**
    - write your second version of code.
    - Test it again.
    - Now we need again do code & data versioning in the same manner
        ```
        dvc status
        dvc add data/
        ```
        ```
        git status
        ```
        It must show that data.dvc has been modified along with other updated files & folders.

        ```
        git add .
        git commit -m "your commit for second version of code"
        dvc push
        git push
        ```
**Second version of the code & data has been successfully tracked.**

---------------------------------------------------------------------------------------------------------------
## **Now it's the time to check**
- Suppose we want to go the previous version of the project. To do that --
    ```
    git log --oneline
    ```
    It will show all the commits.
- then we can do -
    ```
    git checkout <your commit id for that version of codes>
    ```
    Here we can observe that although the code of this version has been updated but the data is yet to update. In order to fetch data run
    ```
    dvc checkout
    ```
## **Alternative way to connect our project with remote location in `DagsHub` using `S3`:**
- when we connect with our `GitHub` & `DagsHub` then -
    - Go to the remote in the `DagsHub` repo then in DVC section where protocal is being set to `s3`.
    - Then copy the following command into our project terminal (make sure that `dvc-s3` is already installed if not execute run this) -
        ```
        pip install dvc-s3
        ```
        then we can run the following -
        ```
        dvc remote add origin -d s3://dvc
        dvc remote modify origin endpointurl https://dagshub.com/<user_name>/<repo_name>.s3

        dvc remote modify origin --local access_key_id your_token
        dvc remote modify origin --local secret_access_key your_token
        ```
    and thus also we can add our remote location into `DagsHub-s3`.

**[ Note that whatever ways we choose during versioning, we need to execute that respective credential during pulling then run `dvc pull` ]**


## **And that's how we can do the data versioning with `DVC`& `DagsHub`.**

### **[Additional Notes about git]:**

- Suppose, we want to checkout any previous commit & then we want to push some changes from it then -
    ```
    git checkout main

    git reset --hard aac8f3c8fdf0615c3c4ec8806481f8cd4fb75763

    git push -f
    ```


___________________________________________________________________________________
# **Thank You.**
    




       


    
    


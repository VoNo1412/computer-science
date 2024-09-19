# Exercise 1 - Getting the environment ready
    Run the command below to download the staging area setup script.
    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/8ZUkKar_boDbhNgMiwGAWg/setupstagingarea.sh
    Copied!Executed!
    Step 3: Export your postgres password.

    Run the below command in the terminal by replacing <your postgres password> with your postgres password that can be found under the connection information tab.

    export PGPASSWORD=<your postgres password>

    Step 4: Run the setup script.

    Run the command below to execute the staging area setup script.
    bash setupstagingarea.sh

# Exercise 2 - Getting the testing framework ready
    You can perform most of the data quality checks by manually running sql queries on the data warehouse.

    It is a good idea to automate these checks using custom programs or tools. Automation helps you to easily

    create new tests,
    run tests,
    and schedule tests.
    We will be using a python based framework to run the data quality tests.

    Step 1: Download the framework.

    Run the commands below to download the framework

    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/dataqualitychecks.py

    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/HB0XK4MDrGwigMmVPmPoeQ/dbconnect.py

    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Verifying%20Data%20Quality%20for%20a%20Data%20Warehouse/mytests.py

    wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/saTxV8y9Kt-e8Zxe29M0TA/generate-data-quality-report.py

    ls
    Step 2: Install the python driver for Postgresql.

    Run the command below to install the python driver for Postgresql database


    python3 -m pip install psycopg2
    Copied!Executed!
    Step 3: Update Password in dbconnect.py

    Go to File>Open. A window will appear; double-click on dbconnect.py to open it.
    
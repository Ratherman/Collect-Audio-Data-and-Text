# Collect-Audio-Data-and-Text

# Update Description
* Lastest Updated Date: 2021/10/17
* - - - - - - - - - - - - - - - - -
* 2021/10/16: Add Env and Guide.
* 2021/10/17: Add Guide and Write Code (crawl & insert).
####  2021/10/18: Tomorrow's goal is use flask to display ramdom 10 sentences from db. 

# Env
* OS_1: Ubuntu 20.04
* OS_2: Windows 10
* Necessary Tools:
    1. VScode
    2. MSSQL
    3. Conda

# Guide:
* (2021/10/17) Setup Conda Virtual Env for this specific purpose?
* (2021/10/16) How to install VScode on Ubuntu 20.04?
* (2021/10/16) How to install MSSQL on Ubuntu 20.04?
* (2021/10/16) How to use sqlcmd (i.e. sqlcmd basic)?
* (2021/10/17) How to install MSSQL on Windows 10?
* (2021/10/17) How to let VScode recognize Conda (i.e. Edit Env Path)?

## Setup Conda Virtual Env for this specific purpose
* Step 1: Make sure you've installed anaconde.
* Step 2: `conda create -n "CADAT" python=3.8`
* Step 3: `conda activate CADAT`
* Step 4: `conda install jupyter notebook` -> Use jupyter notebook to write some draft.
* Step 5: `conda install beautifulsoup4`
* Step 6: `conda install requests`
* Step 7: `conda install numpy`
* Step 8: `conda install pandas`
* Step 9: `conda install pyodbc`

## How to install Vscode on Ubuntu 20.04?
* Step 1: Go to this [website](https://code.visualstudio.com/download) and download **.deb**.
* Step 2: After downloading, open up terminal and enter the following command.
* Step 3: `sudo apt install ./code_1.61.1-1634175470_amd64.deb` the number might be different
* Step 4: You are good to go! By entering `code` in terminal, VSCode would show up.

## How to install MSSQL on Windows 10?
* If needed, you're encouraged to follow this [Tutorial](https://www.guru99.com/download-install-sql-server.html).
* Step 1: Go to this [website](https://www.microsoft.com/en-in/sql-server/sql-server-downloads) and download the express version, i.e., SQL Server 2019 Express.
* Step 2: Open the **.exe** file.
* Step 3: Choose the **Basic** option.
* Step 4: Click **Accept** and **Choose the installed location**.
* (Optional) Step 5: Click **Install SSMS** and a webpage would be popped up.
* (Optional) Step 6: Click the hypytertext **"下載 SQL Server Management Studio (SSMS) 18.10"**.
* (Optional) Step 7: Open the **.exe** file.

## How to install MSSQL on Ubuntu 20.04?
* Great tutorial on YouTube: [Installing Microsoft SQL Server 2019 on Ubuntu 20.04 LTS // Linux can host your MSSQL Server](https://www.youtube.com/watch?v=x6pYoWwtVAY)

* Step 1: Update Ubuntu
    * `sudo apt update`
    * `sudo apt upgrade -y`
    * `sudo reboot`
* Step 2: Import Microsoft public repository GPG key for Ubuntu
    * `sudo wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -`
* Step 3: Register the Microsoft SQL Server Ubuntu repository for SQL Server 2019
    * `sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2019.list)"`
* Step 4: Install SQL Server
    * `sudo apt update`
    * `sudo apt install -y mssql-server`
* Step 5: Configure SQL server and set SA password
    * `sudo /opt/mssql/bin/mssql-conf setup`
* Step 6: Check SQL server is running
    * `systemctl status mssql-server --no-pager`
* Step 7: Check the listening port for MSSQL server
    * `sudo apt install net-tools`
    * `sudo netstat -tnlp | grep sqlservr`
* Step 8: Open up the firewall port 1433 to connect remotely
    * Allow ssh and enable firewall
    * `sudo ufw allow 22`
    * `sudo ufw allow 1433`
    * `sudo ufw allow 1434`
    * `sudo ufw enable`
* Step 9: Install SQL Server command-line tools
    * Import the public repository GPG keys.
        * `curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -`
    * Register the Microsoft Ubuntu repository
        * `curl https://packages.microsoft.com/config/ubuntu/20.04/prod.list | sudo tee /etc/apt/sources.list.d/msprod.list`
    * Install tools and ODBC drivers
        * `sudo apt update`
        * `sudo apt install -y mssql-tools unixodbc-dev`
        * I actually went into a dependecy-related bug here, this [post](https://askubuntu.com/questions/1123273/unable-to-connect-microsoft-sql-server-and-visual-studio-code) helps me a lot.
    * Add tools folder to PATH environment variable in a bash shell.
        * `echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bash_profile`
        * `echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc`
        * `source ~/.bashrc`
    * Connect to your server
        * (Ubuntu 20.04) `sqlcmd -S localhost -U SA -P 'Password'`
        * (Windows 10) `sqlcmd -E -S .\SQLEXPRESS`

## How to use sqlcmd (i.e. sqlcmd basic) ? 
* Target: Create a simple Table (**ATdata**) containing two columns. One is "Text", and another is "Audio_Path".
* Step 1: Create a Database named **DB**
    * `Create Database DB`
    * `Go`
* Step 02: Specify the database we want to use.
    * `Use DB`
    * `Go`
* Step 3: Create a Table called **ATdata**
    * `Create Table dbo.ATdata (ID int NOT NULL IDENTITY(1,1) Primary KEY, TEXT varchar(500) NOT NULL, Audio_Path varchar(200) Default 'C:default/path/to/your/audio/file')`
    * `Go`
* Step 4: Insert a row for testing purpose
    * `INSERT dbo.ATdata (Text) VALUES ('Hi, my name is Eric.')`
    * `Go`
* Step 5: Make sure the data is inserted successfully
    * `SELECT * FROM dbo.ATdata`
    * `Go`
* Step 6: Drop Database
    * `Drop Database DB`
    * `Go`

## How to let VScode recognize Conda (i.e. Edit Env Path)
* Step 1: Click Windows Icon and search for **環境變數(environmental variable)**
* Step 2: In **System Variable**, click **path**.
* Step 3: Make sure you've installed **Anaconda**.
* Step 4: Add the following 3 paths into the clicked **path**.
    1. `c:\users\[username]\anaconda3`
    2. `c:\users\[username]\anaconda3\Scripts`
    3. `c:\users\[username]\anaconda3\Library\bin`
* Step 5: Restart VScode, then you are good to go!
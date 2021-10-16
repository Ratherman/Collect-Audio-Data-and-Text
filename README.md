# Collect-Audio-Data-and-Text

# Update Description
* Lastest Updated Date: 2021/10/16
* - - - - - - - - - - - - - - - - -
* 2021/10/16: Add Env and Guide.
# Tomorow's Goal is to use python to (1) crawl texts and (2) insert into db, i.e., ATdata 

# Env
* OS: Ubuntu 20.04

# Guide:
* (2021/10/16) How to install Vscode on Ubuntu 20.04?
* (2021/10/16) How to install MSSQL on Ubuntu 20.04?
* (2021/10/16) How to use sqlcmd (i.e. sqlcmd basic)?

## How to install Vscode on Ubuntu 20.04?
1. Go the this [website](https://code.visualstudio.com/download) and download **.deb**.
2. After downloading, open up terminal and enter the following command.
3. `sudo apt install ./code_1.61.1-1634175470_amd64.deb` the number might be different
4. You are good to go! By entering `code` in terminal, VSCode would show up.

## How to install MSSQL on Ubuntu 20.04?
* Great tutorial on YouTube: [Installing Microsoft SQL Server 2019 on Ubuntu 20.04 LTS // Linux can host your MSSQL Server](https://www.youtube.com/watch?v=x6pYoWwtVAY)

1. Update Ubuntu
    * `sudo apt update`
    * `sudo apt upgrade -y`
    * `sudo reboot`
2. Import Microsoft public repository GPG key for Ubuntu
    * `sudo wget -qO- https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -`
3. Register the Microsoft SQL Server Ubuntu repository for SQL Server 2019
    * `sudo add-apt-repository "$(wget -qO- https://packages.microsoft.com/config/ubuntu/20.04/mssql-server-2019.list)"`
4. Install SQL Server
    * `sudo apt update`
    * `sudo apt install -y mssql-server`
5. Configure SQL server and set SA password
    * `sudo /opt/mssql/bin/mssql-conf setup`
6. Check SQL server is running
    * `systemctl status mssql-server --no-pager`
7. Check the listening port for MSSQL server
    * `sudo apt install net-tools`
    * `sudo netstat -tnlp | grep sqlservr`
8. Open up the firewall port 1433 to connect remotely
    * Allow ssh and enable firewall
    * `sudo ufw allow 22`
    * `sudo ufw allow 1433`
    * `sudo ufw allow 1434`
    * `sudo ufw enable`
9. Install SQL Server command-line tools
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
        * `sqlcmd -S localhost -U SA -P 'Password'`

## How to use sqlcmd (i.e. sqlcmd basic) ? 
* Target: Create a simple Table (**ATdata**) containing two columns. One is "Text", and another is "Audio_Path".
    * Step 01: Create a Database named **DB**
        * `Create Database DB`
        * `Go`
    * Step 02: Specify the database we want to use.
        * `Use DB`
        * `Go`
    * Step 03: Create a Table called **ATdata**
        * `Create Table dbo.ATdata (ID int NOT NULL IDENTITY(1,1) Primary KEY, TEXT varchar(50) NOT NULL, Audio_Path varchar(200) Default 'C:default/path/to/your/audio/file')`
        * `Go`
    * Step 04: Insert a row for testing purpose
        * `INSERT dbo.ATdata (Text) VALUES ('Hi, my name is Eric.')`
        * `Go`
    * Step 05: Make sure the data is inserted successfully
        * `SELECT * FROM dbo.ATdata`
        * `Go`
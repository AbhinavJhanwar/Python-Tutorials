# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:50:21 2018

@author: abhinav.jhanwar
"""

import pyodbc

# Driver: Here you have to specify the ODBC Connection, or SQL Server Native Client.
# Server: You have to specify the server instance name.
# Database Name: You have to specify the database name from where you want to extract the data.
# UserName: Please specify the user name who has access to SQL Server. If you are using the Windows authentication then you can omit the Username and password.
# password: Please specify the password for the above user name

'''pyodbc.connect("Driver = {SQL Server Native Client 11.0};"               
               "Server = Server_Name;"
               "Database = Database_Name;"
               "username = User_Name;"
               "password = User_Password;"
               "Trusted_Connection = yes;")'''

'''const string CLASS_NAME = "MYWIZARD_JIRA_Populate_Publisher";
 NOTIFICATIONQUERY = "SELECT [Name],[Registered] FROM [dbo].[JIRA_SqlDependency];";
 TRUE = "true";
 CREATECMDTXT = "CREATE TABLE [dbo].[JIRA_SqlDependency]([Name][nvarchar](50) NOT NULL,[Registered] [bit] NULL,[LastUpdated][DateTime] NULL)";
 CHECKEXISTCMDTXT = "IF EXISTS(select * from information_schema.tables  where table_name = 'JIRA_SqlDependency') SELECT 1 ELSE SELECT 0";
 INSERTCMDTXT = "INSERT INTO [dbo].[JIRA_SqlDependency]([Name],[Registered])VALUES('JIRA','0')";
 UPDATECMDTXT = "UPDATE[dbo].[JIRA_SqlDependency] SET LASTUPDATED = @lastUpdated";
 SELECTCMDTXT = "SELECT COUNT(Name) FROM [dbo].[JIRA_SqlDependency]";
 TRUNCATECMDTXT = "TRUNCATE TABLE [dbo].[JIRA_SqlDependency]";'''

conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=localhost;"
                      "Database=master;"
                      "Trusted_Connection=yes;")
with conn:
    cursor = conn.cursor()
    #cursor.execute("INSERT INTO [master].[dbo].[Jira_Project]([ProjectKey],[ProjectID],[ProjectName],[LastModified],[Lead],[Category])VALUES('BEN1', '10006', 'Benefits', '2018-05-09T14:43:52', 'prasanna', 'None')")
    #cursor.execute("INSERT INTO [master].[dbo].[Jira_Project]([ProjectKey],[ProjectID],[ProjectName],[LastModified],[Lead],[Category])VALUES('CLAI', '10000', 'Claims', '2018-05-09T14:43:52', 'prasanna', 'None')")
    
    cursor.execute('''SELECT TOP (10) [ID]
          ,[ProjectKey]
          ,[ProjectID]
          ,[ProjectName]
          ,[Category]
          ,[Lead]
          ,[LastModified]
      FROM [master].[dbo].[Jira_Project]''')
    for row in cursor:
        print('row = %r' % (row,))
    cursor.commit()

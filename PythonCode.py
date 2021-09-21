import mysql.connector

# Connecting the Database
db = mysql.connector.connect(
    host="localhost", user="root", passwd="[ provide_your_password ]", database="books"
)

cursor = db.cursor()

# ------------------------------------------------------------------------------------
# Creating table in the Database
print(
    "The MySQL query for creating the BookDetails table in the Database called 'books'"
)

print("\n")

print(
    "create table BookDetails(Book_no int Primary key, Book_name varchar(100), Author_name varchar(100), Edition varchar(30), Year_of_release int, Publication_Company text);"
)

cursor.execute(
    "create table BookDetails(Book_no int Primary key, Book_name varchar(100), Author_name varchar(100), Edition varchar(30), Year_of_release int, Publication_Company text);"
)


# -----------------------------------------------------------------------------------------------------
# Inserting Rows in the Database

sql = """
INSERT INTO BookDetails(Book_no, Book_name, Author_name, Edition, Year_of_release, Publication_Company) VALUES  (%s, %s, %s, %s, %s, %s)
"""


data_list = [
    (
        1,
        "Cryptography and Network Security",
        "William Stallings",
        "10th Edition",
        2006,
        "Pearson Education",
    ),
    (2, "Computer Networking", "William Stallings", "10th", 2006, "Pearson Education"),
    (
        3,
        "Artificial Intelligence",
        "Steve Mark, Santhosh Kumar",
        "5th Edition",
        "2018",
        "Pearson Education",
    ),
    (
        4,
        "Artificial Intelligence. A Systems Approach",
        "M. Tim Jones",
        2008,
        "Jones and Bartlett Publishers",
    ),
    (
        5,
        "Foundations of Computational Agents",
        "David L. Poole; Alan K Mackworth",
        "2nd Edition",
        2017,
        "Cambridge University Press",
    ),
    (
        6,
        "The quest for Artificial Intelligence - ideas and achievements",
        "Nilsson, Nils J.",
        "4th Edition",
        2013,
        "Cambridge University Press",
    ),
    (
        7,
        "Cloud Computing",
        "Sai Seena",
        "4th Edition",
        "2012",
        "Technical Publications",
    ),
    (
        8,
        "Artificial Intelligence_ A Modern Approach",
        "Stuart Russell, Peter Norvig",
        "4th Edition",
        2020,
        "Pearson Series in Artificial Intelligence",
    ),
    (
        9,
        "Data Mining-Concepts and Techniques",
        "Han, Jiawei_Kamber, Micheline_Pei, Jian",
        "2nd Edition",
        2018,
        "Elsevier, Morgan Kaufmann",
    ),
    (
        10,
        "Data Mining - Concepts, Models and Techniques",
        "Florin Gorunescu",
        "1st Edition",
        "2011",
        "Springer",
    ),
    (
        11,
        "Data Mining for Business Analytics - Concepts, Techniques and Applications in R",
        "Galit Shmueli, Peter C. Bruce, Inbal Yahav, Nitin R. Patel, Kenneth C. Lichtendahl Jr.",
        "3rd Edition (US)",
        2017,
        "Wiley",
    ),
    (
        12,
        "Engineering a Compiler",
        "Keith Cooper, Linda Torczon",
        "4th Edition",
        2015,
        "Elsevier (Science & Technology)",
    ),
    (
        13,
        "Internet and World Wide Web - How to Program",
        "(How to Program Series) Deitel, Paul Deitel, Harvey Deitel, Abbey",
        "10th Edition (US)",
        2011,
        "Pearson Education",
    ),
    (
        14,
        "Web Technologies - a Computer Science perspective",
        "Jeffrey C. Jackson",
        "6th Edition",
        2007,
        "Prentice Hall",
    ),
    (
        15,
        "The Practice of Clinical Engineering",
        "Cesar Caceres",
        "2nd Edition",
        2017,
        "Academic Press Inc.",
    ),
]

for i in range(len(data_list)):
    cursor.execute(
        "INSERT INTO BookDetails(Book_no, Book_name, Author_name, Edition, Year_of_release, Publication_Company) VALUES  (%s, %s, %s, %s, %s, %s)",
        data_list[i],
    )
db.commit()


# -----------------------------------------------------------------------------------------------
# Selection Operations

print("Selecting all the rows from the \b BookDetails \b table")
print("SELECT * FROM BookDetails;")
print("\n")

cursor.execute("SELECT * FROM BookDetails;")

for rows in cursor:
    print(rows)

print("\n")
print(
    "---------------------------------------------------------------------------------------------------"
)
print("\n")
"""----------------------------------------------------------------------------------------------------"""


print("The query to select the column containing the Booknames of all Books ")
print("SELECT Book_name from BookDetails;")
print("\n")

cursor.execute("SELECT Book_name from BookDetails;")
for rows in cursor:
    print(rows)

print("\n")
print(
    "---------------------------------------------------------------------------------------------------"
)
print("\n")
# -----------------------------------------------------------------------------------------------------

print("The query to select the column containing the Author names of all Books ")
print("SELECT Author_name from BookDetails;")
print("\n")

cursor.execute("SELECT Author_name from BookDetails;")
for rows in cursor:
    print(rows)

print("\n")
print(
    "---------------------------------------------------------------------------------------------------"
)
print("\n")
# --------------------------------

print(
    "The query to select the column containing the Publication Companies of all Books "
)
print("SELECT Publication_Company from BookDetails;")
print("\n")

cursor.execute("SELECT Publication_Company from BookDetails;")
for rows in cursor:
    print(rows)

print("\n")
print(
    "---------------------------------------------------------------------------------------------------"
)
print("\n")
# -------------------------------------------------------


print(
    "The following query selects only the rows which has the Books published from the Pearson Education"
)
print("select * from BookDetails where Publication_Company = 'Pearson Education';")
print("\n")

cursor.execute(
    "select * from BookDetails where Publication_Company = 'Pearson Education';"
)
for row in cursor:
    print(row)

print("\n")
print(
    "---------------------------------------------------------------------------------------------------"
)
print("\n")
# ----------------------------------------------------

print("Use the below query to get the Books which are published in the year 2017")
print("SELECT * FROM BookDetails where Year_of_release  = 2017;")
print("\n")

cursor.execute("SELECT * FROM BookDetails where Year_of_release  = 2017;")
for rows in cursor:
    print(rows)

print("\n")
print(
    "---------------------------------------------------------------------------------------------------"
)
print("\n")
# ----------------------------------------------------

print("Use the below query to get the Books which are published in the year 2017")
print("SELECT * FROM BookDetails where Year_of_release  = 2017;")
print("\n")

cursor.execute("SELECT * FROM BookDetails where Year_of_release  = 2017;")
for rows in cursor:
    print(rows)

print("\n")
print(
    "---------------------------------------------------------------------------------------------------"
)
print("\n")
# ----------------------------------------------------

print(
    "To know about the details of a particular book using its name, use the below query to get the details"
)
print(
    "SELECT * FROM BookDetails where Book_name = 'Artificial Intelligence. A Systems Approach';"
)
print("\n")

cursor.execute(
    "SELECT * FROM BookDetails where Book_name = 'Artificial Intelligence. A Systems Approach';"
)
for rows in cursor:
    print(rows)

print("\n")
print(
    "--------------------------------------------------------------------------------------------"
)

# lenslog 

### a photography portfolio management system

**LensLog** is a desktop-based photography portfolio management system developed using **Python and MySQL**. It helps photographers organize and manage their photographs by storing important metadata such as camera, lens, ISO, shutter speed, aperture, location, rating, editing status, and date taken.

The application provides a graphical interface using **Tkinter**, connects to a **MySQL relational database**, displays image previews, generates portfolio analytics, and allows portfolio data to be exported to CSV.

> developed as a Class XII Computer Science (083) project for the academic year 2026–27.

---

## features

### portfolio management

* add photograph records
* update existing records
* delete photograph records
* view all photographs in a tabular interface
* store detailed photography metadata
* attach local image files to portfolio records

### database management

* MySQL relational database
* CRUD operations using SQL
* parameterized SQL queries
* structured photograph metadata
* automatic ID generation using `AUTO_INCREMENT`

### image handling

* select images directly from the computer
* display image previews inside the application
* open full-resolution images using the system's default image viewer
* store image file paths instead of large image binaries in the database

### search

* search photographs by category
* reset the table to display all records

### analytics

* generate photograph count charts by category
* generate rating distribution charts
* visualize portfolio data using Matplotlib

### export

* export the complete portfolio database to a CSV file
* create a portfolio backup using Pandas

---

## technology stack

| technology             | purpose                       |
| ---------------------- | ----------------------------- |
| Python                 | application logic and GUI     |
| Tkinter                | graphical user interface      |
| MySQL                  | database management           |
| mysql-connector-python | Python–MySQL connectivity     |
| Pillow                 | image processing and previews |
| Pandas                 | data analysis and CSV export  |
| Matplotlib             | data visualization            |

The project uses a two-tier desktop architecture, with Tkinter handling the presentation layer and MySQL handling persistent data storage.

---

## database

LensLog uses a MySQL database named:

```text
lenslog_db
```

The main table is:

```text
photographs
```

The table stores information including:

```text
photo_id
title
category
location
date_taken
camera_used
lens_used
iso
shutter_speed
aperture
rating
editing_status
image_path
```

Photographs themselves are not stored as BLOBs in the database. Instead, LensLog stores their file paths and accesses the original images from the local file system.

---

## requirements

### software

* Python 3.x
* MySQL Server
* MySQL Connector/Python
* Pillow
* Pandas
* Matplotlib
* Windows operating system

### hardware

**minimum:**

* 4 GB RAM
* dual-core 1.8 GHz processor
* 500 MB available storage
* 1366 × 768 display

**recommended:**

* 8 GB RAM or higher
* Intel Core i5 / AMD Ryzen 5 or higher
* SSD with at least 2 GB available space
* 1920 × 1080 display

---

## setup

### 1. clone the repository

```bash
git clone https://github.com/your-username/lenslog.git
cd lenslog
```

### 2. install the required Python packages

```bash
pip install mysql-connector-python pillow pandas matplotlib
```

### 3. create the MySQL database

Create a database named:

```sql
CREATE DATABASE lenslog_db;
```

Then create the `photographs` table according to the schema included with the project.

### 4. configure the database connection

Update the MySQL connection details in the Python source code:

```python
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="lenslog_db"
)
```

> **important:** do not upload your real MySQL password to GitHub. Use your own local password or environment variables.

### 5. run the application

```bash
python lenslog.py
```

---

## application workflow

```text
start application
       │
       ▼
connect to MySQL
       │
       ▼
load portfolio records
       │
       ▼
┌───────────────────────────┐
│      LensLog GUI          │
├───────────────────────────┤
│ add photograph            │
│ update photograph         │
│ delete photograph         │
│ search portfolio          │
│ preview image             │
│ open full image           │
│ generate analytics        │
│ export portfolio to CSV   │
└───────────────────────────┘
       │
       ▼
MySQL database + local images
```

---

## project structure

```text
lenslog/
│
├── lenslog.py
├── portfolio_backup.csv
├── photographs.sql
├── screenshots/
│   ├── main-interface.png
│   ├── database.png
│   ├── image-preview.png
│   └── analytics.png
│
└── README.md
```

*The exact filenames can be changed to match the files included in the repository.*

---

## analytics

LensLog can generate visual reports from the portfolio database, including:

* photographs per category
* rating distribution

The application retrieves database records using Pandas and uses Matplotlib to generate the charts.

---

## database operations

LensLog supports the four fundamental database operations:

```text
CREATE  → add photograph
READ    → view/search photographs
UPDATE  → modify photograph
DELETE  → remove photograph
```

Parameterized SQL statements are used for database operations rather than directly inserting user input into SQL queries.

---

## limitations

* designed primarily for a single-user local environment
* requires a local MySQL server
* photograph metadata must be entered manually
* moving or renaming image files can break their stored paths
* search functionality is currently focused mainly on categories
* currently designed for Windows because it uses `os.startfile()` to open images

These limitations are documented in the original project report.

---

## future improvements

Possible future versions could include:

* automatic EXIF metadata extraction
* advanced multi-field search and filtering
* cloud image storage
* multi-user authentication
* photographer profiles
* automatic thumbnail generation
* duplicate image detection
* image tagging
* date-based filtering
* more advanced portfolio analytics
* cross-platform image opening
* backup and restore functionality

---

## concepts demonstrated

This project combines several Class XII Computer Science concepts with additional Python libraries:

* Python programming
* object-oriented programming
* functions
* conditional statements
* loops
* exception handling
* file handling
* GUI programming
* SQL
* relational databases
* CRUD operations
* parameterized queries
* database connectivity
* data analysis
* data visualization
* CSV file handling
* image processing
* operating system file management

---

## academic context

**project:** LensLog – Photography Portfolio Management System

**student:** Faheem Mohammed Shabeer

**class:** XII A

**subject:** Computer Science

**school:** Birla Public School

**academic year:** 2026–27

---

## references

* NCERT – Computer Science Textbook for Class XII (Code 083)
* Sumita Arora – *Computer Science with Python (Class XII)*
* Python documentation
* MySQL 8.0 Reference Manual
* Pillow documentation
* Pandas documentation
* Matplotlib documentation

---

## license

This project was developed for educational purposes as part of the Class XII Computer Science curriculum.

---


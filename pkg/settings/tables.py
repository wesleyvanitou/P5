
TABLES = {}

TABLES['brands'] = (
    """
        CREATE TABLE brands(
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        name VARCHAR (150) UNIQUE NOT NULL)
        ENGINE=InnoDB
    """)

TABLES['products'] = (
    """
        CREATE TABLE product_name (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        barcode int(12) NOT NULL
        product_name VARCHAR(150) UNIAUE NOT NULL,
        nutrition_score CHAR(1) NOT NULL,
        url VARCHAR(512) NOT NULL
    """)

TABLES['substitutes'] = (
    """
        CREATE TABLE product_name (
        id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
        barcode int(12) NOT NULL
        product_name VARCHAR(150) UNIAUE NOT NULL,
        nutrition_score CHAR(1) NOT NULL,
        url VARCHAR(512) NOT NULL
    """)

TABLES['categories'] = (
    """
        CREATE TABLE brands(
        id INT PRIMARY KEY AUTO_INCREMENT,
        brand_name VARCHAR (150) UNIQUE NOT NULL)
        ENGINE=InnoDB
    """)

TABLES['stores'] = (
    """
        CREATE TABLE stores(
        id INT PRIMARY KEY AUTO_INCREMENT,
        store_name VARCHAR (150) UNIQUE NOT NULL)
        ENGINE=InnoDB
    """)

TABLES['product_category'] = (
    """
        CREATE TABLE product_category(
        product_id INT(3) NOT NULL,
        category_id INT(3) NOT NULL)
        ENGINE=InnoDB)
    """)

TABLES['product_stores'] = (
    """
        CREATE TABLE product_category(
        product_id INT(3) NOT NULL,
        stores INT(3) NOT NULL)
        ENGINE=InnoDB)
    """)


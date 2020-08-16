TABLES = {}

TABLES['employees'] = {
    """
        CREATE TABLE IF NOT EXISTS employees (
        emp_no int(11) NOT NULL AUTO_INCREMENT,
        birth_date date NOT NULL,
        ame varchar(15)) NOT NULL,
        lname varchar(15) NOT NULL,
        hired date NOT NULL,
        PRIMARY KEY (emp_no))
        ENGINE=InnoDB
    """}



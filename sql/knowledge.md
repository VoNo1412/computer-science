# DDL - Data Definition Language
DDL is short name of Data Definition Language, which deals with database schemas and descriptions, of how the data should reside in the database.

CREATE - create a new table, view for a table or other object in the database
ALTER - modifies an existing database object, such as a table
DROP - deletes an entire table, a view of a table or other objects in the database
TRUNCATE - remove all records from a table, including all spaces allocated for the records are removed
COMMENT - add comments to the data dictionary
RENAME - rename an object


# DML - Data Manipulation Language
SELECT - retrieves records from one or more tables
INSERT - creates a record
UPDATE - modifies records
DELETE - deletes records
MERGE - UPSERT operation (insert or update)
CALL - call a PL/SQL or Java subprogram
EXPLAIN PLAN - interpretation of the data access path
LOCK TABLE - concurrency control


# DCL - Data Control Language
GRANT (Grant privilige(s) to user)
REVOKE (Remove granted privilige(s) from a user)

# TCL - Transaction Control Language
COMMIT - commits a transaction
ROLLBACK - rollback a transaction in case of any error occurs
SAVEPOINT - to rollback the transaction making points within groups
SET TRANSACTION - specify characteristics of the transaction
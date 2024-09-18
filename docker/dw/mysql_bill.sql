CREATE TABLE FACT_BILL(
    rowId int AUTO_INCREMENT primary key,
    customerId int,
    monthId int,
    billAmount float
);

CREATE TABLE Customer(
    customerId int AUTO_INCREMENT primary key,
    category text,
    country text,
    industry text
);

CREATE TABLE DateOfTime(
    monthId int primary key,
    year number,
    month number,
    monthName text,
    quater number,
    quaterName text
);

ALTER TABLE FACT_BILL ADD CONSTRAINT FK_FACTBILL_CUSTOMER FOREIGN KEY (customerId) REFERENCES Customer;
ALTER TABLE FACT_BILL ADD CONSTRAINT FK_FACTBILL_DATEOFTIME FOREIGN KEY (monthId) REFERENCES DateOfTime;





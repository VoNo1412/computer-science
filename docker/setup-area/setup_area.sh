echo "Creating database"
createdb -h postgres -U postgres -p 5432 billingDW 

echo "Unzip downloading file sql"
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0260EN-SkillsNetwork/labs/Setting%20up%20a%20staging%20area/billing-datawarehouse.tgz

echo "Extracting files"
tar -xvzf billing-datawarehouse.tgz

echo "Creating schema"
psql -h postgres -U postgres -p 5432 billingDW < star-schema.sql

echo "LOADING DATA"

psql -h postgres -U postgres -p 5432 billingDW < dimCustomer.sql

psql -h postgres -U postgres -p 5432 billingDW < dimMonth.sql

psql -h postgres -U postgres -p 5432 billingDW < factBilling.sql

echo "Verify data"
psql -h postgres -U postgres -p 5432 billingDW < verify.sql

echo "Successfully!!!"
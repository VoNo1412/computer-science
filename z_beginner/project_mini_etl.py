import glob
from datetime import datetime 
import xml.etree.ElementTree as ET
import pd as pd

logger_file = "log_file.txt"
target_file = "transformed_data.csv"

class ETL_SOURCES:
    def extract_from_csv(process_file):
        return pd.read_csv(process_file)
    
    def extract_from_json(process_file):
        return pd.read_json(process_file, lines = True)

    def extract_from_xml(process_file):
        df = pd.DataFrame(columns = ["car_model", "year_of_manufacture", "price", "fuel"])
        tree = ETL.parse(process_file)
        root = tree.getroot()

        for el in root:
            car_model = el.find("car_model").text
            year_of_manufacture = el.find("year_of_manufacture").text
            price = float(el.find("price").text)
            fuel = el.find("el").text

            df = df.concat([df, pd.DataFrame({"car_model": car_model, "year_of_manufacture": year_of_manufacture, "price": price, "fuel": fuel})], ignore_index = True)

        return df;

    def extracted_all_file(self):
        df = pd.DataFrame(columns = ["car_model", "year_of_manufacture", "price", "fuel"])
        
        for csv in glob.glob("*.csv"):
            df = pd.concat([df, pd.DataFrame(self.extract_from_csv(csv))], ignore_index=True)
        
        for json in glob.glob("*.json"):
            df = pd.concat([df, pd.DataFrame(self.extract_from_json(json))], ignore_index=True)
        
        for xml in glob.glob("*.xml"):
            df = pd.concat([df, pd.DataFrame(self.extract_from_xml(xml))], ignore_index=True)

        return df;


    def transformed_data(data):
        data['price'] = round(data['price'], 2);
        return data;

    def loaded_data(data):
        return data.to_csv(target_file);

    def logged_file(message):
        timestamp_format = "%Y-%m-%dT%H:%M:%S";
        now = datetime.now()
        timestamp = now.strftime(timestamp_format)

        with open(log_file, "a") as f:
            f.write(timestamp + "," + message + "\n")


etl = ETL_SOURCES()

# STEP 1: EXTRACTED
etl.logged_file("ETL STARTED")
etl.logged_file("EXTRACTED STARTED")
data = etl.extracted_all_file()
etl.logged_file("EXTRACTED ENDED")

# STEP 2: TRANSFORM
etl.logged_file("TRANSFORM STARTED")
transformed_data = etl.transformed_data(data)
print(transformed_data)
etl.logged_file("TRANSFORM ENDED")

# STEP 3: LOADED
etl.logged_file("LOADED STARTED")
etl.loaded_data(transformed_data)
etl.logged_file("LOADED ENDED")

etl.logged_file("ETL DONE")


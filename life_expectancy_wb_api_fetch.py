import requests
from lxml import etree
import pandas as pd
import codecs
from pathlib import Path

# The exact 2026 API path for Life Expectancy
url = "https://api.worldbank.org/v2/country/all/indicator/SP.DYN.LE00.IN?format=xml&per_page=3500&date=2018:2024"

# headers = {
#     'User-Agent': 'Mozilla/5.0',
#     'Accept': 'application/xml'
# }

try:
    response = requests.get(url,  timeout=15)
    response.raise_for_status()

    xml_content_str = response.content.decode('utf-8-sig').strip()

    # Verify that the content starts with '<'
    if xml_content_str.startswith('<?xml') or xml_content_str.startswith('<wb:wb'):
        
        
        tree = etree.fromstring(xml_content_str.encode('utf-8')) 
        

        ns = {"wb": "http://www.worldbank.org"}
        records = []
        
        for data_node in tree.xpath("//wb:data", namespaces=ns):
            country_node = data_node.find("wb:country", namespaces=ns)
            year_node = data_node.find("wb:date", namespaces=ns)
            value_node = data_node.find("wb:value", namespaces=ns)

            if value_node is not None and value_node.text:
                records.append({
                    "country": country_node.text if country_node is not None else "N/A",
                    "year": year_node.text if year_node is not None else "N/A",
                    "value": value_node.text
                })

        df = pd.DataFrame(records)
        if not df.empty:
            df.dropna()
            df.sort_values(by=['year','country'], ascending=[False, True], inplace=True)
            df["year"] = pd.to_numeric(df['year'], errors='coerce')
            df["value"] = pd.to_numeric(df["value"], errors='coerce')
            df["value"] = df["value"].round(2)
            print(f"Success: {len(df)} records parsed and loaded into DataFrame.")
            print(df.head(20))
            file_path = Path(r"C:\Users\IVY\Documents\Life_expectancy.csv")
            df.to_csv(file_path, index=False)
        else:
            print("XML was valid but contained no data for these dates.")
            
    else:
        # This branch is now only for genuine HTML errors
        print("Error: Server returned actual HTML/text instead of expected XML.")

except requests.exceptions.RequestException as e:
    print(f"Connection Error: {e}")


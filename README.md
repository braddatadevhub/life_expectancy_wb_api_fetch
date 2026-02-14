# Life Expectancy Data Ingestion (World Bank API)

This project implements a **Python-based data ingestion pipeline** that retrieves life expectancy data from the World Bank API and prepares it for analysis.

The workflow focuses on **reliable API consumption**, structured XML parsing, data validation, and transformation into an analysis-ready format. This script can be adapted to scrape similar structured websites.

---

## Features

- Fetches life expectancy data from the World Bank public API
- Handles XML responses with namespace-aware parsing
- Validates response format before processing
- Normalizes and cleans numeric values
- Sorts and prepares data for analytical use
- Exports structured data to CSV format

---

## Data Source

- **World Bank API**
- Indicator: *Life expectancy at birth, total (years)*
- Time range: 2018–2024
- Coverage: All available countries

---

## Project Workflow

### 1. Extract
- Sends a request to the World Bank API with timeout handling
- Verifies that the response is valid XML
- Parses XML content using lxml with namespace support

### 2. Transform
- Extracts country, year, and indicator values
- Converts year and indicator values to numeric types
- Handles missing or invalid records
- Rounds values for consistency
- Sorts data by year and country

### 3. Load
- Writes the cleaned dataset to CSV format
- Produces an analysis-ready file suitable for reporting or visualization

---

## Technologies Used

- Python
- Requests
- lxml (XML parsing)
- Pandas

---

## Output

The resulting dataset includes:
- Country
- Year
- Life expectancy value (years)

All numeric fields are validated and formatted for analytical workflows.

---

## Use Cases

- Demographic and health data analysis
- API data ingestion demonstrations
- ETL pipeline development
- Integration with dashboards or analytics tools
- Foundation for automated or scheduled data pipelines

---

## Notes

This project emphasizes **robust API handling and data integrity**.  
The pipeline can be extended to:
- Support additional indicators or date ranges
- Persist data to databases or cloud storage
- Run as part of a scheduled or containerized workflow

---

## Author

Developed by **BRADLEY**

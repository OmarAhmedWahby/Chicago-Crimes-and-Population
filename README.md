# 📊 Chicago Crime & Demographics Analysis (2023–2025)

This project provides a comprehensive, data-driven exploration of crime incidents in Chicago, using real-time data from the Chicago Police Department
The analysis covers over **650,000+ reported crimes** from **2023 to the present**, with a focus on identifying **trends, crime hotspots, and socio-demographic factors** that may influence crime rates across the city

It combines crime reports with demographic, economic, and community-level data to uncover patterns and generate actionable insights for policy-making, public safety, and urban planning

---
## 🗂️ Data Sources

This project combines multiple datasets to provide a comprehensive view of crime and community trends in Chicago. Due to the size and dynamic nature of the data (650,000+ records), raw files are not hosted directly in this repository.

### 📌 Main Sources:
1. **Chicago Crime Data (2023–Present)**  
   - Source: [Chicago Data Portal](https://data.cityofchicago.org/resource/ijzp-q8t2.json
   - Updated via automated scripts (not included here due to size and frequency)
   - +650K crime records with full details: location, time, type, arrest status, etc

2. **Community Area Demographics (ACS & City Data)**  
   - Source: U.S. Census Bureau + City of Chicago Open Data
   - Contains population, income, education, and age group distribution per area.

3. **Community Hardship Index**  
   - Source: City of Chicago  
   - Includes metrics like poverty %, unemployment %, education level, etc.

4. **Ward Office Data**  
   - Source: Chicago Ward Offices dataset  
   - Provides city service zones and political boundaries.

5. **Time & Date Dimension Tables**  
   - Generated using custom Power BI scripts to allow temporal analysis (hour, day, quarter, holidays, etc).

### ⚠️ Note:
- To reduce repository size, raw data is processed externally and only the **cleaned, optimized model** is used in Power BI.
- Data update scripts and pipeline details can be shared upon request or linked in a separate GitHub Actions / Notebook repo.

---
## 📘 Data Model Overview


### 🔹 1. `chicago_crime_data_incremental`
| Column          | Description                                  |
|------------------|----------------------------------------------|
| `arrest`         | Indicates if an arrest was made.             |
| `beat`           | Police beat where the incident occurred.     |
| `block`          | Block address of the crime.                  |
| `case_number`    | Unique identifier for the case.              |
| `community_area` | ID linking to the community area.            |
| `danger_level`   | Custom metric indicating crime severity.     |
| `date`           | Date of the incident.                        |
| `date_Time`      | Full datetime of the crime.                  |
| `description`    | Textual description of the incident.         |

---

### 🔹 2. `district`
| Column         | Description                      |
|----------------|----------------------------------|
| `district`     | Police district number.          |
| `district_sid` | Secondary district identifier.   |

---

### 🔹 3. `fbi_codes`
| Column            | Description                         |
|--------------------|-------------------------------------|
| `fbi_codes`        | Official FBI classification code.   |
| `crime_description`| FBI-level crime category.           |

---

### 🔹 4. `Community_Area_level`
| Column                                                  | Description                                       |
|----------------------------------------------------------|---------------------------------------------------|
| `COMMUNITY AREA NAME`                                   | Name of the community area.                       |
| `Community Area Number`                                 | Unique ID for the community area.                 |
| `HARDSHIP INDEX`                                        | Composite score for socio-economic hardship.      |
| `NORM INCOME`, `NORM INCAP`, `NORM POP`                 | Normalized values for income, incapacity, and population. |
| `PER CAPITA INCOME`                                     | Average income per individual.                    |
| `PERCENT AGED 16+ UNEMPLOYED`                           | % of unemployed people aged 16 and above.         |
| `PERCENT AGED 25+ WITHOUT HIGH SCHOOL DIPLOMA`          | % of adults lacking high school education.        |
| `PERCENT AGED UNDER 18 OR OVER 64`                      | % of dependent age population (youth and elderly).|

---

### 🔹 5. `Community_Area (with Demographics)`
| Description |
|-------------|
| Contains over 50+ fields including: |
- Age brackets: `Age 0-17`, `18-24`, ..., `65+`
- Gender breakdowns: `Total Male`, `Total Female`
- Ethnicity: `White`, `Black`, `Asian`, `Hispanic`, `Other`
- Income Segments
- Population size (`Total Population`)
- Record metadata (`Record ID`)

---

### 🔹 6. `IUCR_Codes`
| Column                | Description                            |
|------------------------|----------------------------------------|
| `INDEX CODE`           | Top-level crime category index.        |
| `IUCR`                 | Illinois Uniform Crime Reporting code. |
| `PRIMARY DESCRIPTION`  | General crime category.                |
| `SECONDARY DESCRIPTION`| Specific sub-type of the crime.        |

---

### 🔹 7. `Date`
| Column       | Description                    |
|--------------|--------------------------------|
| `Date`       | Full date.                     |
| `Day`, `DayName`, `Day in Week` | Breakdown of day details.     |
| `IsHoliday`  | Boolean for holiday flags.     |
| `Month`, `Quarter`, `Year` | Standard calendar fields. |

---

### 🔹 8. `Time`
| Column         | Description                      |
|----------------|----------------------------------|
| `Hour`, `Minute`, `Second` | Time breakdown.        |
| `Period`       | AM/PM or custom segment.         |
| `Time Category`| Grouped time buckets.            |

---

### 🔹 9. `ChicagoWardOffices`
| Column              | Description                          |
|----------------------|--------------------------------------|
| `ADDRESS`, `ALDERMAN`, `CITY` | Political location details. |
| `CITY HALL ADDRESS`, `PHONE` | Contact information.         |
| `CITY HALL ZIPCODE`, `LOCATION` | Location and ZIP code.    |

---

### 🔹 10. `Measure Table`
| Description |
|-------------|
| Contains all calculated measures and KPIs including: |
- `Total Crimes`, `Arrest Rate`, `Domestic Crime Rate`
- Crime breakdowns by gender and race
- Age-based crime analysis
- Socio-economic indicators (`% Below Poverty`, `% Unemployed`, etc.)

---

### 🔹 11. `Parameter` & `Tables`
| Description |
|-------------|
| Tables used to control dynamic filtering, parameter selection, and slicers within the Power BI dashboard. |

---

🎯 This model was designed to enable deep exploration of:
- Crime distribution over time and communities
- The influence of socio-economic conditions on crime
- Demographic patterns linked to criminal activity


---

## Snapshots

![Dashboard Preview](Chicago/Chicago_Crimes%20(1)_page-0001.jpg)

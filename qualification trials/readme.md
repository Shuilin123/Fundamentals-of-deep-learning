# Practical Test Questions

## Question 1: Electric Vehicle Charging Pile Analysis (10 Points)

### User Basic Profile Table (dsjjs_cdzfx01)

| Field Code | Field Name | Field Type | Field Description |
|--|--|--|--|
| cons_id | Unique Identifier for User Archives | varchar | Unique identifier for user archives |
| cons_no | Electricity Customer Number | varchar |  |
| trade_code | User Classification | varchar |  |
| build_date | First Establishment Date | varchar |  |
| notify_mode | Notification Method for Monthly Electricity Bill | varchar |  |
| run_cap | Operating Capacity (kVA) | varchar |  |
| lode_attr_code | Importance Level of Load | varchar | Importance level of load (1: Class I; 2: Class II; 3: Class III) |
| ps_date | First Power Supply Date | varchar | First date of power supply |
| org_no | Power Supply Unit | varchar | Power supply unit |

### Charging Pile Information Table (dsjjs_cdzfx02)

| Field Code | Field Name | Field Type | Field Description |
|--|--|--|--|
| cons_id | Unique Identifier for User Archives | varchar | Unique identifier for user archives |
| char_cons_type | Charging Facility User Type | varchar |  |
| char_type | Charging Station Type | varchar | Public; Dedicated |

### Daily Electricity Consumption Information Table (dsjjs_cdzfx03)

| Field Code | Field Name | Field Type | Field Description |
|--|--|--|--|
| cons_no | Electricity Customer Number | varchar | Electricity customer number |
| ds | Charging Date | varchar |  |
| p_e | Daily Electricity Consumption (kWh) | varchar |  |

#### Peak Season Charging Analysis

- **Time Range**: 'YYYY-07-01 to YYYY-09-30'
- **Charging Duration Calculation**: Daily Electricity Consumption (kWh) / Operating Capacity (kVA)
- **Filtering Criteria**:
  - Load importance level: Class III
  - Charging station type: Dedicated
  - Charging date: Weekends
- **Sorting**: Charging duration (descending)
- **Export Result**: Save as 3-1.csv

| Customer Number | Charging Duration |
|--|--|
| ... | ... |

#### Charging Interval Over 7 Days Analysis

- **Condition**: Daily Electricity Consumption < 0.1 considered as no charging
- **Filtering**: Charging intervals > 7 days
- **Export Result**: Save as 3-2.csv

| Customer Number |
|--|
| ... |

## Question 2: Wind Turbine Fault Diagnosis (15 Points)

### Dataset Description

- **Wind Turbine Operation Monitoring Data (dsjjs_fdyx)**
  - Contains 28 attributes, including time, wind_speed, generator_speed, power, etc.

- **Wind Turbine Blade Fault Period Table (dsjjs_failure)**
  - Contains startTime, endTime

- **Wind Turbine Blade Normal Period Table (dsjjs_normal)**
  - Contains startTime, endTime

### Analysis Tasks

1. **Data Loading and Labeling**
   - Read dsjjs_fdyx.csv
   - Determine the time period and add a label column (normal, failure, invalid)
   - Export the result as 5-1.csv

2. **Sample Statistics**
   - Calculate the proportion of normal, failure, and invalid samples
   - Export the result as 5-2.csv

3. **Imbalanced Sample Handling**
   - Under-sampling: Select all failure samples and a random selection of normal samples (twice the number of failure samples)
   - Combine and discard invalid samples, convert labels to numeric (normal: 1, failure: 0)
   - Export the result as 5-3.csv

4. **Sample Classification**
   - Remove the time feature, split the dataset into training (70%) and testing (30%) sets
   - Train a Random Forest model on the training set and evaluate accuracy on the test set
   - Export the result as 5-4.txt

## Question 3: Electricity as an Indicator of Economic Activity (20 Points)

### Dataset Description

- **Above-Scale Industrial Enterprise Annual Output Value Table (dsjjs_gsqycz)**
  - Enterprise Name, Output Value for the First Half of 2023 (RMB 10,000), Output Value for the First Half of 2022 (RMB 10,000)

- **Above-Scale Industrial Enterprise Industry Classification Table (dsjjs_gsqyfl)**
  - Enterprise Name, Industry Classification, Enterprise Size

- **Above-Scale Industrial Enterprise Electricity Consumption Table (dsjjs_gsqydl)**
  - Account Name, Account Number, Actual Town, Monthly Electricity Consumption (kWh) for 2022 and 2023

### Analysis Tasks

1. **Handle Missing and Abnormal Electricity Data**
   - Replace missing values with 0
   - Replace negative values with the average of adjacent normal months
   - Export the result as 6-1.csv

2. **Summarize Basic Enterprise Information**
   - Merge electricity consumption data with industry classification data
   - Calculate cumulative electricity consumption for H1 2022 and H1 2023, and year-over-year growth rate
   - Classify growth rates as steep increase, steep decrease, or stable
   - Export the result as 6-2.csv

3. **Correlation Analysis Between Electricity Consumption and Output Value**
   - Merge electricity consumption data with output value data
   - Calculate the Pearson correlation coefficient for each industry
   - Export the result as 6-3.csv

4. **Visualize Data**
   - Create a pie chart showing the proportion of electricity consumption by industry for H1 2023
   - Label the chart with electricity consumption values and percentages
   - Export the chart as 6-4.jpg

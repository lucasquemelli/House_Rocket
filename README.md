# House_Rocket

# 1. Business Problems

### Description
---
**House Rocket** is a fictiticious company whose business model is the purchase and sale of real estate.

**Purpose:** find the best business opportunities in the real estate market and maximize the company's revenue. 

**Strategy:** buy properties in good condition at low prices and then resell them at higher prices. 

The dataset used in this projetc contains house sales price for King County (USA) in the period between May 2014 and May 2015. It is available on [Kaggle - House Sales in King County](https://www.kaggle.com/harlfoxem/housesalesprediction). 

House Rocket's CEO set the following **business problems**:
- 1. What properties should we purchase and at what price?
- 2. After the properties are in the company's possession, what is the best time to sell them and what would the sale prices be?
- 3. Should House Rocket do a renovation to raise the sale price? What would be the suggestions for changes? What is the price increase given for each refurbishment option?

### Questions and Requests (Q&R)
---
In order to improve the decision making, the House Rocket's CEO created many sets of questions and requests:

#### Q&R 1.0

1. How many properties are available for purchase?
2. How many attributes do properties have?
3. What are the attributes of the properties?
4. What is the most expensive property? (with the highest sale price)
5. What property has the largest number of bedrooms?
6. What is the total sum of the number of bedrooms in the dataset?
7. How many properties have two bathrooms?
8. What is the average price of all properties in the dataset?
9. What is the average price of the properties with two bathrooms?
10. What is the minimum price for the 3-bedrooms properties?
11. How many properties have more than 300 square meters in the living room?
12. How many properties have more than two floors?
13. How many properties have a water view?
14. Among properties with a water view, how many have three bedrooms?
15. Among properties with more than 300 square meters in the living room, how many have more than two bathrooms?

#### Q&R 2.0

1. What is the date of the oldest property in the portfolio?
2. How many properties have the maximum number of floors?
3. Create a low and high standard classification for properties. Above $540000.00 -> high standard. Below $540000.00 -> low standard.
4. Report ordered by price with the following information:
   - Property ID;
   - Date the property became available for purchase;
   - Number of bedrooms;
   - Total lend size;
   - Price;
   - Property classification.
5. A map where the houses are located geographically.

#### Q&R 3.0

1. Create a column called: house_age. 
   - If the value of the column "date" is greater than 2014-01-01 => 'new_house'.
   - If the value of the column "date" is less than 2014-01-01 => 'old_house'.  
2. Create a column called: dormitory_type.
   - If the value of the column "bedrooms" is equal to 1 => 'studio'.
   - If the value of the column "bedrooms" is equal to 2 => 'apartment'.
   - If the value of the column "bedrooms" is greater than 2 => 'house'.
3. Create a column called: condition_type.
   - If the value of the column "condition" is less than or equal to 2 => 'bad'.
   - If the value of the column "condition" is equal to 3 or 4 => 'regular'.
   - If the value of the column "condition" is equal to 5 => 'good'.
4. Change the type of the column "condition" to string.
5. Delete the columns: sqft_living15 and sqft_lot15.
6. Change the type of the column "yr_built" to date.
7. Change the type of the column "yr_renovated" to date.
8. What is the earliest construction date of a property?
9. What is the earliest date for renovation of a property?
10. How many properties have 2 floors?
11. How many properties have the "condition_type" equals to 'regular'?
12. How many properties have the "condition_type" equals to 'bad' and have a water view?
13. How many properties have the "condition_type" equals to 'good' and "house_age" equals to 'new_house'?
14. What is the price of the most expensive property of the "dormitory_type" which is equal to 'studio'?
15. How many properties of the type 'apartment' were renovated in 2015?
16. What is the largest number of "bedrooms" that a property of the type 'house' has?
17. How many properties of the type 'new_house' were renovated in 2014?
18. Select some columns by their names, by their index and by boolean indexing. 
19. Save a .csv file with columns 10 through 17 only.

#### Q&R 4.0

1. What is the number of properties per year of construction?
2. What is the smallest number of bedrooms per year of construction?
3. What is the highest price per number of bedrooms?
4. What is the sum of the price per number of bedrooms?
5. What is the sum of the price per number of bedrooms and bathrooms?
6. What is the average living room size per year of construction?
7. What is the median property size per year of construction?
8. What is the standard deviation of the living room size per year of construction?
9. Create charts for the price by year, by day and by week.
10. A map to visualize the properties with the highest prices.

#### Q&R 5.0

1. Create a column called: dormitory_type.
   - If the value of the column "bedrooms" is equal to 1 => 'studio'.
   - If the value of the column "bedrooms" is equal to 2 => 'apartment'.
   - If the value of the column "bedrooms" is greater than 2 => 'house'.
2. Draw a bar chart: sum of the prices per number of bedrooms.
3. Draw a line chart: average price per year of construction.
4. Draw a bar chart: average price per dormitory type.
5. Draw a line chart: price per year of renovation - since 1930.
6. Make a table: average price per year of construction and per dormitory type.
7. Create a dashboard with the charts of the questions 02, 03 and 04.
8. Create a dashboard with the charts of the questions 02 and 04.
9. Create a dashboard with the charts of the questions 03 and 05.
10. Create a map with the points proportional to to the living room size. 

#### Q&R 6.0

1. How many properties per level?
   - Level 0: price between $0.00 and $321.950
   - Level 1: price between $321.950 and $450.000
   - Level 2: price between $450.000 and $645.000
   - Level 3: price above $645.000
2. Add the following information to the properties:
   - Street;
   - Number;
   - Neighbourhood;
   - City;
   - State.
3. Add the level of the price as a color in the map.
4. Make the points proportional to the price in the map.
5. Add filters to the map:
   - Water view or not;
   - Value of the price.
6. Add a filter to the last dashboard:
   - Show values only from a specific date.


  


# 2. Business Assumptions

# 3. Solution Strategy

# 4. Top 5 Data Insights

# 5. Business Results

# 6. Conclusions 

# 7. Next Steps

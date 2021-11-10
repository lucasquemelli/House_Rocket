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

Furthermore, in order to improve the decision making, the House Rocket's CEO created 7 sets of questions and requests. Those questions will be seen in "Exploratory data analysis" section.

# 2. Business Assumptions (Formulated Hypothesis)

**Assumptions (hypothesis)** were formulated in order to be tested.

  1. Properties with **waterfront** are **45% more expensive on average** and **40% on median**;
  2. Properties with **construction date earlier than 1950** are **10% cheaper on average** and **15% on median**;  
  3. Properties with **basement** have total area (sqft_living) **25% larger** than those without basement;
  4. The **average price growth** is approximately **10% YoY** (Year over Year); 
  5. **3-bathrooms properties** has a MoM (Month over Month) **growth of 15%**;
  6. Properties **constructed after 2010** are **5% more expensive on average** and **3% on median**;
  7. **Renovated** properties are **30% more expensive on average** and **25% on median**. 

# 3. Solution Strategy

**Step 01 - Exploratory data analysis**: the main goal is better understand the dataset by applying statistics metrics as well as identifying missing values and outliers.

**Step 02 - Feature selection**: identifying the most important attributes related to the price.

**Step 03 - Assumptions test (Hypothesis test) and business problems solutions**: testing the formulated hypothesis and solving the business problems set by the CEO.

**Step 04 - Insights**: the highlight of the main insights.

**Step 05 - Conversion of insights**: converting insights into business results.

**Step 06 - Deploy**: publishing the results to Heroku (cloud environment).

# 4. Top 3 Data Insights

**Hypothesis 1:** Properties with waterfront are 45% more expensive on average and 40% on median.

**True.** Although these properties are more expensive as expected, they are much more expensive than supposed: around 213% and 211% more expensive, on average and on median, respectively. That represents more than five times the hypothesis.

**Hypothesis 2:** Properties with construction date earlier than 1950 are 10% cheaper on average and 15% on median.

**False.** The properties constructed earlier than 1950 are 22.84% of the dataset. Although they are older, these properties are 1.58% and 4.7% more expensive, on average and on median, respectively.

**Hypothesis 7:** Renovated properties are 30% more expensive on average and 25% on median.

**True**. As observed, renovated properties are more expensive. However, they cost 43.36% and 33.93% more, on average and on median, respectively. It is around 50% more than supposed.

# 5. Business Results

- An increase of **10%** in price (profit) for properties which had their **purchase price higher than the median price by region and by season** - depends on the season;
- An increase of **30%** in price (profit) for properties which had their **purchase price lower than the median price by region and by season** - depends on the season;
- An increase of **45%** in price for properties which were **submitted to a renovation in the living area and bathrooms**.

# 6. Conclusions 

# 7. Next Steps

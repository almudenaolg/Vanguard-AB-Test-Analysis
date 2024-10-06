# 🖥️ **Data analysis of A/B Testing project**

## 👥 **Authors**:
[Ana Nofuentes](https://www.linkedin.com/in/ana-nofuentes-solano-654026a3/) & [Almudena Ocaña](https://www.linkedin.com/in/almudena-ocaloga/)

### 📋 **Project overview**
This project analyzed the impact of a **new web design** on user behavior using **A/B Testing**. The main objective was to evaluate whether the new design improved **completion rates** and **user engagement** while minimizing **friction** in the process. We also focused on understanding how different user segments (e.g., age groups, high-value clients) responded to the changes.

### 🔧 **Tools used:**
- **Python in Visual Code**: For data cleaning, analysis, and visualization.
- **Seaborn & Matplotlib**: Visual representation of key metrics.
- **Tableau**: Visualization and dashboards for presenting insights.

### 🛠️ **Project workflow:**
1. **Data cleaning & preparation**:
   - Merged and cleaned raw data to create structured and manageable dataframes for analysis.
   - Created two main dataframes: one with **client information** and **web activity** metrics and another focusing on **step-by-step interaction** details.

2. **Data analysis**:
   - Explored key variables such as **tenure, balance, and age**.
   - Analyzed **completion rates**, **error rates**, and **step performance** to understand user experience across the new and old web designs.
   
3. **A/B Testing**:
   - Compared the **Test and Control groups** using statistical tests to identify significant differences in key performance indicators.
   
4. **Recommendations**:
   - Suggested **targeted improvements** for specific user segments and identified steps in the process that could benefit from optimization.

### 📂 **Project structure:**
- **`data/`**:
  - **`raw/`**:
    - Contains the **original data files**: user demographics, web transactions, and experiment groups.
  - **`clean/`**:
    - Contains the **cleaned final dataframes** used for analysis:
      - `complete_df`: Includes client information, web KPIs, and experiment group.
      - `steps_df`: Contains step-level details for each interaction.

- **`exploratory.ipynb`**: The **initial analysis notebook**, where data exploration and hypothesis testing were conducted.
- **`final.ipynb`**: The **final notebook** summarizing key results and providing a clean version for presentation.
- **`functions.py`**: Contains **helper functions** used for data cleaning and visualization.
- **`requirements.txt`**: Lists all **required libraries** for running the project environment.

### 🖼️ **Presentation of data analysis results**
Our findings were compiled into two engaging presentations to communicate insights effectively:

Tableau Dashboard: Explore our interactive Tableau dashboards for detailed visual analysis. 
[📊 View Tableau Presentation](https://public.tableau.com/views/Tableau_AB_testing_17282090726700/ABTestingresults?:language=es-ES&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

Canva Presentation: Visual storytelling with design elements to present key insights.  [📊 View Canva Presentation](https://www.canva.com/design/DAGSiutyywc/7NYwnC683r7DsM51iH8jwA/edit)

### 🗣️ **Recommendations & next steps**
Based on the findings:
1. **Roll out the new design** as the default version since it shows **higher completion rates**.
2. **Focus on Step 1 and Step 4** to reduce time spent and friction in the process.
3. **Implement accessibility improvements** for older clients to improve their experience.
4. Gather **feedback from high-value clients** to ensure that changes cater to their needs.

By addressing these areas, the new design can **maximize engagement**, **enhance satisfaction**, and lead to **higher long-term retention**

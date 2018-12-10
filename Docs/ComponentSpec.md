## Component Specification    
  
### Software Components  
#### Database  
For our project, the database is a component of read-only structured data set that is organized collectively and can be accessed electronically from a computer system. The inputs are two dataset that are differentiated from two sources. Each of the tables will be manipulated using the pandas package to create outputs of two subsets of the original datasets. The first one is several tables from the MIMIC III which contain various elements of the health records, such as patients information, drug prescription, and diagnoses international classification of diseases (ICD) code. All the tables will be combined together with the relational information from each of the tables. The other subset will be a filtered dataset from NARMS that consists of region, year, antibiotic status, and condition.  
  
#### Query System  
The query component is designed only to read from our database. It will be used as a pipeline for the analysis system and directly for the visualization as well. The query system not only can generate the specific elements from the database, but it also can pass a segmented data based on the keywords that the user wants to work or analyze on.  
  
#### Visualization  
An interactive visualization of the dataset will be part of the final output for this project. This tool helps the user to understand the significance of the data by placing it to the visual context. We will provide several types of data presentation of the dataset, such tables and graphs to show patterns, trends, and correlations from our analysis system. Each of them will use different python packages to be implemented, specifically matplotlib, seaborn, bokeh, and arcGIS.  

#### PDF Output
This component will generate a PDF electronic health report, including basic patient information, antibiotic regime, and recent antibiotic resistance. This will produce a file that can be easily used to guide treatment and be incorporated into the patient record and treatment plan. The component will use PyQty to generate the PDF files. 

#### Graphical User Interface 
A graphical user interface will be developed using PyQty or Pyside to make a user friendly way to query and visualize the data. The user will be able to select individual patients to view their current antibiotic treatment regime and recent antibiotic resistance to guide treatment choices. Users will have the ability to generate a health report in the form of a PDF, incorporating basic patient information, antibiotic regime, and recent antibiotic resistance.  

### Interactions
![Interactions Flow](http://staff.washington.edu/mldorr/wordpress/wp-content/uploads/2018/11/Assignment5Interactions2.png)  
The database is presently a very large CSV file, and contains all of the EHR data that was downloaded from the MIMIC III website, joined to the NARMS dataset.  
  
The Query System is used for querying data from the database. Data files have foreign keys to connect with each other, such as subject_id. Query System can extract useful features or attributes and consolidate the information into a simple table. In this case, all data file from the database could be merged into a single big table, which is convenient for future analysis. In addition, in case-relevant data identified processing, query system can also help extracting useful data from the single big table.  
  
Analysis System helps to analyze the data extracted from the Query System. Statistical methods and other data analysis algorithms are applied in this part. The result of the data analysis would be visualized in the Visualization GUI; plots, histograms, or a heat map may be generated, so that it can be easy to understand the distribution or the relationship between features.  
  
In the Use Case Ex1, users can use a query statement to query the data for features such as condition, patientId, region name and other associated features. The query system would then extract the related attributes and tuples from the database and generate a new table. Then, for example, a plot of the condition versus region heat map could be generated based on the table, so the user can intuitively comprehend the highest and lowest prevalence area based on the color ramp. The Analysis System would also analyze the new table; for example, LASSO regression with coordinate descent algorithm could be applied to help finding out what is the top three features that influence a specific condition. Finally, visualization GUI generates three scatterplots of the condition versus the three top associated features with regression curves on them.  
  
The same process can be followed from Use Case Ex3. Users provide a query statement for the query system, and query system generates a new table of data from database, which includes outbreak number, range, peak and other related information. Then a plot of number of outbreak versus time could be generate based on the table. After that, we can apply PDA, ridge regression or other methods, depending on the distribution of data, to predict outbreak number in the future. Also, we may analyze its features to classify what kind of condition (e.g., influenza strain) it is by applying SVM classifier algorithm. Finally, a scatterplot with regression curve can be generated to show the prediction result.  


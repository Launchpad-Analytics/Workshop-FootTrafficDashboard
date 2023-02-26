# Create a real-time dashboard with Python

Session Overview
================

* * *

"Create a real-time dashboard with Python" is a hands-on technical workshop that will guide attendees through the process of creating a real-time dashboard using Python. The workshop will cover the following topics:

*   Using the Faker package to generate simulated foot traffic data for a big box store with multiple locations across the U.S.
*   Building a data pipeline to clean and store the data in a SQL database.
*   Creating a real-time dashboard using Streamlit to visualize the foot traffic data, that updates in real time as new data is generated.

The attendees will learn how to use the Faker package to generate simulated data, create a data pipeline to clean and store data in SQL and use Streamlit to create a real-time dashboard to visualize the data. The workshop will provide hands-on exercises and projects to help the attendees gain practical experience with the tools and techniques covered in the workshop. By the end of the workshop, attendees will be equipped with the knowledge and skills to create their own real-time dashboards using Python, Faker, SQL and Streamlit.

### Prerequisites:

*   Familiarity with Python programming language
*   Understanding of data visualization and SQL concepts
*   Familiarity with Streamlit is a plus but not required

  

About Launchpad Analytics
-------------------------

  

Launchpad Analytics is a boutique consulting firm that specializes in modern data analytics tools and capabilities. We also work with expert learning designers to curate world-class technical training experiences across a wide range of tools and topics.

  

[

Launchpad Analytics

Modern data analytics

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Flaunchpadanalytics.carrd.co%2F)https://launchpadanalytics.carrd.co/

](https://launchpadanalytics.carrd.co/)

  

Support Our Work!
-----------------

[

ko-fi.com

https://ko-fi.com/kellyhopkins

](https://ko-fi.com/kellyhopkins)

  

Pre-Work
========

* * *

Local Environment Setup
-----------------------

If you are going to be using your local environment while participating in this workshop, make sure you have a Python development environment set up on your computer. We recommend you use an environment management system like [Miniconda](https://docs.conda.io/en/latest/miniconda.html) to ensure you don't run into any conflict issues on your machine. You can download the lab files by cloning the workshop repo here:

  

[

GitHub - Launchpad-Analytics/Workshop-FootTrafficDashboard: Learn how to create a real-time Streamlit app and a realistic synthetic dataset with the Faker Package

Learn how to create a real-time Streamlit app and a realistic synthetic dataset with the Faker Package - GitHub - Launchpad-Analytics/Workshop-FootTrafficDashboard: Learn how to create a real-time ...

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fgithub.com%2FLaunchpad-Analytics%2FWorkshop-FootTrafficDashboard)https://github.com/Launchpad-Analytics/Workshop-FootTrafficDashboard

](https://github.com/Launchpad-Analytics/Workshop-FootTrafficDashboard)

  

After downloading the files, run the following terminal command from the root directory of the repo to create an environment with the necessary packages for this workshop:

  

```bash
conda create --name la-workshop --file requirements.txt -y

conda activate la-workshop
```

If conda fails to install the Folium package, remove it from requirements.txt and run the command again. You can then manually install folium using pip in your conda environment.

  

Also, make sure you are using an IDE that has support for Python and Python notebooks. Otherwise, you will have to add [Jupyter](https://jupyter.org/) to your local installation as well.

  

Using the Deepnote Environment
------------------------------

You can find the link to the Deepnote project with all the lab files pre-loaded below:

  

[

Deepnote

Managed notebooks for data scientists and researchers.

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fdeepnote.com%2Fworkspace%2Flaunchpad-analytics-b49c6ef7-b49e-495d-8bcc-82d4f4b77aa9%2Fproject%2FSQL-Workshop-8ead9ff4-6f0b-4585-8592-e2d5389366f5)https://deepnote.com/workspace/launchpad-analytics-b49c6ef7-b49e-495d-8bcc-82d4f4b77aa9/project/SQL-Workshop-8ead9ff4-6f0b-4585-8592-e2d5389366f5

](https://deepnote.com/workspace/launchpad-analytics-b49c6ef7-b49e-495d-8bcc-82d4f4b77aa9/project/SQL-Workshop-8ead9ff4-6f0b-4585-8592-e2d5389366f5)

  

At the top-right corner of the page, click the "Duplicate" button to make a copy of the project in your account, which will allow you to edit the files (You will be prompted to create a Deepnote account if you don't have one already).

  

![](https://t45028606.p.clickup-attachments.com/t45028606/d277b8f0-3757-447f-af43-642f6e912c9c/image.png)

  

It is advised that you get some familiarity with the Deepnote interface if you're new to the platform prior to the workshop, but it is not required. You can checkout the [Deepnote documentation](https://deepnote.com/docs/deepnote-crash-course) for a guided introduction.

  

  

By completing these pre-work instructions, you will be well prepared to actively participate in the workshop and get the most out of the experience.

  

  

  

Workshop Guide
==============

* * *

In the scenario for this workshop, you will be building a dashboard for a growing specialty grocery chain based in the U.S. The dashboard will track some basic stats about in-store purchases made by a subset of customers throughout the country. We will start by creating a simulated dataset for the company, and then set up a Streamlit app to visualize the data. After our static dashboard is operational, we will move our data and application to the cloud on AWS, where we will incorporate some components to make the dashboard automatically update with new data.

  

Simulating foot-traffic data with the Faker package
---------------------------------------------------

In order to create a realistic simulated dataset for our grocery chain, we will use the [Faker](https://faker.readthedocs.io/en/master/) python package to create three tables:

*   `stores` - Contains information about each store location
*   `customers` - Contains basic information about customers who have made in-store purchases
*   `visits` - Contains records of in-store visits for each customer

  

**The next part of this workshop will be done within the** **`01 - faker-data-simulation.ipynb`** **notebook, located within the root directory of the workshop folder.**

  

### Exercise Answers

*   `generate_customer()` function:
    
    ```plain
    def generate_customer():
    ```
    
*   `generate_customers()` function:
    
    ```plain
    def generate_customers(num_customers):
    ```
    

  

Discussion: What are some advantages and disadvantages of simulating data in this manner?

  

Creating our Streamlit App
--------------------------

Now that we have all of our datasets for this exercise created, we can now begin to explore the data and create visualize them. Data visualizations are only as good as the medium used to share them, so we will explore one of the leading tools for quickly creating interactive data applications.

  

### What is Streamlit?

Streamlit is a powerful and user-friendly tool for creating interactive web applications for data science and machine learning projects. It allows developers and data scientists to quickly and easily build beautiful and informative visualizations, dashboards, and applications without the need for extensive web development knowledge. With its simple, Python-based syntax and intuitive interface, Streamlit makes it easy for anyone to build and share interactive data applications with just a few lines of code.

  

  

[

Streamlit • The fastest way to build and share data apps

Streamlit is an open-source app framework for Machine Learning and Data Science teams. Create beautiful web apps in minutes.

![](https://www.google.com/s2/favicons?domain_url=https%3A%2F%2Fstreamlit.io%2F)https://streamlit.io/

](https://streamlit.io/)

  

### Building the Streamlit App Skeleton

We will start by replicating the 'Hello World" example from the Streamlit docs (linked above).

  

![](https://t45028606.p.clickup-attachments.com/t45028606/dc721c3f-b607-4801-bdce-a844c5843c7e/image.png)

  

  

*   Create a new file in your workspace, titled `app.py` . This file will serve as the script that powers your Streamlit app.
*   At the top of the python file, import the `streamlit` module and alias it as `st` .
*   Use the [st.write()](https://docs.streamlit.io/library/api-reference/write-magic/st.write) method to print a simple "Hello World" message at the top of the app.
*   Save your file and in a new terminal, run the command `streamlit run app.py` to start the application.
*   If you are running a terminal from within an IDE, use the command `python -m streamlit run app.py` .
*   Streamlit is set to run on port `8051` by default, so make sure your browser is pointed to that location.

  

Example `app.py` :

```python
import streamlit as st

st.write("Hello, World!)
```

  

Terminal output:

![](https://t45028606.p.clickup-attachments.com/t45028606/d7ffc7c2-6626-44b3-b28d-6f16e4490a1b/image.png)

  

Browser View:

![](https://t45028606.p.clickup-attachments.com/t45028606/01bf7ab7-eae1-413f-bfec-c417ec796e46/image.png)

  

### Building our Dashboard

As we can see with the lightning-fast setup process, Streamlit makes it incredibly easy to get up and running with a basic web application by abstracting away a lot of the tricky configuration details necessary to get a server running. This allows us to focus on creating visuals and communicating insights to our audience.

  

We will start by adding a title and subtitle to our dashboard by editing the text inside the `st.write()` method. This method allows us to use markdown syntax to specify an H1 tag and subtitle for our app.

  

Example `app.py` :

```plain
import streamlit as st




st.write("""
# Foot Traffic Dashboard
Overview of In-Store Performance
""")
```

  

Streamlit supports hot-reloading functionality, where saving new changes to our app file triggers the server to automatically reload and display the new changes. To enable this feature in the browser, select the "Always rerun" option in the top-right corner of the browser window.

  

![](https://t45028606.p.clickup-attachments.com/t45028606/e5208f19-9fe6-4f99-a638-0fd8e5a8ad6d/image.png)

  

![](https://t45028606.p.clickup-attachments.com/t45028606/0154fc8f-6450-4c36-ae79-148d994dec09/image.png)

  

### Displaying Data

The `st.write()` method is a flexible utility that allows us to format and display a number of different elements on screen. This includes the ability to display a data table or Dataframe in an interactive table view. We will do this now by loading the `stores` , `customers` , and `visits` tables into Pandas dataframes with a simple `load_data()` function.

  

*   Checkpoint `app.py` :
    
    ```plain
    import streamlit as st
    ```
    
      
    

  

### Adding the First Charts

Streamlit provides a number of native [chart elements](https://docs.streamlit.io/library/api-reference/charts) that allow you to quickly generate visuallizations for your app, and it also provides wrappers for other popular viz libraries like Plotly, Altair, and Bokeh. Under the datatable we created earlier, we will create a simple line chart that shows the volume of visits for each day represented in the dataset:

```python
st.subheader("Visits by Day")
visits_by_day = visits.groupby("visit_date").size()
st.line_chart(visits_by_day)
```

Because the dataset we're using is randomly generated, there will be a lot of extreme variation in the line chart. If we wanted a slightly smoother line, we could experiment with taking the average visits per day across larger intervals of time, such as a weekly or monthly average:

```python
visits_by_day = visits.groupby("visit_date").size().resample("2W").mean()
```

  

Next, we're going to use another streamlit-native chart type, which is the [scatterplot map](https://docs.streamlit.io/library/api-reference/charts/st.map). This chart type takes a dataframe with a longitude and latitude column and plots each coordinate pair on a standard base map layer. Recall that our `stores` table has the columns `latitude` and `longitude` , so we can pass the dataframe directly to the `st.map()` function. We will plot this map below the `visits_by_day` section.

```plain
st.subheader("Store Locations")
st.map(stores)
```

  

### Input Controls and Data Display

Remember the data table we added at the top of our app? We want to to add the functionality to hide and reveal the underlying data, so we will add a simple check box to create this toggle feature. Streamlit provides a number of different [input elements](https://docs.streamlit.io/library/api-reference/widgets) to help add even more interactivity. Here is how we would use the `st.checkbox()` element to implement a "Show Data" control for the `visits` table:

  

```plain
if st.checkbox("Show Data"):
    st.write(visits.head(25))
```

Discussion: Notice that the app is slow to load the data? Try the @st.cache decorator to save on expensive data read operations.

  

  

What does every good dashboard need? KPIs! Up until now, we've been placing all of our elements right under each other in a single list, but we want to put a row of numbers across the top of our app that will display certain metrics for our dataset. The [st.columns()](https://docs.streamlit.io/library/api-reference/layout/st.columns) method can be used to specify a number of columns to divide your view. We will be exploring a couple ways to use `st.columns()` to create layouts, starting with the row of KPIs which will sit directly above the "Visits by Day" chart:

  

```plain
col1, col2, col3 = st.columns(3)
col1.metric("Active Customers", customers.shape[0])
col2.metric("Total Visits", visits.shape[0])
col3.metric("Total Revenue", f"${round(visits.order_total.sum() / 1000000, 2)}M") 
```

  

Exercise: What other KPIs could be useful for our foot traffic data? Come up with 2-3 additional metrics, and explain why they would be important to have on this dashboard. As a bonus, try to write the code to calculate them and add them to your Streamlit app.

  

You can use the second notebook for this workshop, `02 - dashboard-analysis.ipynb` to complete this exercise.

  

*   Checkpoint `app.py` :
    
    ```plain
    import streamlit as st
    ```
    
      
    

  

Answers to Workshop Exercises
-----------------------------

* * *

  

Wrap Up
=======

* * *

  

Additional Resources
--------------------

* * *
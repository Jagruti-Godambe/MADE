# Exercise Badges

![](https://byob.yarr.is/Jagruti-Godambe/MADE/score_ex1) ![](https://byob.yarr.is/Jagruti-Godambe/MADE/score_ex2) ![](https://byob.yarr.is/Jagruti-Godambe/MADE/score_ex3) ![](https://byob.yarr.is/Jagruti-Godambe/MADE/score_ex4) ![](https://byob.yarr.is/Jagruti-Godambe/MADE/score_ex5)

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.
Before you begin, make sure you have [Python](https://www.python.org/) and [Jayvee](https://github.com/jvalue/jayvee) installed. We will work with [Jupyter notebooks](https://jupyter.org/). The easiest way to do so is to set up [VSCode](https://code.visualstudio.com/) with the [Jupyter extension](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter).

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.
2. Setup the exercise feedback by changing the exercise badge sources in the `README.md` file following the patter `![](https://byob.yarr.is/<github-user-name>/<github-repo>/score_ex<exercise-number>)`. 
For example, if your user is _myuser_ and your repo is _myrepo_, then update the badge for _exercise 1_ to `![](https://byob.yarr.is/myrepo/myuser/score_ex1)`. Proceed with the remaining badges accordingly.


## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to html: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervalls, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/). At the end of the semester, you will therefore have the following files in your repository:

1. `./exercises/exercise1.jv`
2. `./exercises/exercise2.jv`
3. `./exercises/exercise3.jv`
4. `./exercises/exercise4.jv`
5. `./exercises/exercise5.jv`

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions -> Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```

# PROJECT OVERVIEW

## Analyzing the Impact of Climate Change on Crop Production and CO2 Emissions in the USA (1990-2015)

This Project aims to analyze and find the co relation between Crop production and Co2 emission in USA region from year 1990 to 2015.

## Technologies Used
1. `Data Analysis: Python (Pandas)`
2. `Visualization: Matplotlib`
3. `Version Control: Git, GitHub`

## Datasets

### Crop Production & Climate Change
This dataset, sourced from Kaggle, provides information on crop yields, harvested areas, and production quantities for key crops such as wheat, maize, rice, and soybeans. Crop yields are measured in tonnes per hectare, with data available from 2010-2016.

### CO2 Emissions
This dataset, also from Kaggle, offers a comprehensive overview of CO2 emissions by country from 1960 to 2023. It includes annual CO2 emission data for all countries worldwide.

## Analysis
The analysis focused on examining the trends in crop production and CO2 emissions over the 25-year period. Methods included statistical analysis and visualization to interpret the data patterns.

<img src="data\data/Screenshot 2024-07-03 at 20.48.09.png">


## RESULTS:
Showed variability over the period, influenced by factors such as industrial activities and changes in energy consumption.CO2 emissions showed a VARIABILITY.
Demonstrated a consistent increase despite variability, driven by advancements in agricultural technology and practices, as well as natural climate variability.


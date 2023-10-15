# Weekly Meal Plan Maker

#### Video Demo:  <https://youtu.be/DdUETc1vdOo>

#### Web App Access Link: <http://mealplanmaker.pythonanywhere.com>

This is my final project for CS50's Web Programming with Python and Javascript Course.
As the capstone project for this course, my task was to design and implement a dynamic web application, albeit with a few requirements and constraints.

I will be discussing the distinctiveness and complexity of my project, what each file contains, how to run this application and any other additional information needed.

My initial idea for this project was to create an application that would allow users to create a weekly meal plan, and for said application to automatically calculate macronutrients(fats, carbs, and proteins) as well as general calories as a daily average based on the meals selected. 

Having always been interested in fitness, I know that nutrition is just as important, if not more, than working out for both losing weight (burning fat and getting leaner) or gaining weight (muscle size).

However, one of the main things I hear people complain about is that counting calories is hard enough, let alone figuring out and tracking macros (fats, carbs, and proteins). I wanted to find a way to make this whole ordeal easier instead of tracking macros meal by meal after consuming said meal, which would be a tedious manual task that requires a lot of self-discipline in the long run, and which I believe is one of the main reasons people would want to lose or gain weight tend to give up. 

Planning your meals ahead is what I found to be the easiest way to implement this. By creating meals you tend to eat more often than not, and allocating them to a specific day of the week, you would implement some form of reverse tracking, where you try to stick to the plan you created. Furthermore, this would save a lot of time having to decide what to eat, and you can just bring your plan at the store when doing your groceries to make sure you always have all the ingredients needed. 
Furthermore, some people tend to meal prep in advance for the next few days by cooking a big batch of whatever meals repeat for the next few days in their plan, saving them even more time in the process.

This is where my web application comes in, I have done extensive research on the nutrition values of the most common foods and divided them into three sources based on the three macronutrients (fats, carbs and proteins) and populated a database of Django models with said values. When creating a meal by selecting different ingredients and quantities, my application will automatically calculate the calories and macros for said meal. 
After allocating your meals to the seven days of the week, my application will calculate a daily average based on your weekly plan, and output average calories, grams of fat, carbs and protein. This makes the process of making a meal plan for fitness purposes very quick and as frictionless as possible.

One great thing about this app is that there are no hard limits as to how many meals per day you can have or even if there needs any food in a given day. This makes this app fully functionning and inclusive for people practicing any form of fasting, whether that be intermittent fasting (breakfast skipping), or full day fasting (a practice becoming more and more common where people eat 5 days of the week and fast for 2 days for example). 

## How to use this web app

This app is comprised of three main parts:

- TDEE Calorie Calculator
- Single Meal Creator
- Weekly Plan Maker

The TDEE Calculator can be accessed and used without creating an account, while the other two functionalities require an account to be created or a user to be logged in in order to create and save meals to the database, as well as implement a weekly plan based on a selection of those meals, followed by a calculation of macronutrients and average daily calories.

###### TDEE Calorie Calculator

Total Daily Energy Expenditure, or TDEE, is an estimation of how many calories your burn per day when your activity level is taken into account. 
It is calculated by first figuring out you Basal Metabolic Rate (BMR), which is roughly how many calories your body burns by just simply living, or in layman's terms, how many calories your body would burn if you were to just lay in bed all day never moving an inch. 
This is calculated using a mathematical formula called the The Harris–Benedict equation, which uses physical characteristics such as age, gender, height, and weight. 
It is then multiplied by an activity level factor, which is based on factors such as exercise and whether a person has a sedentary or very active job.

This in turn gives you an estimation of how many calories you *should* eat in a given day.

There are limitations to this calculation though, as stated in my web app:
> This is an average figure using the Harris–Benedict equations revised by Mifflin and St Jeor, an equation predictive for modern lifestyles. It does not account for lean body mass and body composition, meaning total daily energy expenditure might be a little higher for a very lean and muscular individual, while slightly lower for a plus size individual.

The TDEE was written in JavaScript, allowing me to make the calculation instantaneous, and which recalculates and updates every time the user types or changes anything in the form, instead of having to click a button every time.

###### Single Meal Creator

The Single Meal Creator functionality allows a user to create a meal. 
The user is prompted to give the meal a title, select food sources and input a quantity for each source.
By saving the meal, the application calculates how many grams of fat, carbs and protein each meal has in total based on the food sources contained in said meal, before saving all those figures in a Django model.

Below the form, the user can see all the meals he has created, including the calories and macros for that meal. He/She can also delete the meal. Since creating a meal is such as easy and short task, I decided not to let the user edit a meal but simply delete it, which makes the user experience simpler.

###### Weekly Plan Maker

After having created as many meals as needed through the Single Meal Creator, users can finally add said meals to their weekly meal plan. 
The index page for this app is the weekly plan maker, which allows users to select from a dropdown of all their meals, and add them to any day of the week.
Below the selection form is a weekly plan outputting each meal for each day of the week. Meals can be deleted one by one from any of the days.

At the bottom of the page, the web app calculates average calories and macros, and outputs the results both in numerical values, and as a donut chart showing which percentage of which macro makes up for the total amount of calories. This is important as many people are not aware than fats account for many more calories than carbs and protein, as 1 gram of fat is 9 calories, while 1 gram of both carbs and protein are 4 calories.

### Project Requirements

Although the nature of the application was completely up to me, there were a few requirements to be satisfied. These are:

- My application must be sufficiently distinct from other projects in this course
- It must utilize Django on the back-end, including at least one model, and JavaScript on the front-end.
- My web application must be mobile-responsive

### Distinctiveness and Complexity

This web app is quite distinct from any of the projects from CS50's Web Programming Course. It is a meal plan maker where users get to create their own meals based on their personal preferences for food sources and quantities. 

This app is built on the Django framework and is comprised of many models. Each macronutrient source has its own model object which gets called when calculating the figures for a meal. Each meal gets saved as an object in order to be able to be used later when implementing a weekly plan. The weekly plan itself is a model, which allows for a daily average calculation of calories and macros.

Javascript is used on the front end for two main functionalities. The TDEE calculator uses Javascript's "onkeydown" and "onchange" methods which allowed me to make that part very interactive by constantly re-calculating the user's calories every time he types of changes anything in the form.
Furthermore, the donut chart visualizing the percentages of calories by macronutrient source at the bottom of the weekly meal plan was also implemented using JavaScript.
Most of the styling in this app was done using Bootstrap, and my app is fully mobile-responsive.


### Hosting

Since this is the best project I made so far in my short life as a developer, I wanted to get hosting and make my website available online. 
After doing some research online, I found two main options that had a free plan offering, [pythonanywhere](https://www.pythonanywhere.com/) and [Heroku](https://www.heroku.com/).

I decided to go with pythonanywhere, and after a little bit of struggle, I managed to get it to work.
Here is a [link](http://mealplanmaker.pythonanywhere.com/) to it.



# Day 38 - 100 Days of Code: The Complete Python Pro Bootcamp for 2023

## Workout Tracking application - Tracking your exercises using Python and Google Sheets

### Step 1: Google Sheets https://docs.google.com/spreadsheets/u/0/
- Create a new sheet on Google Sheets, e.g.:

![image](https://github.com/CristinaAlina/workout-tracking/assets/148490551/74bebc36-d558-4c32-86e1-b6bebf18acce)

### Step 2: Connect to [Nutritionix](https://www.nutritionix.com/)
- Get your app id and api key from https://www.nutritionix.com/business/api
- Get input from user (e.g. input("Tell me which exercises you did: "))
- Use the user input for POST request to Nutrionix: [natural-language-for-exercise](https://developer.syndigo.com/docs/natural-language-for-exercise) to get parse json data from the input


### Step 3: Use the response json specific data from it and make a POST request to Sheety, to add a new row with data on Google Sheets:
- Connect your Google Sheets account with Sheety to get access, on https://sheety.co/
- Create a new project on Sheety using the sheet template from Google Sheets url
- Change your settings on Sheety to Enable GET and POST methods
- Choose an authentication method on Sheety project
- Use POST method to add a new row with exercise data: [Making requests](https://sheety.co/docs/requests.html)


## Result for input "I swam for 3 hours":
![image](https://github.com/CristinaAlina/workout-tracking/assets/148490551/8d27dd3b-8348-45ab-b020-edb7dae1bd81)

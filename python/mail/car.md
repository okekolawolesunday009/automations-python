Sales summary
In this section, let's view the summary of last month's sales for all the models offered by the company. This data is in a JSON file named car_sales.json. Let's have a look at it.

cat ~/car_sales.json
Copied!
Output:

[{"id":1,"car":{"car_make":"Ford","car_model":"Club Wagon","car_year":1997},"price":"$5179.39","total_sales":446},
{"id":2,"car":{"car_make":"Acura","car_model":"TL","car_year":2005},"price":"$14558.19","total_sales":589},
{"id":3,"car":{"car_make":"Volkswagen","car_model":"Jetta","car_year":2009},"price":"$14879.11","total_sales":825},
{"id":4,"car":{"car_make":"Chevrolet","car_model":"Uplander","car_year":2006},"price":"$17045.06","total_sales":689},
{"id":5,"car":{"car_make":"Plymouth","car_model":"Roadrunner","car_year":1969},"price":"$14770.44","total_sales":691},
{"id":6,"car":{"car_make":"GMC","car_model":"Safari","car_year":2000},"price":"$13390.83","total_sales":531},
{"id":7,"car":{"car_make":"Lamborghini","car_model":"Murciélago","car_year":2003},"price":"$7267.94","total_sales":374},
{"id":8,"car":{"car_make":"GMC","car_model":"3500","car_year":1999},"price":"$19292.10","total_sales":638},
{"id":9,"car":{"car_make":"Maybach","car_model":"62","car_year":2004},"price":"$11020.45","total_sales":945},
{"id":10,"car":{"car_make":"Chevrolet","car_model":"Cavalier","car_year":2001},"price":"$10708.87","total_sales":870},
To simplify the JSON structure, here is an example of one of the JSON objects among the list.

{
        "id": 47,
        "car": {
                "car_make": "Lamborghini",
                "car_model": "Murciélago",
                "car_year": 2002
        },
        "price": "$13724.05",
        "total_sales": 149
}
Copied!
Here id, car, price and total_sales are the field names (key).

The script cars.py already contains part of the work, but learners need to complete the task by writing the remaining pieces. The script already calculates the car model with the most revenue (price * total_sales) in the process_data method. Learners need to add the following:

Calculate the car model which had the most sales by completing the process_data method, and then appending a formatted string to the summary list in the below format:
"The {car model} had the most sales: {total sales}"
Calculate the most popular car_year across all car make/models (in other words, find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year) by completing the process_data method, and append a formatted string to the summary list in the below format:
"The most popular year was {year} with {total sales in that year} sales."
The challenge
Here, you are going to update the script cars.py. You will be using the above JSON data to process information. A part of the script is already done for you, where it calculates the car model with the most revenue (price * total_sales). You should now fulfil the following objectives with the script:

Calculate the car model which had the most sales.
a. Call format_car method for the car model.

Calculate the most popular car_year across all car make/models.
Hint: Find the total count of cars with the car_year equal to 2005, equal to 2006, etc. and then figure out the most popular year.
open cars.py python script in the nano editor.

nano ~/scripts/cars.py
Copied!
The code is well commented including the TODO sections for you to understand and fulfill the objectives.

Generate PDF and send Email
Once the data is collected, you will also need to further update the script to generate a PDF report and automatically send it through email.

To generate a PDF:

Use the reports.generate() function within the main function.

The report should be named as cars.pdf, and placed in the folder /tmp/.

The PDF should contain:

A summary paragraph which contains the most sales/most revenue/most popular year values worked out in the previous step.
Note: To add line breaks in the PDF, use: <br/> between the lines.
A table which contains all the information parsed from the JSON file, organised by id_number. The car details should be combined into one column in the form <car_make> <car_model> (<car_year>).
Note: You can use the cars_dict_to_table function for the above task.
Example:

ID

Car

Price

Total Sales

47

Acura TL (2007)

€14459,15

1192

73

Porsche 911 (2010)

€6057,74

882

85

Mercury Sable (2005)

€45660,46

874

To send the PDF through email:

Once the PDF is generated, you need to send the email, using the emails.generate() and emails.send() methods.

Use the following details to pass the parameters to emails.generate():

From: automation@example.com
To: student@example.com
Subject line: Sales summary for last month
E-mail Body: The same summary from the PDF, but using \n between the lines
Attachment: Attach the PDF path i.e. generated in the previous step
Once you have completed editing cars.py script, save the file by typing Ctrl+o, Enter key, and Ctrl+x.

Grant the executable permissions to the file cars.py.

sudo chmod +x ~/scripts/cars.py
Copied!
Run the cars.py script, which will generate mail to their user.

./scripts/cars.py
Copied!
Now, check the webmail for any new mail. You can click on the Refresh button to refresh your inbox.

Output:

image4.png

Open cars.pdf that's located on the right most side.

image5.png

Click Check my progress to verify the objective.
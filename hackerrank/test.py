# 1. SECTION 1: GENERAL PROGRAMMING CAPABILITIES (REQUIRED)
# This is the only required section of this Assessment. To qualify for this position you need to be able to successfully write this simple array to matrix transformation program. It's not a difficult problem and if you select a high level language like Java or Python or Javascript, then it won't take a lot of code to write this program. If you choose to write it in C or another low level language, it could take a lot of code. You are free to write this program in any computer language of your choice.



# Hints for passing this assessment :

# Take your time and write the code like a professional.
# Be kind to the assessment graders - make the code easy to read and understand.
# Coding syntax is not important but readability and good logic is. For example, we don't care if you miss a semicolon or if you misspell something.
# Get the logic right.  Our graders will NOT try to compile and run your code. But they will analyze it in their minds, and they will determine if your code would deliver the desired output.
# Most of all, have fun! We are looking for people who have a core passion to solve puzzles and to make the world better by applying their engineering talents.  By evaluating the way a person writes code and communicates, it is easy to determine if the person truly enjoys his/her profession.


# Write a program that does the following:



# Given a string variable: StrRates



# StrRates is a string with delimited list of numbers. This list can be of arbitrary length. The pattern of this list is:

# Rate1 "," Price 1,1 "," ... Raten "," Price1,n ":L" LockPeriod1 ";" ... Rate2 "," Pricem,2 "," ... Raten "," Pricem,n ":L" LockPeriodm ";"



# The Objective of the Program is to transform this string into the following two-dimensional matrix and display it as an html page. So the output should look like this:







# Here is an example input value: "5.0,100,5.5,101,6.0,102:L10;5.0,99,5.5,100,6.0,101:L20;"

# The result will be an HTML page with a table that looks something like this:


def transform_to_matrix(StrRates):
    # Split the input string by ';'
    rate_periods = StrRates.split(';')

    # Initialize an empty HTML string with a table header
    html_output = "<table border='1'><tr><th>Rate</th><th>Price</th><th>Lock Period</th></tr>"

    for rate_period in rate_periods:
        # Split each rate period by ','
        rate_info = rate_period.split(',')

        # Extract rate and price information
        rate = rate_info[0]
        price = rate_info[1]

        # Extract lock period information, removing the 'L' character
        lock_period = rate_info[2][1:]

        # Create a table row for this rate period
        html_output += f"<tr><td>{rate}</td><td>{price}</td><td>{lock_period}</td></tr>"

    # Close the table
    html_output += "</table>"

    return html_output

# Example input value
StrRates = "5.0,100,5.5,101,6.0,102:L10;5.0,99,5.5,100,6.0,101:L20;"

# Transform the input and print the HTML table
html_table = transform_to_matrix(StrRates)
print(html_table)


# #! Javascript
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Rate Matrix</title>
# </head>
# <body>

# <script>
# function transformToMatrix(StrRates) {
#     // Split the input string by ';'
#     const ratePeriods = StrRates.split(';');

#     // Create a table element and a table row for the header
#     const table = document.createElement('table');
#     const headerRow = document.createElement('tr');
#     headerRow.innerHTML = "<th>Rate</th><th>Price</th><th>Lock Period</th>";
#     table.appendChild(headerRow);

#     for (const ratePeriod of ratePeriods) {
#         // Split each rate period by ','
#         const rateInfo = ratePeriod.split(',');

#         // Extract rate and price information
#         const rate = rateInfo[0];
#         const price = rateInfo[1];

#         // Extract lock period information, removing the 'L' character
#         const lockPeriod = rateInfo[2].substring(1);

#         // Create a table row for this rate period
#         const row = document.createElement('tr');
#         row.innerHTML = `<td>${rate}</td><td>${price}</td><td>${lockPeriod}</td>`;

#         // Append the row to the table
#         table.appendChild(row);
#     }

#     // Append the table to the body of the HTML document
#     document.body.appendChild(table);
# }

# // Example input value
# const StrRates = "5.0,100,5.5,101,6.0,102:L10;5.0,99,5.5,100,6.0,101:L20;"

# // Transform the input and display the HTML table
# transformToMatrix(StrRates);
# </script>

# </body>
# </html>

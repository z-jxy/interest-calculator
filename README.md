# Interest Calculator

Solution for automating calculation of interest; within statement cycles which was a missing feature from the core CSS application.
#
For this as I did not have access to the source to be able work with the actual data types values with specific values, I had to create a way of mapping these values and corresponding dates to be able to retrieve them while writing the code.
I began by creating a JSON file with the following format:
#
```
{
	Transactions: [
		{	
			Amount: “$x”,
			Date:	 “xx/xx/xx”
		},
	],
	Cycle: [
		{
			StartDate: “xx/xx/xx””
			EndDate:  “xx/xx/xx””
        },
    ],
StartingBalance: [
	    {
		    Amount: “$x”
	    }
    ]
}
```
#
The program (written in Python) would begin by creating a class from the JSON data retrieved via the RESTful API. From here the program then finds the range from the cycle start date, to the current date. Following this it then takes note of the previous balance from the start of the cycle.
#
Before we’re able to calculate the current interest accrued, we must get the average daily balance which consists of the sum of each daily balance divided by the number of days in the cycle. To do this I created an instance of the current date and a function variable for the total days in the cycle to date which is set to 0. Since this is a solution for provided the interest amount BEFORE the statement is generated, the most days that could ever be in a cycle for this operation would be 30. 
From here, we take the previous daily balance and for each day from the start of the cycle until the current day, we add the values together while also checking the date to see if there was a different daily balance amount, if so we can then set the current balance to the previous balance + the new transaction amount and take note of the amount of days this balance persisted as. 
#
Then, we must find the daily percentage rate, this was just the APR divided by 365. Finally, to get the total interest accrued up to the current date in the cycle, we multiply the daily percentage rate * average daily balance * number of days in cycle. Then in this case, since the daily percentage rate is a percentage value, we must divide the final number by 100 and since we’ve been working with float values for the operations, we can then round the final number by 2, 
Finally, we can then we get the total amount of interest accrued to the current date withing the cycle. After creating all the functions and classes, I organized them accordingly based on the type of operations being completed and after importing the files, we’re able to calculate all these values using just 2 lines.
#
```
poc = Profile(data)
poc.get_interest_cycle_to_date()
``` 
#
As we can see it’s much more efficient to give these sets of instructions to a computer vs. having employees manually calculate add every single different balance for each day in the cycle which could potentially result in up to 29 repeated actions by employees on a given interest inquiry. That’s IF there are 0 mistakes in their calculations at any point in doing this math operation 

Furthermore, given the limited/scattered documentation that was available regarding which values we’re required for calculating the interest. Considering the time needed to be able to identify and find the required values (personally it took me about 15 to 20 minutes to able to find out how to get all the values and then realizing that the daily percentage rate needed to be a percentage value… and this was after a roughly 35 minute team minute with this being one of the talking points), with the desired time for bankers to complete the call within 3 minutes and 50 seconds. That is over a 300% increase in call handling time compared to the 2-3 seconds it would take for this code to calculate it for us.


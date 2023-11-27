The trainings_processor is a small application that takes a few inputs and does the following:
- Reads all data from a .JSON file (default: trainings.txt).
- Generate output as JSON in the three following ways:
  1. List each completed training with a count of how many people have completed that training.
  2. Given a list of trainings and a fiscal year (defined as 7/1/n-1 – 6/30/n), for each specified training, list all people that completed that training in the specified fiscal year. Use parameters: Trainings = "Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"; Fiscal Year = 2024
  3. Given a date, find all people that have any completed trainings that have already expired, or will expire within one month of the specified date (A training is considered expired the day after its expiration date). For each person found, list each completed training that met the previous criteria, with an additional field to indicate expired vs expires soon. Use date: Oct 1st, 2023
- A note for all tasks. It is possible for a person to have completed the same training more than once. In this event, only the most recent completion should be considered.
 
To use the application:
1. Run the application
2. Choose a function to test by entering a number between 1 and 5:
  - 1, 2, 3 are ways to generate output with the specified description from above,
  - 4 is to enter the .JSON input file (default: trainings.txt)
  - 5 is to exit the application
3. When running a function, enter the appropriate input specified
4. Have fun! :)
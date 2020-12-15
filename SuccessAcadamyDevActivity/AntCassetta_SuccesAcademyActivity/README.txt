Option B:​ Write some tested and commented code to grab emails from a table called Student in AWS Dynamo
and send an email to each of them. Be sure to do some light validation on the email field before sending it,
as well as some handling of errors. Don’t do this exercise if you show us a piece of code or blog post or stack
overflow answer from the past year, and if its code walk us through it in writing(briefly)

Additional info for Option B:
● The Student table has three columns, a uuid called id, a string field called email, and a
string field called name.
● The subject and body of the email aren't important
● If you would like to use a formal email service, we generally use amazon ses
● Any language or script is fine, we generally use python



Walk-through
The implementation is fairly straight forward.
The main method runs the script, first retrieving the student data from Dynamo,
then validating the email address before sending an email out to the student using SES.

Get student data is done by establishing a connection with DynamoDB, grabbing the table
and query for the student records, with error handling at each step to make us aware of any network or credential issues.
I chose to write the data download in a batch model as in real life there would be far more than three entries in the database.
From there I wrote a quick validation to ensure the returned data wasn't empty.
This is also a wonderful place to put more robust validation inplace such as duplicate searches or corruption of data.

Sending the email takes the given data, passes the student email to a validate email method which checks that the given
email is in the format "Something@SomeDomain.com". There is opportunity here to use more sophisticated python modules to
check the validity more stringently but I wanted to show something I wrote up.
If valid the students data is passed into the email template and an email is attempted with SES.
In the case of the students email being invalid or the email send failing warnings are printed
and the process moves on to the next student if there is one.

I have also included the setup code and a basic integration test I used as a sanity check for the connection setup.
It simply attempts a connection and checks some meta data from the table.

Thank you for spending time to review my code.
Cheers,
Ant "Kit" Cassetta
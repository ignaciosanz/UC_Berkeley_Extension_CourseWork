In terminal launch the MongoDB server 'mongod'
In terminal launch the MongoDB client 'mongo'

In terminal cd to the folder holding the app.py
Then in terminal type: 'FLASK_APP=app.py'
Then 'flask run'

Then open index.html in browser and click scarp button to launch the program.

Use MongoDBCompass to look at the MongoDB database



How to stop Mongod or any other process
this is the command ‘ps -ef | grep mongo’, then kill it with ‘sudo kill  ...’ add the four digit number instead of the  dots, int his example it woudl be ‘sudo kill 1523’
ps (procesess)
 -ef will show all the process
|  grep mongo (will look for anything that has mongo)
then  kill the  process
-bash: quit: command not found
ISANZ-MBP:~ isanz$ ps -ef | grep mongo
1582474661  1523     1   0 12:08PM ??         0:02.39 mongod
1582474661  1666  1616   0 12:16PM ttys001    0:00.00 grep mongo
ISANZ-MBP:~ isanz$ sudo kill 1523
Password:
ISANZ-MBP:~ isanz$ 
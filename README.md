---------------Installation instructions for Windows --------

1. Install the pakages given in the requirements.txt file
	- pip install -r requirements.txt

2. Create the database by writing following commands on python(if there is an existing database created - Delete it): 
	- from seatbooking import db
	- db.create_all()

3. Set the environment variables 
	3.1. Go to My computer Properties
	3.2. Click on Advance System settings 
	3.3. Dialogue box will appear.Click on Environment Variables button
	3.4  Find Path variable in System variables box
	3.5 Select Path varible and click on edit button
	3.6 copy paste the followin at the end 
C:\Python34;C:\Python34\python.exe;C:\Python34\Scripts\;

4. Copy paste the whole project file  intelligent seat allocation system to desktop

Open Cmd
 - Go to the Directory where the project is to be created and enter the following commands
 - cd Desktop
 - cd intelligent seat allocation system
 - python run.py
 - Goto your Browser and enter the following url
	http://localhost:5000/

-------------------------------------------------------------------------------------------------------------------

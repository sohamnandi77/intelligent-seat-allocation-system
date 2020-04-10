# ---------------Installation instructions for Windows --------

(first, confirm that your pip is working)
(Also, python version 3.7.0+ is recommended)

1. Install the pakages given in the requirements.txt file
	- pip install -r requirements.txt

2. Create the database by writing following commands on python(if there is an existing database created - Delete it): 
	- from seatbooking import db
	- db.create_all()

3. Set the environment variables 
	- Go to My computer Properties
	- Click on Advance System settings 
	- Dialogue box will appear.Click on Environment Variables button
	- Find Path variable in System variables box
	- Select Path varible and click on edit button
	- Copy paste the followin at the end 
```
C:\Python34;C:\Python34\python.exe;C:\Python34\Scripts\
```

4. Copy paste the whole project file  intelligent seat allocation system to desktop

5. Open Cmd and Go to the Directory where the project is to be created and enter the following commands
 ```
cd Desktop
 ```
 ```
cd intelligent seat allocation system
 ```
 ```
python main.py
```
6. Goto your Browser and enter the following url
	http://localhost:5000/

-------------------------------------------------------------------------------------------------------------------


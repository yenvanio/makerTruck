# makerTruck

## DBMS Course Project (Python-Flask)

The makerTruck program is an engineering outreach program by UOIT, sponsored by General Motors. Through this program highschool and elementary school students are exposed to various engineering related workshops to familiarize them with engineering concepts.

### Windows Setup

- Install Git
- Install Python 2.7
- Install PostgreSQL and PGAdmin4
- Install virutalenv `pip install virtualenv virtualenvwrapper`
- Create a virtual environment `virtualenv venv`
- Activate the environment  `venv\Scripts\activate`
- Clone this repository `git clone https://github.com/yenvanio/makerTruck`
- Install the required packages `pip install -r requirements.txt`
- Create a database called `makerTruck` using PGAdmin 4
  - Make sure the owner of the database is `root` and the password is also `root`
- Navigate to the `db` folder and copy and paste the `makerTruck.sql` from there into PGAdmin4 to create tables and populate the database
- In the command prompt, navigate to the root of the repository and run the app.py file `python app.py`

### Making Changes (For Collaborators)
- `git add .`
- `git commit -m 'meaningful message'`
- `git push`


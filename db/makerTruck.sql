CREATE TABLE Workshops (
	id	int	NOT NULL,
	price	float	NOT NULL,
	name	varchar(255)	NOT NULL,
  description varchar(255) NOT NULL,
	PRIMARY KEY (ID)
);

INSERT INTO workshops VALUES (1, 499, '3D Printing', 'An introductory workshop on 3D printing and creating your own models that can be 3D printed');
INSERT INTO workshops VALUES (2, 399, 'Programming', 'A workshop on programming
where students will build a program in scratch
or turing.');
INSERT INTO workshops VALUES (4, 349, 'Electric Car', 'A workshop where students will program and control an electric car');
INSERT INTO workshops VALUES (3, 449, 'Arduino', 'A workshop on programming
where students will use an arduino and simple breadboard
circuitry to build a take home project');
INSERT INTO workshops VALUES (6, 599, 'Robotics', 'A workshop that allows students to get familiarized with robotics');
INSERT INTO workshops VALUES (5, 329, 'Electricity', 'An introductory workshop on electricity and circuit building');

CREATE TABLE Bins (
	id		int	NOT NULL,
	mame		varchar(255)	NOT NULL,
	workshop_id	int	NOT NULL,
	quantity	int	NOT NULL,
	PRIMARY KEY (id),
	FOREIGN KEY (workshop_id) REFERENCES Workshops (id)
);
INSERT INTO bins VALUES (2, '3D Printing B', 1, 5);
INSERT INTO bins VALUES (3, 'Electric Car Kits', 4, 9);
INSERT INTO bins VALUES (5, 'Programming Exercises', 2, 15);
INSERT INTO bins VALUES (6, 'Robotics Kits', 5, 12);
INSERT INTO bins VALUES (1, '3D Printing A', 1, 0);
INSERT INTO bins VALUES (4, 'Arduino Kits', 3, 0);

CREATE TABLE Schools (
	id		int	NOT NULL,
	address		varchar(255)	NOT NULL,
	school_name	varchar(255)	NOT NULL,
	email		varchar(255)	NOT NULL,
	phone		numeric(10)	NOT NULL,
	username	varchar(255)	NOT NULL,
	password	varchar(255)	NOT NULL,
	PRIMARY KEY (id)
);
INSERT INTO schools VALUES (1, '31 Spooner St', 'JClarke Richardson', 'jcr@gmail.com', 6474761312, 'jcr123', 'eofnef');
INSERT INTO schools VALUES (2, '678 Sabbe Cres', 'Middlefield', 'mdlfld@yahoo.ca', 9056784564, 'mfld678', 'qofnoewn');
INSERT INTO schools VALUES (3, '96 Brick Lane', 'Bill Crothers', 'bc@hotmail.com', 5195256765, 'bc_tu78', 'ewofjnoe');
INSERT INTO schools VALUES (4, '66 Owl Ave', 'Markham District', 'mdst@gmail.com', 4167458745, 'mdst_878', 'eofjedf');
INSERT INTO schools VALUES (5, '45 Comm Dr', 'Milliken', 'mkl@yahoo.ca', 6478917523, 'mkl_786', 'pkeruj');
INSERT INTO schools VALUES (6, '93 Pavillion St', 'Algonquin', 'aquinn@yahoo.ca', 6474701543, 'quinn_123', 'qwmelie');

CREATE TABLE Trucks (
  id		int	NOT NULL,
  model		varchar(255)	NOT NULL,
  vin		varchar(255)	NOT NULL,
  license_plate	varchar(255)	NOT NULL,
  PRIMARY KEY (id)
);
INSERT INTO trucks VALUES (2, 'GMC G-3500 - 10''', '6G7A1AF5LLF142A5F', 'BZBY234');
INSERT INTO trucks VALUES (1, 'GMC G-3500 - 10''', '2A3G0DF48SF723B4S', 'BFRA878');
INSERT INTO trucks VALUES (4, 'GMC G-3500 - 17''', '10HJ7XA4OSP89KBWA', 'BHJP576');
INSERT INTO trucks VALUES (3, 'GMC G-3500 - 14''', '7D2AFH2SCSH324N4M', 'YSHD089');
INSERT INTO trucks VALUES (6, 'Ford E450 - 14''', '032BFJ2SESJ4TIC0V', 'VGKA802');
INSERT INTO trucks VALUES (5, 'Ford E450 - 10''', 'ZL1ASBF0PLE1W708B', 'VUBI594');



CREATE TABLE Workshop_Bookings (
  id		int	NOT NULL,
  workshop_id	int	NOT NULL,
  school_id	int	NOT NULL,
  truck_id	int	NOT NULL,
  type		varchar(255)	NOT NULL,
  period		varchar(1)	NOT NULL,
  date		date	NOT NULL,
  PRIMARY KEY (id),
	FOREIGN KEY (workshop_id) REFERENCES Workshops (id),
	FOREIGN KEY (school_id) REFERENCES Schools (id),
	FOREIGN KEY (truck_id) REFERENCES Trucks (id)
);
INSERT INTO workshop_bookings VALUES (2, 3, 3, 2, 'Full', 'M', '2017-11-23');
INSERT INTO workshop_bookings VALUES (4, 6, 2, 1, 'Half', 'A', '2017-11-27');
INSERT INTO workshop_bookings VALUES (5, 6, 2, 1, 'Half', 'A', '2017-11-28');
INSERT INTO workshop_bookings VALUES (1, 1, 1, 1, 'Full', 'M', '2017-11-22');
INSERT INTO workshop_bookings VALUES (3, 2, 1, 2, 'Full', 'A', '2017-11-24');
INSERT INTO workshop_bookings VALUES (6, 4, 4, 2, 'Half', 'M', '2017-11-26');

import psycopg2

class Connection:
    def __init__(self):
        con = psycopg2.connect(database='makerTruck', user='root', host='localhost', password='root')
        self.cur = con.cursor()

    def get_workshops(self):
        self.cur.execute('select "id","name","description" from workshops')
        return self.cur.fetchall()

    def get_availWorkshops(self):
        self.cur.execute('select "name", "price", "description" from workshops where "id" not in (select "workshop_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_unavailWorkshops(self):
        self.cur.execute('select "name", "price", "description" from workshops where "id" in (select "workshop_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_schools(self):
        self.cur.execute('select "school_name", "address", "email", "phone" from schools')
        return self.cur.fetchall()

    def get_availTrucks(self):
        self.cur.execute('select "model", "vin", "license_plate" from trucks where "id" not in (select "truck_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_unavailTrucks(self):
        self.cur.execute('select "model", "vin", "license_plate" from trucks where "id" in (select "truck_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_availBins(self):
        self.cur.execute('select "name", "quantity" from bins where "quantity" > 0')
        return self.cur.fetchall()

    def get_unavailBins(self):
        self.cur.execute('select "name", "quantity" from bins where "quantity" = 0')
        return self.cur.fetchall()

#View Needed
# 1. List all workshops booked by a certain school
# 2. Show workshops that have bins remaining
# 3. Show Statistics - which schools booked above average priced workshops
# 4. "             " - which schools have not booked before
# 5. "             " - show all schools info
# 6. Show all trucks available
# 7. Show all bins on certain truck
# 8.
# 9. Show all available workshops
# 10. Show all bins that are booked and the trucks they belong to

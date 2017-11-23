import psycopg2
import sys

class Connection:
    def __init__(self):
        con = psycopg2.connect(database='makerTruck', user='root', host='localhost', password='root')
        self.cur = con.cursor()

    def get_workshopsAll(self):
        self.cur.execute('select "id","name","description" from workshops')
        return self.cur.fetchall()

    def get_workshops(self, school_id):
        self.cur.execute('select w."name", w."price", w."description", b."date" from workshops as w left join workshop_bookings as b on w."id" = b."workshop_id" left join schools as s on b."school_id" = s."id" where s."id" = %s', [school_id])
        return self.cur.fetchall()

    def get_availWorkshops(self):
        self.cur.execute('select "name", "price", "description" from workshops where "id" not in (select "workshop_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_unavailWorkshops(self):
        self.cur.execute('select "name", "price", "description" from workshops where "id" in (select "workshop_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_schools(self):
        self.cur.execute('select "school_name", "address", "email", "phone", "id" from schools')
        return self.cur.fetchall()

    def get_schoolName(self, school_id):
        self.cur.execute('select "school_name" from schools where "id"  = %s', [school_id])
        return self.cur.fetchall()

    def get_availTrucks(self):
        self.cur.execute('select "id", "model", "vin", "license_plate" from trucks where "id" not in (select "truck_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_unavailTrucks(self):
        self.cur.execute('select "id", "model", "vin", "license_plate" from trucks where "id" in (select "truck_id" from workshop_bookings where "date"=CURRENT_DATE)')
        return self.cur.fetchall()

    def get_availBins(self):
        self.cur.execute('select "name", "quantity" from bins where "quantity" > 0')
        return self.cur.fetchall()

    def get_unavailBins(self):
        self.cur.execute('select "name", "quantity" from bins where "quantity" = 0')
        return self.cur.fetchall()

    def get_aboveAvgPrice(self):
        self.cur.execute('select s."school_name" from schools as s left join workshop_bookings as b on s."id" = b."school_id" left join workshops as w on b."workshop_id" = w."id" where w."price">(select avg(price) from workshops) group by s."school_name"')
        return self.cur.fetchall()

    def get_noBookSchool(self):
        self.cur.execute('select s1."school_name" from schools as s1 except select s2."school_name" from schools as s2 where s2."id" in (select school_id from workshop_bookings)')
        return self.cur.fetchall()

    def get_bookSchool(self):
        self.cur.execute('select "school_name" from schools where "id" = any (select school_id from workshop_bookings)')
        return self.cur.fetchall()

    def get_bookBins(self, id):
        self.cur.execute('select b."name", t."model", t."license_plate" from bins as b left join workshop_bookings as wb on b."workshop_id" = wb."workshop_id" full join trucks as t on wb."truck_id"=t."id" where wb."date">now() and t."id" = %s', [id])
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

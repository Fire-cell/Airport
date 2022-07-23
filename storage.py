import csv
from plane import Plane
from flight import Flight
from ticket import Ticket

def rd_planes(planes):
    with open("Plane.cvs", "r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            planes.append(Plane(row[0], int(row[1]), int(row[2])))
def rd_flights(flights):
    with open("Flights.cvs", "r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            if row[9] != "":
                flights.append(Flight(int(row[0]), int(row[1]), int(row[2]), row[3], row[4],
                                  row[5], row[6], row[7], int(row[8]), row[9].split('.')))
            else:
                flights.append(Flight(int(row[0]), int(row[1]), int(row[2]), row[3], row[4],
                                      row[5], row[6], row[7], int(row[8])))
def rd_tickets(tickets):
    with open("Tickets.cvs", "r") as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            tickets.append(Ticket(row[0], int(row[1]), int(row[2]), int(row[3])))
def sv_planes(planes):
    with open("Plane.cvs", "w") as f:
        for i in range(len(planes)):
            f.writelines(','.join(map(str, planes[i].get_info())) + '\n')
def sv_flights(flights):
    with open("Flights.cvs", "w") as f:
        for i in range(len(flights)):
            f.writelines(','.join(map(str, flights[i].get_info())) + "," + '.'.join(flights[i].get_transfers() + '\n'))
def sv_tickets(tickets):
    with open("Tickets.cvs", "w") as f:
        for i in range(len(tickets)):
            f.writelines(','.join(map(str, tickets[i].get_info())) + '\n')
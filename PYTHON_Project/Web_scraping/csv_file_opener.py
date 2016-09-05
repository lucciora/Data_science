import csv

def write_csv(title, genre, strorywriter, illustrator,
               platform, startdate, address,weekday, image):
    with open("nate.csv", 'a', newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow([title, genre, strorywriter,
                         illustrator, platform,
                         startdate, address, weekday, image])
        print("succeeded")
    

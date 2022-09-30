import csv
# field names  
fields = ['Name', 'Branch', 'Year', 'CGPA']  
    
# data rows of csv file  
rows = [ ['Nikhil', 'COE', '2', '9.0'],  
         ['Sanchit', 'COE', '2', '9.1'],  
         ['Aditya', 'IT', '2', '9.3'],  
         ['Sagar', 'SE', '1', '9.5'],  
         ['Prateek', 'MCE', '3', '7.8'],  
         ['Sahil', 'EP', '2', '9.1']]  
    
# name of csv file  
filename = "university_records.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:  
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  
        
    # writing the fields  
    csvwriter.writerow(fields)  
        
    # writing the data rows  
    csvwriter.writerows(rows) 



    # fields = ["Crew Name", "Job Title", 'Flight', 'Plane']
    # rows = [['Nonno', 'CA', 'BR17', 'B77W'],
    #         ['Yen', 'CA', 'BR18', 'B77W']]

    # csvFileName = "test.csv"

    # with open(csvFileName, 'a', newline='') as csvFile:
    #     csvWrite = csv.writer(csvFile)

    #     # csvWrite.writerow(fields)
        
    #     for x in range(10):
    #         csvWrite.writerows(rows)



    if __name__ == '__main__':
        fields = ["Crew Name", "Job Title", 'Flight', 'Plane']
    rows = [['Nonno', 'CA', 'BR17', 'B77W'],
            ['Claire', 'CA', 'BR18', 'B77W']]

    csvFileName = "test.csv"

    with open(csvFileName, 'a', newline='') as csvFile:
        csvWrite = csv.writer(csvFile)

        # csvWrite.writerow(fields)
        
        for x in range(10):
            csvWrite.writerows(rows)

    # csvWrite.writerow({'Crew Name' : 'Claire',
    #                    'Job Title' : 'CA',
    #                    'Flight' : 'BR17',
    #                    'Plane' : 'B77W'})

# if __name__ == '__main__':
#     while True:


class cars:
    def __init__(self, color, seat):
        self.color = color
        self.seat = seat

    def drive(self):
        print(f"My car is {self.color} and {self.seat} seats.")

tesla = cars("green", 4)
tesla.drive()
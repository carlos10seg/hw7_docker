import csv

class FileManager:

    def get_file_content(self):
        content = []
        count = -1
        with open("Popular_Baby_Names.csv") as csvfile:
            csv_content = csv.reader(csvfile, delimiter=',')
            for row in csv_content:
                count += 1
                if count == 0: # skip headers
                    continue

                rank = int(row[5])
                year = int(row[0])
                gender = row[1]
                if (rank <= 10 and year == 2016 and gender == "FEMALE"): #only add the top 10
                    item = {"Year": row[0], "Gender": row[1], "Ethnicity": row[2], "FirstName": row[3]}
                    content.append(item)
            return content
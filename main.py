import convertor.temperature as te

import csv

def extract_temperature(reading):
    return int(reading.split()[0])

def convert_temperatures(input_file, output_file, target_temperature):
    with open(input_file, 'r', newline='') as infile, open(output_file, 'w', newline='') as outfile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames + [f"Converted {target_temperature}"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
   
        if target_temperature == 'F':
            for row in reader:
                if  row['Reading'].split()[1] == "C":
                    celsius_reading = extract_temperature(row['Reading'])
                    converted_temperature = te.celsius_to_fahrenheit(celsius_reading) 
                    row[f"Converted {target_temperature}"] = f"{converted_temperature} F"
                    writer.writerow(row)
                else:
                    row[f"Converted {target_temperature}"] = row['Reading']
                    writer.writerow(row)
        elif target_temperature == 'C':
            for row in reader:
                if  row['Reading'].split()[1] == "F":
                    f_reading = extract_temperature(row['Reading'])
                    converted_temperature = te.fahrenheit_to_celsius(f_reading) 
                    row[f"Converted {target_temperature}"] = f"{converted_temperature} C"
                    writer.writerow(row)
                else:
                    row[f"Converted {target_temperature}"] = row['Reading']
                    writer.writerow(row)            



convert_temperatures("data.csv", "output_file.csv", "C")                
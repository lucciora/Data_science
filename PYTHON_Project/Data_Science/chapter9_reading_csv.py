import csv

with open('SURFACE_AWS_400_DAY_2014_2014_2015.csv', 'r') as f:
    reader = csv.reader(f, delimiter=',')
    result= []
    for row in reader:    
        print(row)
    

    


#    for row in reader:
#        print(row[2:len(row)])



'''
    for row in reader:
        region = row["지점"]
        date = row["일시"]
        avg_temper = row["평균기온(°C)"]
        low_temper = row["최저기온(°C)"]
        low_temper_time = row["최저기온 시각(hhmi)"]
        high_temper = row["최고기온(°C)"]
        high_temper_time = row["최고기온 시각(hhmi)"]
        high_mm = row['1시간 최다강수량(mm)']
        high_hhmi = row['1시간 최다 강수량 시각(hhmi)']
        day_mm = row['일강수량(mm)']
        high_ms = row['최대 순간 풍속(m/s)']
        high_ms_time = row['최대 순간풍속 시각(hhmi)']
        avg_ms = row['평균 풍속(m/s)']
        high_ms_direction = row['최대 순간 풍속 풍향(hhmi)']
        print(high_hhmi)
'''        
        
        
        
        
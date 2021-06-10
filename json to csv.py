# -*- coding: utf-8 -*-
"""
File: Converter.py
-----------

This is a JSON to CSV converter program
This program will convert JSON to CSV file 
"""

import json
import csv

    #read json file
    with open ("file.json", "r") as JSON_file:
        data = json.load(JSON_file)
        users = data["users"]
        txs = data["txs"]
        
        #describe output name
        output1 = "CSV_1"
        output2 = "CSV_2"
        output3 = "CSV"
        
    #Create CSV_1 file
    with open(output1, "w") as file1:
        csv_file1 = csv.writer(file1)
        csv_file.writerow(["user_id","tx_id"])
        for i in users["id"]:
            for j in txs["id"]:
                csv_file.writerow([i["id"], j["id"]])
                
    
    #Create CSV_2 file
    with open(output12, "w") as file2:
        csv_file2 = csv.writer(file2)
        csv_file.writerow(["id","name","email"])
        for k in data["users"]:
                csv_file.writerow([k["id"], k["name"], k["email"]])
                
    #Create CSV file
    with open(output13, "w") as file3:
        csv_file3 = csv.writer(file3)
        csv_file.writerow(["id","tx_date","tx_mount","tx_type"])
        for l in data["txs"]:
                csv_file.writerow([l["id"], l["tx_date"], k["tx_amount"], l["tx_type"]])
        
                
    
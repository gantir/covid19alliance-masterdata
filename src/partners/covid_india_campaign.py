import requests
import csv
from datetime import datetime
from io import StringIO


sheets_verified_data_28_apr = [
  {
    "org_name": "Covid India Campaign",
    "sheet_name": "Believe_upto_28/04/2021",
    "sheet_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRD3sKzqUuX976yaGvCR1SfdV8fVRkYOH-2MFIII_ozEtcW9vKFbFvWg7o4mXiMLDa-R_Hcc-F5E4uH/pub?gid=1635462133&single=true&output=csv",
    "master_mapping": {
      "name": ["Name", "misc"],
      "category": "Type of Help",
      "phone_1": "Number",
      "address": "Address",
      "state": "State",
      "city": "City",
      "source_link": "Link",
      "last_verified_on": "Last Verified Date",
      "verification_status": "Status",
      "verifier_comment": "Comment",
      "last_verified_by": "Volunteer Name"
    }
  },
  {
    "org_name": "Covid India Campaign",
    "sheet_name": "BB_upto_28/04/2021",
    "sheet_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRD3sKzqUuX976yaGvCR1SfdV8fVRkYOH-2MFIII_ozEtcW9vKFbFvWg7o4mXiMLDa-R_Hcc-F5E4uH/pub?gid=1875160514&single=true&output=csv",
    "master_mapping": {
      "name": "Name",
      "category": "Requirement",
      "phone_1": "Number",
      "description": "Remarks",
      "city": "City",
      "state": "State",
      "source_link": "Link",
      "last_verified_on": "Last Verified Time",
      "verification_status": ["Contacted", "Status"],
      "verifier_comment": "Comments",
      "last_verified_by": "volunteer"
    }
  },
  {
    "org_name": "Covid India Campaign",
    "sheet_name": "CarD_upto_28/04/2021",
    "sheet_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRD3sKzqUuX976yaGvCR1SfdV8fVRkYOH-2MFIII_ozEtcW9vKFbFvWg7o4mXiMLDa-R_Hcc-F5E4uH/pub?gid=1828211395&single=true&output=csv",
    "master_mapping": {
      "name": "Twitter Search for COVID Resources",
      "category": "All Information",
      "phone_1": "Phone Number",
      "address" : "Type of verification",
      "city": "City",
      "state": "State",
      "verification_status": ["Connectivity", "Final Status"],
      "verifier_comment": "Comments"
    }
  },
  {
    "org_name": "Covid India Campaign",
    "sheet_name": "BB_27/04/2021",
    "sheet_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRD3sKzqUuX976yaGvCR1SfdV8fVRkYOH-2MFIII_ozEtcW9vKFbFvWg7o4mXiMLDa-R_Hcc-F5E4uH/pub?gid=1618395342&single=true&output=csv",
    "master_mapping": {
      "name": "Twitter Search for COVID Resources",
      "category": "Catetgory",
      "phone_1": "Phone",
      "address": "Address",
      "city": "City",
      "state": "State",
      "source_link": "link",
      "last_verified_on": "Last Verified Time",
      "verification_status": ["Contacted/ Not Contacted","Status"],
      "verifier_comment": "Comments",
      "last_verified_by": "volunteer"
    }
  },
  {
    "org_name": "Covid India Campaign",
    "sheet_name": "Believe_upto 27/04/2021",
    "sheet_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRD3sKzqUuX976yaGvCR1SfdV8fVRkYOH-2MFIII_ozEtcW9vKFbFvWg7o4mXiMLDa-R_Hcc-F5E4uH/pub?gid=1362519089&single=true&output=csv",
    "master_mapping": {
      "state": "State",
      "city": "City",
      "address": "Address/Link",
      "pin_code": "pin code",
      "category": "Type of Help",
      "last_verified_on": ["Last Verified at Date", "Last Verified at Time"],
      "verification_status" : ["Contacted/ Not Contacted", "Status"],
      "resource_availability": "Stock Availability",
      "name":"Point of Contact",
      "phone_1": "Phone",
      "verifier_comment": ["Comments_1", "Comments 2"],
      "last_verified_by": "Volunteer Name"
    }
  },
  {
    "org_name": "Covid India Campaign",
    "sheet_name": "BB_upto_26/04/2021",
    "sheet_url": "https://docs.google.com/spreadsheets/d/e/2PACX-1vRD3sKzqUuX976yaGvCR1SfdV8fVRkYOH-2MFIII_ozEtcW9vKFbFvWg7o4mXiMLDa-R_Hcc-F5E4uH/pub?gid=0&single=true&output=csv",
    "master_mapping": {
      "state": "State",
      "city": "City",
      "address": ["Address 1", "Address 2"],
      "pin_code": "Pin Code",
      "category": "Category",
      "last_verified_on": ["Date","Time"],
      "verification_status": ["Connectivity","Status", "Status_1", "Status_2","Status_3","Status_4"],
      "name": "Name",
      "phone_1": "Phone Number",
      "verifier_comment":"Verifier Comments",
      "last_verified_by": "Volunteer"
    }
  }
]

def csv2dict(csv_data):
  # The first row is taken to be header
  columns = next(csv_data)
  dict_list = []
  for row in csv_data:
    dict_list.append({col: val for col, val in zip(columns, row)})
  return dict_list

def get_master_row(org_name: str) -> dict:
  master_row = {
    "name": "",
    "phone_1": "",
    "phone_2": "",
    "category": "",
    "state": "",
    "district": "",
    "city": "",
    "pin_code": "",
    "address": "",
    "resource_type": "",
    "quantity_available": "",
    "resource_availability": "",
    "verification_status": "",
    "last_verified_by": "",
    "last_verified_org": org_name,
    "last_verified_on": "",
    "verifier_comment": "",
    "description": "",
    "email": "",
    "price": "",
    "source_link": "",
    "source_name": "",
    "comment": "",
    "created_by": "",
    "created_by_org": org_name,
    "created_on": "",
    "hospital_available_normal_beds": "",
    "hospital_available_oxygen_beds": "",
    "hospital_available_icu_beds": "",
    "hospital_available_ventilator_beds": "",
  }
  return master_row

def transform_2_master(org_name: str, csv_url: str, source_master_header_map: dict):

  response = requests.get(csv_url)
  source_data = csv.reader(StringIO(response.text))
  source_data_dict = csv2dict(source_data)
  master_row = get_master_row(org_name)

  output = []
  for source_row in source_data_dict:
    row = master_row.copy()
    for master_col, source_col in source_master_header_map.items():
      if type(source_col) == list:
        row[master_col] = "|".join([source_row[scol] for scol in source_col if source_row[scol]])
      else:
        row[master_col] = source_row[source_col]
    output.append(row)

  return output
if __name__ == "__main__":
  master_row = get_master_row("Dummy")
  with open("compiled.csv", "w") as fccsv:
    compiled_sheet = csv.DictWriter(fccsv, master_row.keys(), dialect='excel')
    compiled_sheet.writeheader()
    for i, sheet_detail in enumerate(sheets_verified_data_28_apr):
      # if i == 3:
      #   exit()
      print(sheet_detail["sheet_name"])
      o = transform_2_master(sheet_detail["org_name"], sheet_detail["sheet_url"], sheet_detail["master_mapping"])
      compiled_sheet.writerows(o)

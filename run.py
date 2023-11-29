#!/usr/bin/env python3

import os
import requests
import reports
import report_email

file_path = "/home/donsacafq/Module_29_project/supplier-data/descriptions/"
images_path = "/home/donsacafq/Module_29_project/supplier-data/images/"
pdf_path_file = "/home/donsacafq/Module_29_project/tmp/processed.pdf"
# file_path = "/home/student-03-62189c45288d/supplier-data/descriptions/" # lab VM URL
# images_path = "/home/student-03-62189c45288d/supplier-data/images" # lab VM URL
# pdf_path = "/home/student-03-62189c45288d/tmp" # lab VM URL
# pdf_path_file = "/home/student-03-62189c45288d/tmp/processed.pdf" # VM URL
post_url = "http://localhost/fruits/" # VM URL

def list_files():
  """Get list of files"""
  file_list = os.listdir(file_path)
  return file_list

def create_dict_with_txt_data_and_image_and_post(file_list):
  """Convert the data from the txt files & the image names into a dictionary"""
  titles = ["name", "weight", "description", "image_name"]
  fruits_list_of_dicts_name_weight = []
  for file in file_list:
    file_is_a_txt = 1
    dictionary = {}
    data_line = 0
    if file.endswith('.txt'):
      with open(os.path.join(file_path, file)) as my_file:
        for line in my_file:
          key = titles[data_line]
          if key == "weight": # If "weight", strip "lbs"
            weight_int = line.split(" ", 1)[0]
            dictionary[key] = weight_int
          else: # If not weight, just add key, value as-is
            dictionary[key] = line.strip()
          data_line += 1
          if data_line == 3: # If we're at the fourth index (image path and name)
            dictionary[titles[data_line]] = file.split(".", 1)[0] + ".jpeg"
            break
    else:
      print("{} is not a txt file.".format(os.path.join(path, file)))
      file_is_a_txt = 0
    if file_is_a_txt: # Don't post unless current file is a txt file, ignore other files
      post_fruits_to_web_service(dictionary) # post each file contents individually
    dictionary.pop("description") # Strip "description" key
    dictionary.pop("image_name") # Strip "image_name" key
    fruits_list_of_dicts_name_weight.append(dictionary) # Concatenate to list of dicts
  return fruits_list_of_dicts_name_weight # return list of dicts

def post_fruits_to_web_service(line):
  # response = requests.post(post_url, data=line)
  # if response.status_code != 201:
    response = 202 # temp - replace with two lines at top
    if response == 201: # temp - replace with two lines at top
      print(response)

def fruits_dict_name_weight_to_sorted_string(fruits_list):
  """Turns the data in car_data into a list of lists."""
  table_data = ""
  fruits_list = sorted(fruits_list, key=lambda x: x["name"]) # sort list of dicts
  for line in fruits_list:
    table_data = table_data + "name: " + line["name"] + "<br/>"
    table_data = table_data + "weight: " + line["weight"] + " lbs"  + "<br/>" + "<br/>"
  table_data = table_data.strip("<br/>")
  """ Below, for creating the report using a Table (i.e., with frames using list of dicts) instead of a Paragraph (using continuous string) """
  # table_data = []
  # for item in fruits_list:
  #   table_data.append(["name: " + item["name"]])
  #   table_data.append(["weight: " + item["weight"] + " lbs"])
  #   table_data.append([""])
  # table_data.pop()
  return table_data # return sorted string

def prepare_email_and_send():
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = report_email.generate_email(sender, receiver, subject, body, pdf_path_file)
  # report_email.send(message)

def main():
  """ 1. Generate list of txt files, convert that and the corresponding image into a dictionary then post to web service """
  fruits_list_of_dicts = create_dict_with_txt_data_and_image_and_post(list_files())
  """ 2. Generate PDF report """
  reports.generate_report(pdf_path_file, "Processed Update on ", fruits_dict_name_weight_to_sorted_string(fruits_list_of_dicts))
  """ 3. Generate message then send email with PDF report """
  prepare_email_and_send() # send email with PDF attachment

if __name__ == "__main__":
  main()
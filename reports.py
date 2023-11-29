#!/usr/bin/env python3

import reportlab

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from datetime import datetime
import calendar

def generate_report(filename, title, fruits_description):
  """ Prepare and build report """
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  month = int(datetime.now().strftime("%m"))
  month = calendar.month_name[month]
  title = title + month + str(datetime.now().strftime(" %d, %Y"))
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(fruits_description, styles["BodyText"])
  """ Replace line above with below 3 lines to use a table as data instead of a string """
  # table_style = [('FONTNAME', (0,0), (0,0), 'Helvetica'),
                # ('ALIGN', (0,0), (0,0), 'LEFT')]
  # report_table = Table(data=fruits_list_of_lists_name_weight, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info])
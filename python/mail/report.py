#!/usr/bin/env python3

import reportlab
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet    
from reportlab.lib import colors


def generate(filename, title, addictional_info, table_data):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles['h1'])
    report_info = Paragraph(addictional_info, styles['BodyText'])
    table_style = [('GRID', (0, 0), (-1, -1), colors.black),
                   ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER')]   
    report_table = reportlab.platypus.Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1, 20)
    report.build([report_title, empty_line, report_info, empty_line, report_table])
"""
Created on Wed Sep 14 15:21:58 2016

@author: James Rocker
"""
import xlsxwriter


def build_workbook(workbook_name: str):
    workbook = xlsxwriter.Workbook(workbook_name + '.xlsx')
    worksheet = workbook.add_worksheet()

    sample = (
        ['Text Log -', 12220],
        ['Total Errors in Text -', 561651],
        ['Format Errors -', 656],
        ['Limit Errors -', 51651],
        ['Change Errors -', 5484],
        ['Address Error -', 5651561],
    )
    row = 0
    col = 0

    for item, cost in sample:
        worksheet.write(row, col, item)
        worksheet.write(row, col + 1, cost)
        row += 1

    workbook.close()

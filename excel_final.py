from openpyxl import load_workbook
import json
import time

#load the file  
wb = load_workbook(filename="Marshall_ALItoGISanalysis.xlsx")

#to freeze the top row
def freeze_row_sheet(sheet_name):
    ws = wb[sheet_name]
    ws.freeze_panes = "A2"
    wb.save("Marshall_ALItoGISanalysis.xlsx")

#to print headers top row
def show_columns(sheet_name):
    ws = wb[sheet_name]
    names=[]
    t_val=0
    for column in ws.iter_cols():
        s={"c_name":column[0].value,"c_pos":t_val}
        json.dumps(s)
        names.append(s)
        t_val=t_val+1
    return names

#to delete column from worksheet
def del_col_sheet(sheet_name,column_pos):
    ws = wb[sheet_name]
    ws.delete_cols(idx=column_pos+1)
    wb.save("Marshall_ALItoGISanalysis.xlsx")

#to autofit all columns max length  
def auto_adj_width_sheet(sheet_name):
    ws = wb[sheet_name]
    for column in ws.columns:
        max_length = 0
        column_letter = column[0].column_letter
        for cell in column:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2) * 1.2
        ws.column_dimensions[column_letter].width = adjusted_width
    wb.save("Marshall_ALItoGISanalysis.xlsx")

#to rename the sheet
def rename_sheet(sheet_name,new_name):
    ws=wb[sheet_name]
    ws.title=new_name
    wb.save("Marshall_ALItoGISanalysis.xlsx")

#to sort/filter descending order
def filter_sort_sheet(sheet_name):
    ws=wb[sheet_name]
    ws.auto_filter.ref="A1:B95"
    ws.auto_filter.add_sort_condition(ref="B2:B95",descending=True)
    wb.save("Marshall_ALItoGISanalysis.xlsx")



sh_name=wb.sheetnames
#print all worksheet
for s in sh_name:
    print (s)
    if s== "UnmatchedALI":
        auto_adj_width_sheet(s)
        time.sleep(2)
        freeze_row_sheet(s)
        time.sleep(1)
        s_columns=show_columns(s)
        for col in s_columns:
            print(col['c_name'])
            if col['c_name'] == 'OBJECTID' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        sheet_new_name="Unmatched ALI"
        rename_sheet(s,sheet_new_name)

    elif s=="UnmatchedALIstats":
        auto_adj_width_sheet(s)
        time.sleep(2)
        freeze_row_sheet(s)
        time.sleep(1)
        s_columns=show_columns(s)
        for col in s_columns:
            print(col['c_name'])
            if col['c_name'] == 'OBJECTID' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        s_col=show_columns(s)
        for col in s_col:
            print(col['c_name'])
            if col['c_name'] == 'COUNT_OBJECTID' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        time.sleep(2)
        filter_sort_sheet(s)
        sheet_new_name="Unmatched ALI Stats"
        rename_sheet(s,sheet_new_name)

    elif s=="APMsagComm":
        auto_adj_width_sheet(s)
        time.sleep(2)
        freeze_row_sheet(s)
        time.sleep(1)
        s_columns=show_columns(s)
        for col in s_columns:
            print(col['c_name'])
            if col['c_name'] == 'OBJECTID' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        sheet_new_name="State QA Issues"
        rename_sheet(s,sheet_new_name)

    elif s=="APesn":
        auto_adj_width_sheet(s)
        time.sleep(2)
        freeze_row_sheet(s)
        time.sleep(1)
        s_columns=show_columns(s)
        for col in s_columns:
            print(col['c_name'])
            if col['c_name'] == 'OBJECTID' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        sheet_new_name="MCN Issues"
        rename_sheet(s,sheet_new_name)

    elif s=="StreetESN":
        auto_adj_width_sheet(s)
        time.sleep(2)
        freeze_row_sheet(s)
        time.sleep(1)
        s_columns=show_columns(s)
        for col in s_columns:
            print(col['c_name'])
            if col['c_name'] == 'OBJECTID' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        s_colu=show_columns(s)
        for col in s_colu:
            print(col['c_name'])
            if col['c_name'] == 'GIS_Address' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        sheet_new_name="Street Match Reference"
        rename_sheet(s,sheet_new_name)
        
    elif s=="StreetEsnU":
        auto_adj_width_sheet(s)
        time.sleep(2)
        freeze_row_sheet(s)
        time.sleep(1)
        s_columns=show_columns(s)
        for col in s_columns:
            print(col['c_name'])
            if col['c_name'] == 'OBJECTID' :
                del_col_sheet(s,col['c_pos'])
                print("column deleted successfully")
        time.sleep(2)
        auto_adj_width_sheet(s)
        sheet_new_name="No Match"
        rename_sheet(s,sheet_new_name)
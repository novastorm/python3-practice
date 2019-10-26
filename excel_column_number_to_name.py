def excel_column_number_to_name(column_number):
    results = ""
    
    while column_number > 0:
        results = chr(ord('A') + (column_number - 1) % 26) + results
        column_number = (column_number - 1) // 26
        
    return results

print(excel_column_number_to_name(1))
print(excel_column_number_to_name(2))
print(excel_column_number_to_name(26))
print(excel_column_number_to_name(27))

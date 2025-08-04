from src import clean_manager,analyze_manager

print('taking data and cleaning than writing to new csv')
clean = clean_manager.ManagerClean()
clean .write_to_csv()
print('csv created successfully')

print('analyzing data and writing to json all the analysis')
analyze_data = analyze_manager.ManagerAnalyzer()
analyze_data.write_to_json()
print('json created successfully')

import pandas as pd

# Load the Excel file
file_path = '/path/to/your/excel/file.xlsx'
novels_df = pd.read_excel(file_path)

# Adjusting the DataFrame to group themes into a single list under 'Themes'
theme_columns = [col for col in novels_df.columns if 'Theme' in col]
novels_df['Themes'] = novels_df[theme_columns].apply(lambda x: [theme for theme in x if not pd.isna(theme)], axis=1)

# Dropping the individual theme columns
novels_df.drop(columns=theme_columns, inplace=True)

# Convert the modified DataFrame to JSON and save to a file
json_file_path = '/path/to/save/json_file.json'
novels_df.to_json(json_file_path, orient='records', force_ascii=False)

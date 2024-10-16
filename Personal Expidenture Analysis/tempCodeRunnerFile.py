def load_csv_data(file_name="expense_data_1.csv"):
    data = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            row['Amount'] = float(row['Amount'])  # Amount ko float mein kr rahe
            row['INR'] = float(row['INR'])        # INR ko float mein kar rahe
            data.append(row)
    print(f"Data loaded from {file_name}.")
    return data
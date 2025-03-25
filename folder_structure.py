import os

def create_ticker_folder_structure(ticker):
    ticker_folder_path = os.path.join(os.path.join(os.getcwd(), "Companies"), ticker)
    os.makedirs(ticker_folder_path, exist_ok=True)

    for subfolder in ["Customers", "Suppliers"]:
        subfolder_path = os.path.join(ticker_folder_path, subfolder)
        os.makedirs(subfolder_path, exist_ok=True)
        for year in [2018, 2019, 2020, 2021, 2022, 2023]:
            os.makedirs(os.path.join(subfolder_path, str(year)), exist_ok=True)

    competitors_folder = os.path.join(ticker_folder_path, "Competitors")
    os.makedirs(competitors_folder, exist_ok=True)

    print(f"Folder structure created for {ticker}")

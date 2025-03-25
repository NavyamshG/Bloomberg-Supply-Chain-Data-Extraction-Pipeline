import pandas as pd
from folder_structure import create_ticker_folder_structure
from screenshot_capture import capture_screenshots_for_ticker
import os

def main():

    # # Load ticker list from CSV
    # input_csv = "data/source/test.csv"  # Provide path to input CSV
    # try:
    #     df = pd.read_csv(input_csv)
    # except FileNotFoundError:
    #     print(f"Error: Could not find file at {input_csv}. Please check the path.")
    #     return

    # Iterate over each ticker in the CSV
    while True:
        ticker = input("Please enter ticker id to continue : ")
                                              

        # Step 1: Create folder structure
        create_ticker_folder_structure(ticker)

        # Step 2: Capture screenshots for suppliers and customers
        try:
            capture_screenshots_for_ticker(ticker)
        except Exception as e:
            print(f"Error: Could not capture screenshots for {ticker}. Check logs for details.")
            continue

        # # Step 3: Export competitors' data
        # try:
        #     export_competitor_data(ticker)
        # except Exception as e:
        #     log_info(f"Error exporting competitor data for {ticker}: {e}")
        #     print(f"Error: Could not export competitor data for {ticker}. Check logs for details.")
        #     continue

        print(f"Completed processing for ticker: {ticker}")



if __name__ == "__main__":
    main()
import pyautogui
import time
import os
from datetime import datetime
import logging
from PIL import ImageGrab, Image
import numpy as np
import sys
from paddleocr import PaddleOCR
import pandas as pd

# Initialize PaddleOCR
ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Helper function to find the location of a UI element by image
def click_element(image_path, confidence=0.8):
    try:
        location = pyautogui.locateCenterOnScreen(image_path, confidence=confidence)
        if location:
            pyautogui.click(location)
            time.sleep(1)  # Slight delay to ensure UI updates
        else:
            print(f"Warning: Could not find element: {image_path}. Please verify the image reference.")
    except Exception as e:
        print(f"Error: Could not locate element {image_path}. Exception: {e}")


# Function to enter the ticker and select "US Equity"
def enter_ticker(ticker):
    pyautogui.click(x=500, y=120) # Click search bar
    pyautogui.write(ticker+" US Equity")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)


# Function to navigate to SPLC Supply Chain Analysis
def navigate_to_splc():
    pyautogui.write("SPLC")
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(2)


# Function to set the date
def set_date(year):
    time.sleep(2)

    #click_element("date_dropdown.png",40)  # Image of the date selector
    if str(year)=="2018":
        pyautogui.click(x=480, y=255)
        time.sleep(2)
        pyautogui.write("31")
        time.sleep(0.1)
        #pyautogui.press("tab")
        pyautogui.write("Dec")
        time.sleep(0.1)
        pyautogui.press("tab")
        pyautogui.write(str(year))
    else:
        print(year)
        pyautogui.click(x=440, y=250)
        pyautogui.write("\b"+str(year))
        time.sleep(2)
    pyautogui.press("enter")
    time.sleep(1)

# Function to scroll and take screenshots
def capture_scrolling_screenshots(save_dir, category):
    # scroll the outer window to botton
    pyautogui.click(x=1910, y=550)
    pyautogui.scroll(-200)  # Adjust scroll value as needed
    time.sleep(0.2)  # Ensure the UI has time to update
    
    pyautogui.click(x=1895, y=292)
    pyautogui.click(x=1895, y=292)
    pyautogui.click(x=1895, y=292)

    time.sleep(0.5)
    screenshot_index = 1
    try:
        os.remove("bbox_preview.png")
    except Exception as e:
        print(f"An error occurred: {e}")

    while not is_at_end():
        screenshot_path = os.path.join(save_dir, f"{category}_{screenshot_index}_{time.time()}.png")
        pyautogui.screenshot(screenshot_path)
        print(f"Captured screenshot: {screenshot_path}")
        time.sleep(1)
        # Scroll down and capture another screenshot
        for _ in range(5):
            pyautogui.scroll(-100)
            time.sleep(0.1)  # Ensure the UI has time to update

        screenshot_index += 1
    pyautogui.click(x=1910, y=550)
    pyautogui.scroll(200)  # Adjust scroll value as needed
    time.sleep(2)



def is_at_end(bbox=(10, 800, 1800, 980), saved_image_path="bbox_preview.png"):
    try:
        current_image = ImageGrab.grab(bbox)

        if not os.path.exists(saved_image_path):
            current_image.save(saved_image_path)
            print(f"Saved initial reference image as {saved_image_path}")
            return False  # Not at the end because we just started scrolling

        reference_image = Image.open(saved_image_path)

        current_image_array = np.array(current_image)
        reference_image_array = np.array(reference_image)

        if np.array_equal(current_image_array, reference_image_array):
            print("Reached the end of the list.")
            return True  # The images are the same, meaning no new content loaded
        else:
            # Save the current image as the new reference for the next comparison
            current_image.save(saved_image_path)
            print("Continuing to scroll...")
            return False  # Not at the end of the list

    except Exception as e:
        print(f"Error in is_at_end(): {e}")
        return True  # Return True to stop scrolling in case of an error
    
# Main function to capture data for suppliers and customers
def capture_screenshots_for_ticker(ticker):

    base_save_path = os.path.join(os.path.join(os.getcwd(), "Companies"), ticker)
    os.makedirs(base_save_path, exist_ok=True)

    # enter_ticker(ticker)
    # navigate_to_splc()

    # # Record supplier and customer counts from the graph
    # supplier_count, customer_count = record_counts_from_graph()
    # log_info(f"Suppliers: {supplier_count}, Customers: {customer_count}")

    for year in range(2018, 2024):
        time.sleep(2)
        set_date(year)
        time.sleep(3)

        time.sleep(2)
        pyautogui.click(x=220, y=300) #Click Key Metrics
        pyautogui.click(x=53, y=255) #Click Supplierss
        time.sleep(2)
        suppliers_save_path = os.path.join(base_save_path, "Suppliers", str(year))
        os.makedirs(suppliers_save_path, exist_ok=True)
        capture_scrolling_screenshots(suppliers_save_path, "Suppliers")
        
        pyautogui.click(x=220, y=300) #Click Key Metrics
        time.sleep(2)
        pyautogui.click(x=200, y=255) #Click customers
        time.sleep(2)
        customers_save_path = os.path.join(base_save_path, "Customers", str(year))
        os.makedirs(customers_save_path, exist_ok=True)
        capture_scrolling_screenshots(customers_save_path, "Customers")
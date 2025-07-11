from functions.json_creatation import create_json_data
from functions.inv_extraction import extract_inventories_from_excel, extract_annual_data
import os, openpyxl, glob
from pprint import pprint

def main():
    file_path = glob.glob(os.path.join("input", "*.xlsx"))

    inventory_sheet = openpyxl.load_workbook(file_path[0], data_only=True)

    seasonal_sheep = extract_inventories_from_excel(inventory_sheet, "sheep")
    json_data = create_json_data(seasonal_sheep, group=1, northOfTropicOfCapricorn=False, rainfallAbove600mm=False)

    json_data = extract_annual_data(inventory_sheet, json_data, "sheep")

    pprint(json_data)


if __name__ == "__main__":
    main()
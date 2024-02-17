import os
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USER_AGENTS_FILE = os.path.join(APP_DIR, "config", "user-agents.json")
DATA_DIRECTORY = os.path.join(APP_DIR, "data")
DATA_FILE_SUFFIX = "price.json"


class FileType:
    JSON = 0


# drugs settings
DRUG_NAMES_MBID_URL = "https://www.zyctd.com/Ajax/AjaxHandle.ashx?CommandName=common/MCodexService/GetCodexNameByLetter"
DRUG_LETTERS_URL = "https://www.zyctd.com/Ajax/AjaxHandle.ashx?CommandName=common/MCodexService/GetCodexLetter"
DRUG_PRICE_TABLE_URL = "https://www.zyctd.com/Breeds/GetPriceTable"
DRUG_AREA_URL = "https://www.zyctd.com/Breeds/GetAreaByMBID"
DRUG_SPEC_URL = "https://www.zyctd.com/Breeds/GetSpecByAreaID"

DRUG_CRAWLED_FILE = os.path.join(APP_DIR, "data", "drugs.txt")

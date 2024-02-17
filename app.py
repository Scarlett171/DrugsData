from utils import utils
from bll import drugs

if __name__ == "__main__":
    session = utils.build_requests_session()
    # letters = utils.get_letters()
    # letters_mapping = drugs.crawling_letters_mapping(session, letters)
    # print(letters_mapping)
    # utils.dumps_dict_2_json(letters_mapping, json_file="letters_mapping.json")
    # mbids_letters = utils.get_mbids_letters("letters_mapping.json")
    # mbids = drugs.crawling_names_and_mbids(session, mbids_letters)
    # print(mbids)
    # utils.dumps_dict_2_json(mbids, json_file="mbids.json")
    # drugs.crawling_drugs_price(session, mbids_file="mbids.json")
    utils.to_excel(excel_file="data.xlsx")

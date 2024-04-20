import unittest
import contract_data_processing
import json


class TestGeminiDataExtraction(unittest.TestCase):
    def test_gemini_data_extraction_cost(self):
        input_text = "Honeywell International Inc., Clearwater, Florida, has been awarded a maximum $70,000,000 firm-fixed-price, indefinite-delivery/indefinite-quantity contract to produce spare parts in support of the Radar Altimeter Common Core APN-209 receiver transmitters and indicator receiver transmitters spares and repairs. This was a sole-source acquisition using 10 U.S. Code 3204 (a)(1), as stated in Federal Acquisition Regulation 6.302-1 (a)(1). This is a five-year base contract with three one-year option periods. The performance completion date is Oct. 29, 2029. Using military service is Army. Type of appropriation is fiscal 2024 through 2029 Army working capital funds. The contracting activity is the Defense Logistics Agency Land and Maritime, Aberdeen Proving Ground, Maryland (SPRBL1-24-D-0007)."
        expected_result = "$70,000,000"
        result = contract_data_processing.gemini_data_extraction(input_text)
        result=contract_data_processing.clean_data(result)
        print(result)
        data = json.loads(result)
        cost = data['cost']
        self.assertEqual(cost, expected_result)

    def test_gemini_data_extraction_companyName(self):
        input_text = "Honeywell International Inc., Clearwater, Florida, has been awarded a maximum $70,000,000 firm-fixed-price, indefinite-delivery/indefinite-quantity contract to produce spare parts in support of the Radar Altimeter Common Core APN-209 receiver transmitters and indicator receiver transmitters spares and repairs. This was a sole-source acquisition using 10 U.S. Code 3204 (a)(1), as stated in Federal Acquisition Regulation 6.302-1 (a)(1). This is a five-year base contract with three one-year option periods. The performance completion date is Oct. 29, 2029. Using military service is Army. Type of appropriation is fiscal 2024 through 2029 Army working capital funds. The contracting activity is the Defense Logistics Agency Land and Maritime, Aberdeen Proving Ground, Maryland (SPRBL1-24-D-0007)."
        result = contract_data_processing.gemini_data_extraction(input_text)
        result=contract_data_processing.clean_data(result)
        print(result)
        data = json.loads(result)
        contractor = data['contractor']
        self.assertEqual(contractor, "Honeywell International Inc.")
if __name__ == '__main__':
    unittest.main()


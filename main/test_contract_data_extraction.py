import unittest
import json

from main import contract_data_extraction,util


class test_contract_data_extraction(unittest.TestCase):
    def test_gemini_data_extraction_cost1(self):
        # Test case with sample text
        input_text = "Honeywell International Inc., Clearwater, Florida, has been awarded a maximum $70,000,000 firm-fixed-price, indefinite-delivery/indefinite-quantity contract to produce spare parts in support of the Radar Altimeter Common Core APN-209 receiver transmitters and indicator receiver transmitters spares and repairs. This was a sole-source acquisition using 10 U.S. Code 3204 (a)(1), as stated in Federal Acquisition Regulation 6.302-1 (a)(1). This is a five-year base contract with three one-year option periods. The performance completion date is Oct. 29, 2029. Using military service is Army. Type of appropriation is fiscal 2024 through 2029 Army working capital funds. The contracting activity is the Defense Logistics Agency Land and Maritime, Aberdeen Proving Ground, Maryland (SPRBL1-24-D-0007)."

        expected_result = "$70,000,000"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        cost = data['cost']
        self.assertEqual(cost, expected_result)
        
    def test_gemini_data_extraction_cost2(self):
        # Test case with sample text
        input_text = "Raytheon Technologies Corp., Pratt and Whitney Military Engines, East Hartford, Connecticut, is awarded a $53,062,503 cost-plus-fixed-fee, fixed-price incentive (firm-target) order (N0001924F0010) against a previously issued basic ordering agreement (N0001922G0001). This order provides non-recurring engineering in support of early identification, development, and qualification of corrections to potential and actual F135 propulsion system operational issues, to include safety, reliability and maintainability problems identified through fleet usage. Additionally, this order provides for continued engine maturation, evaluates component life limits based on operational experience, improves operational readiness, and reduces engine maintenance and life cycle costs in support of the F-35 Lightning II program for the Air Force, Navy, F-35 Cooperative Program Partners and Foreign Military Sales customers. Work will be performed in East Hartford, Connecticut (93%); and Indianapolis, Indiana (7%), and is expected to be completed in December 2026. Fiscal 2024 research, development, test and evaluation (Navy) funds in the amount of $8,000,000; and fiscal 2024 research, development, test and evaluation (Air Force) funds in the amount of $4,000,000, will be obligated at time of award, none of which will expire at the end of the fiscal year. Naval Air Systems Command, Patuxent River, Maryland, is the contracting activity."
        

        expected_result = "$53,062,503"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        cost = data['cost']
        self.assertEqual(cost, expected_result)
        
    def test_gemini_data_extraction_cost3(self):
        # Test case with sample text
        input_text = "The Lighthouse for the Blind Inc.,** Seattle, Washington, has been awarded a maximum $29,131,666 firm-fixed-price, indefinite-delivery/indefinite-quantity contract for hydration bladders. This is a three-year contract with no option periods. The ordering period end date is March 26, 2027. Using military services are Army and Air Force. Type of appropriation is fiscal 2024 through 2027 defense working capital funds. The contracting activity is the Defense Logistics Agency Troop Support, Philadelphia, Pennsylvania (SPE1C1-24-D-B013)."
        
        expected_result = "$29,131,666"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        cost = data['cost']
        self.assertEqual(cost, expected_result)
        
    def test_gemini_data_extraction_cost4(self):
        # Test case with sample text
        input_text = "PCX Aerosystems-Manchester LLC, Manchester, Connecticut, has been awarded a maximum $22,099,593 firm-fixed-price, indefinite-delivery requirements contract for main extension assemblies. This was a limited competitive acquisition with one response received. This is a five-year contract with no option periods. The performance completion date is Sept. 15, 2029. Using military service is Army. Type of appropriation is fiscal 2024 through 2029 Army working capital funds. The contracting activity is the Defense Logistics Agency Aviation, Redstone Arsenal, Alabama."
        

        expected_result = "$22,099,593"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        cost = data['cost']
        self.assertEqual(cost, expected_result)
        
    
        
    def test_gemini_data_extraction_contractor1(self):
        # Test case with sample text
        input_text = "KBR Wyle Services LLC, Lexington Park, Maryland, was awarded a cost plus-fixed-fee and indefinite-delivery/indefinite-quantity contract with the ceiling of $99,000,000. This contract will be supporting the transition and integration of mission-critical Space Domain Awareness, Battle Management Command and Control, and space enterprise capabilities to support the Air Force Space Vehicles Directorate. Work is expected to be completed by April 2029. Fiscal 2024 research, development, test, and evaluation funds in the amount of $750,000 are being obligated on the first task order. Work will be performed in Colorado Springs, Colorado. This was a competitive acquisition with one offer received. The contracting activity responsible for this action is with Air Force Research Laboratory/RVKE, Kirtland Air Force Base, Albuquerque, New Mexico (FA9453-24-D-X002)."

        expected_result = "KBR Wyle Services LLC"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        contractor = data['contractor']
        self.assertEqual(contractor, expected_result)
     
    
    def test_gemini_data_extraction_contractor2(self):
        # Test case with sample text
        input_text = "Bernard Cap LLC,* Hialeah, Florida, has been awarded a maximum $43,907,294 firm-fixed-price, indefinite-delivery/indefinite-quantity contract for men\u2019s, woman\u2019s and General Officer lightweight jackets. This was a competitive acquisition with five responses received. This is a five-year contract with no option periods. The ordering period end date is March 4, 2029. Using military service is Air Force. Type of appropriation is fiscal 2024 through 2029 defense working capital funds. The contracting activity is the Defense Logistics Agency Troop Support, Philadelphia, Pennsylvania (SPE1C1-24-D-0035)."

        expected_result = "Bernard Cap LLC"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        contractor = data['contractor']
        self.assertEqual(contractor, expected_result)
        
    def test_gemini_data_extraction_contractor3(self):
        # Test case with sample text
        input_text = "Vigor Marine LLC, Portland, Oregon, was awarded a $15,845,754 firm-fixed-price modification to a previously awarded contract (N00024-19-C-4447) to perform a 237-day pier side extension for the USS Cape St. George (CG 71) fiscal 2021 modernization period availability. Work will be performed in Seattle, Washington, and is expected to be completed by October 2024. Fiscal 2018 other procurement (Navy) funding in the amount of $15,845,754 will be obligated at time of award and will not expire at the end of the current fiscal year. The Puget Sound Naval Shipyard and Intermediate Maintenance Facility, Bremerton, Washington, is the contracting activity. (Awarded Mar. 4, 2024)"

        expected_result = "Vigor Marine LLC"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        contractor = data['contractor']
        self.assertEqual(contractor, expected_result)

    def test_gemini_data_extraction_contractor4(self):
        # Test case with sample text
        input_text = "The Boeing Corp., St. Louis, Missouri, has been awarded a $21,300,367 firm-fixed-price contract modification (P00037) to previously awarded contract FA8634-21-C-2702 for the F-15 Eagle Passive/Active Warning Survivability System. The modification brings the total cumulative face value of the contract to $805,527,798. Work will be performed at Nashua, New Hampshire, and is expected to be completed by Nov. 30, 2025. Fiscal 2023 procurement funds in the amount of $21,300,367 are being obligated at time of award. The Air Force Life Cycle Management Center, Wright-Patterson Air Force Base, Ohio, is the contracting activity."


        expected_result = "Boeing Corp"

        # Call the method with the sample text
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        contractor = data['contractor']
        self.assertTrue(expected_result in contractor)
            
    def test_gemini_data_extraction_completion_date1(self):
        # Test case with sample text
        input_text = "Leidos Inc., Reston, Virginia, was awarded a $631,174,000 hybrid (cost-no-fee, cost-plus-fixed-fee, cost-plus-incentive-fee, firm-fixed-price, fixed-price-incentive) contract for development, integration, acquisition, bridging to logistics and operations. Work locations and funding will be determined with each order, with an estimated completion date of March 31, 2034. Army Contracting Command, Aberdeen Proving Ground, Maryland, is the contracting activity."
        expected_result = "March 31, 2034"
        
        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        date = data['completion_date']
        self.assertEqual(date, expected_result)

    def test_gemini_data_extraction_completion_date2(self):
        # Test case with sample text
        input_text = "Cummins Power Generation Inc., Minneapolis, Minnesota, was awarded a $459,000,000 firm-fixed-price contract for advanced medium mobile power sources generators. Bids were solicited via the internet with one received. Work locations and funding will be determined with each order, with an estimated completion date of Feb. 25, 2033. Army Contracting Command, Aberdeen Proving Ground, Maryland, is the contracting activity (W909MY-24-D-0002)."
        expected_result = "Feb. 25, 2033"

        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        date = data['completion_date']
        self.assertEqual(date, expected_result)

    def test_gemini_data_extraction_location1(self):
        # Test case with sample text
        input_text = "Kyrus Tech Inc., Sterling, Virginia, is being awarded a maximum ceiling $200,000,000 indefinite-delivery/indefinite-quantity contract (HDTRA1-24-D-0001) with a five-year base ordering period and an additional five-year optional ordering period. The contract allows for firm-fixed-price and cost-plus-fixed-fee type task orders. The contract provides for research, development, test, and evaluation in support of counter proliferation to combat weapons of mass destruction. Work will be performed in Sterling, Virginia; and Centennial, Colorado, and is expected to be complete by Jan. 21, 2034. This award is the result of a sole-source acquisition. Fiscal 2024 research, development, test, and evaluation funds in the amount of $1,957,442 are being obligated under the first task order at the time of award. The Defense Threat Reduction Agency, Fort Belvoir, Virginia, is the contracting activity."

        expected_result = "Sterling, Virginia"

        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        date = data['location']
        self.assertEqual(date, expected_result)

    def test_gemini_data_extraction_location2(self):
        # Test case with sample text
        input_text = "Intrepid LLC,* Huntsville, Alabama, was awarded a $534,439,851 cost-plus-fixed-fee contract for programmatic and technical support in the areas of program operations, systems engineering, systems test, systems software engineering and systems logistics. Bids were solicited via the internet with one received. Work locations and funding will be determined with each order, with an estimated completion date of July 16, 2029. Army Contracting Command, Redstone Arsenal, Alabama, is the contracting activity (W9113M-24-F-0006)."

        expected_result = "Huntsville, Alabama"

        result = contract_data_extraction.gemini_data_extraction(input_text)

        # Assert that the result matches the expected result
        result=util.clean_data(result)
        #print(result)
        data = json.loads(result)
        date = data['location']
        self.assertEqual(date, expected_result)

    # def test_gemini_data_extraction_work_location1(self):
    #     # Test case with sample text
    #     input_text = "L3Harris Technologies Inc., Colorado Springs, Colorado, was awarded a $17,780,613 contract modification (P00248) to previously awarded contract FA8823-20-C-0004 for the Ground-Based Electro-Optical Deep Space Surveillance (GEODSS). This change will result in support for GEODSS System sustainment, travel, materials and subcontractors, and licenses. The modification brings the total cumulative face value of the contract to $818,624,499. The location of performance is at White Sands Missile Range, New Mexico; Diego Garcia, British Indian Ocean Territories; and Maui, Hawaii; and is expected to be completed by Jan. 31, 2025. Fiscal 2024 operation and maintenance funds in the amount of $5,208,750 are being obligated at time of award. The Space Systems Center Directorate of Contracting, Peterson Space Force Base, Colorado Springs, Colorado, is the contracting activity. (Awarded Jan. 22, 2024)"
    #
    #     expected_result = "White Sands Missile Range, New Mexico; Diego Garcia, British Indian Ocean Territories; and Maui, Hawaii"
    #
    #     result = contract_data_extraction.gemini_data_extraction(input_text)
    #
    #     # Assert that the result matches the expected result
    #     result=util.clean_data(result)
    #     #print(result)
    #     data = json.loads(result)
    #     date = data['work_location']
    #     self.assertEqual(date, expected_result)
        
if __name__ == '__main__':
    unittest.main()

import sys
import os
HOME_DIR = os.path.expanduser('~')
sys.path.insert(0, HOME_DIR)
from eligibility_test.src.acme_eligibility import AcmeEligibility

test_jsons = [
    '{"employee_id": 23}',
    '{"emp_id": 32}',
    '{"employee_id": 23, "company": "Google"}'
]

obj = AcmeEligibility(HOME_DIR + '/eligibility_test/data/employees.tsv')
print ("Config is {0}".format(obj.config()))

for test_json in test_jsons:
    print ("Input : {0}, Response : {1}".format(test_json, obj.check_eligibility(test_json)))

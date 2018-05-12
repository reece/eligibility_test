import csv
import json
import pkg_resources

import jsonschema

from eligibility_test.eligibility import EligibilityBase


class AcmeEligibility(EligibilityBase):
    def __init__(self, file_path):
        with pkg_resources.resource_stream(__name__, "_data/schema.json") as f:
            schema_data = f.read()
        self.schema = json.loads(schema_data)

        self.emp_ids = []
        with open(file_path) as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                self.emp_ids.append(int(row['employee_id']))

    def config(self):
        return (json.dumps(self.schema))

    def validate(self, inp_json):
        is_valid = True
        try:
            jsonschema.validate(inp_json, self.schema)
        except Exception as e:
            is_valid = False
        return is_valid

    def check_eligibility(self, inp):
        final_msg = None
        resp_json = {}
        try:
            inp_json = json.loads(inp)
        except Exception as e:
            is_eligible = False
            final_msg = "Invalid json input format"
        else:
            is_eligible = self.validate(inp_json)
            if is_eligible is False:
                final_msg = "Input validation failed. Please validate against config"
                resp_json['config'] = json.loads(self.config())
            else:
                emp_id = inp_json['employee_id']
                is_eligible = False
                final_msg = "employee_id = {0} not found".format(emp_id)
                if emp_id in self.emp_ids:
                    is_eligible = True
                    final_msg = "Success"
            
        resp_json['eligible'] = is_eligible
        resp_json['message'] = final_msg
        return json.dumps(resp_json)

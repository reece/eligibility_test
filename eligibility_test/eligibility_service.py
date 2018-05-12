import os, sys
from flask import Flask, request, current_app, Response

from eligibility_test.acme_eligibility import AcmeEligibility

app = Flask(__name__)

HOME_DIR = os.path.expanduser('~')
acme_obj = AcmeEligibility(HOME_DIR + '/eligibility_test/data/employees.tsv')

@app.route("/v1/ping", methods=["GET"])
def ping_api():
    return Response(None, status=200)


@app.route("/v1/<string:partner>/config", methods=["GET"])
def config_api(partner):
    resp = None
    if partner == 'acme':
        resp = acme_obj.config()
        
    return Response(resp, status=200, mimetype="application/json")

@app.route("/v1/<string:partner>/check", methods=["POST"])
def check_api(partner):
    resp = None
    if partner == 'acme':
        inp_data = request.data.decode('utf-8')
        print ("Input data : {0}".format(inp_data))
        resp = acme_obj.check_eligibility(inp_data)
    return Response(resp, status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0")

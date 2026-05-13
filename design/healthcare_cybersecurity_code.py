# Welcome to your Python project!

import time

# Convert text values to numbers
def convert_to_numeric(value):
    if value.lower() == "high":
        return 3
    if value.lower() == "medium":
        return 2
    if value.lower() == "low":
        return 1
    else:
        return 0

#Risk Assessment Logic
def calculate_risk(likelihood, impact):
    li = convert_to_numeric(likelihood)
    i = convert_to_numeric(impact)

    if li == 0 or i == 0:
        return "Invalid input"

    return li * i


#Risk Classification
def classify_risk(score):
        if score >= 7:
            return "High Risk"
        elif score >=4:
            return "Medium Risk"
        else:
            return "Low Risk"


#Role-Based Access Control
def check_access(role):
    if role.lower() in ["admin", "doctor", "nurse"]:
        return "Access Granted"
    else:
        return "Access Denied"



#Threat Intelligence Module
#STRIDE

def classify_threat(threat):

    stride = {
        "phishing": "Spoofing",
        "ransomware": "Denial of Service",
        "data breach": "Information Disclosure",
        "insider attack": "Elevation of Privilege"
    }

    return stride.get(threat.lower(), "Unkown Threat")


#Compliance Mapping Mdule
#HIPAA/NIST

def check_compliance(encryption_enabled, rbac_enabled):

    if encryption_enabled and rbac_enabled:
        return "HIPAA/NIST Compliant"

    else: 

        return "Compliance Gap Found"

#Incident Response Module
def incident_response(risk_level):
    if risk_level == "High Risk":
        return "Activate Incident Response Team and Protocol"

    elif risk_level == "Medium Risk":
        return "Monitor and Investigate"

    else:

        return "Start Monitor"

#Reporting Dashboard Module
def generate_report():
    start_time = time.time()

    likelihood = input("Enter likelihood of asset (high, medium, low): ")
    impact = input("Enter impact of asset (high, medium, low): ")
    role = input("Enter your role: ")
    threat = input("Enter threat type (phishing, ransomware, data breach, insider attack): ")


    # Calculate risk
    risk_score = calculate_risk(likelihood, impact)

    print("\n======Healthcare Cybersecurity Report ======")

    print("\nRisk Score:", risk_score)

    if risk_score != "Invalid input": 
        risk_level = classify_risk(risk_score)    
        print("\nRisk Level:", risk_level)

        print("\nThreat Classification:", classify_threat(threat))

        compliance_status = check_compliance(
            True, 
            True
            )
        print("\nCompliance Status:", compliance_status)

        response = incident_response(risk_level)
        print("\nIncident Response:", response)

    # Check access
    print("\nAccess Result:", check_access(role))

    #End Timer
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nExecution Time: {execution_time:.6f} seconds")


#Unit Testing
def test_calculate_risk():
    tests = [
        calculate_risk("high", "high") == 9,
        calculate_risk("high", "medium") == 6,
        calculate_risk("medium", "high") == 6,
        calculate_risk("medium", "medium") == 4,
        calculate_risk("high", "low") == 3,
        calculate_risk("low", "high") == 3,
        calculate_risk("medium", "low") == 2,
        calculate_risk("low", "medium") == 2,
        calculate_risk("low", "low") == 1,
        calculate_risk("invalid", "high") == "Invalid input"
    ]

    return tests

def test_access():
    tests = [
        check_access("admin") == "Access Granted",
        check_access("doctor") == "Access Granted",
        check_access("nurse") == "Access Granted",
        check_access("guest") == "Access Denied",
    ]
    return tests
#Run tests
all_tests = test_calculate_risk() + test_access()

correct_tests = sum(all_tests)
total_tests = len(all_tests)

accuracy = (correct_tests / total_tests) * 100

#Quantitative Metric
print("\n======System Testing Results ======")
print(f"Passed Tests: {correct_tests}/{total_tests}")
print(f"System Accuracy: {accuracy:.2f}%")

if accuracy == 100:
    print("\nAll tests passed!")
else:
    print("\nSome tests failed.")
generate_report()

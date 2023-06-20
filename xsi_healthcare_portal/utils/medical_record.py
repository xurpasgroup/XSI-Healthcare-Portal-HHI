import frappe
import json

@frappe.whitelist()
def get_medical_record_list(record, patient_name):

    Medical_Record_List = frappe.get_all(record, filters={"patient":patient_name,"docstatus":1}, fields=["name","patient","docstatus"])

    return Medical_Record_List

@frappe.whitelist(allow_guest=True)
def get_medical_record_by_name(record, name):

    Medical_Record = frappe.get_last_doc(record, filters={"name":name})

    return Medical_Record
@frappe.whitelist()
def get_medical_record_count(patient):

    Medical_Record = {
    "PT Initial Evaluation":0,
    "Physical Therapy Visit Note":0,
    "HCS Activity Note":0,
    "End Shift Endorsement Template":0,
    "ECG Template":0,
    "Nurse Re Assessment Report":0,
    "Care Program":0,
    "Plan of Care":0,
    "Summary of Consultation":0,
    "SOAP":0,
    "Health Profiling Questionnaire":0,
    "Medical Symptom Questionnaire":0,
    "Doctor Examination Record":0,
    "Physical Therapy Evaluation Form":0,
    "Food Journal Sheet":0,
    "Home Executive Evaluation Summary":0,
    "Home Visit Record":0,
    "Home Environment Evaluation" :0,
    }

    Record = Medical_Record.keys()

    for each in Record:
        result  = frappe.get_all(each,filters={"docstatus":1,"patient":patient})
        count = len(result)
        Medical_Record[each] = count
    


    return Medical_Record
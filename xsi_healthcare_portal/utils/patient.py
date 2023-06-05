import frappe
import json
from xsi_healthcare_portal.utils.email import send_email_to_poe

def insert_patient(data):
    try:
        # data = json.loads(frappe.request.data)

        firstname = data["first_name"]
        middlename = data["middle_name"]
        lastname = data["last_name"]
        gender = data["sex"]
        birthdate = data["dob"]
        mobile = data["mobile"]
        email = data["email"]
        addressline = data["address_line"]
        city = data["city"]

        patient = frappe.new_doc("Patient")

        patient.first_name = firstname
        patient.middle_name = middlename
        patient.last_name = lastname
        patient.sex = gender
        patient.dob = birthdate
        patient.mobile = mobile
        patient.email = email
        patient.invite_user = 0
        newpatient = patient.insert(ignore_permissions=True)

        patient_address = frappe.new_doc("Address")
        patient_address.address_line1 = addressline
        patient_address.city = city
        patient_address.address_title = firstname + " " + lastname

        this_address = patient_address.insert(ignore_permissions=True)

        link_patient = frappe.get_doc("Patient", newpatient.name)
        link_address = frappe.get_doc("Address", this_address.name)

        link_address.append("links", dict(link_doctype="Patient", link_name = link_patient.name))
        link_address.save(ignore_permissions=True)
        # patient.address = patient_ad.name
        # patient.append("links", {
        # "link_doctype": "Address",
        # "link_name": p_address.name
        # })

        send_mail_result = send_email_to_poe(firstname, middlename, lastname, mobile, email)
        if send_mail_result != "Success":
            return  send_mail_result

    except Exception as e:
        return e

    return "Success"
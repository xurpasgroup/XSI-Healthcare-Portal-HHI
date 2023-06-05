import frappe
import json

@frappe.whitelist(allow_guest=True)
def test0002():
    subject = "FOR HEALTH CARE"
    recipient = "melvin.xurpas@gmail.com"
    message = "THIS IS SAMPLE FRAPPE MESSAGE"
    # email_queue = EmailQueue()
    try:
        frappe.sendmail(recipients=[recipient], subject=subject, message=message)
    except Exception as e:
        return e
    
    return "SUCCESS"
@frappe.whitelist(allow_guest=True)
def test0001():

    # patients = frappe.get_all("Address",filters={"name": "John Doe-Billing"},fields={"name","link_doctype"})
    # return patients

    Address = frappe.get_all("POE Emails",fields="email")
    return Address
@frappe.whitelist(allow_guest=True)
def get_poe_emails():
    emails = []

    POE_email = frappe.get_all("POE Emails",fields="email")

    for each in POE_email:
        emails.append(each.email)

    return emails

@frappe.whitelist(allow_guest=True)
def insert_patient():
    try:
        data = json.loads(frappe.request.data)

        firstname = data["first_name"]
        middlename = data["middle_name"]
        lastname = data["last_name"]
        gender = data["sex"]
        birthdate = data["dob"]
        mobile = data["mobile"]
        email = data["email"]
        # address = data["address"]

        patient = frappe.new_doc("Patient")

        patient.first_name = firstname
        patient.middle_name = middlename
        patient.last_name = lastname
        patient.sex = gender
        patient.dob = birthdate
        # patient.mobile = mobile
        # patient.email = email
        newpatient = patient.insert(ignore_permissions=True)

        patient_address = frappe.new_doc("Address")
        patient_address.address_line1 = "Sample Address"
        patient_address.city = "San Pablo"
        patient_address.address_title = firstname + " " + lastname

        this_address = patient_ad = patient_address.insert(ignore_permissions=True)

        link_patient = frappe.get_doc("Patient", newpatient.name)
        link_address = frappe.get_doc("Address", this_address.name)

        link_address.append("links", dict(link_doctype="Patient", link_name = link_patient.name))
        link_address.save(ignore_permissions=True)
        # patient.address = patient_ad.name
        # patient.append("links", {
        # "link_doctype": "Address",
        # "link_name": p_address.name
        # })

    except Exception as e:
        return e

    return "Successfully added patient"

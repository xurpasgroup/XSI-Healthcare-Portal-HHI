import frappe

def get_poe_emails():
    emails = []

    POE_email = frappe.get_all("POE Emails",fields="email")

    for each in POE_email:
        emails.append(each.email)

    return emails

def send_email_to_poe(first_name, middle_name, last_name, mobile, email):

    subject = "New Patient Record Has Been Submitted"
    recipient = get_poe_emails()
    message = f"""Hi PEOs,

A new record has been submitted. Kindly reach out to the patient and discuss Home Healthlink's program and services.

Name: {first_name}, {middle_name}, {last_name}
Mobile: {mobile}
Email: {email}

*** This is a system generated email, please don't reply. ***
"""
    # email_queue = EmailQueue()
    try:
        frappe.sendmail(recipients=[recipient], subject=subject, message=message)
    except Exception as e:
        return e
    
    return "Success"
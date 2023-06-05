import frappe
import json
from xsi_healthcare_portal.utils.patient import insert_patient

@frappe.whitelist(allow_guest=True)
def register_patient():
   data = json.loads(frappe.request.data)

   result = insert_patient(data)
   if result is "Success":
      return "Patient Added Successfully"
   else:
      return result


# @frappe.whitelist(allow_guest=True)
# def test_endpoint():
#    return "TESTING SUCCESS"


   

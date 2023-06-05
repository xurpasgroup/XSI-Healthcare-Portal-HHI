import frappe
import json
from utils.patient import insert_patient

@frappe.whitelist()
def register_patient():
   data = json.loads(frappe.request.data)

   result = insert_patient(data)
   if result is "Success":
      return "Patient Added Successfully"
   else:
      return result



   

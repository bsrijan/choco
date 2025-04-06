# Copyright (c) 2025, Srijan Bandreddi and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe
import base64

@frappe.whitelist()
def attach_file_to_call_doc(docname, filename, filedata):
    """
    Attach a decoded audio file to a specified document and link it to the 'call_recording' field.

    Args:
        docname (str): Name of the document to attach the file to.
        filename (str): Name of the file being uploaded.
        filedata (str): Base64-encoded content of the audio file.

    Returns:
        dict: Success message with file URL.
    """
    try:
        # Decode Base64 string into binary data
        decoded_file = base64.b64decode(filedata)

        # Save the file as an attachment
        filedoc = save_file(
            filename=filename,
            content=decoded_file,
            dt="Incoming Customer Call",  # Replace with your DocType name
            dn=docname,
            is_private=True
        )

        # Link the file URL to the 'call_recording' field in the document
        doc = frappe.get_doc("Incoming Customer Call", docname)
        
        # Ensure 'call_recording' is an Attach field in your DocType
        doc.call_recording = filedoc.file_url  # Update the Attach field with the file URL
        
        # Save changes to document
        doc.save()

        return {
            "status": "success",
            "message": f"File {filename} attached successfully.",
            "file_url": filedoc.file_url
        }
    except Exception as e:
        frappe.log_error(f"Error attaching file: {e}", "Attach File Error")
        return {
            "status": "error",
            "message": f"Failed to attach file: {e}"
        }

class IncomingCustomerCall(Document):
	pass

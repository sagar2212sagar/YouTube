from pdf_mail import sendpdf
import Connection_email as ce
import csv
sender_email=ce.sender_email
sender_email_password=ce.sender_email_password
receiver_email=ce.receiver_email

Subject="Hello {name}|| Daily Attachment"
Body="""
Hello {name},

Please find out the attachment with this email.


Thanks,
Sagar Prajapati


"""
filename='Sample'
location_file=r'C:\Users\sagar'
with open("Contact.csv") as f1:
    read=csv.reader(f1)
    next(read)
    for name,emailid in read:
        k=sendpdf(sender_email,emailid,sender_email_password,Subject.format(name=name),Body.format(name=name),filename,location_file)
        k.email_send()



import webapp2
import jinja2
from google.appengine.api import app_identity
import urllib2
from model import Info
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from urllib2 import Request, urlopen, URLError





JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class start(webapp2.RequestHandler):
    def get(self):
        file = open('home.html')
        self.response.write(file.read())


class home(webapp2.RequestHandler):
    def get(self):
        file = open('home.html')
        self.response.write(file.read())

class Ngo(webapp2.RequestHandler):
    def get(self):
        file = open('NGOs.html')
        self.response.write(file.read())

class Contact(webapp2.RequestHandler):
    def get(self):
        file = open('contact.html')
        self.response.write(file.read())

class Volunteer(webapp2.RequestHandler):
    def get(self):
        file = open('volunteers.html')
        self.response.write(file.read())

class About(webapp2.RequestHandler):
    def get(self):
        file = open('about.html')
        self.response.write(file.read())    


class Donate(webapp2.RequestHandler):
    def get(self):
        file = open('Donate.html')
        self.response.write(file.read())

class AddMoney(webapp2.RequestHandler):
    def get(self):
        file = open('addMoney.html')
        self.response.write(file.read())
    
class AddContact(webapp2.RequestHandler):
    def get(self):
        First_Name = self.request.get('first_name')
        email = self.request.get('email')
        city_name = self.request.get('city')
        state_name = self.request.get('state')
        zip_code = self.request.get('zip')
        

        b1 = Info()
        b1.First =First_Name
        b1.Email = email
        b1.City = city_name
        b1.State = state_name
        b1.Zip = zip_code
        self.response.write("<script>confirm('your form has been submitted')</script>")
        file = open('contact.html')
        self.response.write(file.read())
        
#         me = "romiljoshi172@gmail.com   "
#         my_password = "Doraemon5678"   
#         you = "romiljoshi172@gmail.com"

#         msg = MIMEMultipart('alternative')
#         msg['Subject'] = "Alert"
#         msg['From'] = me
#         msg['To'] = you

#         html = '<html><body><p>Hi, I have the following alerts for you!</p></body></html>'
#         part2 = MIMEText(html, 'html')

#         msg.attach(part2)

# # Send the message via gmail's regular server, over SSL - passwords are being sent, afterall
#         s = smtplib.SMTP('smtp.gmail.com',587)
# # uncomment if interested in the actual smtp conversation
# # s.set_debuglevel(1)
# # do the smtp auth; sends ehlo if it hasn't been sent already
#         s.login(me, my_password)

#         s.sendmail(me, you, msg.as_string())
#         s.quit()    
    





app = webapp2.WSGIApplication([
    ('/home' , home),
    ('/', start),
    ('/addcontact', AddContact),
    ('/NGOs' , Ngo),
    ('/volunteers',Volunteer),
    ('/contact' , Contact),
    ('/about' , About),
    ('/donate',Donate),
    ('/addDonation',AddMoney)

    

], debug=True)
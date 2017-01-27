import webapp2
import caesar
import cgi

def build_page(textarea_content):
    rotation_label = "<label>Rotate by: </label>"
    rotation_input = "<input type='number' name='rotation' />"

    message_label = "<label>Type a message: </label>"
    textarea = "<textarea name='message'>" + textarea_content + "</textarea>"
    
    submit = "<input type='submit' />"
    form = ("<form method='post'>" + 
            rotation_label + rotation_input + "<br>" + 
            message_label + textarea + "<br>" + 
            submit + "</form>")

    header = "<h2>Web Caesar</h2>"

    return header + form

class MainHandler(webapp2.RequestHandler):

        def get(self):
            content = build_page("")
            self.response.write(content)

        def post(self):
            # str() type conversion was needed in my implementation due to
            # the islower() function in my caeser.py
            message = str(self.request.get("message"))
            # int() type conversion was needed in my implementation due to
            # the + operand in my caeser.py
            rotation = int(self.request.get("rotation"))
            encrypted_message = caesar.encrypt(message, rotation)
            escaped_message = cgi.escape(encrypted_message)

            header = "<h2>Web Caesar</h2>"
            content = build_page(escaped_message)
            self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

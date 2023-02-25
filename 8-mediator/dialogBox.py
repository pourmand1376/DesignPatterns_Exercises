from components import TextBox, Button, CheckBox
class SignUpDialogBox:
    def __init__(self):
        self.textbox_username = TextBox()
        self.textbox_password = TextBox()

        self.agree_checkbox = CheckBox()
        self.signup_button = Button()

        self.textbox_username.attach(self.check_button)
        self.textbox_password.attach(self.check_button)
        self.agree_checkbox.attach(self.check_button)

    def simulate_changes(self):
        self.textbox_username.content = 'new username'
        self.textbox_password.content = 'new password'
        self.agree_checkbox.checked = True

    def check_button(self):
        if  len(self.textbox_username.content)>0 and \
            len(self.textbox_password.content)>0 and \
            self.agree_checkbox.checked==True:
                self.signup_button.enabled= True
                print('dialogBox Enabled')
        else:
             self.agree_checkbox.enabled= False
            
        

def main():
    dialog_box = SignUpDialogBox()
    dialog_box.simulate_changes()

if __name__ == '__main__':
    main()
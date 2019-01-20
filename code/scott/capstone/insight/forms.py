from django import forms

class IP_Form(forms.Form):
    ip_address = forms.GenericIPAddressField(protocol="both", unpack_ipv4=True)
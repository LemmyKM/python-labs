# A good way to think about how classes are blueprints of objects is to think of
# an empty form, for example one that you would get at a doctor's office.
# The empty form contains all the placeholders that define what information
# you need to fill to complete the form. If you fill it correctly, then you've
# successfully instantiated a form object, and your completed form now holds
# information that is specific to just you.
# Another patient's form will follow the same blueprint, but hold different info.
# You could say that every patient's filled form instance is part of the same
# empty form blueprint class that the doctor's office provided.
#
# Model such an application form as a Python class below, and instantiate
# a few objects from it.


class PatientForm:
    """Creates a patient form."""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def height(self, measure):
        return f"height is {measure} cm."
    
    def weight(self, weight_):
        return f"weight is {weight_} kg."

    def address(self, nr_street):
        return f"{self.first_name}'s address is : {nr_street}."
    
    def doctor(self, name_doctor):
        return f"his doctor is Dr. {name_doctor}"
    
    def surgery(self, *performed_surgery):
        return f"performed surgery : {performed_surgery}"
    
    def issue(self, *known_issues):
        return f"known issues are : {known_issues}."

    def __str__(self):
        return f"{self.first_name}, last name : {self.last_name}"

patient = PatientForm('Karel', 'Swinnen')

print()
print(patient.address('82 Willowvale Road, 2194 Blairgowrie'))
print(patient.height(173))
print(patient.weight(80))
print(patient.doctor('Mitchell'))
print(patient.surgery('burst appendix', 'hart valve'))
print(patient.issue('hypertension', 'bee sting allergy'))

print()
print(patient)
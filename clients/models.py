from django.db import models


class Client(models.Model):
    enrollment_date = models.DateTimeField('Enrollment Date')
    first_name = models.CharField('First Name', max_length=36)
    last_name = models.CharField('Last Name', max_length=60)

    # CROSS-REF WITH ACTUAL DATA BEFOR LOCKING IN VALIDATIONS
    family_size = ''
    over64 = ''
    under19 = ''
    addr_line_1 = ''
    addr_line_2 = ''
    city = ''
    state = ''
    zipcode = ''
    jeffco_resident = ''
    data_review_date = ''
    ethnicity = ''
    validated = ''
    validated_date = ''
    created_date = ''
    updated_date = ''


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Visit(models.Model):
    client = models.ForeignKey(Client)

    # FIXME:
    # def __str__(self):
    #     return '{} {}'.format(self.date_of_vist, self.first_name, self.last_name)

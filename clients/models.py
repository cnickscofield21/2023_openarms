from django.db import models


US_STATES = (
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District of Columbia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PA', 'Pennsylvania'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')
)


ETHNICITIES = (
    ('D', 'Will not answer'),
    ('W', 'White'),
    ('H', 'Hispanic'),
    ('A', 'Asian'),
    ('B', 'Black'),
    ('N', 'Native'),
)


class Client(models.Model):
    enrollment_date = models.DateTimeField('Enrollment Date')
    first_name = models.CharField('First Name', max_length=36, blank=False)
    last_name = models.CharField('Last Name', max_length=60, blank=False)
    family_size = models.PositiveSmallIntegerField('Family Size', default=1, blank=False)
    over64 = models.PositiveSmallIntegerField('Over 64', default=0, blank=False)
    under19 = models.PositiveSmallIntegerField('Under 19', default=0, blank=False)
    addr_line_1 = models.CharField('Address 1', max_length=60, blank=False)
    addr_line_2 = models.CharField('Address 2', max_length=60, blank=True)
    city = models.CharField('City', max_length=60, blank=False)
    state = models.CharField('State', choices=US_STATES, default='CO', blank=False)
    zipcode = models.CharField('Zipcode', max_length=10, blank=False)
    jeffco_resident = models.BooleanField('Jeffco Resident', default=True)
    data_review_date = models.DateTimeField('Data Review Date')
    ethnicity = models.CharField('Ethnicity', choices=ETHNICITIES, default='D', blank=False)
    validated = models.BooleanField('Validated', default=False)
    validated_date = models.DateTimeField('Validated Date')
    created_date = models.DateTimeField('Created Date')
    updated_date = models.DateTimeField('Updated Date')
    comments = models.CharField('Comments', max_length=320, blank=True)
    banned = models.BooleanField('Banned', default=False)


    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Visit(models.Model):
    # visit_id = models.('visit id')
    # FIXME: on_delete=models.CASCADE may not be the desired effect here
    member_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    visit_date = models.DateTimeField('Visit Date', default=False)
    line_number = models.PositiveSmallIntegerField('Line Number', default=False)
    commodities_box = models.PositiveSmallIntegerField('Commodities Box', default=False)
    commodities_box_num = models.PositiveSmallIntegerField('Commodities Box Num', default=False)
    commodities_line_num = models.PositiveSmallIntegerField('Commodities Line Num', default=False)
    commodities_box_pack = models.PositiveSmallIntegerField('Commodities Box Pack', default=False)


    # FIXME:
    # def __str__(self):
    #     return '{} {}'.format(self.date_of_vist, self.first_name, self.last_name)

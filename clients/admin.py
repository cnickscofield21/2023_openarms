from django.contrib import admin

from .models import Client, Visit


class ClientAdmin(admin.ModelAdmin):
    fields = [
        'enrollment_date',
        'first_name',
        'last_name',
        'family_size',
        'over64',
        'under19',
        'addr_line_1',
        'addr_line_2',
        'city',
        'state',
        'zipcode',
        'jeffco_resident',
        'data_review_date',
        'ethnicity',
        'validated',
        'validated_date',
        'created_date',
        'updated_date',
        'comments',
    ]
    list_display = ['last_name', 'first_name', 'city', 'state']
    list_filter = ['enrollment_date']

class VisitAdmin(admin.ModelAdmin):
    fields = [
        'member_id',
        'visit_date',
        'line_number',
        'commodities_box',
        'commodities_box_num',
        'commodities_line_num',
        'commodities_box_pack',
    ]
    list_display = ['visit_date', 'commodities_box', 'commodities_box_num', 'commodities_line_num', 'commodities_box_pack']
    list_filter = ['visit_date']

admin.site.register(Client, ClientAdmin)
admin.site.register(Visit, VisitAdmin)
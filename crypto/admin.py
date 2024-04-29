from django.contrib import admin
from .models import CustomUser, Payment,Currency, History, Withdrawal, Investment, Reinvestment,NotificationVisibility, Transfer, Notification, Plan, SystemEaring, ReferalBonus, Contact



admin.site.site_header = 'Zenithport Administrator'
admin.site.site_title = 'Zenithport Administrator'




admin.site.register(CustomUser)
admin.site.register(Payment)
admin.site.register(Currency)
admin.site.register(Plan)
admin.site.register(History)
admin.site.register(Withdrawal)
admin.site.register(Investment)
admin.site.register(Transfer)
admin.site.register(Notification)
admin.site.register(ReferalBonus)
admin.site.register(SystemEaring)
admin.site.register(Contact)
admin.site.register(Reinvestment)
#admin.site.register(NotificationVisibility) 





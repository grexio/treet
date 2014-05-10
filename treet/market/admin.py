from django.contrib import admin

from market.models import Treet, TreetReview, TreetPurchase

class TreetAdmin(admin.ModelAdmin):
    list_display = ('title', 'user')


class TreetPurchaseAdmin(admin.ModelAdmin):
    list_display = ('purchaser', 'seller', 'treet',
                    'state', 'purchased_on', 'resolved_on',)


class TreetReviewAdmin(admin.ModelAdmin):
    list_display = ('user', 'treet_purchase', 'title', 'rating')

admin.site.register(Treet, TreetAdmin)
admin.site.register(TreetPurchase, TreetPurchaseAdmin)
admin.site.register(TreetReview, TreetReviewAdmin)

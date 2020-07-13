from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):

    # Show most recent objects first.
    ordering = ['-id']

    # The default value is "-".
    empty_value_display = ''

    def __init__(self, model, admin_site):
        super().__init__(model, admin_site)

        # Enable searching in all the list_display fields.
        self.search_fields = self.list_display

        # Make all list_display fields clickable.
        self.list_display_links = self.list_display

from django import forms
from .models import *
import datetime

JAPANESE_MONTHS = {
    1: "1月", 2: "2月", 3: "3月", 4: "4月",
    5: "5月", 6: "6月", 7: "7月", 8: "8月",
    9: "9月", 10: "10月", 11: "11月", 12: "12月",
}

class MonthYearSelectWidget(forms.Widget):
    def __init__(self, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = '<select name="%s" class="select border-0">' % name
        output += '<option value="" selected>%s</option>' % self.empty_label

        for year in range(2023, datetime.date.today().year + 1):
            for month in range(1, 13):
                value_option = datetime.date(year, month, 1)
                # Format the option value as "YYYY-MM"
                value_option_str = value_option.strftime("%Y-%m")
                month_selected = "selected" if value_option_str == value else ""
                output += '<option value="%s" %s>%s年%s</option>' % (value_option_str, month_selected, year, JAPANESE_MONTHS[month])

        output += '</select>'
        return output

class MandaraYearSelectWidget(forms.Widget):
    def __init__(self, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = '<select name="%s" class="select" id="id_%s">' % (name, name)
        output += '<option value="" selected>%s</option>' % self.empty_label

        for year in range(datetime.date.today().year, datetime.date.today().year + 3):
            for month in range(1, 13):
                if month > datetime.date.today().month or year > datetime.date.today().year:
                    value_option = datetime.date(year, month, 1)
                    # Format the option value as "YYYY-MM"
                    value_option_str = value_option.strftime("%Y%m")
                    month_selected = "selected" if value_option_str == value else ""
                    output += '<option value="%s" %s>%s年%s</option>' % (value_option_str, month_selected, year, JAPANESE_MONTHS[month])

        output += '</select>'
        return output

class MandaraMonthYearSelectWidget(forms.Widget):
    def __init__(self, company_id=None, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        self.company_id = company_id
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        today = datetime.date.today()
        mandara_periods = MandaraPeriod.objects.all().filter(company_id=self.company_id,end_date__lt=today
                ).order_by('start_date')
        output = '<select name="%s" class="select border-0">' % name
        output += '<option value="" selected>%s</option>' % self.empty_label
        print(value)
        for period in mandara_periods:
            date = period.start_date.strftime("%Y-%m-%d")
            date_text = period.display_time_start()
            if name == 'end':
                date = period.end_date.strftime("%Y-%m-%d")
                date_text = period.display_time_end()
            month_selected = "selected" if date == value else ""
            output += '<option value="%s" %s>%s</option>' % (date, month_selected, date_text)

        output += '</select>'
        return output
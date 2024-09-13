from django import forms
from .models import *
from datetime import datetime
import calendar

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
    
class CultetSheetMonthYearSelectWidget(forms.Widget):
    def __init__(self, company_id=None, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        self.company_id = company_id
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = '<select name="%s" class="select border-0">' % name
        output += '<option value="" selected>%s</option>' % self.empty_label

        # Lấy evaluation_start đầu tiên
        first_period = HonneEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('evaluation_start').first()
        if first_period:
            first_date = first_period.evaluation_start

            current_date = datetime.now().date()

            # Tạo danh sách các tháng từ first_date đến current_date hoặc last_date
            year, month = first_date.year, first_date.month

            end_date = current_date

            while first_date <= end_date:
                date_text = f'{year}年{month}月'
                if name == "honne_start":
                    date = f'{year}-{str(month).zfill(2)}-01'
                else:
                    last_day = calendar.monthrange(year, month)[1]
                    date = f'{year}-{str(month).zfill(2)}-{last_day}'
                    
                month_selected = "selected" if date == value else ""
                output += '<option value="%s" %s>%s</option>' % (date, month_selected, date_text)

                # Chuyển sang tháng tiếp theo
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
                first_date = datetime(year, month, 1).date()

        output += '</select>'
        return output

class SelfcheckMonthYearSelectWidget(forms.Widget):
    def __init__(self, company_id=None, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        self.company_id = company_id
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = '<select name="%s" class="select border-0">' % name
        output += '<option value="" selected>%s</option>' % self.empty_label

        # Lấy evaluation_start đầu tiên
        first_period = SelfcheckEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('evaluation_start').first()
        if first_period:
            first_date = first_period.evaluation_start

            current_date = datetime.now().date()

            # Tạo danh sách các tháng từ first_date đến current_date hoặc last_date
            year, month = first_date.year, first_date.month

            end_date = current_date
    
            while first_date <= end_date:
                date_text = f'{year}年{month}月'
                if name == "selfcheck_start":
                    date = f'{year}-{str(month).zfill(2)}-01'
                else:
                    last_day = calendar.monthrange(year, month)[1]
                    date = f'{year}-{str(month).zfill(2)}-{last_day}'
                    
                month_selected = "selected" if date == value else ""
                output += '<option value="%s" %s>%s</option>' % (date, month_selected, date_text)

                # Chuyển sang tháng tiếp theo
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
                first_date = datetime(year, month, 1).date()

        output += '</select>'
        return output

class MandaraMonthYearSelectWidget(forms.Widget):
    def __init__(self, company_id=None, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        self.company_id = company_id
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = '<select name="%s" class="select border-0">' % name
        output += '<option value="" selected>%s</option>' % self.empty_label

        # Lấy evaluation_start đầu tiên
        first_period = MandaraPeriod.objects.filter(company_id=self.company_id).order_by('start_date').first()
        if first_period:
            first_date = first_period.start_date

            current_date = datetime.now().date()

            # Tạo danh sách các tháng từ first_date đến current_date hoặc last_date
            year, month = first_date.year, first_date.month

            end_date = current_date

            while first_date <= end_date:
                date_text = f'{year}年{month}月'
                if name == "mandara_start":
                    date = f'{year}-{str(month).zfill(2)}-01'
                else:
                    last_day = calendar.monthrange(year, month)[1]
                    date = f'{year}-{str(month).zfill(2)}-{last_day}'
                    
                month_selected = "selected" if date == value else ""
                output += '<option value="%s" %s>%s</option>' % (date, month_selected, date_text)

                # Chuyển sang tháng tiếp theo
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
                first_date = datetime(year, month, 1).date()

        output += '</select>'
        return output

class BonknowMonthYearSelectWidget(forms.Widget):
    def __init__(self, company_id=None, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        self.company_id = company_id
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = '<select name="%s" class="select border-0">' % name
        output += '<option value="" selected>%s</option>' % self.empty_label

        # Lấy evaluation_start đầu tiên
        first_period = BonknowEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('evaluation_start').first()
        if first_period:
            first_date = first_period.evaluation_start

            current_date = datetime.now().date()

            # Tạo danh sách các tháng từ first_date đến current_date hoặc last_date
            year, month = first_date.year, first_date.month

            end_date = current_date

            while first_date <= end_date:
                date_text = f'{year}年{month}月'
                if name == "bonknow_start":
                    date = f'{year}-{str(month).zfill(2)}-01'
                else:
                    last_day = calendar.monthrange(year, month)[1]
                    date = f'{year}-{str(month).zfill(2)}-{last_day}'
                    
                month_selected = "selected" if date == value else ""
                output += '<option value="%s" %s>%s</option>' % (date, month_selected, date_text)

                # Chuyển sang tháng tiếp theo
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
                first_date = datetime(year, month, 1).date()

        output += '</select>'
        return output
    
class FanTotalMonthYearSelectWidget(forms.Widget):
    def __init__(self, company_id=None, attrs=None, empty_label="----"):
        self.empty_label = empty_label
        self.company_id = company_id
        super().__init__(attrs)

    def render(self, name, value, attrs=None, renderer=None):
        output = '<select name="%s" class="select border-0">' % name
        output += '<option value="" selected>%s</option>' % self.empty_label

        # Lấy evaluation_start đầu tiên
        first_period_bonknow = BonknowEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('evaluation_start').first()
        first_period_mandara = MandaraPeriod.objects.filter(company_id=self.company_id).order_by('start_date').first()
        first_period_selfcheck = SelfcheckEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('evaluation_start').first()
        first_period_honne = HonneEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('evaluation_start').first() 

        end_period_bonknow = BonknowEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('-evaluation_start').first()
        end_period_mandara = MandaraPeriod.objects.filter(company_id=self.company_id).order_by('-start_date').first()
        end_period_selfcheck = SelfcheckEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('-evaluation_start').first()
        end_period_honne = HonneEvaluationPeriod.objects.filter(company_id=self.company_id).order_by('-evaluation_start').first() 

        dates = []
        last_dates = []

        if first_period_bonknow:
            dates.append(first_period_bonknow.evaluation_start)
        if first_period_mandara:
            dates.append(first_period_mandara.start_date)
        if first_period_selfcheck:
            dates.append(first_period_selfcheck.evaluation_start)
        if first_period_honne:
            dates.append(first_period_honne.evaluation_start)  

        if end_period_bonknow:
            last_dates.append(end_period_bonknow.evaluation_start)
        if end_period_mandara:
            last_dates.append(end_period_mandara.start_date)
        if end_period_selfcheck:
            last_dates.append(end_period_selfcheck.evaluation_start)
        if end_period_honne:
            last_dates.append(end_period_honne.evaluation_start)           

        if dates:

            first_date = min(dates)
            last_date = max(last_dates)

            current_date = last_date

            # Tạo danh sách các tháng từ first_date đến current_date hoặc last_date
            year, month = first_date.year, first_date.month

            end_date = current_date

            while first_date <= end_date:
                date_text = f'{year}年{month}月'
                if name == "total_start":
                    date = f'{year}-{str(month).zfill(2)}-01'
                else:
                    last_day = calendar.monthrange(year, month)[1]
                    date = f'{year}-{str(month).zfill(2)}-{last_day}'
                    
                month_selected = "selected" if date == value else ""
                output += '<option value="%s" %s>%s</option>' % (date, month_selected, date_text)

                # Chuyển sang tháng tiếp theo
                if month == 12:
                    month = 1
                    year += 1
                else:
                    month += 1
                first_date = datetime(year, month, 1).date()

        output += '</select>'
        return output
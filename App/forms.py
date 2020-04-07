from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from App.models import Periods


class PeriodsForm(forms.ModelForm):
    class Meta:
        model = Periods
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        agreement_name = cleaned_data.get("agreement")
        res = self.validate_date(cleaned_data.get("period_start"), agreement_name)
        res2 = self.validate_date(cleaned_data.get("period_finish"), agreement_name)
        res3 = self.check_start_finish_date(cleaned_data.get("period_start"), cleaned_data.get("period_finish"))

        if res3 is False:
            raise forms.ValidationError("Дата старта больше чем дата начала")

        if res is False or res2 is False:
            error_text = "Неправильній период дат. Пересекающийся период {} - {}. Ошибочная дата {}".format(self.error_date_start, self.error_date_finish, self.wrong_date)
            raise forms.ValidationError(error_text)
            # return None

    def check_start_finish_date(self, period_start, period_finish):
        if period_start >= period_finish:
            return False
        else:
            return True

    def validate_date(self, value, agreement_name):
        agreement_list = Periods.objects.filter(agreement=agreement_name).all()
        period_start_list = [obj.period_start for obj in agreement_list]
        period_finish_list = [obj.period_finish for obj in agreement_list]

        for date_start in period_start_list:
            for date_finish in period_finish_list:
                if date_start <= value <= date_finish:
                    self.error_date_start = date_start
                    self.error_date_finish = date_finish
                    self.wrong_date = value
                    return False
        else:
            return True
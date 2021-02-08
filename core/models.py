from django.db import models
import datetime as dt

class Data(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    portfolio_name = models.CharField(max_length=255,blank=True,null=True)#
    campaign_type = models.CharField(max_length=255,blank=True,null=True)
    campaign_name = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255,blank=True,null=True)
    currency = models.CharField(max_length=255,blank=True,null=True)
    budget = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=2)
    targeting_type = models.CharField(max_length=255,blank=True,null=True)
    bidding_strategy = models.CharField(max_length=255,blank=True,null=True)
    impressions = models.CharField(max_length=255,blank=True,null=True)#models.PositiveIntegerField()
    last_year_impressions = models.CharField(max_length=255,blank=True,null=True)#models.DateField()
    clicks = models.CharField(max_length=255,blank=True,null=True)#models.PositiveIntegerField()
    last_year_clicks = models.CharField(max_length=255,blank=True,null=True)#models.PositiveIntegerField()
    click_thru_rate_ctr = models.CharField(max_length=255,blank=True,null=True)#models.FloatField()
    spend = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=2)
    last_year_spend = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_click_cpc = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=5)
    last_year_cost_per_click_cpc = models.CharField(max_length=255,blank=True,null=True)#models.PositiveIntegerField()
    seven_day_total_orders = models.CharField(max_length=255,blank=True,null=True)#models.PositiveIntegerField()
    total_advertising_cost_of_sales_acos = models.CharField(max_length=255,blank=True,null=True)#models.FloatField()
    total_return_on_advertising_Spend_roas = models.CharField(max_length=255,blank=True,null=True)#models.FloatField()
    seven_day_total_sales = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        self.budget = self.budget.replace('€','')
        self.click_thru_rate_ctr = self.click_thru_rate_ctr.replace('%','')

        super().save(*args, **kwargs)

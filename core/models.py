from django.db import models
import datetime as dt

class Data(models.Model):
    start_date = models.DateField()
    end_date = models.DateField(blank=True,null=True)
    portfolio_name = models.CharField(max_length=255,blank=True,null=True)
    campaign_type = models.CharField(max_length=255,blank=True,null=True)
    campaign_name = models.CharField(max_length=255,blank=True,null=True)
    status = models.CharField(max_length=255,blank=True,null=True)
    currency = models.CharField(max_length=255,blank=True,null=True)
    budget = models.DecimalField(max_digits=10, decimal_places=2, blank=True,null=True)
    targeting_type = models.CharField(max_length=255,blank=True,null=True)
    bidding_strategy = models.CharField(max_length=255,blank=True,null=True)
    impressions = models.PositiveIntegerField(blank=True,null=True)
    last_year_impressions = models.PositiveIntegerField(blank=True,null=True)
    clicks = models.PositiveIntegerField(blank=True,null=True)
    last_year_clicks = models.PositiveIntegerField(blank=True,null=True)
    click_thru_rate_ctr = models.CharField(max_length=255,blank=True,null=True)#models.FloatField()
    spend = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=2)
    last_year_spend = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_click_cpc = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=5)
    last_year_cost_per_click_cpc = models.CharField(max_length=255,blank=True,null=True)#models.PositiveIntegerField()
    seven_day_total_orders = models.PositiveIntegerField()
    total_advertising_cost_of_sales_acos = models.CharField(max_length=255,blank=True,null=True)#models.FloatField()
    total_return_on_advertising_Spend_roas = models.FloatField(max_length=255,blank=True,null=True)
    seven_day_total_sales = models.CharField(max_length=255,blank=True,null=True)#models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        print('-------------')
        self.budget = self.budget.replace('€','')
        self.click_thru_rate_ctr = self.click_thru_rate_ctr.replace('%','')
        self.spend = self.spend.replace('€','')
        self.last_year_spend = self.last_year_spend.replace('€','')
        self.cost_per_click_cpc = self.cost_per_click_cpc.replace('€','')
        self.total_advertising_cost_of_sales_acos = self.total_advertising_cost_of_sales_acos.replace('%','')
        self.seven_day_total_sales = self.seven_day_total_sales.replace('€','')

        super().save(*args, **kwargs)

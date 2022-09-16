from django.shortcuts import render
from django.views.generic import ListView
from shop.models import Goods
import pandas as pd


# create list of goods ordered by date of creation and pagination 20 items by page
class GoodsListView(ListView):
    model = Goods
    ordering = ('-date_added',)
    template_name = 'shop/goods_list.html'
    paginate_by = 20

    # create validator for field 'date_added' witch should be more than current date
    def get_queryset(self):
        return Goods.objects.filter(date_added__gt=pd.Timestamp.now())










#
# # example
# record = {
#     'Date': ['2022-01-01', '2022-02-02', '2022-03-04', '2022-04-05', '2022-05-08', '2022-06-09'],
#     'B': [22, None, None, None, 18, 30]
# }
# df = pd.DataFrame(record, columns=['Date', 'B'])
#
# # replace None with previous value
# df['B'].fillna(method='ffill', inplace=True)



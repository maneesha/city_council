from django.conf.urls import patterns, include, url
#from views import hello, goodbye, gender_view, gender_search, choice_results, show_chart, show_chart_year, search_page, slider_form_test
from views import *

from django.contrib import admin


#"When somebody visits the URL /foo/, call the view function foo_view()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'city_council.views.home', name='home'),
    # url(r'^city_council/', include('city_council.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #the regex is the url, the 2nd term is the view
   
    #simple tests, just say hello & goodbye
    url(r'^hello/$', hello),
    url(r'^goodbye/$', goodbye),

    #admin interface   
    url(r'^admin/', include(admin.site.urls)),

    #static page - renders pie chart for all data by gender
    url(r'^chart/$', gender_view),

    #select male/female & get list of ALL councilpeople of that gender
    url(r'^choice/$', gender_search),

    #contains a non-working slider to choose year
    url(r'^genderbyyear/$', show_chart_year),

    #radio button to select a year; render pie chart for that year 
    url(r'^gbyr/$', gender_race_by_year_radio),

    #render bar graph of unique councilmembers
    url(r'^unique/$', unique_councilmembers),

    #show how councilmembers left their seats
    url(r'departing/$', departing),

    url(r'^$', index),

)

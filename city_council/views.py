from django.shortcuts import render
from council.models import Councilperson, Term
#from chartit import PivotDataPool, PivotChart
from django.db.models import Count
from django.shortcuts import render_to_response
from council.forms import *
from django.template import RequestContext


def hello(request):
    return render(request, 'hello.html')

def goodbye(request):
    return render(request, 'goodbye.html')

def gender_view(request):
    #Create a DataPool with the data we want to retreive
    #terms is a list of all fields (both for x-axis and y-axis) to retrieve from the model.
    gender_data = PivotDataPool(series =[{'options': \
        {'source':Councilperson.objects.all(), \
        'categories':['gender']}, \
        'terms':{'count_gender':Count('gender')}\
        }])

    #chartit docs don't make this clear.... Even if you have no chartoptions you must include empty dict!!
    #also chartit must be in settings installed apps
    #Data labels display as expected in bar graph but not in pie chart
    pivcht = PivotChart(datasource = gender_data, \
        series_options = [{'options': \
        {'type':'pie'}, \
        'terms':['count_gender']}], \
        chart_options = {'title':{'text':'City Council By Gender'}})

    #also remember render_to_response takes the html template as a parameter
    return render_to_response('pivcht.html', {'pivcht':pivcht})


#page that lets you choose gender or race breakdown - text only
def gender_search(request):
    #This just calls the html template identified below
    return render(request, 'choice.html')

def show_chart_year(request):
    #this function will return number of M and number of F, to be passed into jquery to create a graph but it does not actually work
    #html template contains a non-working slider 

    if 'year' in request.GET and request.GET['year']:
        year = request.GET['year']
        male = Term.objects.filter(start_date__lte = year).filter(end_date__gte = year).filter(councilperson__gender__exact = 'M').count()
        female = Term.objects.filter(start_date__lte = year).filter(end_date__gte = year).filter(councilperson__gender__exact = 'F').count()
    else:
        male, female = 0,0       

    return render_to_response('chartpage_year.html', {'male':male, 'female':female})


def gender_race_by_year_radio(request):
    #male, female need to be initialized because they are called in render_to_response below
    #need to have something to load the page
    #maybe I can have a conditional in the js so that chart does not load unless male, female > 0
    male, female, white, black, asian, hispanic, race_unknown, democrat, republican, party_unknown, query = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,0
    form = SearchFormByYear()
    councilpeople = []
    show_results = False
    if 'query' in request.GET:
        show_results = True
        query = request.GET['query'].strip()  #query is year
        if query:
            form = SearchFormByYear({'query':query})
            male = Term.objects.filter(start_date__lte = query).filter(end_date__gte = query).filter(councilperson__gender__exact = 'M').count()
            female = Term.objects.filter(start_date__lte = query).filter(end_date__gte = query).filter(councilperson__gender__exact = 'F').count()
            white = Term.objects.filter(start_date__lte = query).filter(end_date__gte = query).filter(councilperson__race__exact = 'White').count()
            black = Term.objects.filter(start_date__lte = query).filter(end_date__gte = query).filter(councilperson__race__exact = 'Black').count()
            asian = Term.objects.filter(start_date__lte = query).filter(end_date__gte = query).filter(councilperson__race__exact = 'Asian').count()
            hispanic = Term.objects.filter(start_date__lte = query).filter(end_date__gte = query).filter(councilperson__race__exact = 'Hispanic').count()
            race_unknown = Term.objects.filter(start_date__lte=query).filter(end_date__gte = query).filter(councilperson__race__exact = 'unknown').count()
            democrat = Term.objects.filter(start_date__lte=query).filter(end_date__gte = query).filter(party__exact = 'Democrat').count()
            republican = Term.objects.filter(start_date__lte=query).filter(end_date__gte = query).filter(party__exact = 'Republican').count()
            party_unknown = Term.objects.filter(start_date__lte=query).filter(end_date__gte = query).filter(party__exact = 'Unknown').count()
        else:
            male = 'no data'
            female = 'no data'
    variables = RequestContext(request, {'form':form, 'query':query, 'male':male, 'female':female, 'white':white, 'black':black, 'asian':asian, 'hispanic':hispanic, 'race_unknown':race_unknown, 'democrat':democrat, 'republican':republican, 'party_unknown':party_unknown, 'show_results':show_results})
    return render_to_response('search.html', variables)




def unique_councilmembers(request):
    """this is what this function should return:
    select district, count(district) from council_councilperson join council_term on council_councilperson.id = council_term.councilperson_id group by district order by district; 
    """
    #create list of all districts (excluding at large)
    districts = range(1, 11)
    unique = {}
    for district in districts:
        unique[district] = Term.objects.filter(district__exact = str(district)).count()
    
    #is there a better way to do this below?        
    district1 = unique[1]
    district2 = unique[2]
    district3 = unique[3]
    district4 = unique[4]
    district5 = unique[5]
    district6 = unique[6]
    district7 = unique[7]
    district8 = unique[8]
    district9 = unique[9]
    district10 = unique[10]

    variables = RequestContext(request, {'district1':district1, 'district2':district2, 'district3':district3,'district4':district4, 'district5':district5, 'district6':district6, 'district7':district7, 'district8':district8, 'district9':district9, 'district10':district10 })
    print unique
    return render_to_response('unique.html', variables)


def index(request):
    return render(request, 'index.html')


def departing(request):
    retired, defeated, resigned, died, scandal, unknown = 0, 0, 0, 0, 0, 0
    retired = Term.objects.filter(departed__exact = 'retired').count()
    defeated = Term.objects.filter(departed__exact = 'defeated').count()
    resigned = Term.objects.filter(departed__exact = 'resigned').count()
    died = Term.objects.filter(departed__exact = 'died').count()
    scandal = Term.objects.filter(departed__exact = 'scandal').count()
    unknown = Term.objects.filter(departed__exact = 'unknown').count()
    variables = RequestContext(request, {'retired':retired, 'defeated':defeated, 'resigned':resigned, 'died':died, 'scandal':scandal, 'unknown':unknown })
    return render_to_response('departing.html', variables)




# #WHY IS THIS A LIST & NOT AN INT?
# counter = [0]
# def index(request):
#     """AJAX Sample.  Not used in this app. Renders a template and increments a constant each time the view is loaded.  Will reset if server restarts!"""
#     counter[0] = counter[0] + 1
#     if request.is_ajax():
#         template = 'index_ajax.html'
#     else:
#         template = 'index.html'
#     return render_to_response(template, {'counter':str(counter[0])}, context_instance=RequestContext(request))





    



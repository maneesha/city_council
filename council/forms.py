from django import forms
#import floppyforms as forms


GENDER_CHOICES = (('M', "Male"), ('F', 'Female'))

#YEAR_CHOICES = (('1952', '1952'), ('1962', '1962'), ('1972', '1972'), ('1982', '1982'), ('1992', '1992'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2012', '2012'))





YEAR_CHOICES = (('1952', '1952'), ('1953', '1953'), ('1954', '1954'), ('1955', '1955'), ('1956', '1956'), ('1957', '1957'), ('1958', '1958'), ('1959', '1959'), ('1960', '1960'), ('1961', '1961'), ('1962', '1962'), ('1963', '1963'), ('1964', '1964'), ('1965', '1965'), ('1966', '1966'), ('1967', '1967'), ('1968', '1968'), ('1969', '1969'), ('1970', '1970'), ('1971', '1971'), ('1972', '1972'), ('1973', '1973'), ('1974', '1974'), ('1975', '1975'), ('1976', '1976'), ('1977', '1977'), ('1978', '1978'), ('1979', '1979'), ('1980', '1980'), ('1981', '1981'), ('1982', '1982'), ('1983', '1983'), ('1984', '1984'), ('1985', '1985'), ('1986', '1986'), ('1987', '1987'), ('1988', '1988'), ('1989', '1989'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'))


#class SearchForm(forms.Form):
#    query = forms.ChoiceField(label = "enter a gender", widget = forms.RadioSelect, choices = CHOICES)

class SearchFormByYear(forms.Form):
    query = forms.ChoiceField(label = "choose a year", widget = forms.Select, choices = YEAR_CHOICES)

# class Slider(forms.RangeInput):
#     min = 5
#     max = 20
#     step = 5
#     template_name = 'slider.html'

#     class Media:
#         js = (
#             'js/jquery.min.js',
#             'js/jquery-ui.min.js',
#         )
#         css = {
#             'all': (
#                 'css/jquery-ui.css',
#             )
#         }


# class SlideForm(forms.Form):
#     num = forms.IntegerField(widget=Slider)

#     def clean_num(self):
#         num = self.cleaned_data['num']
#         if not 1900 <= num <= 2000:
#             raise forms.ValidationError("Enter a value between 1900 and 2000")
#         return num

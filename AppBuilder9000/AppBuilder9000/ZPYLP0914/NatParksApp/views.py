# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import NatParksForm, NewsletterUserSignUpForm
# from .models import natParksReview
# from .filters import NatparksFilter
# from django.core.paginator import Paginator
# from .models import NewsletterUser
#
#
# def national_parks_home(request):
#     return render(request, 'NatParksApp/NatParksApp_home.html')
#
#
# # top 10 US National Parks
# def top_10_national_parks(request):
#     return render(request, 'NatParksApp/US_Top_10_NP.html')
#
#
# # Park Reviews page
# def leave_national_park_reviews(request):
#     form = NatParksForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         return redirect('SelectParkReview')
#     else:
#         print(form.errors)
#         form = NatParksForm()
#
#     context = {'form': form}
#     return render(request, 'NatParksApp/National_Parks_Review.html', context)
#
#
# def news_letter_signup(request):
#     form = NewsletterUserSignUpForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('NatParks_Home')
#     else:
#         print(form.errors)
#         form = NewsletterUserSignUpForm
#
#     context = {
#         'form': form,
#     }
#     return render(request, 'NatParksApp/sign_up.html', context)
#
#
# def nat_parks_review_index(request):
#     context = {}
#
#     filtered_natparks = NatparksFilter(
#         request.GET,
#         queryset=natParksReview.objects.all()
#     )
#
#     context['filtered_natparks'] = filtered_natparks
#
#     paginated_filtered_natparks = Paginator(filtered_natparks.qs, 1)
#     page_number = request.GET.get('page')
#     parks_page_obj = paginated_filtered_natparks.get_page(page_number)
#
#     context['parks_page_obj'] = parks_page_obj
#
#     return render(request, 'NatParksApp/NatParks_review_index.html', context=context)
#
#
# def nat_parks_detail_view(request, pk):
#     park = natParksReview.objects.filter(pk=pk)
#     context = {
#         'park': park
#     }
#     return render(request, 'NatParksApp/NatParks_details_page.html', context)

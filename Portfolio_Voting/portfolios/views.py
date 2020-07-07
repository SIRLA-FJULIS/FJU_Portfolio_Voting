from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from portfolios.models import Work, UserVote

# Create your views here.
def index(request, college):
	work_list = Work.objects.filter(work_college=college).all()
	context = {
		'work_list': work_list,
		'college': college
	}
	return render(request, 'portfolios/index.html', context)

def article(request, college, portfolio_id):
	work = get_object_or_404(Work, pk=portfolio_id)
	print(portfolio_id)
	return render(request, 'portfolios/article.html', {'work': work})

def results(request, choiceText_id):
	work = get_object_or_404(Work, pk=choiceText_id)
	work_vote = UserVote.objects.all().filter(choice_workTitle=work.id)
	work_vote_counting = len(work_vote)

	context = {
		'work': work, 
		'work_vote_counting': work_vote_counting
	}
	return render(request, 'portfolios/article_results.html', context)


def vote(request, choiceText_id):
	work = get_object_or_404(Work, pk=choiceText_id)

	StudVoted = len(UserVote.objects.all().filter(studID=request.user.username))
	if (StudVoted == 1) == False:
		Stud_Voting = UserVote.objects.create(
			choice_workTitle=Work.objects.filter(pk=work.id).get(),
			studID=request.user.username
		)
		Stud_Voting.save()
		return HttpResponseRedirect(reverse('portfolios:results', args=(work.id,) ))
	else:
		print('你已投過票囉！')
		return HttpResponseRedirect(reverse('portfolios:results', args=(work.id,) ))

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

from portfolios.models import Work, UserVote

# Create your views here.
def index(request, college):
	work_list = Work.objects.filter(work_college=college).all()
	context = {
		'work_list': work_list,
		'college': college
	}
	return render(request, 'portfolios/index.html', context)

def article(request, portfolio_id):
	work = get_object_or_404(Work, pk=portfolio_id)
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


def vote(request, portfolio_id):
	work = get_object_or_404(Work, pk=portfolio_id)

	StudVoted = len(UserVote.objects.filter(studID=request.user.username).all())
	if StudVoted == 0:
		Stud_Voting = UserVote.objects.create(
			choice_workTitle=Work.objects.filter(pk=work.id).get(),
			studID=request.user.username
		)
		Stud_Voting.save()
		return HttpResponseRedirect(request.GET.get('next'))
	else:
		messages.add_message(request, messages.WARNING, '您已經投過票了喔!')
		return HttpResponseRedirect(request.GET.get('next'))

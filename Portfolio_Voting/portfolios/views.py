from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponseRedirect
from django.urls import reverse
from portfolios.models import Work, User_Vote

# Create your views here.
def index(request):
	### TESTING: 傳遞 session ###
	print("app: PORTFOLIOS ->", request.session['USER_INPUT_STUD_ID'])
	STUD_ID = request.session['USER_INPUT_STUD_ID']
	
	work_list = Work.objects.order_by('work_management')
	context = {
		'work_list': work_list,
		'STUD_ID': STUD_ID,
	}
	return render(request, 'portfolios/index.html', context)

def detail(request, choiceText_id):
	work = get_object_or_404(Work, pk=choiceText_id)
	print('送出後，就無法修改投票囉！')
	print("app: PORTFOLIOS ->", work, '===== 作品ID：', choiceText_id)
	return render(request, 'portfolios/article.html', {'work': work})


def results(request, choiceText_id):
	work = get_object_or_404(Work, pk=choiceText_id)
	work_vote = User_Vote.objects.all().filter(choiceText_workTitle=work.id)
	work_vote_counting = len(work_vote)
	return render(request, 'portfolios/article_results.html', {'work': work, 'work_vote_counting': work_vote_counting})


def vote(request, choiceText_id):
	print("app: PORTFOLIOS vote ->", request.session['USER_INPUT_STUD_ID'])
	STUD_ID = request.session['USER_INPUT_STUD_ID']
	work = get_object_or_404(Work, pk=choiceText_id)

	student_vote = len(User_Vote.objects.all().filter(studID=STUD_ID))
	if (student_vote == 1) == False:
		studentVoting = User_Vote.objects.create(
			choiceText_workTitle=Work.objects.filter(pk=work.id).get(),
			studID=STUD_ID, 
			votes=1,
		)
		studentVoting.save()
		a = User_Vote.objects.order_by('choiceText_workTitle', 'studID')
		print('--- 票數(後)：', a)
		return HttpResponseRedirect(reverse('portfolios:results', args=(work.id,) ))
	else:
		print('你已投過票囉！')
		return HttpResponseRedirect(reverse('portfolios:results', args=(work.id,) ))

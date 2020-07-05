from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from polls.models import Question

# Create your views here.
def index(request):
	'''
	### TESTING: 傳遞 session ###
	print("app: POLLS ->", request.session['USER_INPUT_DEPARTMENT'])
	'''
	latest_question_list = Question.objects.order_by('pub_date')[:5]
	context = {
		'latest_question_list': latest_question_list,
	}
	return render(request, 'polls/index.html', context)

def detail(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	messages.success(request, '注意：\\n\\n送出後，就無法修改投票囉！')
	return render(request, 'polls/detail.html', {'question': question})
	#https://blog.csdn.net/u012561176/java/article/details/84552532

def results(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	'''
	# 缺少提示視窗，讓使用者輸入 studID fullName department ，
	# 並寫入 choice_text	(所投票的作品名稱)
	'''
	return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)

	## 存到 User_Vote 資料表 ## ------------------------------

	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		return render(request, 'polls/detail.html', {
				'question': question,
				'error_message': "You didn't select a choice.",
			})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
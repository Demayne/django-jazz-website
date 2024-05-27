from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/user_auth/')
def index(request):
    """
    View to display the latest 5 poll questions.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered index.html template with the latest questions.
    """
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, "polls/index.html", context)

@login_required(login_url='/user_auth/')
def detail(request, question_id):
    """
    View to display the details of a specific poll question.

    Args:
        request: The HTTP request object.
        question_id (int): The id of the question to display.

    Returns:
        HttpResponse: The rendered detail.html template with the question details.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

@login_required(login_url='/user_auth/')
def results(request, question_id):
    """
    View to display the results of a specific poll question.

    Args:
        request: The HTTP request object.
        question_id (int): The id of the question to display the results for.

    Returns:
        HttpResponse: The rendered results.html template with the question results.
    """
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

@login_required(login_url='/user_auth/')
def vote(request, question_id):
    """
    View to handle voting on a specific poll question.

    Args:
        request: The HTTP request object.
        question_id (int): The id of the question to vote on.

    Returns:
        HttpResponseRedirect: Redirects to the results page after voting.
        HttpResponse: Redisplays the voting form with an error message if no choice is selected.
    """
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with error message
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Tally the vote
        selected_choice.votes += 1
        selected_choice.save()
        # Redirect to results page after voting
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

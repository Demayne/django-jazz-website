from django.db import models

class Question(models.Model):
    """
    Model representing a poll question.

    Attributes:
        question_text (str): The text of the question.
        pub_date (datetime): The date and time the question was published.
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        String representation of the Question model, returns the question text.
        """
        return self.question_text

class Choice(models.Model):
    """
    Model representing a choice for a poll question.

    Attributes:
        question (ForeignKey): The question the choice belongs to.
        choice_text (str): The text of the choice.
        votes (int): The number of votes the choice has received, defaults to 0.
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        String representation of the Choice model, returns the choice text.
        """
        return self.choice_text

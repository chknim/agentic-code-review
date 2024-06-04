from textwrap import dedent
from crewai import Task

class CodeReviewTasks():
  def code_task(self, agent, code):
    return Task(
      description=dedent(
        f"""\
        You will create a software using javascript, these are the instructions:

        Instructions
        ------------
        {code}

        Your final answer must be the full javascript code, only the javascript code and nothing else.
        """
      ),
      agent=agent,
      expected_output='A javascript function.'
    )

  def review_task(self, agent, code):
    return Task(
      description=dedent(
        f"""\
        You are helping create a software using javascript.  These are the instructions:

        Instructions
        ------
        {code}

        Using the code you got, you will check for logic errors, syntax errors, missing imports,
        variable declarations, mismatched brackets, and security vulnerabilities.

        You will provide suggestions and update the code such that any flaws is corrected and any improvement is applied.

        Your final answer must be the full javascript code, only the javascript code and nothing else.
        """
      ),
      agent=agent,
      expected_output='A javascript function.'
    )
  

"""CrewAI — Python quickstart (a small two-step crew).

Setup:
    pip install -r requirements.txt
    export OPENAI_API_KEY="sk-..."     # CrewAI uses OpenAI by default; configurable

Run:
    python quickstart.py

Docs: https://github.com/crewAIInc/crewAI
"""

from crewai import Agent, Crew, Process, Task

researcher = Agent(
    role="Researcher",
    goal="Find the key facts about {topic}",
    backstory="You are a meticulous researcher who cites concrete facts.",
    verbose=True,
)

writer = Agent(
    role="Writer",
    goal="Write a tight 3-sentence summary about {topic}",
    backstory="You turn research notes into crisp, readable prose.",
    verbose=True,
)

research_task = Task(
    description="Gather the 3 most important facts about {topic}.",
    expected_output="A bullet list of 3 well-sourced facts.",
    agent=researcher,
)

write_task = Task(
    description="Using the research, write a 3-sentence summary of {topic}.",
    expected_output="A 3-sentence summary.",
    agent=writer,
    context=[research_task],
)

crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)


def main() -> None:
    result = crew.kickoff(inputs={"topic": "the Model Context Protocol"})
    print(result)


if __name__ == "__main__":
    main()

# crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import FileWriterTool

import os

from crewai import LLM


llm = LLM(
    model="nvidia_nim/meta/llama-3.3-70b-instruct",
    api_key=os.environ["NVIDIA_API_KEY_NEMOTRON"],   # your NVIDIA build.nvidia.com API key
    base_url="https://integrate.api.nvidia.com/v1",  # optional, this is the default anyway
)


@CrewBase
class EngineeringTeam():
    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(config=self.agents_config['engineering_lead'], verbose=True, llm=llm)

    @agent
    def backend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["backend_engineer"],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=800,
            max_retries=5,
            tools=[FileWriterTool()],
            llm=llm
        )

    @agent
    def frontend_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["frontend_engineer"],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=800,
            max_retries=5,
            tools=[FileWriterTool()],
            llm=llm
        )

    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config["test_engineer"],
            verbose=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_execution_time=900,
            max_retries=5,
            tools=[FileWriterTool()],
            llm=llm
        )

    @task
    def design_task(self) -> Task:
        return Task(config=self.tasks_config["design_task"])

    @task
    def code_task(self) -> Task:
        return Task(config=self.tasks_config["code_task"])

    @task
    def frontend_task(self) -> Task:
        return Task(config=self.tasks_config["frontend_task"])

    @task
    def test_task(self) -> Task:
        return Task(config=self.tasks_config["test_task"])

    @crew
    def crew(self) -> Crew:
        return Crew(agents=self.agents, tasks=self.tasks, process=Process.sequential, verbose=True)
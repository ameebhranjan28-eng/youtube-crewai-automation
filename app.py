from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.5-flash",
)
import os
from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(
    model="gemini/gemini-2.5-flash",
)

# 1. Voiceover Scriptwriter & Director Agent
scriptwriter = Agent(
    role="Voiceover Scriptwriter & Director",
    goal="Write engaging, high-retention voiceover scripts tailored for YouTube videos.",
    backstory="You are an expert YouTube scriptwriter and voiceover director. You know how to hook viewers in the first 5 seconds, maintain pacing, and deliver clear, compelling storytelling with voice direction notes.",
    llm=llm,
    verbose=True
)

# 2. Visual & B-roll Director Agent
visual_director = Agent(
    role="Visual & B-roll Director",
    goal="Design complete visual shot lists, B-roll suggestions, text overlays, and graphic cues synchronized with the script.",
    backstory="You are a seasoned video editor and creative director specializing in YouTube visuals. You bring scripts to life by mapping out precise visual cues, stock footage ideas, graphics, and screen transitions.",
    llm=llm,
    verbose=True
)

# 3. YouTube Publishing & SEO Specialist Agent
seo_specialist = Agent(
    role="YouTube Publishing & SEO Specialist",
    goal="Generate high-CTR titles, SEO-optimized descriptions, tags, and thumbnail concepts for maximum reach.",
    backstory="You are a top-tier YouTube SEO strategist and growth marketer. You understand YouTube search algorithms, search intent, CTR optimization, thumbnail psychology, and metadata structuring.",
    llm=llm,
    verbose=True
)

# Tasks Definition
task_script = Task(
    description="Write a detailed voiceover script for a video titled '{topic}'. Include opening hooks, structured main body, and a clear call to action.",
    expected_output="A complete video script with voiceover audio cues and pacing notes.",
    agent=scriptwriter
)

task_visuals = Task(
    description="Based on the generated script, create a timestamped visual shot list including B-roll concepts, on-screen text overlays, and animation instructions.",
    expected_output="A structured visual shot list aligned line-by-line with the script.",
    agent=visual_director
)

task_seo = Task(
    description="Create 5 catchy video titles, an SEO-friendly description with timestamps/hashtags, 15 relevant tags, and 3 thumbnail design concepts for the video topic '{topic}'.",
    expected_output="Complete YouTube publishing package including titles, description, tags, and thumbnail concepts.",
    agent=seo_specialist
)

# Crew Pipeline
youtube_crew = Crew(
    agents=[scriptwriter, visual_director, seo_specialist],
    tasks=[task_script, task_visuals, task_seo],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    result = youtube_crew.kickoff(inputs={"topic": "How AI is Changing Video Creation"})
    print("\n\n########################")
    print("## CREW EXECUTION RESULT ##")
    print("########################\n")
    print(result)

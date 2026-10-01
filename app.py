import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process, LLM

load_dotenv()

# Define LLM using CrewAI's native LLM wrapper or environment variables
llm = LLM(model="gpt-4o")

# 1. Voiceover Agent
voiceover_agent = Agent(
    role="Voiceover Scriptwriter & Director",
    goal="Write engaging, natural-sounding voiceover scripts with clear pacing, tone cues, and timing for YouTube videos.",
    backstory="You are a seasoned voiceover artist and audio producer with years of experience crafting compelling narration for top YouTube channels.",
    verbose=True,
    llm=llm
)

# 2. Visual Director Agent
visual_director_agent = Agent(
    role="Visual & B-Roll Director",
    goal="Create detailed visual storyboards, B-roll suggestions, text overlays, and graphic directions matching the voiceover script.",
    backstory="You are a creative director who specializes in visual storytelling, motion graphics, and engaging thumbnail/B-roll concepts.",
    verbose=True,
    llm=llm
)

# 3. Publisher Agent
publisher_agent = Agent(
    role="YouTube Publishing & Metadata Specialist",
    goal="Generate SEO-optimized titles, descriptions, tags, visual prompts for thumbnails, and publishing schedules.",
    backstory="You are a YouTube SEO guru who knows how to maximize click-through rate (CTR), retention, and algorithmic reach.",
    verbose=True,
    llm=llm
)

# Tasks
voiceover_task = Task(
    description="Write a complete, engaging voiceover script for a video about: {topic}.",
    expected_output="A structured voiceover script with timing markers, tone notes, and narration text.",
    agent=voiceover_agent
)

visual_task = Task(
    description="Based on the voiceover script, create a scene-by-scene visual storyboard with B-roll cues and text overlays.",
    expected_output="A scene-by-scene visual breakdown aligned with the voiceover script.",
    agent=visual_director_agent
)

publisher_task = Task(
    description="Create optimized video metadata (3 title options, SEO description, tags, and thumbnail visual concept) for the video about: {topic}.",
    expected_output="A complete YouTube metadata package including titles, description, tags, and thumbnail concept.",
    agent=publisher_agent
)

# Production Crew
youtube_production_crew = Crew(
    agents=[voiceover_agent, visual_director_agent, publisher_agent],
    tasks=[voiceover_task, visual_task, publisher_task],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    topic = "The Future of AI Agents in 2026"
    print(f"Starting YouTube CrewAI Production for topic: '{topic}'...\n")
    result = youtube_production_crew.kickoff(inputs={"topic": topic})
    print("\n--- Production Complete ---")
    print(result)

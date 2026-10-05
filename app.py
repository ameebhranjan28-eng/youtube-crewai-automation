import os
from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
    api_key=os.environ.get("GEMINI_API_KEY")
)

# 1. Voiceover Scriptwriter & Director Agent
scriptwriter = Agent(
    role="Voiceover Scriptwriter & Director",
    goal="Write engaging, retention-focused YouTube scripts with clear narration and visual cues.",
    backstory="You are a seasoned YouTube scriptwriter and creative director. You know how to hook viewers in the first 5 seconds and structure videos for maximum watch time.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 2. Thumbnail & Visual Strategist Agent
visual_strategist = Agent(
    role="Thumbnail & Visual Strategist",
    goal="Design high-CTR thumbnail concepts and visually compelling scene ideas that match the script.",
    backstory="You are a digital artist and YouTube packaging expert. You analyze trending visual styles, color contrast, and psychological triggers to make videos unclickable-to-ignore.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. SEO & Metadata Optimizer Agent
seo_optimizer = Agent(
    role="YouTube SEO & Metadata Optimizer",
    goal="Generate high-ranking titles, description, tags, and chapter timestamps.",
    backstory="You are an algorithm whisperer who understands YouTube search, recommendation systems, and metadata optimization.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Task 1: Scriptwriting
task_script = Task(
    description="Write a complete 3-minute YouTube video script on 'How AI is Changing Video Creation'. Include section timestamps, voiceover lines, and B-roll/visual suggestions.",
    expected_output="A full video script with timestamps, narration text, and visual cues.",
    agent=scriptwriter
)

# Task 2: Thumbnail & Visuals
task_visuals = Task(
    description="Based on the script, create 3 thumbnail concept descriptions (text overlays, focal points, color scheme) and 5 key visual scene descriptions.",
    expected_output="3 thumbnail ideas and 5 scene visual concepts.",
    agent=visual_strategist
)

# Task 3: SEO Optimization
task_seo = Task(
    description="Create 5 catchy video titles, a 200-word SEO-friendly description, 15 relevant tags, and video chapter timestamps based on the script.",
    expected_output="Titles, description, tags, and chapter timestamps.",
    agent=seo_optimizer
)

# Form the Crew
youtube_crew = Crew(
    agents=[scriptwriter, visual_strategist, seo_optimizer],
    tasks=[task_script, task_visuals, task_seo],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    print("--- Starting YouTube Automation Crew ---")
    result = youtube_crew.kickoff()
    print("\n--- Final Output ---")
    print(result)

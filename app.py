from crewai import LLM

llm = LLM(
    model="gemini/gemini-2.5-flash",
)
import os
from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(import os
from crewai import Agent, Task, Crew, Process, LLM
import os
from crewai import Agent, Task, Crew, Process, LLM

llm = LLM(
    model="gemini/gemini-2.0-flash",
)

# 1. Voiceover Scriptwriter & Director Agent
scriptwriter = Agent(
    role="Voiceover Scriptwriter & Director",
    goal="Write engaging, retention-focused YouTube scripts with clear narration and visual cues.",
    backstory="You are a seasoned YouTube scriptwriter and creative director. You know how to hook viewers in the first 5 seconds, maintain pacing, and structure videos for maximum watch time.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 2. Thumbnail & Visual Strategist Agent
visual_strategist = Agent(
    role="Thumbnail & Visual Strategist",
    goal="Design high-CTR thumbnail concepts and visually compelling scene ideas that match the script.",
    backstory="You are a digital artist and YouTube packaging expert. You analyze trending visual styles, color contrast, and emotional triggers to create thumbnail concepts that get clicks.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. YouTube SEO & Metadata Specialist Agent
seo_specialist = Agent(
    role="YouTube SEO & Metadata Specialist",
    goal="Optimize video titles, descriptions, and tags for YouTube search and recommendation algorithms.",
    backstory="You are a YouTube algorithm strategist. You specialize in keyword research, crafting click-worthy yet non-clickbait titles, and writing SEO-optimized descriptions.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define Tasks

task1 = Task(
    description="Write a complete YouTube script on the topic: 'The Future of AI Agents in 2025'. Include hooks, section transitions, and visual/audio cues.",
    expected_output="A full video script with timestamped sections, visual notes, and voiceover text.",
    agent=scriptwriter
)

task2 = Task(
    description="Based on the script, create 3 thumbnail concepts (with text overlays and visual descriptions) and scene-by-scene visual suggestions.",
    expected_output="3 distinct thumbnail ideas with title pairings and visual composition details.",
    agent=visual_strategist
)

task3 = Task(
    description="Create 5 optimized video titles, an SEO-friendly description with timestamps, and 15 relevant tags for the video.",
    expected_output="5 high-CTR titles, a description draft with chapters, and a list of target tags.",
    agent=seo_specialist
)

# Form the Crew
youtube_crew = Crew(
    agents=[scriptwriter, visual_strategist, seo_specialist],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    result = youtube_crew.kickoff()
    print("\n\n########################")
    print("## YOUTUBE CREW RESULTS ##")
    print("########################\n")
    print(result)

llm = LLM(
    model="gemini/gemini-2.0-flash",
)

# 1. Voiceover Scriptwriter & Director Agent
scriptwriter = Agent(
    role="Voiceover Scriptwriter & Director",
    goal="Write engaging, retention-focused YouTube scripts with clear narration and visual cues.",
    backstory="You are a seasoned YouTube scriptwriter and creative director. You know how to hook viewers in the first 5 seconds, maintain pacing, and structure videos for maximum watch time.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 2. Thumbnail & Visual Strategist Agent
visual_strategist = Agent(
    role="Thumbnail & Visual Strategist",
    goal="Design high-CTR thumbnail concepts and visually compelling scene ideas that match the script.",
    backstory="You are a digital artist and YouTube packaging expert. You analyze trending visual styles, color contrast, and emotional triggers to create thumbnail concepts that get clicks.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# 3. YouTube SEO & Metadata Specialist Agent
seo_specialist = Agent(
    role="YouTube SEO & Metadata Specialist",
    goal="Optimize video titles, descriptions, and tags for YouTube search and recommendation algorithms.",
    backstory="You are a YouTube algorithm strategist. You specialize in keyword research, crafting click-worthy yet non-clickbait titles, and writing SEO-optimized descriptions.",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Define Tasks

task1 = Task(
    description="Write a complete YouTube script on the topic: 'The Future of AI Agents in 2025'. Include hooks, section transitions, and visual/audio cues.",
    expected_output="A full video script with timestamped sections, visual notes, and voiceover text.",
    agent=scriptwriter
)

task2 = Task(
    description="Based on the script, create 3 thumbnail concepts (with text overlays and visual descriptions) and scene-by-scene visual suggestions.",
    expected_output="3 distinct thumbnail ideas with title pairings and visual composition details.",
    agent=visual_strategist
)

task3 = Task(
    description="Create 5 optimized video titles, an SEO-friendly description with timestamps, and 15 relevant tags for the video.",
    expected_output="5 high-CTR titles, a description draft with chapters, and a list of target tags.",
    agent=seo_specialist
)

# Form the Crew
youtube_crew = Crew(
    agents=[scriptwriter, visual_strategist, seo_specialist],
    tasks=[task1, task2, task3],
    process=Process.sequential,
    verbose=True
)

if __name__ == "__main__":
    result = youtube_crew.kickoff()
    print("\n\n########################")
    print("## YOUTUBE CREW RESULTS ##")
    print("########################\n")
    print(result)

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

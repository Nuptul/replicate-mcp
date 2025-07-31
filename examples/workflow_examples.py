#!/usr/bin/env python3
"""
Workflow examples for Replicate MCP
By Daniel Fleuren
"""

# Professional workflows that combine multiple AI models
# Type these commands in Claude Code to execute complete workflows

workflow_examples = {
    "logo_to_brand_video": {
        "description": "Transform a simple logo into a complete brand video package",
        "command": "Execute logo to brand video workflow for 'NexGen AI'",
        "steps": [
            "1. Generate or enhance logo in SVG format",
            "2. Create multiple logo variations",
            "3. Extract brand colors",
            "4. Animate logo with professional transitions",
            "5. Generate brand scene images",
            "6. Create video sequences",
            "7. Add synchronized music",
            "8. Export in multiple formats"
        ],
        "output": "Complete brand video package with logo animations, transitions, and music"
    },
    
    "character_animation": {
        "description": "Create consistent animated characters for games or videos",
        "command": "Execute character animation workflow for a friendly robot mascot",
        "steps": [
            "1. Design character with consistent features",
            "2. Generate character turnaround views",
            "3. Create 3D model from images",
            "4. Animate character movements",
            "5. Add voice and lip-sync",
            "6. Export animation sequences"
        ],
        "output": "Fully animated character with voice and consistent appearance"
    },
    
    "product_showcase": {
        "description": "Professional product demonstration video",
        "command": "Execute product showcase workflow for a smartwatch",
        "steps": [
            "1. Generate multiple product angles",
            "2. Remove backgrounds",
            "3. Create 3D model from photos",
            "4. Animate 360° rotation",
            "5. Add feature callouts",
            "6. Generate lifestyle scenes",
            "7. Add voiceover narration",
            "8. Create multiple versions"
        ],
        "output": "Professional product video with 3D animations and voiceover"
    },
    
    "social_media_content": {
        "description": "Complete social media content package",
        "command": "Execute social media content workflow for tech product launch",
        "steps": [
            "1. Generate hero images",
            "2. Create short video clips",
            "3. Add animated captions",
            "4. Reframe for all platforms",
            "5. Generate Instagram stories",
            "6. Create TikTok videos",
            "7. Make Twitter/X graphics",
            "8. Package all assets"
        ],
        "output": "Complete set of optimized content for all social platforms"
    }
}

# Custom workflow examples
custom_workflows = [
    {
        "name": "AI Influencer Creation",
        "description": "Create a consistent AI influencer with multiple posts",
        "steps": [
            "Generate base character with FLUX Kontext Pro",
            "Create multiple poses maintaining consistency",
            "Generate different outfits and scenes",
            "Add captions and branding",
            "Create introduction video",
            "Generate voice for the character"
        ]
    },
    {
        "name": "Music Video Production",
        "description": "Create a complete music video from lyrics",
        "steps": [
            "Generate music from lyrics description",
            "Create visual scenes matching lyrics",
            "Animate transitions between scenes",
            "Sync visuals to music beats",
            "Add visual effects",
            "Export in multiple resolutions"
        ]
    },
    {
        "name": "Educational Content Package",
        "description": "Create educational materials with AI",
        "steps": [
            "Generate infographic illustrations",
            "Create explainer animations",
            "Add voiceover narration",
            "Generate quiz graphics",
            "Create summary video",
            "Package for LMS platforms"
        ]
    }
]

# Step-by-step workflow tutorial
tutorial = """
# How to Execute Workflows in Claude Code

1. **Basic Workflow Execution**
   Type: "Execute [workflow_name] workflow for [your project]"
   Example: "Execute logo to brand video workflow for 'CoolStartup'"

2. **Custom Parameters**
   Add specific requirements:
   "Execute product showcase workflow for wireless headphones with minimalist style"

3. **Workflow Chaining**
   Combine multiple workflows:
   "First execute logo generation, then create brand video workflow"

4. **Budget-Conscious Workflows**
   "Execute social media workflow using fast/budget models"

5. **Quality-First Workflows**
   "Execute product showcase using highest quality models"
"""

if __name__ == "__main__":
    print("\n🔄 Replicate MCP Workflow Examples\n")
    
    for workflow_id, workflow in workflow_examples.items():
        print(f"\n{'='*60}")
        print(f"📋 {workflow_id.replace('_', ' ').title()}")
        print(f"{'='*60}")
        print(f"Description: {workflow['description']}")
        print(f"\nCommand: {workflow['command']}")
        print("\nSteps:")
        for step in workflow['steps']:
            print(f"  {step}")
        print(f"\nOutput: {workflow['output']}")
    
    print("\n\n🎨 Custom Workflow Ideas:\n")
    for custom in custom_workflows:
        print(f"\n{custom['name']}:")
        print(f"  {custom['description']}")
        print("  Steps:")
        for step in custom['steps']:
            print(f"    - {step}")
    
    print(tutorial)

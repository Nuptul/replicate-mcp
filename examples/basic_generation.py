#!/usr/bin/env python3
"""
Basic generation examples for Replicate MCP
By Daniel Fleuren
"""

# These examples show how to use Replicate MCP in Claude Code
# Simply type these commands in Claude Code after installation

examples = {
    "image_generation": [
        "Generate a professional logo for a tech startup called NexGen AI",
        "Create a photorealistic image of a futuristic city at sunset",
        "Make an illustration of a cute robot helping humans with daily tasks",
        "Generate a minimalist poster design with geometric shapes",
        "Create product photography of a luxury watch on black background"
    ],
    
    "video_generation": [
        "Create a 5-second video of a rocket launching into space",
        "Generate a smooth animation of this logo with zoom effect",
        "Make a product showcase video rotating 360 degrees",
        "Create a nature timelapse video of flowers blooming",
        "Generate an animated character waving hello"
    ],
    
    "audio_generation": [
        "Create a 30-second upbeat electronic music track",
        "Generate a voiceover saying 'Welcome to the future of AI'",
        "Make relaxing ambient sounds for meditation",
        "Create sound effects for a sci-fi game menu",
        "Generate a podcast intro jingle"
    ],
    
    "3d_generation": [
        "Create a 3D model of a modern office chair",
        "Generate a 3D character of a friendly robot",
        "Make a 3D version of this product image",
        "Create a low-poly tree for a game",
        "Generate a 3D architectural model of a house"
    ]
}

# Advanced examples with specific models
advanced_examples = {
    "high_quality_image": "Generate using FLUX Pro: A stunning landscape photograph of mountains at golden hour, ultra high resolution, professional photography",
    
    "fast_draft": "Quick image with FLUX Schnell: Rough concept sketch of a mobile app interface",
    
    "character_consistency": "Create with MiniMax Video: Animated character maintaining consistent appearance across multiple scenes",
    
    "background_removal": "Remove background from this product photo and make it transparent",
    
    "image_upscaling": "Upscale this image to 4K resolution with enhanced details",
    
    "workflow_execution": "Execute logo to brand video workflow for company 'TechCorp' with modern, professional style"
}

if __name__ == "__main__":
    print("\n🎨 Replicate MCP Examples\n")
    print("Copy and paste these commands into Claude Code:\n")
    
    for category, prompts in examples.items():
        print(f"\n{category.replace('_', ' ').title()}:")
        for i, prompt in enumerate(prompts, 1):
            print(f"{i}. {prompt}")
    
    print("\n✨ Advanced Examples:")
    for key, prompt in advanced_examples.items():
        print(f"\n{key.replace('_', ' ').title()}:")
        print(f"   {prompt}")

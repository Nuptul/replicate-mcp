"""Complete catalog of Replicate models with working versions"""

# Essential model catalog with working versions
COMPLETE_MODEL_CATALOG = {
    # Image Generation
    "sdxl": {
        "id": "stability-ai/sdxl",
        "name": "Stable Diffusion XL",
        "version": "7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc"
    },
    "flux-schnell": {
        "id": "black-forest-labs/flux-schnell",
        "name": "FLUX Schnell"
    },
    
    # Image Enhancement
    "clarity-upscaler": {
        "id": "philz1337x/clarity-upscaler",
        "name": "Clarity Upscaler",
        "version": "dfad41707589d68ecdccd1dfa600d55a208f9310748e44bfe35b4a6291453d5e"
    },
    "codeformer": {
        "id": "sczhou/codeformer",
        "name": "CodeFormer",
        "version": "7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56"
    },
    
    # Audio Generation
    "bark": {
        "id": "suno-ai/bark",
        "name": "Bark",
        "version": "b76242b40d67c76ab6742e987628a2a9ac019e11d56ab96c4e91ce03b79b2787"
    },
    "xtts-v2": {
        "id": "lucataco/xtts-v2",
        "name": "XTTS-v2",
        "version": "684bc3855b37866c0c65add2ff39c78f3dea3f4ff103a436465326e0f438d55e"
    },
    
    # 3D Generation
    "wonder3d": {
        "id": "camenduru/wonder3d",
        "name": "Wonder3D",
        "version": "b5ad7e1b80c1a5a7e0c0a483f5a45f13797c7c9b6bc1c0fb18eab25cf088f4d6"
    },
    
    # Background Removal
    "rembg": {
        "id": "cjwbw/rembg",
        "name": "Rembg",
        "version": "fb8af171cfa1616ddcf1242c093f9c46bcada5ad4cf6f2fbe8b81b330ec5c003"
    }
}

# Workflow templates
WORKFLOW_TEMPLATES = {
    "logo_to_brand_video": {
        "name": "Logo to Brand Video",
        "steps": ["clarity-upscaler", "rembg", "sdxl"]
    },
    "character_animation": {
        "name": "Character Animation",
        "steps": ["sdxl", "codeformer", "xtts-v2"]
    }
}
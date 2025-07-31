"""Complete catalog of ALL Replicate models with professional workflows"""

from typing import Dict, List, Any, Optional
from enum import Enum

class ModelCapability(str, Enum):
    """Model capabilities"""
    # Image
    TEXT_TO_IMAGE = "text2img"
    IMAGE_TO_IMAGE = "img2img"
    INPAINTING = "inpainting"
    UPSCALING = "upscaling"
    BACKGROUND_REMOVAL = "bg_removal"
    FACE_RESTORATION = "face_restore"
    IMAGE_ENHANCEMENT = "enhance"
    STYLE_TRANSFER = "style"
    COLORIZATION = "colorize"
    
    # Video
    TEXT_TO_VIDEO = "text2video"
    IMAGE_TO_VIDEO = "img2video"
    VIDEO_EDITING = "video_edit"
    VIDEO_ENHANCEMENT = "video_enhance"
    VIDEO_EXTENSION = "video_extend"
    VIDEO_REFRAME = "video_reframe"
    
    # Audio
    TEXT_TO_SPEECH = "tts"
    MUSIC_GENERATION = "music_gen"
    SOUND_EFFECTS = "sfx"
    VOICE_CLONING = "voice_clone"
    AUDIO_ENHANCEMENT = "audio_enhance"
    VIDEO_TO_AUDIO = "video2audio"
    
    # 3D
    TEXT_TO_3D = "text23d"
    IMAGE_TO_3D = "img23d"
    MESH_GENERATION = "mesh_gen"
    TEXTURE_GENERATION = "texture_gen"
    
    # Special
    LOGO_GENERATION = "logo"
    CHARACTER_CONSISTENCY = "character"
    PROMPT_OPTIMIZATION = "prompt_opt"
    CAPTION_GENERATION = "caption"


# Complete model catalog with ALL Replicate models
COMPLETE_MODEL_CATALOG = {
    "image_generation": {
        "flux-pro": {
            "id": "black-forest-labs/flux-1.1-pro",
            "name": "FLUX 1.1 Pro",
            "description": "State-of-the-art image generation, ultra & raw modes, 4MP",
            "cost_per_run": 0.055,
            "capabilities": ["text2img", "img2img", "ultra_quality"],
            "max_resolution": 4096,
            "special_features": ["raw_mode", "ultra_mode", "professional_quality"]
        },
        "flux-schnell": {
            "id": "black-forest-labs/flux-schnell",
            "name": "FLUX Schnell",
            "description": "Fast high-quality image generation",
            "cost_per_run": 0.003,
            "capabilities": ["text2img"],
            "max_resolution": 4096
        },
        "flux-dev": {
            "id": "black-forest-labs/flux-dev",
            "name": "FLUX Dev",
            "description": "Development version with experimental features",
            "cost_per_run": 0.025,
            "capabilities": ["text2img", "img2img"],
            "max_resolution": 4096
        },
        "flux-kontext-pro": {
            "id": "black-forest-labs/flux-kontext-pro",
            "name": "FLUX Kontext Pro",
            "description": "Character consistency and context preservation",
            "cost_per_run": 0.04,
            "capabilities": ["text2img", "character", "context"],
            "special_features": ["character_consistency", "scene_consistency"]
        },
        "sdxl": {
            "id": "stability-ai/sdxl",
            "name": "Stable Diffusion XL",
            "description": "High-quality 1024x1024 images with refiner",
            "cost_per_run": 0.00325,
            "capabilities": ["text2img", "img2img", "inpainting", "refiner"],
            "max_resolution": 1024,
            "version": "7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc"
        },
        "sdxl-lightning": {
            "id": "bytedance/sdxl-lightning-4step",
            "name": "SDXL Lightning",
            "description": "4-step fast SDXL generation",
            "cost_per_run": 0.001,
            "capabilities": ["text2img"],
            "max_resolution": 1024,
            "version": "6f7a773af6fc3e8de9d5a3c00be77c17308914bf67772726aff83496ba1e3bbe"
        },
        "recraft-svg": {
            "id": "recraft-ai/recraft-v3-svg",
            "name": "Recraft V3 SVG",
            "description": "Generate SVG logos, icons, and vector graphics",
            "cost_per_run": 0.01,
            "capabilities": ["text2svg", "logo", "vector"],
            "special_features": ["svg_output", "scalable_graphics", "brand_assets"]
        }
    },
    
    "image_manipulation": {
        "clarity-upscaler": {
            "id": "philz1337x/clarity-upscaler",
            "name": "Clarity Upscaler",
            "description": "High-quality image upscaling up to 10x",
            "cost_per_run": 0.005,
            "capabilities": ["upscaling"],
            "max_scale": 10,
            "version": "dfad41707589d68ecdccd1dfa600d55a208f9310748e44bfe35b4a6291453d5e"
        },
        "real-esrgan": {
            "id": "nightmareai/real-esrgan",
            "name": "Real-ESRGAN",
            "description": "Fast upscaling with face enhancement",
            "cost_per_run": 0.002,
            "capabilities": ["upscaling", "face_restore"],
            "features": ["face_enhance", "anime_mode"],
            "version": "f121d640bd286e1fdc67f9799164c1d5be36ff74576ee11c803ae5b665dd46aa"
        },
        "swinir": {
            "id": "jingyunliang/swinir",
            "name": "SwinIR",
            "description": "Excellent for small/low quality images",
            "cost_per_run": 0.001,
            "capabilities": ["upscaling", "denoising"],
            "version": "660d922d33153019e8c263a3bba265de882e7f4f70396546b6c9c8f9d47a021a"
        },
        "remove-bg": {
            "id": "cjwbw/rembg",
            "name": "Background Remover (RemBG)",
            "description": "Fast and accurate background removal",
            "cost_per_run": 0.0005,
            "capabilities": ["bg_removal"],
            "version": "fb8af171cfa1616ddcf1242c093f9c46bcada5ad4cf6f2fbe8b81b330ec5c003"
        },
        "robust-video-matting": {
            "id": "arielreplicate/robust_video_matting",
            "name": "Robust Video Matting",
            "description": "Remove background from videos",
            "cost_per_run": 0.01,
            "capabilities": ["bg_removal", "video"]
        },
        "codeformer": {
            "id": "sczhou/codeformer",
            "name": "CodeFormer",
            "description": "Face restoration and enhancement",
            "cost_per_run": 0.001,
            "capabilities": ["face_restore", "enhance"],
            "version": "7de2ea26c616d5bf2245ad0d5e24f0ff9a6204578a5c876db53142edd9d2cd56"
        },
        "gfpgan": {
            "id": "tencentarc/gfpgan",
            "name": "GFPGAN",
            "description": "Face restoration with high quality",
            "cost_per_run": 0.001,
            "capabilities": ["face_restore"],
            "version": "9283608cc6b7be6b65a8e44983db012355fde4132009bf99d976b2f0896856e3"
        },
        "restore-image": {
            "id": "flux-kontext-apps/restore-image",
            "name": "Image Restoration",
            "description": "Restore old or damaged images",
            "cost_per_run": 0.003,
            "capabilities": ["restore", "enhance"]
        },
        "ddcolor": {
            "id": "piddnad/ddcolor",
            "name": "DDColor",
            "description": "Colorize black and white images",
            "cost_per_run": 0.002,
            "capabilities": ["colorize"],
            "version": "4918b843fd53b9a1652311449e1ba3afffc11e44a55ac7d5ed0b95c0540779b2"
        },
        "controlnet-tile": {
            "id": "batouresearch/magic-image-refiner",
            "name": "ControlNet Tile Upscaler",
            "description": "Diffusion-based upscaling with tiling",
            "cost_per_run": 0.02,
            "capabilities": ["upscaling", "enhance"],
            "special_features": ["hallucinate_details", "large_scale"]
        }
    },
    
    "video_generation": {
        "google-veo3": {
            "id": "google/veo-3",
            "name": "Google Veo 3",
            "description": "Google's flagship text-to-video model",
            "cost_per_run": 0.3,
            "capabilities": ["text2video"],
            "max_duration": 10,
            "resolutions": ["720p", "1080p"]
        },
        "hailuo-2": {
            "id": "minimax/hailuo-02",
            "name": "Hailuo 2",
            "description": "6-10s videos with realistic physics",
            "cost_per_run": 0.25,
            "capabilities": ["text2video", "img2video"],
            "max_duration": 10,
            "resolutions": ["720p", "1080p"],
            "special_features": ["realistic_physics", "character_consistency"]
        },
        "seedance-pro": {
            "id": "bytedance/seedance-1-pro",
            "name": "Seedance Pro",
            "description": "Professional video generation",
            "cost_per_run": 0.2,
            "capabilities": ["text2video", "img2video"],
            "max_duration": 10,
            "resolutions": ["480p", "720p", "1080p"]
        },
        "wan-2": {
            "id": "wan-video/wan-2.2-t2v-480p-fast",
            "name": "WAN 2.2",
            "description": "Fast open-source video generation",
            "cost_per_run": 0.05,
            "capabilities": ["text2video"],
            "max_duration": 5,
            "resolutions": ["480p"]
        },
        "minimax-video": {
            "id": "minimax/video-01-live",
            "name": "MiniMax Video",
            "description": "Excellent for animated character consistency",
            "cost_per_run": 0.15,
            "capabilities": ["text2video", "img2video", "character"],
            "special_features": ["character_consistency", "animation"]
        },
        "stable-video-diffusion": {
            "id": "stability-ai/stable-video-diffusion",
            "name": "Stable Video Diffusion",
            "description": "Image to video animation",
            "cost_per_run": 0.1,
            "capabilities": ["img2video"],
            "max_duration": 4
        },
        "s2v-01": {
            "id": "s2v/s2v-01",
            "name": "S2V-01",
            "description": "Subject reference video generation",
            "cost_per_run": 0.12,
            "capabilities": ["img2video", "character"],
            "special_features": ["subject_consistency"]
        }
    },
    
    "video_editing": {
        "reframe-video": {
            "id": "luma/reframe-video",
            "name": "Video Reframer",
            "description": "Change video aspect ratio intelligently",
            "cost_per_run": 0.02,
            "capabilities": ["video_reframe", "aspect_ratio"]
        },
        "modify-video": {
            "id": "luma/modify-video",
            "name": "Video Modifier",
            "description": "Style transfer and prompt-based editing",
            "cost_per_run": 0.05,
            "capabilities": ["video_edit", "style_transfer"]
        },
        "video-enhance": {
            "id": "alibaba/rife-video-enhance",
            "name": "Video Enhancer",
            "description": "Enhance video quality and framerate",
            "cost_per_run": 0.03,
            "capabilities": ["video_enhance", "fps_increase"]
        }
    },
    
    "audio_generation": {
        "musicgen": {
            "id": "meta/musicgen",
            "name": "MusicGen",
            "description": "Generate music from text descriptions",
            "cost_per_run": 0.008,
            "capabilities": ["music_gen"],
            "max_duration": 30,
            "features": ["melody_conditioning", "stereo"],
            "version": "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb"
        },
        "musicgen-stereo": {
            "id": "meta/musicgen",
            "name": "MusicGen Stereo",
            "description": "High-quality stereo music generation",
            "cost_per_run": 0.01,
            "capabilities": ["music_gen"],
            "max_duration": 30,
            "version": "671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
            "model_version": "stereo-large"
        },
        "magnet": {
            "id": "facebookresearch/magnet",
            "name": "MAGNeT",
            "description": "Music and sound effect generation",
            "cost_per_run": 0.006,
            "capabilities": ["music_gen", "sfx"],
            "version": "7a76a8258b23fae65c5a22debb8841d1d7e816b75c2f24218cd2bd8573787906"
        },
        "mmaudio": {
            "id": "facebookresearch/mmaudio",
            "name": "MMAudio",
            "description": "Generate audio synchronized with video",
            "cost_per_run": 0.005,
            "capabilities": ["video2audio", "sync"],
            "special_features": ["video_sync", "beat_matching"],
            "version": "c4a831c721ad64be178828c8c40978f92cfd9494ad4c43c3b0267fa4fa58b34f"
        },
        "music-01": {
            "id": "minimax/music-01",
            "name": "Music-01",
            "description": "Advanced music generation",
            "cost_per_run": 0.015,
            "capabilities": ["music_gen"]
        },
        "bark": {
            "id": "suno-ai/bark",
            "name": "Bark",
            "description": "Realistic text-to-speech with emotions",
            "cost_per_run": 0.001,
            "capabilities": ["tts", "voice_presets"],
            "features": ["emotions", "sound_effects", "music"],
            "version": "b76242b40d67c76ab6742e987628a2a9ac019e11d56ab96c4e91ce03b79b2787"
        },
        "whisper": {
            "id": "openai/whisper",
            "name": "Whisper",
            "description": "Speech to text transcription",
            "cost_per_run": 0.0006,
            "capabilities": ["speech2text", "translation"]
        },
        "xtts-v2": {
            "id": "lucataco/xtts-v2",
            "name": "XTTS v2",
            "description": "Voice cloning and multilingual TTS",
            "cost_per_run": 0.002,
            "capabilities": ["tts", "voice_clone"],
            "languages": 17,
            "version": "684bc3855b37866c0c65add2ff39c78f3dea3f4ff103a436465326e0f438d55e"
        }
    },
    
    "3d_generation": {
        "trellis": {
            "id": "firtoz/trellis",
            "name": "Trellis",
            "description": "Advanced 3D generation from images",
            "cost_per_run": 0.04,
            "capabilities": ["img23d", "mesh_gen"],
            "version": "e8f6c45206993f297372f5436b90350817bd9b4a0d52d2a76df50c1c8afa2b3c",
            "output_formats": ["glb", "ply", "mp4"]
        },
        "shap-e": {
            "id": "openai/shap-e",
            "name": "Shap-E",
            "description": "Text to 3D mesh generation",
            "cost_per_run": 0.03,
            "capabilities": ["text23d", "mesh_gen"]
        },
        "wonder3d": {
            "id": "camenduru/wonder3d",
            "name": "Wonder3D",
            "description": "Single image to 3D reconstruction",
            "cost_per_run": 0.035,
            "capabilities": ["img23d", "multi_view"],
            "version": "b5ad7e1b80c1a5a7e0c0a483f5a45f13797c7c9b6bc1c0fb18eab25cf088f4d6"
        },
        "hunyuan3d": {
            "id": "tencent/hunyuan3d",
            "name": "Hunyuan3D",
            "description": "High-quality 3D generation",
            "cost_per_run": 0.05,
            "capabilities": ["text23d", "img23d", "texture"],
            "version": "85e96b5a8eeb2cd1b024c4ba2fe8cb8b456e9419e616f40e8e94d59cc890d1f8"
        },
        "zero123": {
            "id": "stability-ai/stable-zero123",
            "name": "Stable Zero123",
            "description": "Novel view synthesis from single image",
            "cost_per_run": 0.025,
            "capabilities": ["img23d", "multi_view"]
        }
    },
    
    "utility_models": {
        "autocaption": {
            "id": "daanelson/autocaption",
            "name": "Auto Caption",
            "description": "Generate captions for images",
            "cost_per_run": 0.0005,
            "capabilities": ["caption"],
            "version": "07c7c718a3bd96fb991163df80d80cf76fb4e3a47e088b925709f7b3dd8c19ed"
        },
        "blip-2": {
            "id": "andreasjansson/blip-2",
            "name": "BLIP-2",
            "description": "Advanced image captioning",
            "cost_per_run": 0.0008,
            "capabilities": ["caption", "vqa"],
            "version": "f677695e5e89f8b236e52ecd1d3f01beb44c34606419bcc19345e046d8f786f9"
        },
        "llava": {
            "id": "yorickvp/llava-v1.6-34b",
            "name": "LLaVA",
            "description": "Visual question answering",
            "cost_per_run": 0.002,
            "capabilities": ["vqa", "analysis"]
        },
        "nsfw-image-detector": {
            "id": "m1guelpf/nsfw-filter",
            "name": "NSFW Detector",
            "description": "Content moderation",
            "cost_per_run": 0.0002,
            "capabilities": ["moderation"],
            "version": "7d14dd0e0e18e40ce87c4c10dd6362eb2e920cd05059b2473330b690e89cf06f"
        },
        "face-to-many": {
            "id": "flux-kontext-apps/face-to-many-kontext",
            "name": "Face to Many",
            "description": "Transform face into various styles",
            "cost_per_run": 0.02,
            "capabilities": ["style", "character"]
        }
    }
}


# Professional workflow templates
WORKFLOW_TEMPLATES = {
    "logo_to_brand_video": {
        "name": "Logo to Brand Video",
        "description": "Complete brand video creation from logo",
        "steps": [
            {
                "step": "generate_logo",
                "model": "recraft-ai/recraft-v3-svg",
                "params": {"output_format": "svg"}
            },
            {
                "step": "enhance_logo",
                "model": "philz1337x/clarity-upscaler",
                "params": {"scale": 4}
            },
            {
                "step": "animate_logo",
                "model": "stability-ai/stable-video-diffusion",
                "params": {"fps": 24, "duration": 3}
            },
            {
                "step": "generate_brand_scenes",
                "model": "black-forest-labs/flux-1.1-pro",
                "params": {"num_outputs": 5, "style": "professional"}
            },
            {
                "step": "create_video_sequences",
                "model": "minimax/hailuo-02",
                "params": {"duration": 10, "resolution": "1080p"}
            },
            {
                "step": "add_music",
                "model": "meta/musicgen-stereo-large",
                "params": {"duration": 30, "style": "corporate"}
            },
            {
                "step": "sync_audio_video",
                "model": "zsxkib/mmaudio",
                "params": {"sync_mode": "beat_match"}
            }
        ]
    },
    
    "character_animation": {
        "name": "Character Animation Pipeline",
        "description": "Create consistent character animations",
        "steps": [
            {
                "step": "design_character",
                "model": "black-forest-labs/flux-kontext-pro",
                "params": {"character_mode": True}
            },
            {
                "step": "create_turnaround",
                "model": "adirik/wonder3d",
                "params": {"views": 8}
            },
            {
                "step": "animate_character",
                "model": "minimax/video-01-live",
                "params": {"consistency_mode": "high"}
            },
            {
                "step": "add_voice",
                "model": "lucataco/xtts-v2",
                "params": {"emotion": "friendly"}
            }
        ]
    },
    
    "product_showcase": {
        "name": "Product Showcase Video",
        "description": "Professional product demonstration",
        "steps": [
            {
                "step": "product_photos",
                "model": "black-forest-labs/flux-1.1-pro",
                "params": {"mode": "product", "num_outputs": 10}
            },
            {
                "step": "remove_backgrounds",
                "model": "lucataco/remove-bg",
                "params": {"edge_quality": "high"}
            },
            {
                "step": "create_3d_model",
                "model": "firtoz/trellis",
                "params": {"quality": "high"}
            },
            {
                "step": "animate_product",
                "model": "google/veo-3",
                "params": {"style": "professional", "duration": 15}
            },
            {
                "step": "add_voiceover",
                "model": "suno-ai/bark",
                "params": {"voice": "announcer"}
            }
        ]
    },
    
    "social_media_content": {
        "name": "Social Media Content Pack",
        "description": "Complete social media asset generation",
        "steps": [
            {
                "step": "generate_images",
                "model": "bytedance/sdxl-lightning-4step",
                "params": {"num_outputs": 20, "speed": "fast"}
            },
            {
                "step": "create_short_videos",
                "model": "wan-video/wan-2.2-t2v-480p-fast",
                "params": {"duration": 5, "format": "vertical"}
            },
            {
                "step": "add_captions",
                "model": "fictions-ai/autocaption",
                "params": {"style": "social"}
            },
            {
                "step": "reframe_for_platforms",
                "model": "luma/reframe-video",
                "params": {"formats": ["1:1", "9:16", "16:9"]}
            }
        ]
    }
}


# Model selection rules
MODEL_SELECTION_RULES = {
    "quality_priority": {
        "image": ["flux-1.1-pro", "flux-dev", "sdxl"],
        "video": ["google/veo-3", "minimax/hailuo-02", "bytedance/seedance-1-pro"],
        "audio": ["meta/musicgen-stereo-large", "minimax/music-01"],
        "3d": ["prunaai/hunyuan3d-2", "firtoz/trellis"]
    },
    "speed_priority": {
        "image": ["bytedance/sdxl-lightning-4step", "flux-schnell"],
        "video": ["wan-video/wan-2.2-t2v-480p-fast"],
        "audio": ["meta/musicgen", "suno-ai/bark"],
        "3d": ["openai/shap-e"]
    },
    "cost_priority": {
        "image": ["sdxl-lightning", "sdxl"],
        "video": ["wan-video/wan-2.2-t2v-480p-fast", "stable-video-diffusion"],
        "audio": ["suno-ai/bark", "lucataco/magnet"],
        "3d": ["stability-ai/stable-zero123"]
    },
    "character_consistency": {
        "image": ["flux-kontext-pro", "flux-kontext-apps/face-to-many-kontext"],
        "video": ["minimax/video-01-live", "s2v/s2v-01", "minimax/hailuo-02"]
    }
}


def get_models_by_capability(capability: ModelCapability) -> List[Dict[str, Any]]:
    """Get all models that support a specific capability"""
    models = []
    for category in COMPLETE_MODEL_CATALOG.values():
        for model_key, model_info in category.items():
            if capability.value in model_info.get("capabilities", []):
                models.append({**model_info, "key": model_key})
    return models


def get_workflow_models(workflow_name: str) -> Optional[Dict[str, Any]]:
    """Get models for a specific workflow"""
    return WORKFLOW_TEMPLATES.get(workflow_name)


def select_best_model(
    task: str,
    priority: str = "quality",
    budget: Optional[float] = None,
    capabilities_needed: Optional[List[str]] = None
) -> Optional[str]:
    """Select the best model for a task based on criteria"""
    
    # Get priority list
    priority_models = MODEL_SELECTION_RULES.get(f"{priority}_priority", {}).get(task, [])
    
    if not priority_models:
        return None
    
    # Filter by budget if specified
    if budget:
        available_models = []
        for model_id in priority_models:
            # Find model in catalog
            for category in COMPLETE_MODEL_CATALOG.values():
                for model_info in category.values():
                    if model_info["id"] == model_id:
                        if model_info.get("cost_per_run", 0) <= budget:
                            available_models.append(model_id)
                        break
        priority_models = available_models
    
    # Filter by required capabilities
    if capabilities_needed:
        filtered_models = []
        for model_id in priority_models:
            # Find model in catalog
            for category in COMPLETE_MODEL_CATALOG.values():
                for model_info in category.values():
                    if model_info["id"] == model_id:
                        model_caps = set(model_info.get("capabilities", []))
                        if all(cap in model_caps for cap in capabilities_needed):
                            filtered_models.append(model_id)
                        break
        priority_models = filtered_models
    
    return priority_models[0] if priority_models else None
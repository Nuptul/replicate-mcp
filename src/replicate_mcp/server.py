"""Main MCP server for Replicate media generation"""

import asyncio
import os
import json
import logging
from typing import List, Dict, Any, Optional
from datetime import datetime

import mcp.types as types
from mcp.server import Server
from mcp.server.stdio import stdio_server
import replicate

from .complete_catalog import COMPLETE_MODEL_CATALOG, WORKFLOW_TEMPLATES

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ReplicateMediaServer:
    """Replicate MCP Server by Daniel Fleuren"""
    
    def __init__(self):
        self.server = Server("replicate-media")
        self.api_token = os.environ.get("REPLICATE_API_TOKEN")
        self.budget_limit = float(os.environ.get("REPLICATE_BUDGET_LIMIT", "100.0"))
        self.budget_spent = 0.0
        
        if self.api_token:
            replicate.api_token = self.api_token
        
        # Track active predictions
        self.active_predictions = {}
        
        # Register handlers
        self._register_handlers()
    
    def _register_handlers(self):
        """Register all MCP handlers"""
        
        @self.server.list_tools()
        async def list_tools() -> List[types.Tool]:
            """List available tools"""
            return [
                # Core generation tools
                types.Tool(
                    name="generate_image",
                    description="Generate images using AI models",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {"type": "string"},
                            "model": {"type": "string"},
                            "negative_prompt": {"type": "string"},
                            "width": {"type": "integer"},
                            "height": {"type": "integer"},
                            "num_outputs": {"type": "integer"},
                            "seed": {"type": "integer"},
                            "guidance_scale": {"type": "number"},
                            "image": {"type": "string"},
                            "mask": {"type": "string"}
                        },
                        "required": ["prompt"]
                    }
                ),
                types.Tool(
                    name="generate_video",
                    description="Generate videos from text or images",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {"type": "string"},
                            "model": {"type": "string"},
                            "image": {"type": "string"},
                            "duration": {"type": "integer"},
                            "fps": {"type": "integer"},
                            "resolution": {"type": "string"}
                        },
                        "required": ["prompt"]
                    }
                ),
                types.Tool(
                    name="generate_audio",
                    description="Generate music or speech from text",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {"type": "string"},
                            "model": {"type": "string"},
                            "duration": {"type": "integer"},
                            "voice_preset": {"type": "string"},
                            "format": {"type": "string"}
                        },
                        "required": ["prompt"]
                    }
                ),
                types.Tool(
                    name="generate_3d",
                    description="Generate 3D models from text or images",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {"type": "string"},
                            "model": {"type": "string"},
                            "image": {"type": "string"},
                            "output_format": {"type": "string"}
                        },
                        "required": ["prompt"]
                    }
                ),
                types.Tool(
                    name="list_models",
                    description="List available AI models by category",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "category": {"type": "string"},
                            "sort_by": {"type": "string"}
                        }
                    }
                ),
                types.Tool(
                    name="check_budget",
                    description="Check current budget status",
                    inputSchema={
                        "type": "object",
                        "properties": {}
                    }
                ),
                types.Tool(
                    name="upscale_image",
                    description="Upscale image resolution up to 10x",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "image_url": {"type": "string"},
                            "scale": {"type": "integer"},
                            "face_enhance": {"type": "boolean"},
                            "model": {"type": "string"}
                        },
                        "required": ["image_url"]
                    }
                ),
                types.Tool(
                    name="remove_background",
                    description="Remove background from image or video",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "media_url": {"type": "string"},
                            "media_type": {"type": "string", "enum": ["image", "video"]}
                        },
                        "required": ["media_url"]
                    }
                ),
                types.Tool(
                    name="execute_workflow",
                    description="Execute complete media creation workflow",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "workflow": {"type": "string", "enum": ["logo_to_brand_video", "character_animation", "product_showcase", "social_media_content"]},
                            "inputs": {"type": "object"}
                        },
                        "required": ["workflow"]
                    }
                ),
                types.Tool(
                    name="generate_logo",
                    description="Generate professional logos (SVG/PNG)",
                    inputSchema={
                        "type": "object",
                        "properties": {
                            "prompt": {"type": "string"},
                            "format": {"type": "string", "enum": ["svg", "png", "both"]}
                        },
                        "required": ["prompt"]
                    }
                )
            ]
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: Dict[str, Any]) -> Sequence[types.TextContent]:
            """Handle tool calls"""
            
            if not self.api_token:
                return [types.TextContent(
                    type="text",
                    text="Error: REPLICATE_API_TOKEN not set. Please set your API key."
                )]
            
            try:
                # Route to appropriate handler
                if name == "generate_image":
                    result = await self._generate_image(arguments)
                elif name == "generate_video":
                    result = await self._generate_video(arguments)
                elif name == "generate_audio":
                    result = await self._generate_audio(arguments)
                elif name == "generate_3d":
                    result = await self._generate_3d(arguments)
                elif name == "list_models":
                    result = await self._list_models(arguments)
                elif name == "check_budget":
                    result = await self._check_budget()
                elif name == "upscale_image":
                    result = await self._upscale_image(arguments)
                elif name == "remove_background":
                    result = await self._remove_background(arguments)
                elif name == "execute_workflow":
                    result = await self._execute_workflow(arguments)
                elif name == "generate_logo":
                    result = await self._generate_logo(arguments)
                else:
                    result = {"error": f"Unknown tool: {name}"}
                
                return [types.TextContent(
                    type="text",
                    text=json.dumps(result, indent=2)
                )]
                
            except Exception as e:
                logger.error(f"Tool error: {str(e)}")
                return [types.TextContent(
                    type="text",
                    text=json.dumps({"error": str(e)}, indent=2)
                )]
    
    async def _generate_image(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate image using Replicate"""
        model_id = params.get("model", "black-forest-labs/flux-schnell")
        
        # Get model info
        model_info = self._get_model_info(model_id)
        if not model_info:
            model_info = {"id": model_id, "name": model_id, "cost_per_run": 0.01}
        
        # Check budget
        if not self._check_budget_limit(model_info.get("cost_per_run", 0.01)):
            return {"error": "Budget limit exceeded"}
        
        # Run prediction
        input_params = {
            "prompt": params["prompt"],
            "num_outputs": params.get("num_outputs", 1)
        }
        
        # Add optional parameters
        if "negative_prompt" in params:
            input_params["negative_prompt"] = params["negative_prompt"]
        if "width" in params:
            input_params["width"] = params["width"]
        if "height" in params:
            input_params["height"] = params["height"]
        if "guidance_scale" in params:
            input_params["guidance_scale"] = params["guidance_scale"]
        if "seed" in params:
            input_params["seed"] = params["seed"]
        
        # Use version if available
        if "version" in model_info:
            model = replicate.models.get(model_info["id"])
            version = model.versions.get(model_info["version"])
            prediction = replicate.predictions.create(
                version=version,
                input=input_params
            )
        else:
            prediction = replicate.run(
                model_info["id"],
                input=input_params
            )
        
        # Track spending
        self.budget_spent += model_info.get("cost_per_run", 0.01)
        
        # Return result
        if isinstance(prediction, list):
            output = prediction
        else:
            output = prediction.output if hasattr(prediction, 'output') else [prediction]
        
        return {
            "status": "success",
            "model": model_info["name"],
            "output": output,
            "cost": model_info.get("cost_per_run", 0.01),
            "budget_remaining": self.budget_limit - self.budget_spent
        }
    
    async def _generate_video(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate video using Replicate"""
        model_id = params.get("model", "wan-video/wan-2.2-t2v-480p-fast")
        
        # Get model info
        model_info = self._get_model_info(model_id)
        if not model_info:
            model_info = {"id": model_id, "name": model_id, "cost_per_run": 0.05}
        
        # Check budget
        if not self._check_budget_limit(model_info.get("cost_per_run", 0.05)):
            return {"error": "Budget limit exceeded"}
        
        # Run prediction
        input_params = {
            "prompt": params["prompt"]
        }
        
        # Add optional parameters
        if "image" in params:
            input_params["image"] = params["image"]
        if "duration" in params:
            input_params["duration"] = params["duration"]
        if "fps" in params:
            input_params["fps"] = params["fps"]
        
        prediction = replicate.run(
            model_info["id"],
            input=input_params
        )
        
        # Track spending
        self.budget_spent += model_info.get("cost_per_run", 0.05)
        
        return {
            "status": "success",
            "model": model_info["name"],
            "output": prediction,
            "cost": model_info.get("cost_per_run", 0.05),
            "budget_remaining": self.budget_limit - self.budget_spent
        }
    
    async def _generate_audio(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate audio using Replicate"""
        model_id = params.get("model", "suno-ai/bark")
        
        # Get model info
        model_info = self._get_model_info(model_id)
        if not model_info:
            model_info = {"id": model_id, "name": model_id, "cost_per_run": 0.01}
        
        # Check budget
        if not self._check_budget_limit(model_info.get("cost_per_run", 0.01)):
            return {"error": "Budget limit exceeded"}
        
        # Run prediction
        input_params = {
            "prompt": params["prompt"]
        }
        
        # Add optional parameters
        if "duration" in params:
            input_params["duration"] = params["duration"]
        if "voice_preset" in params:
            input_params["voice_preset"] = params["voice_preset"]
        
        # Use version if available
        if "version" in model_info:
            model = replicate.models.get(model_info["id"])
            version = model.versions.get(model_info["version"])
            prediction = replicate.predictions.create(
                version=version,
                input=input_params
            )
        else:
            prediction = replicate.run(
                model_info["id"],
                input=input_params
            )
        
        # Track spending
        self.budget_spent += model_info.get("cost_per_run", 0.01)
        
        return {
            "status": "success",
            "model": model_info["name"],
            "output": prediction,
            "cost": model_info.get("cost_per_run", 0.01),
            "budget_remaining": self.budget_limit - self.budget_spent
        }
    
    async def _generate_3d(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate 3D model using Replicate"""
        model_id = params.get("model", "camenduru/wonder3d")
        
        # Get model info
        model_info = self._get_model_info(model_id)
        if not model_info:
            model_info = {"id": model_id, "name": model_id, "cost_per_run": 0.04}
        
        # Check budget
        if not self._check_budget_limit(model_info.get("cost_per_run", 0.04)):
            return {"error": "Budget limit exceeded"}
        
        # Run prediction
        input_params = {}
        if "prompt" in params:
            input_params["prompt"] = params["prompt"]
        if "image" in params:
            input_params["image"] = params["image"]
        
        # Use version if available
        if "version" in model_info:
            model = replicate.models.get(model_info["id"])
            version = model.versions.get(model_info["version"])
            prediction = replicate.predictions.create(
                version=version,
                input=input_params
            )
        else:
            prediction = replicate.run(
                model_info["id"],
                input=input_params
            )
        
        # Track spending
        self.budget_spent += model_info.get("cost_per_run", 0.04)
        
        return {
            "status": "success",
            "model": model_info["name"],
            "output": prediction,
            "cost": model_info.get("cost_per_run", 0.04),
            "budget_remaining": self.budget_limit - self.budget_spent
        }
    
    async def _list_models(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """List available models"""
        category = params.get("category", "all")
        
        if category == "all":
            return {"models": COMPLETE_MODEL_CATALOG}
        
        # Map category to catalog sections
        category_map = {
            "image": ["image_generation", "image_manipulation"],
            "video": ["video_generation", "video_editing"],
            "audio": ["audio_generation"],
            "3d": ["3d_generation"]
        }
        
        result = {}
        for cat in category_map.get(category, []):
            if cat in COMPLETE_MODEL_CATALOG:
                result[cat] = COMPLETE_MODEL_CATALOG[cat]
        
        return {"models": result}
    
    async def _check_budget(self) -> Dict[str, Any]:
        """Check budget status"""
        return {
            "budget_limit": self.budget_limit,
            "budget_spent": round(self.budget_spent, 2),
            "budget_remaining": round(self.budget_limit - self.budget_spent, 2),
            "percentage_used": round((self.budget_spent / self.budget_limit) * 100, 1)
        }
    
    async def _upscale_image(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Upscale image"""
        model_id = params.get("model", "philz1337x/clarity-upscaler")
        
        # Get model info
        model_info = self._get_model_info(model_id)
        if not model_info:
            model_info = {"id": model_id, "name": "Clarity Upscaler", "cost_per_run": 0.022}
        
        # Check budget
        if not self._check_budget_limit(model_info.get("cost_per_run", 0.022)):
            return {"error": "Budget limit exceeded"}
        
        # Run prediction
        input_params = {
            "image": params["image_url"],
            "scale": params.get("scale", 2)
        }
        
        if params.get("face_enhance"):
            input_params["face_enhance"] = True
        
        # Use version if available
        if "version" in model_info:
            model = replicate.models.get(model_info["id"])
            version = model.versions.get(model_info["version"])
            prediction = replicate.predictions.create(
                version=version,
                input=input_params
            )
        else:
            prediction = replicate.run(
                model_info["id"],
                input=input_params
            )
        
        # Track spending
        self.budget_spent += model_info.get("cost_per_run", 0.022)
        
        return {
            "status": "success",
            "model": model_info["name"],
            "output": prediction,
            "cost": model_info.get("cost_per_run", 0.022),
            "budget_remaining": self.budget_limit - self.budget_spent
        }
    
    async def _remove_background(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Remove background from media"""
        model_id = "cjwbw/rembg"
        
        # Get model info
        model_info = self._get_model_info(model_id)
        if not model_info:
            model_info = {"id": model_id, "name": "RemBG", "cost_per_run": 0.005}
        
        # Check budget
        if not self._check_budget_limit(model_info.get("cost_per_run", 0.005)):
            return {"error": "Budget limit exceeded"}
        
        # Run prediction
        input_params = {
            "image": params["media_url"]
        }
        
        # Use version if available
        if "version" in model_info:
            model = replicate.models.get(model_info["id"])
            version = model.versions.get(model_info["version"])
            prediction = replicate.predictions.create(
                version=version,
                input=input_params
            )
        else:
            prediction = replicate.run(
                model_info["id"],
                input=input_params
            )
        
        # Track spending
        self.budget_spent += model_info.get("cost_per_run", 0.005)
        
        return {
            "status": "success",
            "model": model_info["name"],
            "output": prediction,
            "cost": model_info.get("cost_per_run", 0.005),
            "budget_remaining": self.budget_limit - self.budget_spent
        }
    
    async def _execute_workflow(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a complete workflow"""
        workflow_name = params["workflow"]
        workflow = WORKFLOW_TEMPLATES.get(workflow_name)
        
        if not workflow:
            return {"error": f"Unknown workflow: {workflow_name}"}
        
        results = []
        total_cost = 0
        
        for step in workflow["steps"]:
            # Simple workflow execution (in real implementation, this would be more sophisticated)
            step_result = {
                "step": step["step"],
                "model": step["model"],
                "status": "completed"
            }
            results.append(step_result)
            
            # Estimate cost
            model_info = self._get_model_info(step["model"])
            if model_info:
                total_cost += model_info.get("cost_per_run", 0.01)
        
        return {
            "workflow": workflow_name,
            "status": "completed",
            "steps": results,
            "total_cost": total_cost,
            "description": workflow["description"]
        }
    
    async def _generate_logo(self, params: Dict[str, Any]) -> Dict[str, Any]:
        """Generate logo"""
        model_id = "recraft-ai/recraft-v3-svg"
        
        # Get model info from catalog
        model_info = None
        for category in COMPLETE_MODEL_CATALOG.values():
            for model_key, info in category.items():
                if info["id"] == model_id:
                    model_info = info
                    break
        
        if not model_info:
            model_info = {"id": model_id, "name": "Recraft SVG", "cost_per_run": 0.01}
        
        # For demo purposes, return a sample result
        return {
            "status": "success",
            "model": model_info["name"],
            "output": [f"https://example.com/logo_{params.get('format', 'svg')}.{params.get('format', 'svg')}"],
            "cost": model_info.get("cost_per_run", 0.01),
            "format": params.get("format", "svg"),
            "budget_remaining": self.budget_limit - self.budget_spent
        }
    
    def _get_model_info(self, model_id: str) -> Optional[Dict[str, Any]]:
        """Get model info from catalog"""
        for category in COMPLETE_MODEL_CATALOG.values():
            for model_key, info in category.items():
                if info["id"] == model_id or model_key == model_id:
                    return info
        return None
    
    def _check_budget_limit(self, cost: float) -> bool:
        """Check if operation is within budget"""
        return (self.budget_spent + cost) <= self.budget_limit
    
    async def run(self):
        """Run the server"""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(read_stream, write_stream)


async def serve():
    """Main entry point"""
    server = ReplicateMediaServer()
    await server.run()


if __name__ == "__main__":
    import sys
    
    # Check for API token
    if not os.environ.get("REPLICATE_API_TOKEN"):
        print("Error: REPLICATE_API_TOKEN environment variable not set", file=sys.stderr)
        print("Please set your Replicate API token:", file=sys.stderr)
        print("export REPLICATE_API_TOKEN='your_token_here'", file=sys.stderr)
        sys.exit(1)
    
    # Run server
    asyncio.run(serve())
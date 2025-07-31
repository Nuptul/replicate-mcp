# Replicate MCP

![Replicate MCP Banner](./assets/main_banner_1200x600.png)

<div align="center">

**🚀 AI Media Generation for Claude Code**

*Professional-grade media creation through MCP (Model Context Protocol) integration*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![MCP Compatible](https://img.shields.io/badge/MCP-Compatible-green.svg)](https://modelcontextprotocol.io/)
[![Replicate](https://img.shields.io/badge/Replicate-API-purple.svg)](https://replicate.com/)

*By Daniel Fleuren*

</div>

## ✨ Features

<table>
<tr>
<td width="50%">

### 🎨 **Image Generation**
![Image Generation](./assets/feature_image_generation.png)
- FLUX Pro, Dev, and Schnell models
- SDXL and Lightning variants  
- Professional upscaling and enhancement
- Background removal and face restoration

</td>
<td width="50%">

### 🎬 **Video Creation**
![Video Creation](./assets/feature_video_creation.png)
- Google Veo, Hailuo, and Seedance models
- Text-to-video and image animation
- Professional quality up to 1080p
- Multi-platform aspect ratios

</td>
</tr>
<tr>
<td width="50%">

### 🎵 **Audio Synthesis**
![Audio Synthesis](./assets/feature_audio_synthesis.png)
- Music generation with MusicGen
- Speech synthesis with XTTS-v2 and Bark
- Professional audio enhancement
- Multi-language support

</td>
<td width="50%">

### 🧊 **3D Generation**
![3D Generation](./assets/feature_3d_generation.png)
- Wonder3D and Hunyuan3D models
- Text-to-3D and image-to-3D
- Multiple output formats
- Professional quality meshes

</td>
</tr>
</table>

## 🚀 Quick Start

### One-Line Installation

```bash
curl -sSL https://raw.githubusercontent.com/danielfleuren/replicate-mcp/main/scripts/install.sh | bash
```

### Manual Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/danielfleuren/replicate-mcp.git
   cd replicate-mcp
   ```

2. **Run the installer**
   ```bash
   ./scripts/install.sh
   ```

3. **Add your API key** when prompted

That's it! Restart Claude Code and start creating. 🎉

## 🎯 Usage Examples

### Basic Commands

```python
# Generate an image
"Create a professional logo for my tech startup"

# Upscale an image
"Upscale this image to 4K resolution"

# Generate a video
"Create a 5-second video of a rocket launching"

# Generate music
"Create a 30-second upbeat electronic track"
```

### Advanced Workflows

```python
# Logo-to-brand video workflow
"Create a complete brand package with logo and promotional video"

# Character animation workflow
"Create an animated character that waves hello"

# Product showcase workflow
"Create a professional product showcase video with music"
```

## 📋 Available Models

<details>
<summary><b>🎨 Image Generation (20+ models)</b></summary>

- **FLUX Pro/Dev/Schnell** - State-of-the-art image generation
- **SDXL & Lightning** - Fast, high-quality images
- **Ideogram** - Text rendering specialist
- **Instant ID** - Face-consistent generation
- **Photo Maker** - Realistic photo generation
- **Face to Sticker** - Convert faces to stickers
- **ReVision** - Reference-based generation

</details>

<details>
<summary><b>🎬 Video Generation (10+ models)</b></summary>

- **Google Veo** - Professional video creation
- **Hailuo AI** - Creative video synthesis
- **LTX Video** - Long-form video generation
- **Seedance** - Dance video generation
- **AnyV2V** - Video-to-video transformation
- **Reframe Video** - Aspect ratio conversion

</details>

<details>
<summary><b>🎵 Audio Generation (8+ models)</b></summary>

- **MusicGen** - Music composition
- **MAGNeT** - Advanced music generation
- **Bark** - Realistic speech synthesis
- **XTTS-v2** - Multilingual TTS
- **MMAudio** - Video soundtrack generation
- **AudioLM** - Natural audio synthesis

</details>

<details>
<summary><b>🧊 3D Generation (5+ models)</b></summary>

- **Wonder3D** - Image-to-3D conversion
- **Hunyuan3D** - Text-to-3D generation
- **TripoSR** - Single image 3D reconstruction
- **Zero123** - 3D object generation
- **DreamGaussian** - Fast 3D generation

</details>

<details>
<summary><b>🔧 Enhancement Tools (15+ models)</b></summary>

- **Clarity Upscaler** - 10x resolution enhancement
- **CodeFormer** - Face restoration
- **GFPGAN** - Face enhancement
- **RealESRGAN** - General image upscaling
- **DeOldify** - Photo colorization
- **DDColor** - Dual-decoder colorization
- **Remove Background** - Automatic background removal

</details>

## 🔄 Professional Workflows

### 1. Logo-to-Brand Video
Transform a simple logo into a complete brand package:
- Logo enhancement and variations
- Animated logo intro
- Brand colors extraction
- Promotional video with music
- Social media assets

### 2. Character Animation
Create consistent animated characters:
- Character design from description
- Multiple pose generation
- Smooth animation sequences
- Background integration
- Voice synthesis

### 3. Product Showcase
Professional product presentations:
- Product photography enhancement
- 360° rotation videos
- Feature highlight animations
- Background music generation
- Multi-format export

### 4. Social Media Content
Optimized content for all platforms:
- Platform-specific aspect ratios
- Animated text overlays
- Trending style adaptation
- Batch generation
- A/B testing variants

## 🛠️ Configuration

### Environment Variables

```bash
# Required
export REPLICATE_API_TOKEN="your_token_here"

# Optional
export REPLICATE_BUDGET_LIMIT="100.0"          # Monthly budget ($)
export REPLICATE_QUALITY_PREFERENCE="balanced" # quality|speed|cost
export REPLICATE_CACHE_ENABLED="true"          # Result caching
```

### MCP Settings

The configuration is automatically handled by the installer.

Location by platform:
- **Linux**: `~/.config/claude-code/mcp_settings.json`
- **macOS**: `~/Library/Application Support/claude-code/mcp_settings.json`
- **Windows**: `%APPDATA%/claude-code/mcp_settings.json`

## 📊 Budget Management

### Cost Optimization

- **Smart Model Selection**: Automatically chooses cost-effective models
- **Budget Tracking**: Real-time spending monitoring
- **Usage Analytics**: Detailed cost breakdowns
- **Warnings**: Alerts before budget limits

### Pricing Examples

| Task | Model | Approximate Cost |
|------|-------|------------------|
| Logo Generation | FLUX Schnell | $0.003 |
| 4K Upscaling | Clarity Upscaler | $0.022 |
| 5-sec Video | LTX Video | $0.045 |
| 30-sec Music | MusicGen | $0.008 |
| 3D Model | Wonder3D | $0.036 |

## 🧪 Testing

### Run Installation Tests
```bash
python scripts/test_installation.py
```

### Test Specific Models
```bash
python scripts/test_models.py --category image
```

### Verify Workflows
```bash
python scripts/test_workflows.py
```

## 🔧 Troubleshooting

### Common Issues

<details>
<summary><b>MCP Server Not Loading</b></summary>

1. Restart Claude Code
2. Check configuration path
3. Verify API key is set
4. Run installation test

</details>

<details>
<summary><b>Model Errors</b></summary>

1. Check model availability
2. Verify API limits
3. Try alternative model
4. Check error logs

</details>

<details>
<summary><b>Performance Issues</b></summary>

1. Enable caching
2. Use faster models
3. Reduce output resolution
4. Check network speed

</details>

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Areas for Contribution

- New model integrations
- Workflow templates
- Performance optimizations
- Documentation improvements
- Bug fixes

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- **Replicate** for the amazing AI models
- **Anthropic** for Claude and MCP
- **Community** for feedback and contributions
- **Daniel Fleuren** for professional design and branding

## 📞 Support

- 📖 [Documentation](docs/)
- 💬 [GitHub Discussions](https://github.com/danielfleuren/replicate-mcp/discussions)
- 🐛 [Issue Tracker](https://github.com/danielfleuren/replicate-mcp/issues)
- ✉️ Email: daniel@example.com

---

<div align="center">

**Ready to create amazing AI media?** 🚀

[Get Started](docs/quickstart.md) | [View Examples](examples/) | [Read Docs](docs/)

*Powered by Replicate API and Claude MCP*

</div>
